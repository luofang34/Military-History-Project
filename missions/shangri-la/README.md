# Shangri-La

The Doolittle Raid, 18 April 1942: sixteen B-25s from USS *Hornet*, the attacks on Japan,
and the flight to China or the Soviet Union. The replay follows the individual aircraft
and gives the rescue effort and subsequent human cost room in the story.

[Open the replay](https://history.sokoly.app/shangri-la/) ·
[Starting article](https://en.wikipedia.org/wiki/Doolittle_Raid)

“Shangri-La” is the name Roosevelt used at his 21 April 1942 press conference to conceal
the bombers’ origin. It is the title of this reconstruction, not an operational codename
used by the raiders.

## Rebuild and check

```sh
python3 missions/shangri-la/build/shangri_la.py
python3 missions/shangri-la/build/test_mission.py
python3 tools/composition.py missions/shangri-la
python3 verify.py
```

Build the viewer and set `SOKOLY_APP` as described in the repository’s `AGENTS.md`.
The generator writes the operation, events, presentation, tables below, stable facts and
content manifest. No downloaded dependency or network request is needed to regenerate it.

## Method and limits

The action runs from 06:30 to 22:10 **Japan time (UTC+9)** on 18 April. Authoring tables
and the original reports use **ship time (UTC+10)**: subtract one hour for the screen.
Thus Doolittle’s 08:20 take-off and 13:30 bombing become 07:20 and 12:30 in Japan.
Times over China remain on the same clock; the replay never silently switches zones.
The naval “zone minus ten” convention means UTC+10, not UTC−10.

The primary spine is Mitscher’s and Murray’s action reports and Doolittle’s compilation,
including the pilots’ individual reports and Potter’s navigation anchors. HyperWar supplies
transcriptions, not verified facsimiles: missing pages, inconsistent serials, names and times
are retained in the ledger or described here. The aircraft roster cross-checks all sixteen
serials and outcomes against the Children of the Doolittle Raiders archive. The malformed
opening roster in the report is not used as a clean manifest. Contemporary claims of bomb
and fighter damage are not treated as independent confirmation.

Every moving position is marked **reconstructed**. Between the carrier, coast, target district
and recovery-region anchors, paths are illustrative great-circle segments. They are not
radar tracks, complete navigator logs, precise attack runs or surveyed crash positions.
Flight heights are illustrative above-ground heights, not conversions of historical barometric
altitudes. The mission has no fabricated Japanese fighter tracks, kill animations, bomb-impact
points or precision wreck locations. Symbols disappear at estimated bailouts; this represents
loss of the aircraft track, not an assertion that every airman died.

Hornet starts from its reported 0800 position and a plausible turn into wind. Enterprise and
Nashville are contextual offsets, not a recovered formation plot. The other escorts are not
individually tracked. The retiring ships continue east at a reconstructed 25 knots. Most flight
fixes carry 40 km horizontal bounds and terminal regions 80 km; these are editorial uncertainty
bounds, not statistical confidence intervals. The distinct terminal times for aircraft without
reliable clocks are estimates, explicitly recorded as such. China’s interior recovery areas
must not be read as exact bailout sites. Quzhou is the Chuchow intended as the refuelling field;
Lishui was also called Chuchow in contemporary romanization, so the two must not be conflated.

The closing two notes are explicitly retrospective. They do not place the October executions,
Meder’s death, Roosevelt’s press conference or the Zhejiang–Jiangxi campaign on the raid-day
clock. The reprisal-toll fact is undated because it concerns a campaign, not one moment.
Japanese civilian deaths are part of the raid’s account; the often-cited 87 deaths is a postwar
count reported by the starting article. The Chinese campaign’s estimated 250,000 deaths is
not a count of rescuers and is not presented as exact. Japanese decisions and responsibility
for the reprisals remain explicit. The Midway plan predated the raid; the raid strengthened
its advocates rather than creating it.

## Preparation and consequences

Navy Captain Francis Low’s carrier-launch proposal and Doolittle’s planning joined Army
bombers to naval reach. Crews trained for short take-offs at Eglin; extra tanks, removal of
the lower turret and a simple low-altitude bombsight supported the mission. Hornet departed
Alameda on 2 April and joined Enterprise on 13 April. Discovery by Japanese pickets forced
an early departure before the carriers could reach their intended launch area.
The AAF official history also describes restricted information to China, Chiang’s concern
about retaliation and resistance to using Chuchow, and preparations expecting a later arrival.
Bad weather was therefore only part of the failure to complete the planned landing.

Holstrom jettisoned his bombs without attacking a land target. York’s aircraft was impounded
in the USSR, whose neutrality toward Japan also meant internment for its crew. Fifteen bombers
were lost in China. Of the eighty airmen, three died at the end of the flight, eight became
Japanese prisoners, five were interned in the USSR, and sixty-four evaded capture in China.
Chinese civilians, soldiers and local networks were essential to their survival; Smith’s
flight surgeon Thomas White also helped the seriously injured Lawson.

Japan executed Hallmark, Farrow and Spatz on 15 October 1942. Meder died in captivity in
December 1943; the four other prisoners survived until 1945. The Japanese Zhejiang–Jiangxi
campaign targeted airfields and punished communities, with massacres and biological warfare.
Its human cost belongs beside the raid’s boost to American morale and its limited physical
effect on Japan’s war production. The ledger distinguishes estimates, contemporary knowledge
and later findings.

## Aircraft

Launch times follow Doolittle’s compiled aircraft accounts; conflicting readings appear below.
Attack districts and terminal outcomes do not imply precise coordinates.

<!-- crew table -->
| No. | Aircraft | Pilot | Launch (ship) | Attack / release | End of flight |
| --- | --- | --- | --- | --- | --- |
| 1 | 40-2344 | James H. Doolittle | 08:20 | Tokyo industrial districts; four incendiary clusters | bailout |
| 2 | 40-2292 | Travis Hoover | 08:25 | Tokyo arsenal district | forced landing |
| 3 | 40-2270 | Robert M. Gray | 08:30 | Tokyo gas and chemical works | bailout |
| 4 | 40-2282 | Everett W. Holstrom | 08:33 | Bombs jettisoned offshore under fighter attack | bailout |
| 5 | 40-2283 | David M. Jones | 08:37 | Tokyo oil, power and factory targets | bailout |
| 6 | 40-2298 | Dean E. Hallmark | 08:40 | Tokyo; detailed attack report unavailable | ditching |
| 7 | 40-2261 | Ted W. Lawson | 08:43 | Tokyo factories and residential area | ditching |
| 8 | 40-2242 | Edward J. York | 08:46 | Tokyo; then Soviet diversion | internment |
| 9 | 40-2303 | Harold F. Watson | 08:50 | Tokyo Gas and Electric; identification disputed | bailout |
| 10 | 40-2250 | Richard O. Joyce | 08:53 | Japan Special Steel and surrounding Tokyo districts | bailout |
| 11 | 40-2249 | Charles R. Greening | 08:56 | Reported refinery near Sakura; identification uncertain | bailout |
| 12 | 40-2278 | William M. Bower | 08:59 | Yokohama refinery and factories | bailout |
| 13 | 40-2247 | Edgar E. McElroy | 09:01 | Yokosuka naval yard | bailout |
| 14 | 40-2297 | John A. Hilger | 09:07 | Nagoya barracks, oil storage, arsenal and aircraft works | bailout |
| 15 | 40-2267 | Donald G. Smith | 09:15 | Kobe waterfront and aircraft industry | ditching |
| 16 | 40-2268 | William G. Farrow | 09:19 | Nagoya; detailed contemporary report unavailable | bailout |
<!-- end crew table -->

## Evidence ledger

Records marked as quotations preserve the checked transcription’s wording. Other records are
concise paraphrases; “checked” means compared with the linked publication, not its underlying
archival original. Approximate attack and recovery minutes are disputes with explicit bases,
so an editorial estimate cannot silently become a reported fact.

<!-- evidence ledger: generated by build/shangri_la.py from build/evidence/ -->
| Dispute | Records (source: what it says) | Replay estimate and basis |
| --- | --- | --- |
| Distances to Japan use different reference points and units (`launch-distance`) | [Doolittle, report of 5 June 1942, aircraft accounts](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#1): Gives the launch as approximately 824 statute miles east of central Tokyo.<br>[Murray, Enterprise action report, 23 April 1942](https://www.ibiblio.org/hyperwar/USN/ships/logs/CV/cv6-Tokyo.html): Describes the first launch as approximately 650 miles from Tokyo. | **Use the geographic fixes, not a distance ring**. Doolittle’s navigator coordinate is about 1,231 km from the Tokyo district used here. It does not exactly reproduce either prose distance; coast versus city and nautical versus statute miles matter. |
| When the picket was sighted (`picket-contact`) | [Mitscher, Hornet action report, 28 April 1942](https://www.ibiblio.org/hyperwar/USN/ships/logs/CV/cv8-Tokyo.html): Patrol craft sighted at 0738, bearing 220°, 20,000 yards.<br>[Murray, Enterprise action report, 23 April 1942](https://www.ibiblio.org/hyperwar/USN/ships/logs/CV/cv6-Tokyo.html): Patrol vessel sighted at 0744, bearing 221°, 10,000 yards.<br>[Doolittle Raid, Wikipedia (research starting point)](https://en.wikipedia.org/wiki/Doolittle_Raid): Identifies the sighting vessel as No. 23 Nittō Maru. | **07:38 ship / 06:38 Japan**. Use Hornet’s first sighting; the ships had different viewpoints. |
| Doolittle’s launch time (`doolittle-launch`) | [Doolittle and Potter, personal and navigation reports, 4 May 1942](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#11): “Take off at 8:20 A.M. ship time.”<br>[Mitscher, Hornet action report, 28 April 1942](https://www.ibiblio.org/hyperwar/USN/ships/logs/CV/cv8-Tokyo.html): First B-25 launched at 0825.<br>[Murray, Enterprise action report, 23 April 1942](https://www.ibiblio.org/hyperwar/USN/ships/logs/CV/cv6-Tokyo.html): First bomber launched at 0820. | **08:20 ship / 07:20 Japan**. The pilot and Enterprise agree; retain Hornet’s five-minute difference. |
| The offshore launch position (`launch-position`) | [Mitscher, Hornet action report, 28 April 1942](https://www.ibiblio.org/hyperwar/USN/ships/logs/CV/cv8-Tokyo.html): 0800 position: 35°26′N, 153°27′E.<br>[Doolittle and Potter, personal and navigation reports, 4 May 1942](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#11): Navigator gives take-off at 35°43′N, 153°25′E. | **Hornet’s 0800 fix, followed by a reconstructed 22-knot turn into wind**. The latitude difference is about 31 km; use a 40 km horizontal bound. Neither point is an exact deck trajectory. |
| Farrow leaves last (`last-launch`) | [Doolittle, report of 5 June 1942, aircraft accounts](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#1): Farrow’s 40-2268 took off at 9:19 a.m. ship time.<br>[Mitscher, Hornet action report, 28 April 1942](https://www.ibiblio.org/hyperwar/USN/ships/logs/CV/cv8-Tokyo.html): Last bomber launched at 0920.<br>[Murray, Enterprise action report, 23 April 1942](https://www.ibiblio.org/hyperwar/USN/ships/logs/CV/cv6-Tokyo.html): Last bomber off at 0921. | **09:19 ship / 08:19 Japan**. Use the individual aircraft account; naval completion reports differ by one or two minutes. |
| Travis Hoover launches (`hoover-launch`) | [Doolittle, report of 5 June 1942, aircraft accounts](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#1): 40-2292: take-off 08:25 ship time.<br>[Mitscher, Hornet action report, 28 April 1942](https://www.ibiblio.org/hyperwar/USN/ships/logs/CV/cv8-Tokyo.html): Second plane seven minutes after the first at 0825. | **08:25 ship time**. Use the compiled aircraft sequence consistently. Preserve conflicting individual timings in the ledger. |
| Richard O. Joyce launches (`joyce-launch`) | [Doolittle, report of 5 June 1942, aircraft accounts](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#1): 40-2250: take-off 08:53 ship time.<br>[Joyce, mission and personal reports, May 1942](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#3): The transcription gives 08:05, explicitly zone minus ten. | **08:53 ship time**. Use the compiled aircraft sequence consistently. Preserve conflicting individual timings in the ledger. Joyce’s 08:05 would precede the lead aircraft and is unusable as a sequence anchor. |
| Charles R. Greening launches (`greening-launch`) | [Doolittle, report of 5 June 1942, aircraft accounts](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#1): 40-2249: take-off 08:56 ship time.<br>[Greening, mission report, 2 May 1942](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#5): Time of take-off 0855 Hornet time. | **08:56 ship time**. Use the compiled aircraft sequence consistently. Preserve conflicting individual timings in the ledger. |
| William M. Bower launches (`bower-launch`) | [Doolittle, report of 5 June 1942, aircraft accounts](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#1): 40-2278: take-off 08:59 ship time.<br>[Bower, mission report, 2 May 1942](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#6): Time of take-off 0910. | **08:59 ship time**. Use the compiled aircraft sequence consistently. Preserve conflicting individual timings in the ledger. |
| Edgar E. McElroy launches (`mcelroy-launch`) | [Doolittle, report of 5 June 1942, aircraft accounts](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#1): 40-2247: take-off 09:01 ship time.<br>[McElroy, personal report, 4 May 1942](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#10): Personal report gives 0900. | **09:01 ship time**. Use the compiled aircraft sequence consistently. Preserve conflicting individual timings in the ledger. |
| John A. Hilger launches (`hilger-launch`) | [Doolittle, report of 5 June 1942, aircraft accounts](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#1): 40-2297: take-off 09:07 ship time.<br>[Hilger, mission and personal reports, 5 May 1942](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#8): Mission report gives 09:13; personal report gives 09:15.<br>[Hilger, report of airplane 40-2297](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#9): Take-off made at 09:15. | **09:07 ship time**. Use the compiled aircraft sequence consistently. Preserve conflicting individual timings in the ledger. |
| Reported hits and the raid’s material effect (`damage-assessment`) | [Doolittle, report of 5 June 1942, aircraft accounts](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#1): Initial assessment claimed damage exceeded expectations.<br>[AAF Intelligence Summary No. 20, 5 October 1942](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Summary_20.html): Pilot observations describe explosions and fires, including residential districts.<br>[Doolittle Raid, Wikipedia (research starting point)](https://en.wikipedia.org/wiki/Doolittle_Raid): Postwar count: 87 killed, 151 seriously injured and more than 311 lightly injured in Japan. | **Local destruction and civilian deaths; limited overall military damage**. Aircrew claims are not a surveyed damage assessment. No destroyed target or confirmed fighter-kill symbols are drawn. |
| What Greening bombed (`greening-target`) | [Greening, mission report, 2 May 1942](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#5): Reported an oil refinery and storage tanks.<br>[AAF Intelligence Summary No. 20, 5 October 1942](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Summary_20.html): Identifies a reported refinery near Sakura; Yokohama primary not reached. | **A broad district east of Tokyo, with 40 km uncertainty**. The identification is a crew report; no exact refinery footprint is asserted. This uncertainty also covers the route to it. |
| Watson’s target identification (`watson-target`) | [AAF Intelligence Summary No. 20, 5 October 1942](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Summary_20.html): Tokyo Gas and Electric; the same target was also reported as a tank and truck factory. | **Tokyo industrial district, not an identified building**. The summary itself records competing identifications. Use a 40 km bound. |
| Travis Hoover over the target area (`hoover-attack`) | [AAF Intelligence Summary No. 20, 5 October 1942](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Summary_20.html): Tokyo arsenal district; no precise attack clock adopted from this account. | **13:35 ship time, approximate**. An editorial placement within the raid, constrained by the launch, destination and feasible transit. The route and minute are reconstructed; this does not establish a bomb impact location. |
| Robert M. Gray over the target area (`gray-attack`) | [AAF Intelligence Summary No. 20, 5 October 1942](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Summary_20.html): Tokyo gas and chemical works; no precise attack clock adopted from this account. | **13:40 ship time, approximate**. An editorial placement within the raid, constrained by the launch, destination and feasible transit. The route and minute are reconstructed; this does not establish a bomb impact location. |
| Holstrom jettisons his bombs (`holstrom-attack`) | [AAF Intelligence Summary No. 20, 5 October 1942](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Summary_20.html): Bombs jettisoned offshore under fighter attack; no precise attack clock adopted from this account. | **13:35 ship time, approximate**. An editorial placement within the raid, constrained by the launch, destination and feasible transit. The route and minute are reconstructed; this does not establish a bomb impact location. |
| David M. Jones over the target area (`jones-attack`) | [AAF Intelligence Summary No. 20, 5 October 1942](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Summary_20.html): Tokyo oil, power and factory targets; no precise attack clock adopted from this account. | **13:45 ship time, approximate**. An editorial placement within the raid, constrained by the launch, destination and feasible transit. The route and minute are reconstructed; this does not establish a bomb impact location. |
| Dean E. Hallmark over the target area (`hallmark-attack`) | [Doolittle, report of 5 June 1942, aircraft accounts](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#1): Tokyo; detailed attack report unavailable; no precise attack clock adopted from this account. | **13:50 ship time, approximate**. An editorial placement within the raid, constrained by the launch, destination and feasible transit. The route and minute are reconstructed; this does not establish a bomb impact location. |
| Ted W. Lawson over the target area (`lawson-attack`) | [AAF Intelligence Summary No. 20, 5 October 1942](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Summary_20.html): Tokyo factories and residential area; no precise attack clock adopted from this account. | **13:45 ship time, approximate**. An editorial placement within the raid, constrained by the launch, destination and feasible transit. The route and minute are reconstructed; this does not establish a bomb impact location. |
| Edward J. York over the target area (`york-attack`) | [AAF Intelligence Summary No. 20, 5 October 1942](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Summary_20.html): Tokyo; then Soviet diversion; no precise attack clock adopted from this account. | **13:50 ship time, approximate**. An editorial placement within the raid, constrained by the launch, destination and feasible transit. The route and minute are reconstructed; this does not establish a bomb impact location. |
| Harold F. Watson over the target area (`watson-attack`) | [AAF Intelligence Summary No. 20, 5 October 1942](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Summary_20.html): Tokyo Gas and Electric; identification disputed; no precise attack clock adopted from this account. | **14:00 ship time, approximate**. An editorial placement within the raid, constrained by the launch, destination and feasible transit. The route and minute are reconstructed; this does not establish a bomb impact location. |
| Richard O. Joyce over the target area (`joyce-attack`) | [AAF Intelligence Summary No. 20, 5 October 1942](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Summary_20.html): Japan Special Steel and surrounding Tokyo districts; no precise attack clock adopted from this account. | **14:00 ship time, approximate**. An editorial placement within the raid, constrained by the launch, destination and feasible transit. The route and minute are reconstructed; this does not establish a bomb impact location. |
| Charles R. Greening over the target area (`greening-attack`) | [AAF Intelligence Summary No. 20, 5 October 1942](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Summary_20.html): Reported refinery near Sakura; identification uncertain; no precise attack clock adopted from this account. | **14:10 ship time, approximate**. An editorial placement within the raid, constrained by the launch, destination and feasible transit. The route and minute are reconstructed; this does not establish a bomb impact location. |
| William M. Bower over the target area (`bower-attack`) | [AAF Intelligence Summary No. 20, 5 October 1942](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Summary_20.html): Yokohama refinery and factories; no precise attack clock adopted from this account. | **14:15 ship time, approximate**. An editorial placement within the raid, constrained by the launch, destination and feasible transit. The route and minute are reconstructed; this does not establish a bomb impact location. |
| Donald G. Smith over the target area (`smith-attack`) | [AAF Intelligence Summary No. 20, 5 October 1942](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Summary_20.html): Kobe waterfront and aircraft industry; no precise attack clock adopted from this account. | **15:45 ship time, approximate**. An editorial placement within the raid, constrained by the launch, destination and feasible transit. The route and minute are reconstructed; this does not establish a bomb impact location. |
| William G. Farrow over the target area (`farrow-attack`) | [Children of the Doolittle Raiders, sixteen crew roster](https://childrenofthedoolittleraiders.com/crew-members/doolittle-raider-crews/): Farrow attacked Nagoya; no contemporary pilot report survives in the checked compilation. | **15:30 ship time, approximate**. An editorial placement within the raid, constrained by the launch, destination and feasible transit. The route and minute are reconstructed; this does not establish a bomb impact location. |
| Doolittle’s crew abandons its bomber (`doolittle-bailout`) | [Doolittle and Potter, personal and navigation reports, 4 May 1942](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#11): Pilot gives 21:20 ship time.<br>[Doolittle and Potter, personal and navigation reports, 4 May 1942](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#11): Navigator gives 21:15–21:20. | **21:20 ship / 20:20 Japan**. Use the pilot’s time at the end of the navigator’s five-minute interval; no second-level accuracy is claimed. |
| Confused early reports of Hallmark’s fate (`hallmark-loss-location`) | [Doolittle, report of 5 June 1942, aircraft accounts](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#1): Initial information placed Hallmark near Nanchang/Poyang and explicitly warned it was unreliable.<br>[Children of the Doolittle Raiders, sixteen crew roster](https://childrenofthedoolittleraiders.com/crew-members/doolittle-raider-crews/): Crew 6 ditched; three captured.<br>[Doolittle Raid, Wikipedia (research starting point)](https://en.wikipedia.org/wiki/Doolittle_Raid): Hallmark’s bomber ditched off Wenzhou. Dieter and Fitzmaurice drowned. | **Wenzhou coastal area, 80 km bound**. Use the later coastal account; do not map the unconfirmed Poyang report as a crash site. |
| Confused early reports of Farrow’s fate (`farrow-loss-location`) | [Doolittle, report of 5 June 1942, aircraft accounts](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#1): Places Farrow near Shipu and warns that accounts of his and Hallmark’s crews may be confused.<br>[Children of the Doolittle Raiders, sixteen crew roster](https://childrenofthedoolittleraiders.com/crew-members/doolittle-raider-crews/): All five of Farrow’s crew became prisoners. | **Shipu region, 80 km bound**. This is a recovery region, not a precise bailout or capture coordinate. |
| Why the intended landing was not available (`chinese-airfield-preparations`) | [Doolittle and Potter, personal and navigation reports, 4 May 1942](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#11): Could not raise Chuchow by radio; cloud and darkness prevented a landing.<br>[Craven and Cate, The Army Air Forces in World War II, vol. I, chapter 12, pp. 438–444](https://www.ibiblio.org/hyperwar/AAF/I/AAF-I-12.html): Secrecy restricted Chinese information; fields expected arrivals later, and Chiang resisted using Chuchow. | **Weather, fuel, disrupted timing and incomplete coordination**. The immediate crew experience and the official planning history explain different parts of the failure; do not blame it solely on weather or portray Chinese assistance as absent. |
| Deaths in the Zhejiang–Jiangxi campaign (`chinese-reprisal-toll`) | [James M. Scott, Chinese reprisals, Smithsonian, 15 April 2015](https://www.smithsonianmag.com/history/untold-story-vengeful-japanese-attack-doolittle-raid-180955001/): Estimates a quarter-million deaths; documents massacres, destruction and biological warfare.<br>[Samuel Cox, NHHC H-004-4: Doolittle Raid](https://www.history.navy.mil/about-us/leadership/director/directors-corner/h-grams/h-gram-004/h-004-4.html): Attributes 250,000 to Chiang Kai-shek and Chennault; says the real total is unknown. | **An estimated 250,000, with the total uncertain**. This describes the subsequent 1942 campaign, not deaths on 18 April or a count of people who directly helped airmen. No raid-day timestamp is assigned. |
| Travis Hoover loses the aircraft in China (`hoover-recovery`) | [Children of the Doolittle Raiders, sixteen crew roster](https://childrenofthedoolittleraiders.com/crew-members/doolittle-raider-crews/): 40-2292: forced landing; 5 survived the flight, 0 subsequently captured by Japan. | **21:10 ship time, approximate**. Outcome is documented; the terminal minute and regional coordinate are reconstruction. Bailout symbols disappear rather than drawing an invented crash descent. |
| Robert M. Gray loses the aircraft in China (`gray-recovery`) | [Children of the Doolittle Raiders, sixteen crew roster](https://childrenofthedoolittleraiders.com/crew-members/doolittle-raider-crews/): 40-2270: bailout; 4 survived the flight, 0 subsequently captured by Japan. | **22:15 ship time, approximate**. Outcome is documented; the terminal minute and regional coordinate are reconstruction. Bailout symbols disappear rather than drawing an invented crash descent. |
| Everett W. Holstrom loses the aircraft in China (`holstrom-recovery`) | [Children of the Doolittle Raiders, sixteen crew roster](https://childrenofthedoolittleraiders.com/crew-members/doolittle-raider-crews/): 40-2282: bailout; 5 survived the flight, 0 subsequently captured by Japan. | **22:00 ship time, approximate**. Outcome is documented; the terminal minute and regional coordinate are reconstruction. Bailout symbols disappear rather than drawing an invented crash descent. |
| David M. Jones loses the aircraft in China (`jones-recovery`) | [Children of the Doolittle Raiders, sixteen crew roster](https://childrenofthedoolittleraiders.com/crew-members/doolittle-raider-crews/): 40-2283: bailout; 5 survived the flight, 0 subsequently captured by Japan. | **22:10 ship time, approximate**. Outcome is documented; the terminal minute and regional coordinate are reconstruction. Bailout symbols disappear rather than drawing an invented crash descent. |
| Dean E. Hallmark loses the aircraft in China (`hallmark-recovery`) | [Children of the Doolittle Raiders, sixteen crew roster](https://childrenofthedoolittleraiders.com/crew-members/doolittle-raider-crews/): 40-2298: ditching; 3 survived the flight, 3 subsequently captured by Japan. | **22:00 ship time, approximate**. Outcome is documented; the terminal minute and regional coordinate are reconstruction. Bailout symbols disappear rather than drawing an invented crash descent. |
| Ted W. Lawson loses the aircraft in China (`lawson-recovery`) | [Children of the Doolittle Raiders, sixteen crew roster](https://childrenofthedoolittleraiders.com/crew-members/doolittle-raider-crews/): 40-2261: ditching; 5 survived the flight, 0 subsequently captured by Japan. | **21:00 ship time, approximate**. Outcome is documented; the terminal minute and regional coordinate are reconstruction. Bailout symbols disappear rather than drawing an invented crash descent. |
| Edward J. York lands in the Soviet Union (`york-recovery`) | [Children of the Doolittle Raiders, sixteen crew roster](https://childrenofthedoolittleraiders.com/crew-members/doolittle-raider-crews/): 40-2242: internment; 5 survived the flight, 0 subsequently captured by Japan. | **19:30 ship time, approximate**. Outcome is documented; the terminal minute and regional coordinate are reconstruction. Bailout symbols disappear rather than drawing an invented crash descent. |
| Harold F. Watson loses the aircraft in China (`watson-recovery`) | [Children of the Doolittle Raiders, sixteen crew roster](https://childrenofthedoolittleraiders.com/crew-members/doolittle-raider-crews/): 40-2303: bailout; 5 survived the flight, 0 subsequently captured by Japan. | **22:30 ship time, approximate**. Outcome is documented; the terminal minute and regional coordinate are reconstruction. Bailout symbols disappear rather than drawing an invented crash descent. |
| Richard O. Joyce loses the aircraft in China (`joyce-recovery`) | [Children of the Doolittle Raiders, sixteen crew roster](https://childrenofthedoolittleraiders.com/crew-members/doolittle-raider-crews/): 40-2250: bailout; 5 survived the flight, 0 subsequently captured by Japan. | **22:20 ship time, approximate**. Outcome is documented; the terminal minute and regional coordinate are reconstruction. Bailout symbols disappear rather than drawing an invented crash descent. |
| Charles R. Greening loses the aircraft in China (`greening-recovery`) | [Children of the Doolittle Raiders, sixteen crew roster](https://childrenofthedoolittleraiders.com/crew-members/doolittle-raider-crews/): 40-2249: bailout; 5 survived the flight, 0 subsequently captured by Japan. | **22:40 ship time, approximate**. Outcome is documented; the terminal minute and regional coordinate are reconstruction. Bailout symbols disappear rather than drawing an invented crash descent. |
| William M. Bower loses the aircraft in China (`bower-recovery`) | [Children of the Doolittle Raiders, sixteen crew roster](https://childrenofthedoolittleraiders.com/crew-members/doolittle-raider-crews/): 40-2278: bailout; 5 survived the flight, 0 subsequently captured by Japan. | **22:30 ship time, approximate**. Outcome is documented; the terminal minute and regional coordinate are reconstruction. Bailout symbols disappear rather than drawing an invented crash descent. |
| Donald G. Smith loses the aircraft in China (`smith-recovery`) | [Children of the Doolittle Raiders, sixteen crew roster](https://childrenofthedoolittleraiders.com/crew-members/doolittle-raider-crews/): 40-2267: ditching; 5 survived the flight, 0 subsequently captured by Japan. | **22:10 ship time, approximate**. Outcome is documented; the terminal minute and regional coordinate are reconstruction. Bailout symbols disappear rather than drawing an invented crash descent. |
| William G. Farrow loses the aircraft in China (`farrow-recovery`) | [Children of the Doolittle Raiders, sixteen crew roster](https://childrenofthedoolittleraiders.com/crew-members/doolittle-raider-crews/): 40-2268: bailout; 5 survived the flight, 5 subsequently captured by Japan. | **23:00 ship time, approximate**. Outcome is documented; the terminal minute and regional coordinate are reconstruction. Bailout symbols disappear rather than drawing an invented crash descent. |

Key moments, on which the sources agree:

| Moment | Records (source: what it says) | Time |
| --- | --- | --- |
| Nashville opens fire on the Japanese picket (`nashville-opens-fire`) | [Mitscher, Hornet action report, 28 April 1942](https://www.ibiblio.org/hyperwar/USN/ships/logs/CV/cv8-Tokyo.html): Nashville opened fire at 0755; Enterprise aircraft also attacked the vessel. | 07:55 |
| Halsey orders the Army bombers launched (`launch-order`) | [Mitscher, Hornet action report, 28 April 1942](https://www.ibiblio.org/hyperwar/USN/ships/logs/CV/cv8-Tokyo.html): Received the task-force commander’s launch order at 0800. | 08:00 |
| The carrier force turns east (`fleet-retirement`) | [Murray, Enterprise action report, 23 April 1942](https://www.ibiblio.org/hyperwar/USN/ships/logs/CV/cv6-Tokyo.html): Force commenced retirement eastward at 0927, 25 knots. | 09:27 |
| Robert M. Gray launches (`gray-launch`) | [Doolittle, report of 5 June 1942, aircraft accounts](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#1): 40-2270: take-off 08:30 ship time. | 08:30 |
| Everett W. Holstrom launches (`holstrom-launch`) | [Doolittle, report of 5 June 1942, aircraft accounts](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#1): 40-2282: take-off 08:33 ship time. | 08:33 |
| David M. Jones launches (`jones-launch`) | [Doolittle, report of 5 June 1942, aircraft accounts](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#1): 40-2283: take-off 08:37 ship time. | 08:37 |
| Dean E. Hallmark launches (`hallmark-launch`) | [Doolittle, report of 5 June 1942, aircraft accounts](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#1): 40-2298: take-off 08:40 ship time. | 08:40 |
| Ted W. Lawson launches (`lawson-launch`) | [Doolittle, report of 5 June 1942, aircraft accounts](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#1): 40-2261: take-off 08:43 ship time. | 08:43 |
| Edward J. York launches (`york-launch`) | [Doolittle, report of 5 June 1942, aircraft accounts](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#1): 40-2242: take-off 08:46 ship time. | 08:46 |
| Harold F. Watson launches (`watson-launch`) | [Doolittle, report of 5 June 1942, aircraft accounts](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#1): 40-2303: take-off 08:50 ship time. | 08:50 |
| Donald G. Smith launches (`smith-launch`) | [Doolittle, report of 5 June 1942, aircraft accounts](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#1): 40-2267: take-off 09:15 ship time. | 09:15 |
| Doolittle bombs Tokyo (`doolittle-attack`) | [Doolittle and Potter, personal and navigation reports, 4 May 1942](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#11): “Dropped first bomb at 1:30 (ship time).” | 13:30 |
| McElroy attacks Yokosuka naval yard (`mcelroy-attack`) | [McElroy, personal report, 4 May 1942](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#10): Bombs dropped about 1440; a crane and ship in the slips were reported hit. | 14:40 |
| Hilger attacks Nagoya (`hilger-attack`) | [Hilger, report of airplane 40-2297](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#9): Attack at 15:20, explicitly zone minus ten; four incendiary targets. | 15:20 |
| McElroy’s crew bails out (`mcelroy-bailout`) | [McElroy, personal report, 4 May 1942](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#10): Crew bailed out at 2245; Williams injured his knee. | 22:45 |
| Hilger orders his crew to jump (`hilger-bailout`) | [Hilger, report of airplane 40-2297](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#9): At 22:20, an estimated position over Chuchow and about 40 gallons remaining; ordered crew out. | 22:20 |
<!-- end of evidence ledger -->

## Camera

Moves are specified in viewing seconds. The pacing accelerates the long ocean legs and adds
beats to the launch and documented bombing passes. The camera promises only what its frame
can show; the wide recovery shots do not claim to display each disappearing aircraft.

<!-- camera table -->
| Ship time | Intent | Entities promised |
| --- | --- | --- |
| 07:30–07:38 | Establish the carrier force far east of Japan before discovery. | HORNET, TOKYO |
| 07:38–08:00 | Close on the ships as a Japanese picket forces the decision to launch. | HORNET, ENTERPRISE, NASHVILLE |
| 08:00–08:20 | Hold on Hornet while the crews prepare and the carrier turns into wind. | HORNET |
| 08:20–08:21 | Follow Doolittle off the deck and into the open Pacific. | B25-01, HORNET |
| 08:21–09:19 | Pull back to the departure stream as the other crews launch separately. | HORNET |
| 09:19–09:27 | Show Farrow, the last bomber, clearing the retiring carriers. | B25-16, HORNET |
| 09:27–12:50 | Open the scale of the ocean crossing without holding the quiet transit. | B25-01 |
| 12:50–13:25 | Follow the lead aircraft to landfall north of its intended course. | B25-01 |
| 13:25–13:32 | Tighten on the lead bombing pass over Tokyo. | B25-01 |
| 13:32–13:39 | Cut to Holstrom offshore: a crew unable to complete its attack. | B25-04 |
| 13:39–14:05 | Re-establish the dispersed attacks around Tokyo, not a massed bomber formation. | TOKYO |
| 14:05–14:32 | Shift southeast to Greening and Bower’s reported industrial targets. | YOKOHAMA |
| 14:32–14:48 | Cut to the documented Yokosuka pass and follow McElroy out. | B25-13 |
| 14:48–15:16 | Cut west to the aircraft assigned beyond the Tokyo region. | NAGOYA, KOBE |
| 15:16–15:28 | Follow Hilger across his Nagoya target area at the reported attack time. | B25-14 |
| 15:28–15:52 | Cut to Smith at Kobe, completing the western attacks. | B25-15 |
| 15:52–17:10 | Pull out along the southwest escape route toward the East China Sea. | B25-01 |
| 17:10–19:35 | Cut north to York’s separate flight to Soviet territory. | B25-08 |
| 19:35–20:50 | Return to the Chinese coast as the weather closes in. | NINGBO, QUZHOU |
| 20:50–21:25 | Show the coastal and inland separation as Lawson, Hoover and Doolittle come down. | NINGBO, QUZHOU |
| 21:25–22:18 | Widen across the recovery region to place the losses in China. | QUZHOU, NINGBO |
| 22:18–23:01 | Resolve the final aircraft losses across Zhejiang and Jiangxi. | QUZHOU, SHANGRAO |
| 23:01–23:05 | Hold the region for the later human consequences, explicitly outside the raid-day clock. | QUZHOU |
| 23:05–23:10 | End at regional scale, connecting the secret launch, American morale and the cost in China. | TOKYO, QUZHOU |
<!-- end camera table -->

## Sources

US government reports are public-domain documents. The modern sources are linked and
summarized; no archival photographs or third-party map assets are redistributed in this package.

<!-- sources -->
- [Doolittle, report of 5 June 1942, aircraft accounts](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#1)
- [Doolittle and Potter, personal and navigation reports, 4 May 1942](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#11)
- [Gray, mission report, 2 May 1942](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#2)
- [Joyce, mission and personal reports, May 1942](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#3)
- [Greening, mission report, 2 May 1942](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#5)
- [Bower, mission report, 2 May 1942](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#6)
- [McElroy, personal report, 4 May 1942](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#10)
- [Hilger, mission and personal reports, 5 May 1942](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#8)
- [Hilger, report of airplane 40-2297](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Report.html#9)
- [Mitscher, Hornet action report, 28 April 1942](https://www.ibiblio.org/hyperwar/USN/ships/logs/CV/cv8-Tokyo.html)
- [Murray, Enterprise action report, 23 April 1942](https://www.ibiblio.org/hyperwar/USN/ships/logs/CV/cv6-Tokyo.html)
- [AAF Intelligence Summary No. 20, 5 October 1942](https://www.ibiblio.org/hyperwar/AAF/rep/Doolittle/Summary_20.html)
- [Children of the Doolittle Raiders, sixteen crew roster](https://childrenofthedoolittleraiders.com/crew-members/doolittle-raider-crews/)
- [Craven and Cate, The Army Air Forces in World War II, vol. I, chapter 12, pp. 438–444](https://www.ibiblio.org/hyperwar/AAF/I/AAF-I-12.html)
- [Roosevelt, press conference, 21 April 1942](https://www.presidency.ucsb.edu/documents/excerpts-from-the-press-conference-39)
- [Samuel Cox, NHHC H-004-4: Doolittle Raid](https://www.history.navy.mil/about-us/leadership/director/directors-corner/h-grams/h-gram-004/h-004-4.html)
- [James M. Scott, Chinese reprisals, Smithsonian, 15 April 2015](https://www.smithsonianmag.com/history/untold-story-vengeful-japanese-attack-doolittle-raid-180955001/)
- [AFMC, The Doolittle Raiders: Remembering the Mission, 2023](https://www.afmc.af.mil/News/Article-Display/Article/3364744/the-doolittle-raiders-remembering-the-mission/)
- [Doolittle Raid, Wikipedia (research starting point)](https://en.wikipedia.org/wiki/Doolittle_Raid)
<!-- end sources -->
