# Hardcore Geography

Companion deck to [Ultimate Geography](https://github.com/anki-geo/ultimate-geography) adding obscure territories, islands, and additional card types for map-only entities.

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
