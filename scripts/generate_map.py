#!/usr/bin/env python3
"""Generate map images for the Hardcore Geography Anki deck.

Supports two modes:
  - canal:    Red route line from OpenStreetMap data
  - mountain: Red triangle marker at coordinates

All maps use the same style: Natural Earth base layers, consistent
colors, country borders, and an overview inset with location dot.

Usage:
  # Canal from OSM (query by name tag)
  python scripts/generate_map.py canal suez_canal \
    --osm-query 'way["name:en"="Suez Canal"]["waterway"]' \
    --zoom 31.8 32.65 29.85 31.35 \
    --overview 15 55 10 50 \
    --inset lower-left

  # Mountain at coordinates
  python scripts/generate_map.py mountain mount_everest \
    --lat 27.9881 --lon 86.9250 \
    --zoom 83 91 25 31 \
    --overview 50 120 5 55 \
    --inset lower-left

  # Canal with manual coordinates (when OSM has no data)
  python scripts/generate_map.py canal houston_ship_channel \
    --coords "-94.72,29.37 -94.82,29.45 -95.32,29.76" \
    --zoom -95.5 -94.5 29.2 30.0 \
    --overview -110 -80 20 40 \
    --inset upper-right

Requirements: pip install cartopy matplotlib requests
"""
import argparse
import os
import sys
import time

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

LAND_COLOR = '#f2efe9'
WATER_COLOR = '#c6ecff'
BORDER_COLOR = '#aaa'
HIGHLIGHT_COLOR = '#e04040'
CANAL_LINE_WIDTH = 2.5
MOUNTAIN_MARKER_SIZE = 14
OUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'media', 'maps')

INSET_POSITIONS = {
    'lower-left':  [0.04, 0.04, 0.28, 0.40],
    'upper-right': [0.68, 0.55, 0.28, 0.40],
    'upper-left':  [0.04, 0.55, 0.28, 0.40],
    'lower-right': [0.68, 0.04, 0.28, 0.40],
}


def query_osm(overpass_filter, retries=3):
    import requests
    query = f'[out:json][timeout:90];({overpass_filter});out body;>;out skel qt;'
    for attempt in range(retries):
        r = requests.post(
            'https://overpass-api.de/api/interpreter',
            data={'data': query},
        )
        if r.status_code == 200:
            data = r.json()
            nodes = {
                e['id']: (e['lon'], e['lat'])
                for e in data['elements'] if e['type'] == 'node'
            }
            lines = []
            for e in data['elements']:
                if e['type'] == 'way':
                    coords = [nodes[nid] for nid in e.get('nodes', []) if nid in nodes]
                    if coords:
                        lines.append(coords)
            return lines
        wait = 30 * (attempt + 1)
        print(f'HTTP {r.status_code}, retrying in {wait}s...', file=sys.stderr)
        time.sleep(wait)
    print('Failed after retries', file=sys.stderr)
    return []


def render_map(outpath, zoom, overview, inset_pos, lines=None, marker=None):
    fig = plt.figure(figsize=(5, 3.5), dpi=100)

    # Main map
    ax = fig.add_axes([0.02, 0.02, 0.96, 0.96], projection=ccrs.PlateCarree())
    ax.set_extent(zoom, crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.OCEAN, color=WATER_COLOR, zorder=0)
    ax.add_feature(cfeature.LAND, color=LAND_COLOR, zorder=1)
    ax.add_feature(cfeature.BORDERS, linewidth=0.8, edgecolor=BORDER_COLOR, zorder=2)
    ax.add_feature(cfeature.COASTLINE, linewidth=0.5, edgecolor='#999', zorder=2)
    ax.add_feature(cfeature.LAKES, color=WATER_COLOR, zorder=1)
    ax.add_feature(cfeature.RIVERS, edgecolor=WATER_COLOR, linewidth=0.5, zorder=1)

    if lines:
        all_lons = [c[0] for l in lines for c in l]
        all_lats = [c[1] for l in lines for c in l]
        for line in lines:
            ax.plot(
                [c[0] for c in line], [c[1] for c in line],
                color=HIGHLIGHT_COLOR, linewidth=CANAL_LINE_WIDTH,
                transform=ccrs.PlateCarree(), zorder=5, solid_capstyle='round',
            )
        center_lon = (min(all_lons) + max(all_lons)) / 2
        center_lat = (min(all_lats) + max(all_lats)) / 2

    if marker:
        center_lon, center_lat = marker
        ax.plot(
            center_lon, center_lat, marker='^',
            color=HIGHLIGHT_COLOR, markersize=MOUNTAIN_MARKER_SIZE,
            markeredgecolor='#a02020', markeredgewidth=1.2,
            transform=ccrs.PlateCarree(), zorder=5,
        )

    # Overview inset
    ax_in = fig.add_axes(INSET_POSITIONS[inset_pos], projection=ccrs.PlateCarree())
    ax_in.set_extent(overview, crs=ccrs.PlateCarree())
    ax_in.add_feature(cfeature.OCEAN, color=WATER_COLOR, zorder=0)
    ax_in.add_feature(cfeature.LAND, color=LAND_COLOR, zorder=1)
    ax_in.add_feature(cfeature.COASTLINE, linewidth=0.3, edgecolor='#999', zorder=2)
    ax_in.add_feature(cfeature.BORDERS, linewidth=0.4, edgecolor=BORDER_COLOR, zorder=2)
    ax_in.plot(
        center_lon, center_lat, 'o',
        color=HIGHLIGHT_COLOR, markersize=5,
        transform=ccrs.PlateCarree(), zorder=5,
    )
    for spine in ax_in.spines.values():
        spine.set_edgecolor('#666')
        spine.set_linewidth(0.8)

    plt.savefig(outpath, dpi=100, bbox_inches='tight', pad_inches=0.02,
                facecolor='white', edgecolor='none')
    plt.close()
    print(f'Saved: {outpath}')


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('mode', choices=['canal', 'mountain'])
    parser.add_argument('name', help='Output filename stem, e.g. suez_canal -> ug-map-suez_canal.png')
    parser.add_argument('--zoom', nargs=4, type=float, required=True,
                        metavar=('W', 'E', 'S', 'N'), help='Main map extent')
    parser.add_argument('--overview', nargs=4, type=float, required=True,
                        metavar=('W', 'E', 'S', 'N'), help='Inset overview extent')
    parser.add_argument('--inset', default='lower-left', choices=INSET_POSITIONS.keys(),
                        help='Inset position (default: lower-left)')
    parser.add_argument('--outdir', default=OUT_DIR, help='Output directory')

    canal = parser.add_argument_group('canal mode')
    canal.add_argument('--osm-query', help='Overpass filter, e.g. way["name"="X"]["waterway"]')
    canal.add_argument('--coords', help='Manual coords as "lon,lat lon,lat ..." (when OSM has no data)')

    mountain = parser.add_argument_group('mountain mode')
    mountain.add_argument('--lat', type=float, help='Mountain latitude')
    mountain.add_argument('--lon', type=float, help='Mountain longitude')

    args = parser.parse_args()
    outpath = os.path.join(args.outdir, f'ug-map-{args.name}.png')

    if args.mode == 'canal':
        if args.osm_query:
            lines = query_osm(args.osm_query)
            if not lines:
                sys.exit('No data from OSM')
        elif args.coords:
            coords = [tuple(map(float, p.split(','))) for p in args.coords.split()]
            lines = [coords]
        else:
            sys.exit('Canal mode requires --osm-query or --coords')
        render_map(outpath, args.zoom, args.overview, args.inset, lines=lines)

    elif args.mode == 'mountain':
        if args.lat is None or args.lon is None:
            sys.exit('Mountain mode requires --lat and --lon')
        render_map(outpath, args.zoom, args.overview, args.inset, marker=(args.lon, args.lat))


if __name__ == '__main__':
    main()
