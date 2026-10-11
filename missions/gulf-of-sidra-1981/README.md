# Gulf of Sidra incident, 19 August 1981

Two US Navy F-14A Tomcats from USS Nimitz (VF-41, Fast Eagle 102 and 107) shoot down two
Libyan Su-22M3 Fitters from Ghurdabiya, the first AIM-9L kills in the Gulf of Sidra
dispute. Clock: Tripoli time (UTC+2), the Libyan clock; Pentagon Zulu times are converted.

This folder is the package (`operation.json`, `events.jsonl`, `presentations/default.json`)
and its generator, `build/`. Regenerate with `python3 build/gulf_of_sidra.py`, then run
`python3 ../../verify.py`.

## Method

Clock times are the sourced anchors. The Biddle tape gives times relative to its start, which
is placed at 07:15 Tripoli time so that its "vector north" falls on Stanik's 07:19 rejoin;
Stanik and the UPI wire give absolute times. Operation zero is 07:00, about when the Pentagon
says the F-14s first picked up the Libyan jets (Washington Post), with ±15 minutes. No source
times the Su-22s' launch. Positions
are `reconstructed`, and each fix carries a horizontal `bound_m`. No published source gives
coordinates for the fight, so the geometry is built in a local nautical-mile frame around the
merge and constrained by the tape's ranges and times.

- **Sourced anchors (clock)**, as tape time → Tripoli time:
  - Venlet's radar contact, 80 miles due south (Stanik), placed at 07:11 (see the ledger).
  - 00:15 → 07:15:15 "twenty miles, twenty thousand feet"; then 16, 14, 8 (tally-ho) and
    6 miles at 00:27, 00:38, 00:54 and 01:03.
  - 01:31 → 07:16:31 "two fitters has shot at my leader". The Atoll launch is placed at
    07:16:23, where the closure puts the pair about 300 m apart.
  - 02:21 → 07:17:21 Kleemann (102) kills the wingman ("shot one of them down"; "clean
    target" at 02:29).
  - 02:34 "Want me shoot my guy down?" / "Shoot him down."
  - 02:53 → 07:17:53 Muczynski (107) kills the leader ("Fox 2 kill from music").
  - 03:05 "His chute is not deploying"; 03:14 "123 DME on the 180"; 03:29 and 03:31 "clear
    to defend yourself"; 03:59 "vector north". Stanik: rejoin at 07:19.
  - Pentagon: shootdowns at 0520Z, equal to 07:20 at UTC+2.
- **Reconstructed geometry**:
  - The merge is placed at 32.07°N 17.05°E. The Pentagon briefing puts the fight "30 miles
    below" 32°30′N and "60 miles from the nearest land" (Washington Post). That is 26 nm below
    the line and 53 nm from the Natural Earth shore. No longitude is published; Stanik's "due
    south" contact puts it roughly north of Ghurdabiya.
  - Su-22s climb from Ghurdabiya (31.0606°N 16.6117°E, Wikipedia/ICAO HLGD) to 20,000 ft,
    the altitude on the tape. The Libyan account says 7,000 m.
  - F-14s fly a racetrack CAP at about 300 kt on the southernmost CAP station (Stanik),
    Kleemann at 18,000 ft and Muczynski 4,000 ft higher. The racetrack is placed just north of
    32°30′N; its shape and exact position are not sourced. They are vectored south at 07:11.
  - The S-3A Diamond Cutter 702 (VS-30, Forrestal) orbits parallel to the shore at 10,000
    ft, then dives to 300 ft and runs north on Nimitz's "Buster North" (Sanders). Sanders puts
    it about 15 miles from shore, and Wikipedia outside the 12 nm limit. Its position along the
    shore is not sourced; it is placed east of Sirte, at least 14 nm from the shore, with a
    30 km bound.
  - The closure is head-on at about 1,000 kt, matching the tape's range calls within 30 %.
    After the merge the Libyans break northwest and southeast and the F-14s turn hard port
    (Stanik). Each kill is placed where an F-14 can reach it between the tape's calls.
  - Each AIM-9L flies from its shooter for 3 s and ends on its target. Each hit Su-22 falls
    to the sea over 40 s; its last fix is the wreck.
  - Nimitz is placed 123 nm due north of 107's position at 03:14, reading "123 DME on the
    180" as the carrier's TACAN. That lands about 100 nm north of 32°30′N, matching the
    Pentagon's "about 100 miles away from the gulf" (Washington Post), and about 190 nm off
    Sirte, close to UPI's "200 miles off the coast". The bound is 40 km.
- **Build checks**: `build/gulf_of_sidra.py` fails if:
  - the F-14 to Su-22 range at the tape's calls drifts more than 30 % from the call;
  - the S-3A comes inside 12.5 nm of the shore, or the merge leaves 50–60 nm from it;
  - any camera shot would lose a subject from the screen;
  - an estimate in `build/evidence.py` falls outside its records' times without saying why.

  Distances to land use `build/coast.py`, a 35-point extract of the Natural Earth 10 m shore
  from Misrata to the gulf's southern bend. Camera shots are north-up and never orbit, since
  open sea gives no ground reference. Moving subjects are followed, and each shot is zoomed to
  fit its subjects over the whole shot. The fit counts the upward shift a pitched camera gives
  an aircraft at altitude.
- **Line of Death**: the 1973 Libyan declaration takes the Gulf of Surt north to 32°30′N
  (Ratner quotes its text). The line meets the coast west of Misrata and northeast of Benghazi,
  about 297 nm (computed from Natural Earth 10 m coastline; Francioni gives about 300 miles).
  The 62 nm fishing zone is a 2005 decision, not part of the 1973 claim.

## Conflicts carried

Where sources disagree, `build/evidence.py` keeps each source's record apart from the
replay's estimate:

- Each record stands under its own source, quoted exactly where the table shows quotation
  marks and compared with the fetched text of the cited page. Stanik is read from The
  Aviation Geek Club's reprint, Cooper's *Libyan Air Wars* from the extracts The Aviation
  Geek Club and Warrior Maven print, and the Nimitz cruise book from its scanned page.
- The records stay in the code base for study and correction; the replay is for a general
  audience and shows at most a dispute's one-line note for viewers.
- The E-2C picket that vectored the F-14s is named only by squadron, VAW-124 "Bear Aces"
  (Nimitz cruise book; the patch reads BEAR ACE). No source gives its bureau number, callsign
  or station, so it is described in the briefing but not placed on the map. The tape's
  controller is "Bare Ace" in the Biddle transcript, not a confirmed E-2C callsign. No source
  gives Nimitz's coordinates; her position is the DME inference above. Forrestal and Biddle
  are not placed.

<!-- evidence ledger: generated by build/gulf_of_sidra.py from build/evidence.py -->
| Dispute | Records (source: what it says) | Replay estimate and basis |
| --- | --- | --- |
| Where the Biddle tape sits on the clock (`tape-clock`) | USS Biddle CIC audio (relative times): times relative to the tape's start: “00:15 102 Tweny miles for 102. Twenty thousand feet.”<br>Stanik, "Sudden Victory", Naval Aviation News, 1996 (The Aviation Geek Club reprint): reprint: “At 0719, Fast Eagles 102 and 107 joined up and headed back to Nimitz.”<br>Washington Post, 20 Aug 1981 (Pentagon briefing): “bringing down both of the Libyan warplanes at 7:20 a.m. local time (1:20 a.m. EDT), the Pentagon said.”<br>UPI wire reports, 19-20 Aug 1981: “downing both Libyan aircraft with heat-seeking Sidewinder missiles at 1:20 a.m. EDT, the Pentagon said.” | **The tape starts at 07:15**. Its 03:59 "vector north" then falls on Stanik's 07:19 rejoin; the Pentagon's 07:20 for the shootdowns comes two to three minutes after the tape's kills. |
| The first radar contact (`detection`) | Stanik, "Sudden Victory", Naval Aviation News, 1996 (The Aviation Geek Club reprint): reprint, after "At about 0715": “Suddenly, Venlet detected an air contact due south at 80 miles, proceeding north from the Libyan air base at Ghurdabiyah”<br>Cooper, Grandolini and Delalande, Libyan Air Wars (extracts): “Dave [Venlet] detected a contact in a southerly direction, some 80 miles (128 kilometres) away”<br>Washington Post, 20 Aug 1981 (Pentagon briefing): “But about 7 a.m. Libyan time yesterday, two of the F14s on patrol picked up on their cockpit radars two more Libyan jets about 30 to 40 miles away and heading toward the fleet.” | **80 miles at 07:11**. Stanik's range, timed so that a head-on closure of about 1,000 kt reaches the tape's twenty miles at 07:15:15; his "about 0715" leaves no time to close from 80 miles to twenty. |
| Which F-14 shot down which Su-22 (`who-killed-whom`) | Stanik, "Sudden Victory", Naval Aviation News, 1996 (The Aviation Geek Club reprint): reprint: “Satisfied that Muczynski was pursuing the lead Fitter, Kleemann settled in one-half mile behind the wingman”<br>Cooper, Grandolini and Delalande, Libyan Air Wars (extracts): “Kleemann followed the Libyan wingman through his right-hand turn”<br>Tom Cooper, "Libyan Wars 1980-89 Part 2", ACIG, 2003: “The Libyan leader was shot down by the Tomcat wingman, the „Fast Eagle 102“, and the Libyan wingman was shot down by the leader of the US formation and CO VF-41, Lt.Cdr. Henry Kleeman, which flew as „Fast Eagle 107“.” | **Kleemann (102) shoots down the wingman, Muczynski (107) the leader**. Stanik and Cooper's book agree; the ACIG article swaps the callsigns while still naming Kleemann as leader, and Stanik gives "Kleemann flew the lead F-14, Fast Eagle 102". |
| What became of the Libyan pilots (`pilot-fate`) | USS Biddle CIC audio (relative times): “03:05 107 Fox 2 kill. His chute is not deploying. He is falling free.”<br>Lt Mike Sasser, USS Biddle account: “No survivors were ever found.”<br>Stanik, "Sudden Victory", Naval Aviation News, 1996 (The Aviation Geek Club reprint): reprint: “Kleemann observed him descending in his parachute.”<br>Washington Post, 20 Aug 1981 (Pentagon briefing): “One parachute was sighted, and a Libyan helicopter and surface ship were seen moving toward the area where the downed pilot was heading.”<br>UPI wire reports, 19-20 Aug 1981: “The pilot of one of the single-seat SU-22s was seen parachuting from his downed aircraft, the Pentagon said, but it was not known what happened to the other pilot.”<br>UPI wire report, 20 Aug 1981: “A Libyan press spokesman told a London news conference one of the Libyan pilots was found after parachuting into the sea. The other was missing.”<br>Cooper, Grandolini and Delalande, Libyan Air Wars (extracts): Warrior Maven's extract: “Both were recovered by Libyan air force helicopters and brought to Tripoli.” | **Not settled; the replay shows no parachute**. Each Su-22's track ends where it falls to the sea; the records disagree even within each side. |
| The Su-22s' base (`base`) | Stanik, "Sudden Victory", Naval Aviation News, 1996 (The Aviation Geek Club reprint): reprint: “the Libyan air base at Ghurdabiyah on the south shore of the Gulf of Sidra”<br>Tom Cooper, "Libyan Wars 1980-89 Part 2", ACIG, 2003: “an E-2C of the VAW-124 detected two Libyan fighters taking off from the Ghurdabiya-Sirte AB, and moving north at high speed.”<br>Sanders, 'Bait and Switch in Libya', Air & Space, 2012: “an airborne early-warning E-2 Hawkeye radioed that two Su-22s were lifting off from Okba Ben Nafi Air Base, near Tripoli, and to stand by.” | **Ghurdabiya**. The base in Stanik, the ACIG article and Cooper's book, against Sanders' recollection. |
| The Su-22s' squadron (`squadron`) | Cooper, Grandolini and Delalande, Libyan Air Wars (extracts): Warrior Maven's extract: “The two Sukhois were from No. 1022 Squadron commanded by Maj. Abdelsalam Djalloud”<br>Cooper, Grandolini and Delalande, Libyan Air Wars (extracts): The Aviation Geek Club's extract: “Su-22Ms from Syrte-based No. 1032 Squadron LAAF”<br>EasternOrbat: Ghardabiya Air Base: “shot down two Su-22M aircraft from the Libyan Air Force's 1022nd Squadron.” | **1022 Squadron**. Two of the three records; EasternOrbat lists 1032 as a training squadron. |
| How far off the carriers were (`carrier`) | Washington Post, 20 Aug 1981 (Pentagon briefing): “The carriers, Pentagon officials say, were well to the north, about 100 miles away from the gulf.”<br>UPI wire report, 20 Aug 1981: “The two Navy Tomcats were stationed on the nuclear-powered aircraft carrier Nimitz, which was 200 miles off the coast of Libya at the time.”<br>Sanders, 'Bait and Switch in Libya', Air & Space, 2012: “Late one night in August, the USS Nimitz and the Forrestal took up station in the gulf, about 100 miles off Libya.” | **123 nm north of 107 at the tape's 03:14**. The tape's "123 DME on the 180" read as Nimitz's TACAN; that lands about 100 nm north of 32°30'N and about 190 nm off Sirte. |
| How far offshore the fight was (`distance-offshore`) | Washington Post, 20 Aug 1981 (Pentagon briefing): “The attack took place 60 miles from the nearest land, according to Pentagon officials.”<br>UPI wire reports, 19-20 Aug 1981: “taking part in a 6th Fleet exercise about 60 nautical miles off the Libyan coast.”<br>Stanik, "Sudden Victory", Naval Aviation News, 1996 (The Aviation Geek Club reprint): reprint: “The dogfight over the Gulf of Sidra occurred approximately 60 miles off the coast of Libya and lasted less than a minute.”<br>EasternOrbat: Ghardabiya Air Base: “ejected about 75km off the coast of Syrte.”<br>Cooper, Grandolini and Delalande, Libyan Air Wars (extracts): Warrior Maven's extract: “Zintani and Jafaari ended up floating under their parachutes around 35 miles off the coast of Syrte.” | **53 nm from the nearest shore**. The US figure, checked by the build to lie 50–60 nm from the Natural Earth coast; the Libyan figures put it nearer Sirte. |
| How long the fight lasted (`duration`) | USS Nimitz 1980-82 cruise book: VF-41 page, read from the scan: “In 45 seconds, the "TOMCATS" had turned a defensive situation into two confirmed AIM-9L Sidewinder direct hits, bringing the "FITTERS" down”<br>UPI wire reports, 19-20 Aug 1981: “The F-14s returned safely to the Nimitz after the dogfight, which lasted about one minute.”<br>Cooper, Grandolini and Delalande, Libyan Air Wars (extracts): “This encounter had lasted about three minutes and 44 seconds, from the US pilots sighting the Sukhois for the first time until second Su-22M was shot down” | **About 90 s from the Atoll to the second kill**. The tape's times, from the merge to "Fox 2 kill from music" at 02:53. |
| The claimed F-14 loss (`f14-loss`) | Cooper, Grandolini and Delalande, Libyan Air Wars (extracts): Warrior Maven's extract: “Moment later, he fired one R-13M missile that, he claimed, destroyed the lead F-14.”<br>UPI wire reports, 19-20 Aug 1981: “Libya's official Jamahiriyah news agency said its jets shot down one F-14 and the Libyan navy retrieved the wreckage of the U.S. plane.”<br>Ratner, Yale Journal of International Law, 1984: note 11: “The Libyan government claimed that it shot down one U.S. fighter, and that the American plane crashed about ten miles west of Poisano, Sardinia.”<br>Washington Post, 20 Aug 1981 (Pentagon briefing): “The Libyan news agency also reported one F14 had been shot down, but the Pentagon denied this” | **No F-14 is lost**. Both returned to Nimitz (UPI); the two Libyan claims also place the wreck in different seas. |
| When the F-14s were cleared to defend themselves (`clear-to-defend`) | USS Biddle CIC audio (relative times): “03:29 Nimitz 102 107, you are clear to defend yourself.”<br>USS Biddle CIC audio (relative times): “03:31 Bare Ace 102 107, you are clear to defend yourself. Pass from the ship.”<br>DVIDS: Fast Eagles made history over the Gulf of Sidra: “By the time the ship had advised them to fight back, the two F-14 aviators had already taken down the enemy aircraft.”<br>Lt Mike Sasser, USS Biddle account: “Immediately after the engagement, the F-14s were returning to the carrier and at that time received “Permission to defend yourselves” from the carrier.”<br>Cooper, Grandolini and Delalande, Libyan Air Wars (extracts): The Aviation Geek Club's extract, before the kills: “the two Tomcat crews, now granted permission to take immediate action and defend themselves.” | **After both kills**. The tape and both Biddle and DVIDS accounts; Cooper alone puts it first. |
<!-- end of evidence ledger -->

Other accounts the replay does not show:

- **The Atoll**: Stanik's AA-2 Atoll is an R-13M in Cooper, and the ACIG article notes a
  claim that it was a dropped tank.
- **MiG-25s**: Cooper has two MiG-25s run toward Nimitz within the hour and turn back from
  VF-41 and VF-84 Tomcats.

## Sources

- Stanik, "Sudden Victory", Naval Aviation News, Jul–Aug 1996, as reprinted by The Aviation
  Geek Club:
  https://theaviationgeekclub.com/tomcats-2-fitters-0-how-two-u-s-navy-f-14s-shot-down-two-qaddafis-su-22s-over-the-gulf-of-sidra-on-aug-19-1981/
- USS Biddle CIC audio, transcript of the fitter engagement (Wayback Machine copy):
  https://web.archive.org/web/20060212192336/http://www.ussbiddle.org/history/fitter_engagement_audio.html
- UPI wire, 19 and 20 August 1981 (Pentagon times, "about one minute"; the Libyan spokesman and
  "200 miles off the coast"):
  https://www.upi.com/Archives/1981/08/19/Two-US-Navy-jet-fighters-early-Wednesday-shot-down/9720367041600/ ,
  https://www.upi.com/Archives/1981/08/20/The-Reagan-administration-says-the-attack-by-two-Libyan/5669367128000/
- Joe Baugher, third-series serials (160403 = AJ102, 160390 = AJ107), Wayback copy:
  https://web.archive.org/web/2022/http://www.joebaugher.com/navy_serials/thirdseries21.html
- DVIDS, "Two enemy kills: Fast Eagles made history over the Gulf of Sidra" (2022):
  https://www.dvidshub.net/news/436006/two-enemy-kills-fast-eagles-made-history-over-gulf-sidra
- Tom Cooper, ACIG "Libyan Wars 1980–89 Part 2" (13 November 2003):
  http://acig.org/artman/publish/article_356.shtml
- Cooper, Grandolini and Delalande, *Libyan Air Wars Part 1*, via extracts at
  https://theaviationgeekclub.com/vf-41-black-aces-f-14-tomcat-crew-members-who-took-part-in-gulf-of-sidra-incident-recall-the-shooting-down-of-gaddafi-sukhoi-su-22m-fitter-fighter-bombers/
  and https://warriormaven.com/news/history/the-libyans-have-a-different-take-on-their-battle-with-the-us-navy
- Yale Journal of International Law, Ratner (1984), quoting the 1973 Libyan declaration.
- Francioni, Syracuse Journal of International Law, on the 1973 line:
  https://jilc.syr.edu/wp-content/uploads/2024/12/Gulf-of-Sirte.pdf
- Ghardabiya Air Base, Wikipedia (coordinates) and EasternOrbat (1022 Sqn, 1032 Sqn):
  https://easternorbat.com/african_af/Libyan-AF/libyan_sirte_ab/libyan_sirte_ab.html
- Tzdb: Africa/Tripoli, UTC+2 with no DST in August 1981 (checked against the system zoneinfo).
- VAW-124 E-2C squadron: https://www.globalsecurity.org/military/agency/navy/vaw-124.htm ;
  https://www.seaforces.org/usnair/VAW/Carrier-Airborne-Early-Warning-Squadron-124.htm
- Washington Post, "U.S. Navy Fighters Shoot Down 2 Libyan Jets", 20 Aug 1981 (Pentagon
  briefing: 07:20 local, 20,000 ft, 60 miles from land, 30 miles below the line):
  https://www.washingtonpost.com/archive/politics/1981/08/20/us-navy-fighters-shoot-down-2-libyan-jets/324a4b20-d0c7-42c2-a61a-92b51c7012eb/
  (read from the Wayback copy of 15 July 2024)
- USS Nimitz 1980–82 cruise book (OOMEX, VAW-124, VF-41 pages):
  https://www.navysite.de/cruisebooks/cvn68-82/index.html
- Thompson Sanders, "Bait and Switch in Libya", Air & Space, July 2012 (S-3A Diamond Cutter
  702): https://web.archive.org/web/2016/http://www.airspacemag.com/military-aviation/bait-and-switch-in-libya-94267482/
- Lt Mike Sasser, USS Biddle account:
  https://web.archive.org/web/2015/http://www.ussbiddle.org/history/fitter_engagement.html
- Coastline: Natural Earth 10 m (public domain); `build/coast.py` embeds a 35-point extract of
  the gulf shore. No other map data is bundled.
