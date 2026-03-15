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

## Importing into Anki

1. Install the [CrowdAnki add-on](https://ankiweb.net/shared/info/1788670778) (code: `1788670778`)
2. Restart Anki
3. File → CrowdAnki: Import from disk
4. Select a deck folder from `build/`, e.g. `Hardcore Geography [EN]/`
