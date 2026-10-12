# Military History Project

Reconstructions of historical military operations, each published as a replayable
operation package. Every mission is a folder under `missions/` with its own README
(method, anchors, conflicts and sources), its generator in `build/`, and the package
files; [`catalog.json`](catalog.json) lists them.

| Mission | Event | Open |
| --- | --- | --- |
| [Operation Vengeance](https://github.com/luofang34/Military-History-Project/tree/master/missions/operation-vengeance) | Interception of Admiral Yamamoto over Bougainville, 18 April 1943 | [replay](https://history.sokoly.app/operation-vengeance/) |
| [Gulf of Sidra incident](https://github.com/luofang34/Military-History-Project/tree/master/missions/gulf-of-sidra-1981) | Two F-14s shoot down two Su-22s over the Gulf of Sidra, 19 August 1981 | [replay](https://history.sokoly.app/gulf-of-sidra-1981/) |
| [Operation Chastise](https://github.com/luofang34/Military-History-Project/tree/master/missions/operation-chastise) | The Dams Raid: 617 Squadron breaches the Möhne and Eder dams, 16/17 May 1943 | [replay](https://history.sokoly.app/operation-chastise/) |

## Opening a mission

[history.sokoly.app](https://history.sokoly.app/) hosts this project description.
Each `/<mission-id>/` link launches its replay in [sokoly.app](https://sokoly.app/)
with the story camera. Add `?at=SECONDS` to start elsewhere or `?paused` to open paused.
The viewer URL is `https://sokoly.app/?operation=<package URL>&recorded-path`.
Packages must not use Git LFS, since Pages serves LFS pointers rather than their content.

## Linking to a moment

Every sourced fact, such as a release, a breach or a loss, has an id that never changes,
so a link to it survives every regeneration of the replay that shows it.
`https://history.sokoly.app/f/?id=<id>` opens that replay five seconds before the fact,
for example [Maltby's attack on the Möhne](https://history.sokoly.app/f/?id=f1ba1cfd-69fb-5de4-9b6b-56a6c17e441c).
A fact's id is the UUIDv5 of its key, `<mission>/<dispute key>` ([`tools/facts.py`](tools/facts.py)).
The facts of all missions are filed in [`facts/`](facts) by UTC day and map tile, and
`facts/index/` maps each id to the replay that shows it.

To play one in the native viewer, with its checkout beside this one (or `VIEWER_REPO`
pointing at it): `./run operation-vengeance`, optionally with `--at SECONDS --paused`.

## Adding a mission

[AGENTS.md](https://github.com/luofang34/Military-History-Project/blob/master/AGENTS.md) describes how a mission is built, sourced, shot and checked, for
people and coding agents alike. `python3 verify.py` checks every package before it is
published, including each shot of its story against the viewer's own projection.

The Pages homepage renders this README.

## Licence

The reconstructions, packages and code here are dedicated to the public domain under
[CC0 1.0](LICENSE). Works cited in each mission's sources keep their own terms; briefings
quote them only in short attributed passages.
