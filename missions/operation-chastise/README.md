# Operation Chastise, 16/17 May 1943

The Dams Raid: nineteen Lancasters of 617 Squadron, each carrying one Upkeep mine, attack the
Möhne, Eder and Sorpe dams and, from the reserve, the Ennepe. The record runs from 21:25 at
Scampton to 06:20, after Townsend, the last back, lands at 06:15. Clock: British Double
Summer Time (UTC+2). German summer time was also UTC+2 that night (tzdb `Europe/London` BDST
and `Europe/Berlin` CEST, checked against the system zoneinfo), so British and German times
are on one clock.

[Open the replay in a browser](https://history.sokoly.app/operation-chastise/) · start at
Gibson's attack on the Möhne with `?at=10920`.

This folder is the package (`operation.json`, `events.jsonl`, `presentations/default.json`)
and its generator, `build/`. Regenerate with `python3 build/chastise.py`, then run
`python3 ../../verify.py`.

## Method

Positions are `reconstructed`, and each fix carries a horizontal `bound_m`: 1 km at Scampton,
5 km on the routes, 400 m in the target areas, 20 km for Anderson's wandering in mist. Fixes
are written at the reconstructed tracks' waypoints. Each reconstruction source declares a
great-circle motion model, so the viewer derives positions between fixes and marks them as
derived. Fixed sites, crash sites and quoted annotations are `reported`. Aircraft carry their
captains' names. Mines are entities of their own, each a member of the aircraft that dropped it.

The order of battle is declared through each entity's `parent`. The viewer lists it as a tree
and, on the map, folds overlapping members into one symbol under the formation they share.

- **RAF**: No. 5 Group → No. 617 Squadron → three waves → the first wave's three sections →
  Lancasters (ORB). RAF Scampton and the 5 Group HQ also sit under No. 5 Group.
- **Luftwaffe flak**: Flakgruppe Dortmund → leichte Flak-Abteilung 840 → its 3rd battery at the
  Möhne (LWL), drawn with regiment, battalion and battery echelon amplifiers.

- **Sourced anchors** (617 Squadron ORB, AIR 27/2128, unless noted):
  - Every take-off and landing minute: 21:28 Barlow first off, 06:15 Townsend last down.
  - Releases:

    | Dam | Aircraft and release time |
    | --- | --- |
    | Möhne | Gibson 00:28, Martin 00:38, Maltby 00:49 |
    | Eder | Shannon 01:39 |
    | Sorpe | McCarthy 00:46 at 30 ft, Brown 03:14 |
    | Ennepe | Townsend 03:37 |

    The ORB transcript's 01:39 for Maltby repeats Shannon's time. Maltby's navigation log gives
    00:48–00:50 (dambustersblog).
  - Hopgood about 00:32–00:33 and Young 00:43 (Wikipedia, secondary). Knight about 01:52, on
    his second run (ORB; IWM).
  - Losses (dambustersblog, from the ORB editor's notes, ASN and the crews' logs):

    | Time | Aircraft | Where |
    | --- | --- | --- |
    | 22:57 | Byers | Waddenzee |
    | 23:50 | Barlow | Haldern |
    | 00:15 | Astell | Marbeck, logged by Knight's wireless operator |
    | 00:34 | Hopgood | Ostönnen |
    | 02:00 | Burpee | Gilze-Rijen |
    | 02:35 | Ottley | Heessen |
    | 02:36 | Maudslay | Klein-Netterden |
    | 02:58 | Young | off Castricum aan Zee |
  - Signals at 5 Group:
    - 00:50 Goner 78A (Maltby).
    - 00:56 "Nigger", the Möhne breach codeword and the name of Gibson's dog. It is quoted
      as sent; the word is a racial slur.
    - About 01:54 "Dinghy" for the Eder.
    - 01:57 Goner 28B (Maudslay).
    - About 02:00 Goner 710B (Knight).
    - Diversion orders: 02:26 Townsend to the Ennepe, 02:28 Anderson to the Sorpe, 02:31
      Ottley to the Lister.
  - Other route events:
    - Munro hit by flak at Vlieland at 22:54.
    - Rice over Vlieland at 22:59, then in the water.
    - Anderson turns back at 03:10.
  - Möhne flood front: breach 00:49, Neheim 01:20, Wickede about 02:00, Fröndenberg about
    03:00, Schwerte 05:15 (de.wikipedia Möhnekatastrophe).
  - Eder flood front: Knight's breach about 01:52, then Wabern at 05:30 (Geschichtskreis
    Wabern), at an even pace through Affoldern, Bergheim, Wega and Fritzlar (`eder-flood`).
  - Both fronts are drawn with the APP-6D flood symbol (activity, natural event 170202).
- **Sites**:
  - Dam crests and their axes are from OpenStreetMap geometry, ±20 m.
  - Scampton is from Wikipedia. It was a grass field in May 1943: its concrete runways were
    laid from August 1943. The take-off direction (250°) and the positions on the field are not
    sourced.
  - Crash sites are dambustersblog's memorials and nearest access points, not surveyed impact
    points, and the bounds say so. Byers's is an area 18 miles west of Harlingen, ±10 km.
    Young's is placed offshore of the Castricum memorial, ±2 km.
- **Routes** (±5 km): the turning points of 5 Group Operation Order B.976, in the order and by
  the names on the planned-routes map (IBCC 33688), geocoded.
  - Only the Zero Hour positions 51°52′N 03°00′E (first wave) and 53°19′N 04°00′E (second
    wave) are the order's own coordinates. Appendix A, with the others, is not published
    online.
  - Return routes follow the map's numbering:
    - Return 1 (Maltby's and Martin's logs)
    - Return 2 (Knight's log)
    - Return 3 (Gibson, Young)
    - Shannon's route is not known and is placed on Knight's.
    - McCarthy's, out and home, follows his navigator's log turn by turn, at the times it
      logs (`mccarthy-route-out`, `mccarthy-route-home`).
  - Heights:
    - under 1,500 ft over England;
    - 60 ft on the spotlight altimeter over the sea;
    - about 130 ft over land.
  - Each leg between sourced anchors is flown at constant ground speed. Turns are flown as
    arcs a Lancaster could fly: circuits are joined along their tangent, and corners are
    rounded at about 30° of bank, never through a release point.
  - Maudslay's section is timed to be abeam Marbeck at 00:15, when Astell was seen to go down.
- **Attacks** (±400 m): reconstructed from the crests and the accounts.
  - **Möhne**: runs down the lake on 323°, perpendicular to the crest, toward its water face.
    - Each attacker waits in a left-hand circuit over the hills south of the lake (B.976
      orders left-hand circuits) that runs tangent into the run.
    - The run comes down to 60 ft where it reaches the water past the Heversberg spit, about
      1.4 km before the release. That is where the terrain model the viewer draws meets the
      lake surface (`SHORE_M`, ±20 m).
    - Release is at 60 ft and 220 mph, 425 yards short. A climbing turn to port follows.
    - Gibson flies a dummy run, then draws the flak beside Martin, Young and Maltby. On
      Maltby's run he flies to starboard and Martin to port (dambustersblog). The sides on
      the earlier runs are not recorded.
  - **Eder**: a dive from 1,000 ft over Waldeck castle toward the Hammerberg spit. A hard turn
    to port lines the aircraft up on the wall, on 124°, 500 m before the release, and a steep
    climbing turn to starboard clears the hill beyond (Gibson).
  - **Sorpe**: runs along the crest from over Langscheid on 132°, at 180 mph (B.976). The mine
    is dropped unspun on the water side of the crest. McCarthy comes in over the church
    steeple of St. Antonius, Langscheid, and onto the crest at its north-west end.
  - **Ennepe**: a run perpendicular to the crest from the lake to the south. Townsend reported
    355° magnetic. It crosses the hills south of the lake above 60 ft and comes down to it at
    the shore, about 360 m before the release.
  - Dummy-run counts:
    - Shannon: four before his release.
    - Maudslay and Knight: one each.
    - McCarthy: nine.
    - Brown: seven.
    - Townsend: two.

    Their times are spaced evenly between arrival and release.
  - Upkeep bounce counts are the crews' and dambustersblog's:
    - Gibson 3, Maltby 4, Shannon 2, Knight 3, Townsend 2.
    - Martin 3 and Young 3 are assumed.

    The mines' paths and timings are choreographed.
- **Build checks**: `build/chastise.py` fails if:
  - any Lancaster leg of a second or more leaves 120–245 mph ground speed;
  - a holding circuit cannot be flown within 125–225 mph;
  - a spun release misses 60 ft ±10 ft or 400–450 yards (Hopgood and Maudslay are flagged
    late);
  - a Sorpe release is off the crest or outside 30–60 ft;
  - successive releases at a dam come less than B.976's three minutes apart;
  - a take-off, landing or loss misses its ORB or sourced minute, or a loss misses its crash
    site;
  - any camera shot loses its subject (`build/framer.py` fits each shot's zoom to its
    subjects);
  - an event cites a source that `operation.json` does not declare;
  - a dam photograph is shown before its dam's flood front is on the map, from a camera below
    the ground, other than as an overlay, or without the shot and pace that hand the camera
    to it.

## Photographs

Three photographs taken after the raid show the damage once each dam's flood is running:
Fray's aerial view and a view from below the wall after Maltby breaks the Möhne, and a view
of the Eder after Knight breaks it. The viewer flies from the story's view onto each
photograph's camera, lays the photograph over the terrain half transparent, brings it to full
opacity and fades it out, and the story carries on from that view. `build/photographs.py`
places each, and its brief says when it was taken.
Each `media/<key>/replay.json` holds the photograph, its camera and the photograph draped on
present-day terrain. The camera was fitted by hand to the dam's crest and towers on the
terrain model, then refined against the crest edges in the photograph; automatic image
matching does not confirm it. Each replay's `registration` states the camera and the residual.

## Conflicts carried

Where sources disagree, or no source gives what the replay needs, `build/evidence/` keeps the
original records apart from the replay's estimate:

- Each record stands under its own source. It is quoted exactly where the table shows
  quotation marks; every quote was compared with the source itself (the ORB transcript,
  *Enemy Coast Ahead*, Hinks et al., B.976 and each cited web page). A record that could not
  be compared, such as a reading of a scanned log, is marked as an unchecked relay.
- The records stay in the code base for study and correction; the replay is for a general
  audience and shows at most a dispute's one-line note for viewers.
- The flight plans read their times from the estimates, so revising one is a one-line change
  and a rebuild.
- The build fails if a timed estimate falls outside its records' times without saying why.

<!-- evidence ledger: generated by build/chastise.py from build/evidence/ -->
| Dispute | Records (source: what it says) | Replay estimate and basis |
| --- | --- | --- |
| McCarthy's late take-off (`mccarthy-delay`) | 617 Squadron Operations Record Book, AIR 27/2128: “Had trouble with his compass and took off 20 mins. late.”<br>Operation Chastise (en.wikipedia): “took off in the reserve aircraft 34 minutes late”<br>Charles Foster, Dambusters Blog: “AJ-T eventually took to the air some 33 minutes later than their scheduled departure time” | **22:01**. The ORB's own UP time. |
| McCarthy's route to the Sorpe (`mccarthy-route-out`) | AJ-T navigator's log (Dambusters Blog transcription): Navigator's log, page 3, its legs in order: Stavoren a/c Harderwijk; Harderwijk a/c Doesburg; Doesburg a/c Rees; Rees a/c Lake; Lake a/c Ahlen; Ahlen a/c Target X; Target X a/c Target Z<br>Operation Chastise (en.wikipedia): “Formation No. 2 flew further north, cutting over Vlieland and crossing the IJsselmeer”<br>Operation Chastise (en.wikipedia): “before joining the first route near Wesel” | **The northern route by Doesburg to Rees, then the lakes, Ahlen and the Möhne**. The log's own legs. Rees, where it joins the southern route, lies near Wesel; Target X, the Möhne, is where it turns for the Sorpe, placed 2 km short of the dam. |
| Serials of AJ-A and AJ-T (`serials`) | 617 Squadron Operations Record Book, AIR 27/2128: Young's sheet: “ED. 877G. (A)”<br>Aviation Safety Network wikibase: Young's loss, whose registration field reads ED887: “ED877 was hit by Flak”<br>617 Squadron Operations Record Book, AIR 27/2128: McCarthy's sheet: “Lancaster III ED 923 G. (T)”<br>Charles Foster, Dambusters Blog: Unchecked relay, not compared with the source: McCarthy flew the spare ED825/G. | **ED887/G and ED825/G**. The usual identifications of the aircraft flown; the ORB transcript's serials disagree. |
| Hopgood's attack (`hopgood-release`) | 617 Squadron Operations Record Book, AIR 27/2128: “Was seen to be hit by flak on the run-up and to have an engine on fire. He overshot with his mine”<br>617 Squadron Operations Record Book, AIR 27/2128: ORB editor's note, across a page break after "power": “crashed near the dam power house and exploded at 0034hrs”<br>LWL Westfälische Geschichte: Möhnekatastrophe: “Der deutschen Flak auf den Türmen gelang es immerhin, einen der Bomber auf dem Zielanflug über dem Möhnesee abzuschießen” | **00:32:50**. No source times the release. It follows Gibson's 00:28 by B.976's three minutes for the water and leaves about a minute for the burning climb to Ostönnen. |
| Young's attack (`young-release`) | 617 Squadron Operations Record Book, AIR 27/2128: “Was seen to make an accurate attack with his mine” | **00:43**. No source read times it; it falls between Martin's 00:38 and Maltby's 00:49 at B.976's spacing, and secondary accounts give 00:43. |
| Maltby's attack (`maltby-release`) | 617 Squadron Operations Record Book, AIR 27/2128: “MOHNE DAM. 1 Mine. 60ft. 0139 hrs.”<br>Charles Foster, Dambusters Blog: “Gibson told Maltby to go ahead at 0048.”<br>Charles Foster, Dambusters Blog: “at 0050 wireless operator Antony Stone radioed ‘Goner 78A’ back to Grantham.”<br>LWL Westfälische Geschichte: Möhnekatastrophe: “Erst beim sechsten Anflug gelang es einer Lancaster um 00.49 Uhr, die Staumauer zu zerstören.”<br>Möhnekatastrophe (de.wikipedia): “Die Bombe explodierte um 0:49 Uhr in der Mitte der Mauer und riss die Staumauer auf etwa 30 m Breite auf.” | **00:49**. The ORB's 0139 repeats Shannon's Eder time on the next sheet; the breach was signalled at 00:56 and Maltby landed at 03:11. |
| Martin's mine (`martin-mine`) | 617 Squadron Operations Record Book, AIR 27/2128: “Mine burst about 20 yds. short.”<br>Operation Chastise (en.wikipedia): “Mine missed the target.” | **Bursts 18 m short**. The ORB's distance; Wikipedia agrees it missed. |
| Möhne flak (`mohne-flak`) | LWL Westfälische Geschichte: Möhnekatastrophe: “nur noch sechs 2-cm-Flakgeschütze der 3. Batterie leichte Flakabteilung 840, die zur Flakgruppe Dortmund gehörte.”<br>LWL Westfälische Geschichte: Möhnekatastrophe: “Die Sologeschütze hatten ihre Stellungen am Ende der Sperrmauer, unterhalb der Talsperre und auf den zwei Türmen bezogen.”<br>617 Squadron Operations Record Book, AIR 27/2128: “There were between seven and ten light flak guns around the target” | **Six guns, one battery at the dam**. The German record of the defending battery. |
| Release speed (`release-speed`) | 5 Group Operation Order B.976 (IBCC 10501, 33688): “the height of attack is to be 60 feet and the ground speed 220 m.p.h.”<br>Operation Chastise (en.wikipedia): “at an air speed of 240 mph (390 km/h)”<br>Guy Gibson, Enemy Coast Ahead (1946): “we were being dragged along at four miles a minute” | **220 mph**. The operation order's figure. |
| McCarthy's arrival at the Sorpe (`mccarthy-arrival`) | Charles Foster, Dambusters Blog: “Flying as fast as he could, McCarthy made up 13 or 14 minutes by the time he reached the Sorpe at 0015”<br>AJ-T navigator's log (Dambusters Blog transcription): Navigator's log, page 3: “Target Z”<br>Charles Foster, Dambusters Blog: Foster on MacLean's log: “He recorded the time of arrival at Target Z as 0030” | **00:30**. The log's own time, as the blog later reads it too. Ten approaches from about 00:32, once across from the Möhne side, to the 00:46 release take 90 s each, which the blog also works out ("not much more than 90 seconds") and a tight circuit allows. |
| McCarthy's runs at the Sorpe (`mccarthy-runs`) | Charles Foster, Dambusters Blog: “on the tenth approach, he managed to make a near perfect run, getting down to about 30 feet”<br>Operation Chastise (en.wikipedia): “McCarthy made nine attempted bombing runs before Johnson was satisfied”<br>Guy Gibson, Enemy Coast Ahead (1946): “They had both made twelve dummy runs and had dropped their mines along the lip of the concrete” | **Nine dummy runs, release on the tenth**. Two accounts agree on ten approaches; Gibson was not at the Sorpe. |
| The Sorpe run (`sorpe-geometry`) | Operation Chastise (en.wikipedia): “the approach was made along the length of the dam, not at right angles over the reservoir”<br>617 Squadron Operations Record Book, AIR 27/2128: ORB editor's note: “detailed to fly from left to right at about 30 degrees with the mine bouncing up to the dam face”<br>Operation Chastise (en.wikipedia): “led over a church steeple in the village of Langscheid”<br>Charles Foster, Dambusters Blog: “The approach involved flying over the small town of Langscheid, which had a prominent church steeple” | **Along the crest, unspun; McCarthy in over Langscheid's steeple**. McCarthy's own report of "the run along the Dam" (ORB). His crew came in over the church of St. Antonius, Langscheid, 320 m to the lake side of the crest line, at some 30-40° to the crest, as the editor's note has it, and turned onto it before the dam. |
| Maudslay's attack (`maudslay-release`) | 617 Squadron Operations Record Book, AIR 27/2128: Shannon: “Diverted from the Mohne to the Eder Dam, attacked first and registered a direct hit, but no result was seen.”<br>617 Squadron Operations Record Book, AIR 27/2128: Maudslay: “The mine overshot and struck the parapet, detonating instantaneously.”<br>617 Squadron Operations Record Book, AIR 27/2128: Knight: “Was the third aircraft to attack the Eder Dam.”<br>Charles Foster, Dambusters Blog: “At 0157, some twenty minutes after they had dropped their mine, wireless operator Alden Cottam sent a ‘Goner 28B’ message back to base” | **01:45**. Keeps the ORB's order, after Shannon's 01:39 and before Knight's mine (about 01:52, eder-breach), with B.976's three minutes either side; "some twenty minutes" before 01:57 would put it at about 01:37, before Shannon's. |
| Eder breach (`eder-breach`) | LWL Westfälische Geschichte: Möhnekatastrophe: “Etwa eine Stunde später, um 01.37 Uhr, wurde auch dieser Staudamm zerstört.”<br>Edertalsperre (de.wikipedia): “Am 17. Mai 1943 kurz vor 2 Uhr nachts wurde die Ederstaumauer bei einem Angriff”<br>Guy Gibson (en.wikipedia): “At 01:54, Hutchinson signalled the breach and then confirmed it.”<br>Operation Chastise (en.wikipedia): “The final bomb of the formation, from Knight's aircraft (N for Nut), breached the dam.” | **01:52**. On Knight's attack, two minutes before the signal; LWL's 01:37 comes before Shannon's 01:39 release in the ORB. |
| The Eder flood down the valley (`eder-flood`) | Edertalsperre (de.wikipedia): “In der Folge ergoss sich eine 6 bis 8 m hohe Flutwelle durch das untere Edertal nach Fritzlar, Wabern und Felsberg”<br>Geschichtskreis Wabern, Erinnerungspfad, Tafel 6: Die Ederseekatastrophe: “Um 5.30 Uhr traf die Flutwelle ein” | **05:30**. Wabern's arrival is the one time found below the dam; the front runs there from the breach at an even pace through Affoldern, Bergheim, Wega and Fritzlar. |
| Burpee's loss (`burpee-loss`) | Aviation Safety Network wikibase: Time: “01:53”<br>617 Squadron Operations Record Book, AIR 27/2128: ORB editor's note: “Shot down at 0200 immediately south of Gilze-Rijen (Netherlands) on way to target.” | **02:00**. The ORB editor's note; the two differ by seven minutes. |
| Ottley's loss (`ottley-loss`) | Charles Foster, Dambusters Blog: “At 0231, Group sent the code word “Gilbert” to AJ-C, and the signal was acknowledged.”<br>Charles Foster, Dambusters Blog: “The second signal was not acknowledged, indicating that AJ-C had met its fate at about 0231.”<br>Charles Foster, Dambusters Blog: “Ken Brown, flying AJ-F a few minutes behind, reported seeing him hit the ground at 0235.” | **02:35**. Brown's sighting, the one direct observation. |
| Townsend's target (`townsend-target`) | 617 Squadron Operations Record Book, AIR 27/2128: “ENNEPE DAM. 1 Mine. 60ft. 0337 hrs.”<br>617 Squadron Operations Record Book, AIR 27/2128: ORB editor's note: “Post war research proves that Townsend attacked not the Ennerpe Dam but the Bever Dam nearby to the North West instead.”<br>Hinks, Heitefuss & Chrimes, The Dambusters Revisited (2010): “Sweetman (2002) makes a strong case that the fourth dam attacked was the Bever Dam” | **The Ennepe, as reported**. Townsend's own report; the dams' coordinates put the Bever 11 km south of the Ennepe, not north-west. |
| Young's loss (`young-loss`) | Aviation Safety Network wikibase: Time: “02:57”<br>617 Squadron Operations Record Book, AIR 27/2128: ORB editor's note: “"Dinghy" Young's Lancaster was shot down by flak North of Ijmuiden at 0258 (Castricum aan Zee) killing all the crew.” | **02:58**. The ORB editor's note; the two differ by a minute. |
| McCarthy's route home (`mccarthy-route-home`) | AJ-T navigator's log (Dambusters Blog transcription): Navigator's log, page 3, its legs in order: Target Z a/c Target X; Target X a/c Ahlen; Ahlen a/c Lake; Lake a/c Rees; Rees a/c Doesburg; Doesburg a/c Harderwijk; Harderwijk a/c Stavoren; Wall; Island Vlieland; Mablethorpe<br>Charles Foster, Dambusters Blog: “they simply backtracked along their outbound course”<br>Charles Foster, Dambusters Blog: “McCarthy set course for home, but went via the Möhne, having heard over the radio that it had been breached.”<br>Charles Foster, Dambusters Blog: Foster on MacLean: “ending up over the heavily defended town of Hamm.” | **The outbound legs reversed, off course over Hamm between Ahlen and the lakes**. The log reverses its outbound legs and names no Hamm; its Ahlen to Rees leg, 00:59 to 01:32, takes half as long again as the same leg out, room for the deviation both blog posts describe. Times are the log's legible ones. The log crosses the English coast at Mablethorpe about 03:02 and is over base at 03:18; the replay, with no circuit of Scampton before the 03:23 landing (ORB), crosses about 03:11. |

Key moments, on which the sources agree:

| Moment | Records (source: what it says) | Time |
| --- | --- | --- |
| The first take-off (`first-take-off`) | 617 Squadron Operations Record Book, AIR 27/2128: First take-off 2128; the second wave leaves Scampton singly from 21:28 to 21:31. | 21:28 |
| Gibson's take-off (`gibson-take-off`) | 617 Squadron Operations Record Book, AIR 27/2128: Gibson, Hopgood and Martin take off in a vic at 2139. | 21:39 |
| Munro hit at Vlieland (`munro-hit`) | 617 Squadron Operations Record Book, AIR 27/2128: Light flak at Vlieland hits AJ-W about 2254 and knocks out the intercom; Munro turns for home with his mine. | 22:54 |
| Byers's loss (`byers-loss`) | Charles Foster, Dambusters Blog: Byers, off track over Texel, is shot down by flak at 2257 and falls into the Waddenzee; all seven are killed. | 22:57 |
| Barlow's loss (`barlow-loss`) | Charles Foster, Dambusters Blog: Barlow hits high-tension cables at Haldern at 2350 and crashes; all seven are killed. | 23:50 |
| Astell's loss (`astell-loss`) | Charles Foster, Dambusters Blog: Astell flies into high-tension cables near Marbeck at 0015. | 00:15 |
| Gibson's attack (`gibson-release`) | 617 Squadron Operations Record Book, AIR 27/2128: Gibson attacks first at 60 ft at 0028; the mine explodes short of the wall. | 00:28 |
| Hopgood's loss (`hopgood-loss`) | 617 Squadron Operations Record Book, AIR 27/2128: AJ-M, hit on the run-in, crashes near Ostönnen at 0034; two of the crew survive as prisoners. | 00:34 |
| Martin's attack (`martin-release`) | 617 Squadron Operations Record Book, AIR 27/2128: Martin attacks at 0038 with Gibson alongside; the mine bursts short. | 00:38 |
| The Möhne breaks (`mohne-breach`) | Möhnekatastrophe (de.wikipedia): “Die Bombe explodierte um 0:49 Uhr in der Mitte der Mauer und riss die Staumauer auf etwa 30 m Breite auf.”<br>LWL Westfälische Geschichte: Möhnekatastrophe: “Erst beim sechsten Anflug gelang es einer Lancaster um 00.49 Uhr, die Staumauer zu zerstören.” | 00:49 |
| The Möhne flood reaches Neheim (`neheim-flood`) | Möhnekatastrophe (de.wikipedia): The flood reaches Neheim at 0120. | 01:20 |
| McCarthy's attack (`mccarthy-release`) | 617 Squadron Operations Record Book, AIR 27/2128: McCarthy attacks along the crest at 0046 after nine dummy runs, dropping from 30 ft without spin; the dam holds. | 00:46 |
| Brown's attack (`brown-release`) | 617 Squadron Operations Record Book, AIR 27/2128: Brown attacks the Sorpe from 60 ft at 0314 after marking it with incendiaries; the crest holds. | 03:14 |
| Shannon's attack (`shannon-release`) | 617 Squadron Operations Record Book, AIR 27/2128: Shannon attacks at 0139; the mine bounces twice and explodes, with no visible result. | 01:39 |
| Anderson turns back (`anderson-turns-back`) | 617 Squadron Operations Record Book, AIR 27/2128: Anderson, his rear turret unserviceable and the valleys filling with mist, turns back with his mine at 0310. | 03:10 |
| Townsend's attack (`townsend-release`) | 617 Squadron Operations Record Book, AIR 27/2128: Townsend drops on his third run at 0337; the mine bounces twice and explodes short. | 03:37 |
| Maudslay's loss (`maudslay-loss`) | Charles Foster, Dambusters Blog: Maudslay is shot down by flak at Klein-Netterden, near Emmerich, at 0236; all are killed. | 02:36 |
| Gibson lands (`gibson-landing`) | Operation Chastise (en.wikipedia): Gibson lands at Scampton at 0415. | 04:15 |
| The last landing (`last-landing`) | 617 Squadron Operations Record Book, AIR 27/2128: Last landing 0615: Townsend, the last back, crosses Holland in daylight. | 06:15 |
<!-- end of evidence ledger -->

Other figures that vary between sources:

- **Ground casualties**: at least 1,650 dead (Blank). Of these, at least 1,579 died in the Möhne
  and Ruhr valleys (Blank) and between 47 and 68 in the Eder valley (de.wikipedia); 859 died
  in Neheim, 147 Germans and 712 foreigners (de.wikipedia). The first German count was 1,294.
- **Möhne outflow**: 116 million m³ within twelve hours (1949 US Military Hydrology study),
  against a capacity of 130–135 million m³ (de.wikipedia).

## Sources

- 617 Squadron Operations Record Book, AIR 27/2128 (Dambusters Association transcript, with
  editor's notes): https://www.dambusters.org.uk/docs/recordbook.pdf
- 5 Group Operation Order B.976 and the planned-routes map, IBCC Digital Archive 10501 and
  33688: https://ibccdigitalarchive.lincoln.ac.uk/collections/document/10501 ,
  https://ibccdigitalarchive.lincoln.ac.uk/collections/document/33688
- Guy Gibson, *Enemy Coast Ahead* (1946): https://www.fadedpage.com/books/20251219/20251219.txt
- Charles Foster, Dambusters Blog (crew pages, AJ-J route re-creation, crash-site guide):
  https://dambustersblog.com/2013/04/08/the-dams-raid-complete-list-of-all-participants/ ,
  https://dambustersblog.com/2011/09/21/dams-raid-route-%E2%80%93-a-modern-re-creation/ ,
  https://dambustersblog.com/2022/09/26/dambuster-crash-sites-revised-drivers-guide/
- dambusters.org.uk: https://www.dambusters.org.uk/about.htm
- LWL Westfälische Geschichte, Möhnekatastrophe:
  https://www.lwl.org/westfaelische-geschichte/portal/Internet/input_felder/langDatensatz_ebene4.php?urlID=493&url_tabelle=tab_websegmente
- de.wikipedia: Möhnekatastrophe, Möhnetalsperre, Edertalsperre, Sorpetalsperre,
  Ennepetalsperre, Bevertalsperre, Listertalsperre, Diemeltalsperre
- Hinks, Heitefuss & Chrimes, "The Dambusters Revisited", British Dams Society (2010):
  https://britishdams.org/2010conf/papers/3-1.%20Hinks%20-%20The%20Dambusters%20Revisited.pdf
- RAF Museum, "The Dams Raid" podcast transcript:
  https://www.rafmuseum.org.uk/documents/podcasts/transcripts/the_dams_raid.pdf
- The London Gazette, Supplement 36030, 28 May 1943, p. 2361 (Gibson's Victoria Cross; the
  DSOs for McCarthy, Maltby and Martin): https://www.thegazette.co.uk/London/issue/36030/supplement/2361
- Wikipedia: Operation Chastise, RAF Scampton, St Vincents Hall —
  https://en.wikipedia.org/wiki/Operation_Chastise
- Aviation Safety Network wikibase entries for the eight losses (via
  https://asntest.flightsafety.org/wikibase/)
- Arnsberg and Bezirksregierung Arnsberg on the Möhnewiesen camp:
  https://www.bra.nrw.de/presse/die-vergessenen-opfer-der-moehne-katastrophe
- Dam crests and sites: © OpenStreetMap contributors (ODbL), read through Overpass and
  Nominatim.
- Photographs: Flying Officer Jerry Fray, No. 542 Squadron RAF, 17 May 1943, public domain
  (Wikimedia Commons, "Mohne Dam Breached.jpg"); Bundesarchiv, Bild 101I-637-4192-20 /
  Schalber / CC BY-SA 3.0 DE; Bundesarchiv, Bild 183-C0212-0043-012 / CC BY-SA 3.0 DE. The
  drapes, projections and renders derived from the Bundesarchiv photographs are
  CC BY-SA 3.0 DE.
- Imagery and terrain bundled under `media/`: Geobasis NRW DOP and DOM1 at the Möhne, HVBG
  Hessen DOP20 and DGM1 at the Eder, all dl-de/zero-2-0.
