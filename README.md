# Military History Project

Replayable reconstructions of historical military operations. Each mission is published as an
operation package and played in the Sokoly viewer at [sokoly.app](https://sokoly.app/).

| Mission | Event | Open |
| --- | --- | --- |
| [Operation Vengeance](https://github.com/luofang34/Military-History-Project/tree/master/missions/operation-vengeance) | Interception of Admiral Yamamoto over Bougainville, 18 April 1943 | [replay](https://history.sokoly.app/operation-vengeance/) |
| [Gulf of Sidra incident](https://github.com/luofang34/Military-History-Project/tree/master/missions/gulf-of-sidra-1981) | Two F-14s shoot down two Su-22s over the Gulf of Sidra, 19 August 1981 | [replay](https://history.sokoly.app/gulf-of-sidra-1981/) |
| [Operation Chastise](https://github.com/luofang34/Military-History-Project/tree/master/missions/operation-chastise) | The Dams Raid: 617 Squadron breaches the Möhne and Eder dams, 16/17 May 1943 | [replay](https://history.sokoly.app/operation-chastise/) |

## Opening a mission

`https://history.sokoly.app/<mission-id>/` launches a mission's replay with the story camera.
Add `?at=SECONDS` to start elsewhere or `?paused` to open paused. The viewer URL behind it is
`https://sokoly.app/?operation=<package URL>&recorded-path`.

To play a mission in the native viewer, with the Sokoly-App checkout beside this one (or
`$VIEWER_REPO` pointing at it): `./run operation-vengeance`, optionally with
`--at SECONDS --paused`.

## Linking to a moment

Every key moment and dispute recorded in a mission's `build/evidence/` is a fact with a
permanent id. `https://history.sokoly.app/f/?id=<id>` opens its replay just before it, for
example [Maltby's attack on the Möhne](https://history.sokoly.app/f/?id=f1ba1cfd-69fb-5de4-9b6b-56a6c17e441c).
The id is the UUIDv5 of the fact's key, `<mission>/<evidence key>`, where the evidence key is
the key of the moment or dispute ([`tools/facts.py`](tools/facts.py)).

## Repository

- `missions/<id>/`: one mission: its generator in `build/` (sources in `build/evidence/`),
  its README of method, anchors, disputes and sources, the package files, its launch page and
  its `facts.jsonl`.
- `facts/`: the shared fact layer of all missions, with the index the links resolve through.
- `f/`: the link resolver.
- `tools/`: helpers shared by the generators and checks.
- `verify.py`: the checks every package must pass.
- [`catalog.json`](catalog.json): the list of missions.

## Contributing

The source is at [github.com/luofang34/Military-History-Project](https://github.com/luofang34/Military-History-Project).
Corrections and sources are welcome as
[issues](https://github.com/luofang34/Military-History-Project/issues), and changes as
[pull requests](https://github.com/luofang34/Military-History-Project/pulls).
[AGENTS.md](https://github.com/luofang34/Military-History-Project/blob/master/AGENTS.md)
describes how a mission is built, sourced, shot and checked, for people and coding agents
alike. `python3 verify.py` is the gate before every commit.

## Licence

The reconstructions, packages and code here are dedicated to the public domain under
[CC0 1.0](LICENSE). Works cited in each mission's sources keep their own terms; briefings
quote them only in short attributed passages.
