# Military History Project

Reconstructions of historical military operations, each published as a replayable
operation package. Every mission is a folder under `missions/` with its own README
(method, anchors, conflicts and sources), its generator in `build/`, and the package
files; [`catalog.json`](catalog.json) lists them.

| Mission | Event | Open |
| --- | --- | --- |
| [Operation Vengeance](missions/operation-vengeance/) | Interception of Admiral Yamamoto over Bougainville, 18 April 1943 | [replay](https://luofang34.github.io/Sokoly-App/?operation=https://luofang34.github.io/Military-History-Project/missions/operation-vengeance&recorded-path) |

## Opening a mission

The repository is published with GitHub Pages, so a mission folder's URL opens in the
web viewer: `https://luofang34.github.io/Sokoly-App/?operation=<folder URL>`, plus `&recorded-path` for the story
camera and `&at=SECONDS` to start elsewhere. Packages must not use Git LFS, since Pages
serves LFS pointers rather than their content.

To play one in the native viewer, with its checkout beside this one (or `VIEWER_REPO`
pointing at it): `./run operation-vengeance`, optionally with `--at SECONDS --paused`.

## Adding a mission

Create `missions/<id>/` with the package, a README carrying its method and sources, and
its generator; shared track and event helpers are in `tools/`. Add it to `catalog.json`,
then run `python3 verify.py`, which checks every mission's camera and pacing coverage and
that the catalog matches the folders.

## Licence

The reconstructions, packages and code here are dedicated to the public domain under
[CC0 1.0](LICENSE). Works cited in each mission's sources keep their own terms; briefings
quote them only in short attributed passages.
