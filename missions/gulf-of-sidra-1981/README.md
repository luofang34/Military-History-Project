# Gulf of Sidra incident, 19 August 1981

Two US Navy F-14A Tomcats from USS Nimitz (VF-41, Fast Eagle 102 and 107) shoot down two
Libyan Su-22M3 Fitters from Ghurdabiya, the first AIM-9L kills in the Gulf of Sidra
dispute. Clock: Tripoli time (UTC+2), the Libyan clock; Pentagon Zulu times are converted.

This folder is the package (`operation.json`, `events.jsonl`, `presentations/default.json`)
and its generator, `build/`. Regenerate with `python3 build/gulf_of_sidra.py`, then run
`python3 ../../verify.py`.

## Method

Clock times are the sourced anchors: the Biddle tape gives times relative to its start, and
Stanik and the UPI wire give absolute times. The package's operation zero is the Libyan
launch time (07:00 Tripoli, "7 A.M." in the Libyan account), with ±15 minutes. Positions are
`reconstructed`, and each fix carries a horizontal `bound_m`. No published source gives
coordinates for the fight, so positions are inference from distances and bearings.

- **Sourced anchors (clock)**:
  - 07:15 Venlet's radar contact, about 80 nm south (Stanik; Biddle "twenty miles, twenty
    thousand feet" at 00:15).
  - 16:31 Biddle: "two fitters has shot at my leader", the Libyan AA-2 launch.
  - 17:21 Kleemann (102) kills the wingman with one AIM-9L (Biddle "clean target").
  - 17:53 Muczynski (107) kills the leader with one AIM-9L (Biddle "Fox 2 kill from music").
  - 18:29 "clear to defend yourself" relay, after both kills (Biddle).
  - 19:00 Rejoin and egress (Stanik, 07:19).
  - Pentagon: shootdowns at 0520Z, equal to 07:20 at UTC+2.
- **Reconstructed geometry**:
  - Su-22s climb from Ghurdabiya (31.0606°N 16.6117°E, Wikipedia/ICAO HLGD) to 7,000 m, per
    the Libyan account (US accounts say 20,000 ft).
  - F-14s hold a racetrack at 20,000 ft and 18,000 ft (Stanik) before vectoring south.
  - Engagement positions are inferred: about 60 nm off the coast (Pentagon via UPI; Cooper),
    north of Sirte, and inside the claimed line.
- **Line of Death**: the 1973 Libyan declaration takes the Gulf of Surt north to 32°30′N
  (Ratner quotes its text). The line meets the coast west of Misrata and northeast of Benghazi,
  about 297 nm (computed from Natural Earth 10 m coastline; Francioni gives about 300 miles).
  The 62 nm fishing zone is a 2005 decision, not part of the 1973 claim.

## Conflicts carried

- **Clock**: the Biddle tape is relative; the Libyan launch and the US contact are not
  reconciled to the minute. The anchor is ±15 minutes.
- **Which F-14 killed which Su-22**: the Stanik, Cooper and Biddle accounts agree on
  102 killing the wingman and 107 the leader. The ACIG 2006 article swaps the callsigns.
- **Pilot fate**: the Biddle tape says the leader's chute did not open. The Libyan account
  says both were recovered by helicopter. The UPI wire says one was found and the other
  missing.
- **Engagement distance**: about 60 nm (US) vs about 75 km, or 35 nm, off Syrte (Libyan).
- **Duration**: UPI says about one minute; Cooper says 3 min 44 s from first sighting to the
  second kill.
- **Claimed F-14 loss**: Cooper's Libyan account gives a wreck found by fishermen. A Libyan
  radio report puts a downed F-14 near Sardinia. US sources record no F-14 loss.
- **Squadron**: 1022 (Cooper 2017) vs 1032 (Cooper, via Aviation Geek Club).
- **E-2C and carriers**: the picket that vectored the F-14s is named only by squadron, VAW-124
  "Bear Aces" (GlobalSecurity; SeaForces summary). No source gives its bureau number or
  callsign, and no source gives Nimitz's or Forrestal's position on 19 August. The tape's
  controller is "Bare Ace" in the Biddle transcript, not a confirmed E-2C callsign.
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
- Coastline: Natural Earth 10 m (public domain). No map data is bundled.
