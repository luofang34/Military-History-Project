# Gulf of Sidra incident, 19 August 1981

Two US Navy F-14A Tomcats from USS Nimitz (VF-41, Fast Eagle 102 and 107) shoot down two
Libyan Su-22M3 Fitters from Ghurdabiya, the first AIM-9L kills in the Gulf of Sidra
dispute. Clock: Tripoli time (UTC+2), the Libyan clock; Pentagon Zulu times are converted.

This folder is the package (`operation.json`, `events.jsonl`, `presentations/default.json`)
and its generator, `build/`. Regenerate with `python3 build/gulf_of_sidra.py`, then run
`python3 ../../verify.py`.

## Method

Clock times are the sourced anchors. The Biddle tape gives times relative to its start, which
is placed at 07:15 Tripoli time; Stanik and the UPI wire give absolute times. Operation zero is
the Libyan launch time (07:00, "7 A.M." in the Libyan account), with ±15 minutes. Positions
are `reconstructed`, and each fix carries a horizontal `bound_m`. No published source gives
coordinates for the fight, so the geometry is built in a local nautical-mile frame around the
merge and constrained by the tape's ranges and times.

- **Sourced anchors (clock)**, as tape time → Tripoli time:
  - About 07:11: Venlet's radar contact, about 80 nm south (Stanik).
  - 00:15 → 07:15:15 "twenty miles, twenty thousand feet"; then 16, 14, 8 (tally-ho) and
    6 miles at 00:27, 00:38, 00:54 and 01:03.
  - 01:31 → 07:16:31 "two fitters has shot at my leader". The Atoll launch is placed at
    07:16:23, where the closure puts the pair about 300 m apart.
  - 02:21 → 07:17:21 Kleemann (102) kills the wingman (Biddle "clean target").
  - 02:34 "Want me shoot my guy down?" / "Shoot him down."
  - 02:53 → 07:17:53 Muczynski (107) kills the leader ("Fox 2 kill from music").
  - 03:05 "His chute is not deploying"; 03:14 "123 DME on the 180"; 03:29 "clear to defend
    yourself"; 03:59 "vector north". Stanik: rejoin at 07:19.
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
  - any camera shot would lose a subject from the screen.

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

- **Clock**: the Biddle tape is relative; the Libyan launch and the US contact are not
  reconciled to the minute. The anchor is ±15 minutes.
- **Which F-14 killed which Su-22**: the Stanik, Cooper and Biddle accounts agree on
  102 killing the wingman and 107 the leader. The ACIG 2006 article swaps the callsigns.
- **Pilot fate**: the Biddle tape says the leader's chute did not open, and Biddle's Lt
  Sasser says no survivors were found. The Pentagon saw one parachute (Washington Post). The
  Libyan account says both were recovered by helicopter. The UPI wire says one was found and
  the other missing.
- **Detection range**: 80 nm at about 07:11 (Stanik) vs 30 to 40 miles at about 07:00
  (Pentagon briefing, Washington Post). The replay follows Stanik.
- **Libyan base**: Ghurdabiya (Stanik, ACIG, Wikipedia) vs Okba Ben Nafi near Tripoli
  (Sanders' memoir). The replay follows Ghurdabiya.
- **Carrier distance**: about 100 miles north of the gulf (Pentagon briefing), 200 miles off
  the coast (UPI), about 100 miles off Libya (Sanders).
- **Engagement distance**: about 60 nm (US) vs about 75 km, or 35 nm, off Syrte (Libyan).
- **Duration**: 45 seconds (Nimitz cruise book), about one minute (UPI), 3 min 44 s from
  first sighting to the second kill (Cooper).
- **Claimed F-14 loss**: Cooper's Libyan account gives a wreck found by fishermen. A Libyan
  radio report puts a downed F-14 near Sardinia. US sources record no F-14 loss.
- **Squadron**: 1022 (Cooper 2017) vs 1032 (Cooper, via Aviation Geek Club).
- **E-2C and carriers**: the picket that vectored the F-14s is named only by squadron, VAW-124
  "Bear Aces" (Nimitz cruise book; the patch reads BEAR ACE). No source gives its bureau number,
  callsign or station, so it is described in the briefing but not placed on the map. The
  tape's controller is "Bare Ace" in the Biddle transcript, not a confirmed E-2C callsign. No
  source gives Nimitz's coordinates; her position is the DME inference above. Forrestal and
  Biddle are not placed.
- **"Clear to defend" relay**: DVIDS places it before the kills; the Biddle tape places it
  after both.

## Sources

- Stanik, "Sudden Victory", Naval Aviation News, Jul–Aug 1996.
- USS Biddle CIC audio, transcript of the fitter engagement (Wayback Machine copy):
  https://web.archive.org/web/20060212192336/http://www.ussbiddle.org/history/fitter_engagement_audio.html
- UPI wire, 19 and 20 August 1981 (Pentagon times, "about one minute"):
  https://www.upi.com/Archives/1981/08/19/Two-US-Navy-jet-fighters-early-Wednesday-shot-down/9720367041600/
- Joe Baugher, third-series serials (160403 = AJ102, 160390 = AJ107), Wayback copy:
  https://web.archive.org/web/2022/http://www.joebaugher.com/navy_serials/thirdseries21.html
- DVIDS, "Two enemy kills: Fast Eagles made history over the Gulf of Sidra" (2022):
  https://www.dvidshub.net/news/436006/two-enemy-kills-fast-eagles-made-history-over-gulf-sidra
- Tom Cooper, ACIG "Libyan Wars 1980–89 Part 2": http://acig.org/artman/publish/article_356.shtml
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
- USS Nimitz 1980–82 cruise book (OOMEX, VAW-124, VF-41 pages):
  https://www.navysite.de/cruisebooks/cvn68-82/index.html
- Thompson Sanders, "Bait and Switch in Libya", Air & Space, July 2012 (S-3A Diamond Cutter
  702): https://web.archive.org/web/2016/http://www.airspacemag.com/military-aviation/bait-and-switch-in-libya-94267482/
- Lt Mike Sasser, USS Biddle account:
  https://web.archive.org/web/2015/http://www.ussbiddle.org/history/fitter_engagement.html
- Coastline: Natural Earth 10 m (public domain); `build/coast.py` embeds a 35-point extract of
  the gulf shore. No other map data is bundled.
