# Operation Vengeance

Interception of Admiral Yamamoto over Bougainville, 18 April 1943, from the P-38
take-off at Fighter Two to egress at 10:05. Clock: Henderson Field time (UTC+11).

[Open the replay in a browser](https://luofang34.github.io/Sokoly-App/?operation=https://luofang34.github.io/Military-History-Project/missions/operation-vengeance&recorded-path) ·
start at the 09:34 sighting with `&at=7770`.

This folder is the package (`operation.json`, `events.jsonl`,
`presentations/default.json`) and its generator, `build/`. Regenerate with
`python3 build/vengeance.py`, then run `python3 ../../verify.py`.

## Method

Positions are `reconstructed` and each fix carries a horizontal `bound_m`. Fixes are
written at the reconstructed track's waypoints only; each reconstruction source declares a
great-circle motion model, so the viewer derives positions between them and marks them as
derived. Wreck sites and annotations quoting sources are `reported`. `source.id` names the
evidence for each event, and Japanese-side sources declare Tokyo time as their clock.
Aircraft carry their pilots' names and belong to declared flights and sections, which the
viewer draws as one symbol when they overlap. Times follow the 13th Fighter Command report (Henderson Field time, UTC+11).
Japanese records use Tokyo time (UTC+9), which is two hours behind, and annotations quote them as such.
The operation declares a fixed UTC+11 zone because tzdb's `Pacific/Bougainville` gives
the Japanese occupation clock for 1943.

- **Sourced anchors**:
  - P-38 wheels-up at 07:25 from Fighter Two.
  - McLanahan's tyre failure and Moore's tank failure.
  - Lakunai departure at 06:05–06:10 Tokyo.
  - Sighting at 09:34. The Bettys were at 4,500 ft with the Zeros 1,500 ft above.
  - The cover flight climbed toward 18,000 ft.
  - Barber attacked from astern.
  - T1-323 wreck at 6°47.165′S 155°33.137′E.
  - T1-326 ditched about 100 m off Moila Point.
  - Hine was last seen near Shortland.
- **P-38 route** (±20 km): published leg headings, the island stand-off and timing,
  combined as follows.
  - The published 290° and 305° legs are read as magnetic headings, with about 7.5° E
    variation.
  - The track keeps Condon's 20 nmi island stand-off.
  - It reproduces the sourced turns at 08:20 (about 180 mi west of Henderson) and 08:47,
    plus about 435 mi at about 214 mph.
  - Sources disagree on total distance (410–494 mi) and on the final turn (09:00–09:25).
- **Japanese route** (±30 km, ±5 km near the coast): Lakunai to Empress Augusta Bay, then
  down the south-west coast, as US accounts place it. One secondary source routes it
  along the east coast instead.
- **Engagement** (±1.5 km): manoeuvres between the anchors are choreographed. Speeds stay
  within each type's performance.
- **Coastline-based placements**:
  - The Moila Point ditching is placed 150 m off the OSM shoreline. The Pacific Wrecks
    point label lies about 1 km inland.
  - The take-off order and Fighter Two runway heading are not sourced.
- **Conflicts carried as uncertain timeline markers**:
  - Bettys down: US 09:36–09:40, Japanese 09:45–09:50.
  - Hine last seen: MACR 599 vs 609.
- **Record end**: the record ends during egress at 10:05. Landings (Holmes in the
  Russells; the others at about 11:40) and the aftermath appear in the closing briefing.

## Sources

- 13th Fighter Command, "Fighter Interception" report, 18 Apr 1943 — https://texashistory.unt.edu/ark:/67531/metapth1812456/
- Wikipedia: Operation Vengeance, Isoroku Yamamoto, Rex T. Barber, Kukum Field, Lakunai Airfield, Kahili Airfield, Balalae Airport — https://en.wikipedia.org/wiki/Operation_Vengeance
- 海軍甲事件 (ja.wikipedia) — https://ja.wikipedia.org/wiki/海軍甲事件
- Pacific Wrecks: G4M1 2656 (T1-323), T1-326, P-38 Hine, Moila Point — https://pacificwrecks.com/aircraft/g4m/2656.html, https://pacificwrecks.com/aircraft/g4m/T1-326.html, https://pacificwrecks.com/aircraft/p-38/hine.html, https://pacificwrecks.com/location/bougainville_moila.html
- John P. Condon, "Bringing Down Yamamoto", USNI Proceedings, Nov 1990 — https://www.usni.org/magazines/proceedings/1990/november/bringing-down-yamamoto
- Air & Space Forces Magazine, "Magic and Lightning" and "The Man Who Shot Down Yamamoto" — https://www.airandspaceforces.com/article/0306yamamoto/, https://www.airandspaceforces.com/article/the-man-who-shot-down-yamamoto/
- HistoryNet, "Death by P-38" — https://historynet.com/death-by-p-38/
- Roger Ames via Warfare History Network — https://warfarehistorynetwork.com/article/killing-yamamoto-operation-vengeance-from-roger-ames-cockpit/
- Kenji Yanagiya interview (Yoshimura, 1970s) and Shoichi Sugita account, via ja.wikipedia 柳谷謙治 / 杉田庄一
- Barber v. Widnall, 78 F.3d 1419 (9th Cir. 1996) — https://law.resource.org/pub/us/case/reporter/F3/078/78.F3d.1419.93-36200.html
- Coastlines used to check placements: Natural Earth 10 m; © OpenStreetMap contributors (ODbL). No map data is bundled.
