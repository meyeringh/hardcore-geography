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

## Building

Requires Python 3.8+ and [pipenv](https://pipenv.pypa.io/).

```bash
pipenv --python 3 install
pipenv run build
```

Output is written to `build/` in [CrowdAnki](https://github.com/ohare93/crowd-anki) format.

## Importing into Anki

1. Install the [CrowdAnki add-on](https://ankiweb.net/shared/info/1788670778) (code: `1788670778`)
2. Restart Anki
3. File → CrowdAnki: Import from disk
4. Select a deck folder from `build/`, e.g. `Hardcore Geography [EN]/`
