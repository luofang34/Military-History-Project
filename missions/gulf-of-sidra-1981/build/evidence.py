"""The Gulf of Sidra incident's disputed facts, in the form tools/ledger.py describes: each
source's record, compared with the fetched text of the cited page, and the replay's estimate.
Record times are Tripoli time (UTC+2); the Biddle tape's times are relative to its start and
are given in its own words. Stanik is read from The Aviation Geek Club's reprint, and Cooper's
Libyan Air Wars from the extracts The Aviation Geek Club and Warrior Maven print.
"""
from ledger import Dispute, Record
from geometry import FE102, NIMITZ, SU_LEAD, SU_WING

TAPE = "biddle-tape"
WAPO = "wapo-1981"
UPI = "upi-1981"
UPI_20 = "upi-1981-08-20"
STANIK = "stanik-1996"
COOPER = "cooper-libyan-air-wars"
ACIG = "cooper-acig"
EOB = "easternorbat"
SANDERS = "sanders-2012"
SASSER = "sasser-biddle"
DVIDS = "dvids-2022"
RATNER = "ratner-yale-1984"
CRUISE = "nimitz-cruise-book"
REPRINT = "reprint"

DISPUTES = {
    "tape-clock": Dispute(
        "Where the Biddle tape sits on the clock", None,
        (Record(TAPE, "00:15 102 Tweny miles for 102. Twenty thousand feet.", quote=True,
                label="times relative to the tape's start"),
         Record(STANIK, "At 0719, Fast Eagles 102 and 107 joined up and headed back to Nimitz.",
                "07:19", quote=True, label=REPRINT),
         Record(WAPO, "bringing down both of the Libyan warplanes at 7:20 a.m. local time (1:20 "
                "a.m. EDT), the Pentagon said.", "07:20", quote=True),
         Record(UPI, "downing both Libyan aircraft with heat-seeking Sidewinder missiles at 1:20 "
                "a.m. EDT, the Pentagon said.", "07:20", quote=True)),
        "The tape starts at 07:15", "Its 03:59 \"vector north\" then falls on Stanik's 07:19 "
        "rejoin; the Pentagon's 07:20 for the shootdowns comes two to three minutes after the "
        "tape's kills.", at="07:15", outside=True),
    "detection": Dispute(
        "The first radar contact", FE102,
        (Record(STANIK, "Suddenly, Venlet detected an air contact due south at 80 miles, "
                "proceeding north from the Libyan air base at Ghurdabiyah", "07:15", quote=True,
                label="reprint, after \"At about 0715\""),
         Record(COOPER, "Dave [Venlet] detected a contact in a southerly direction, some 80 "
                "miles (128 kilometres) away", quote=True),
         Record(WAPO, "But about 7 a.m. Libyan time yesterday, two of the F14s on patrol picked "
                "up on their cockpit radars two more Libyan jets about 30 to 40 miles away and "
                "heading toward the fleet.", "07:00", quote=True)),
        "80 miles at 07:11", "Stanik's range, timed so that a head-on closure of about 1,000 kt "
        "reaches the tape's twenty miles at 07:15:15; his \"about 0715\" leaves no time to "
        "close from 80 miles to twenty.", at="07:11"),
    "who-killed-whom": Dispute(
        "Which F-14 shot down which Su-22", SU_WING,
        (Record(STANIK, "Satisfied that Muczynski was pursuing the lead Fitter, Kleemann settled "
                "in one-half mile behind the wingman", quote=True, label=REPRINT),
         Record(COOPER, "Kleemann followed the Libyan wingman through his right-hand turn",
                quote=True),
         Record(ACIG, "The Libyan leader was shot down by the Tomcat wingman, the „Fast Eagle "
                "102“, and the Libyan wingman was shot down by the leader of the US formation "
                "and CO VF-41, Lt.Cdr. Henry Kleeman, which flew as „Fast Eagle 107“.",
                quote=True)),
        "Kleemann (102) shoots down the wingman, Muczynski (107) the leader", "Stanik and "
        "Cooper's book agree; the ACIG article swaps the callsigns while still naming Kleemann "
        "as leader, and Stanik gives \"Kleemann flew the lead F-14, Fast Eagle 102\".",
        shown="07:17:18"),
    "pilot-fate": Dispute(
        "What became of the Libyan pilots", SU_LEAD,
        (Record(TAPE, "03:05 107 Fox 2 kill. His chute is not deploying. He is falling free.",
                quote=True),
         Record(SASSER, "No survivors were ever found.", quote=True),
         Record(STANIK, "Kleemann observed him descending in his parachute.", quote=True,
                label=REPRINT),
         Record(WAPO, "One parachute was sighted, and a Libyan helicopter and surface ship were "
                "seen moving toward the area where the downed pilot was heading.", quote=True),
         Record(UPI, "The pilot of one of the single-seat SU-22s was seen parachuting from his "
                "downed aircraft, the Pentagon said, but it was not known what happened to the "
                "other pilot.", quote=True),
         Record(UPI_20, "A Libyan press spokesman told a London news conference one of the "
                "Libyan pilots was found after parachuting into the sea. The other was "
                "missing.", quote=True),
         Record(COOPER, "Both were recovered by Libyan air force helicopters and brought to "
                "Tripoli.", quote=True, label="Warrior Maven's extract")),
        "Not settled; the replay shows no parachute", "Each Su-22's track ends where it falls to "
        "the sea; the records disagree even within each side.", shown="07:18:05",
        brief="What became of the two pilots is disputed: accounts range from no survivors to "
        "both rescued."),
    "base": Dispute(
        "The Su-22s' base", SU_LEAD,
        (Record(STANIK, "the Libyan air base at Ghurdabiyah on the south shore of the Gulf of "
                "Sidra", quote=True, label=REPRINT),
         Record(ACIG, "an E-2C of the VAW-124 detected two Libyan fighters taking off from the "
                "Ghurdabiya-Sirte AB, and moving north at high speed.", quote=True),
         Record(SANDERS, "an airborne early-warning E-2 Hawkeye radioed that two Su-22s were "
                "lifting off from Okba Ben Nafi Air Base, near Tripoli, and to stand by.",
                quote=True)),
        "Ghurdabiya", "The base in Stanik, the ACIG article and Cooper's book, against "
        "Sanders' recollection.", shown="07:00:20"),
    "squadron": Dispute(
        "The Su-22s' squadron", SU_LEAD,
        (Record(COOPER, "The two Sukhois were from No. 1022 Squadron commanded by Maj. "
                "Abdelsalam Djalloud", quote=True, label="Warrior Maven's extract"),
         Record(COOPER, "Su-22Ms from Syrte-based No. 1032 Squadron LAAF", quote=True,
                label="The Aviation Geek Club's extract"),
         Record(EOB, "shot down two Su-22M aircraft from the Libyan Air Force's 1022nd "
                "Squadron.", quote=True)),
        "1022 Squadron", "Two of the three records; EasternOrbat lists 1032 as a training "
        "squadron.", shown="07:00:40"),
    "carrier": Dispute(
        "How far off the carriers were", NIMITZ,
        (Record(WAPO, "The carriers, Pentagon officials say, were well to the north, about 100 "
                "miles away from the gulf.", quote=True),
         Record(UPI_20, "The two Navy Tomcats were stationed on the nuclear-powered aircraft "
                "carrier Nimitz, which was 200 miles off the coast of Libya at the time.",
                quote=True),
         Record(SANDERS, "Late one night in August, the USS Nimitz and the Forrestal took up "
                "station in the gulf, about 100 miles off Libya.", quote=True)),
        "123 nm north of 107 at the tape's 03:14", "The tape's \"123 DME on the 180\" read as "
        "Nimitz's TACAN; that lands about 100 nm north of 32°30'N and about 190 nm off Sirte.",
        shown="07:00:10"),
    "distance-offshore": Dispute(
        "How far offshore the fight was", None,
        (Record(WAPO, "The attack took place 60 miles from the nearest land, according to "
                "Pentagon officials.", quote=True),
         Record(UPI, "taking part in a 6th Fleet exercise about 60 nautical miles off the Libyan "
                "coast.", quote=True),
         Record(STANIK, "The dogfight over the Gulf of Sidra occurred approximately 60 miles off "
                "the coast of Libya and lasted less than a minute.", quote=True, label=REPRINT),
         Record(EOB, "ejected about 75km off the coast of Syrte.", quote=True),
         Record(COOPER, "Zintani and Jafaari ended up floating under their parachutes around 35 "
                "miles off the coast of Syrte.", quote=True, label="Warrior Maven's extract")),
        "53 nm from the nearest shore", "The US figure, checked by the build to lie 50–60 nm "
        "from the Natural Earth coast; the Libyan figures put it nearer Sirte.",
        shown="07:16:20"),
    "duration": Dispute(
        "How long the fight lasted", None,
        (Record(CRUISE, "In 45 seconds, the \"TOMCATS\" had turned a defensive situation into "
                "two confirmed AIM-9L Sidewinder direct hits, bringing the \"FITTERS\" down",
                quote=True, label="VF-41 page, read from the scan"),
         Record(UPI, "The F-14s returned safely to the Nimitz after the dogfight, which lasted "
                "about one minute.", quote=True),
         Record(COOPER, "This encounter had lasted about three minutes and 44 seconds, from the "
                "US pilots sighting the Sukhois for the first time until second Su-22M was "
                "shot down", quote=True)),
        "About 90 s from the Atoll to the second kill", "The tape's times, from the merge to "
        "\"Fox 2 kill from music\" at 02:53.", shown="07:17:53"),
    "f14-loss": Dispute(
        "The claimed F-14 loss", None,
        (Record(COOPER, "Moment later, he fired one R-13M missile that, he claimed, destroyed "
                "the lead F-14.", quote=True, label="Warrior Maven's extract"),
         Record(UPI, "Libya's official Jamahiriyah news agency said its jets shot down one F-14 "
                "and the Libyan navy retrieved the wreckage of the U.S. plane.", quote=True),
         Record(RATNER, "The Libyan government claimed that it shot down one U.S. fighter, and "
                "that the American plane crashed about ten miles west of Poisano, Sardinia.",
                quote=True, label="note 11"),
         Record(WAPO, "The Libyan news agency also reported one F14 had been shot down, but the "
                "Pentagon denied this", quote=True)),
        "No F-14 is lost", "Both returned to Nimitz (UPI); the two Libyan claims also place the "
        "wreck in different seas.", shown="07:16:25"),
    "clear-to-defend": Dispute(
        "When the F-14s were cleared to defend themselves", None,
        (Record(TAPE, "03:29 Nimitz 102 107, you are clear to defend yourself.", quote=True),
         Record(TAPE, "03:31 Bare Ace 102 107, you are clear to defend yourself. Pass from the "
                "ship.", quote=True),
         Record(DVIDS, "By the time the ship had advised them to fight back, the two F-14 "
                "aviators had already taken down the enemy aircraft.", quote=True),
         Record(SASSER, "Immediately after the engagement, the F-14s were returning to the "
                "carrier and at that time received “Permission to defend yourselves” from the "
                "carrier.", quote=True),
         Record(COOPER, "the two Tomcat crews, now granted permission to take immediate action "
                "and defend themselves.", quote=True, label="The Aviation Geek Club's extract, "
                "before the kills")),
        "After both kills", "The tape and both Biddle and DVIDS accounts; Cooper alone puts it "
        "first.", shown="07:18:29"),
}
