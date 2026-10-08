# Military History Project

Reconstructions of historical military operations, each published as a replayable
operation package. Every mission is a folder under `missions/` with its own README
(method, anchors, conflicts and sources), its generator in `build/`, and the package
files; [`catalog.json`](catalog.json) lists them.

| Mission | Event | Open |
| --- | --- | --- |
| [Operation Vengeance](https://github.com/luofang34/Military-History-Project/tree/master/missions/operation-vengeance) | Interception of Admiral Yamamoto over Bougainville, 18 April 1943 | [replay](https://history.sokoly.app/operation-vengeance/) |
| [Gulf of Sidra incident](https://github.com/luofang34/Military-History-Project/tree/master/missions/gulf-of-sidra-1981) | Two F-14s shoot down two Su-22s over the Gulf of Sidra, 19 August 1981 | [replay](https://history.sokoly.app/gulf-of-sidra-1981/) |

## Opening a mission

[history.sokoly.app](https://history.sokoly.app/) hosts this project description.
Each `/<mission-id>/` link launches its replay in [sokoly.app](https://sokoly.app/)
with the story camera. Add `?at=SECONDS` to start elsewhere or `?paused` to open paused.
The viewer URL is `https://sokoly.app/?operation=<package URL>&recorded-path`.
Packages must not use Git LFS, since Pages serves LFS pointers rather than their content.

To play one in the native viewer, with its checkout beside this one (or `VIEWER_REPO`
pointing at it): `./run operation-vengeance`, optionally with `--at SECONDS --paused`.

## Adding a mission

Create `missions/<id>/` with the package, a README carrying its method and sources, its
generator, and an `index.html` launch page pointing at its package on `history.sokoly.app`;
the page's front matter sets `permalink: /<id>/` so it is served at `/<id>/`. Shared track
and event helpers are in `tools/`. Add the mission to `catalog.json`, then run
`python3 verify.py`, which checks camera and pacing coverage, the catalog and public replay
links. The Pages homepage renders this README.

## Licence

The reconstructions, packages and code here are dedicated to the public domain under
[CC0 1.0](LICENSE). Works cited in each mission's sources keep their own terms; briefings
quote them only in short attributed passages.
