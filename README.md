# Hardcore Geography

Companion deck to [Ultimate Geography](https://github.com/anki-geo/ultimate-geography) adding obscure territories, islands, and additional card types for map-only entities.

## Content decisions

### Canals

The 11 notable ship canals listed in the [Ship canal](https://en.wikipedia.org/wiki/Ship_canal) Wikipedia article, plus the Grand Canal (China) from the [transcontinental canals](https://en.wikipedia.org/wiki/List_of_transcontinental_canals) list (included as the world's longest canal and a UNESCO World Heritage Site).

| Canal | Country | Length |
|-------|---------|--------|
| Saint Lawrence Seaway | Canada | 600 km |
| White Sea-Baltic Canal | Russia | 227 km |
| Suez Canal | Egypt | 193 km |
| Rhine-Main-Danube Canal | Germany | 171 km |
| Volga-Don Canal | Russia | 101 km |
| Kiel Canal | Germany | 98 km |
| Houston Ship Channel | USA | 80 km |
| Panama Canal | Panama | 77 km |
| Danube-Black Sea Canal | Romania | 64 km |
| Manchester Ship Canal | UK | 58 km |
| Welland Canal | Canada | 43 km |
| Grand Canal | China | 1,776 km |

### Mountains

The two highest mountains per continent (excluding Antarctica), based on the [Seven Summits](https://en.wikipedia.org/wiki/Seven_Summits) (Messner list) and [Seven Second Summits](https://en.wikipedia.org/wiki/Seven_Second_Summits) Wikipedia articles. Antarctica is excluded as its peaks are not widely known outside mountaineering.

| Mountain | Continent | Elevation | Country |
|----------|-----------|-----------|---------|
| Mount Everest | Asia | 8,849 m | Nepal/China |
| K2 | Asia | 8,611 m | Pakistan/China |
| Aconcagua | South America | 6,961 m | Argentina |
| Ojos del Salado | South America | 6,893 m | Chile/Argentina |
| Denali | North America | 6,194 m | USA |
| Mount Logan | North America | 5,959 m | Canada |
| Kilimanjaro | Africa | 5,895 m | Tanzania |
| Mount Kenya | Africa | 5,199 m | Kenya |
| Mount Elbrus | Europe | 5,642 m | Russia |
| Dykh-Tau | Europe | 5,205 m | Russia |
| Puncak Jaya | Oceania | 4,884 m | Indonesia |
| Puncak Mandala | Oceania | 4,760 m | Indonesia |

## Building

Requires Python 3.8+ and [pipenv](https://pipenv.pypa.io/).

```bash
pipenv --python 3 install
pipenv run build
```

Output is written to `build/` in [CrowdAnki](https://github.com/ohare93/crowd-anki) format.

## Generating maps

Map images are generated with `scripts/generate_map.py` to ensure a consistent style across all entries.

```bash
pip install -r scripts/requirements.txt
```

Two modes are supported:

```bash
# Mountain: red triangle marker at coordinates
python scripts/generate_map.py mountain mount_everest \
  --lat 27.9881 --lon 86.9250 \
  --zoom 83 91 25 31 \
  --overview 50 120 5 55 \
  --inset lower-left

# Canal: red route line from OpenStreetMap
python scripts/generate_map.py canal suez_canal \
  --osm-query 'way["name:en"="Suez Canal"]["waterway"]' \
  --zoom 31.8 32.65 29.85 31.35 \
  --overview 15 55 10 50 \
  --inset lower-left

# Canal with manual coordinates (when OSM has no data)
python scripts/generate_map.py canal houston_ship_channel \
  --coords "-94.72,29.37 -94.82,29.45 -95.32,29.76" \
  --zoom -95.5 -94.5 29.2 30.0 \
  --overview -110 -80 20 40 \
  --inset upper-right
```

Run `python scripts/generate_map.py --help` for all options.

## Importing into Anki

1. Install the [CrowdAnki add-on](https://ankiweb.net/shared/info/1788670778) (code: `1788670778`)
2. Restart Anki
3. File → CrowdAnki: Import from disk
4. Select a deck folder from `build/`, e.g. `Hardcore Geography [EN]/`
