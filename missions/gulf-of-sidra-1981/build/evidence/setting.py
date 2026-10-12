"""Who flew from where, and where the fight took place."""
from ledger import Dispute, Moment, Record
from geometry import FE102, NIMITZ, SU_LEAD, SU_WING

from .names import ACIG, COOPER, EOB, REPRINT, SANDERS, STANIK, TAPE, UPI, UPI_20, WAPO

MOMENTS = {
    "su22-take-off": Moment(
        "The Su-22s take off", "SU22-LEAD", "07:00:20",
        (Record(ACIG, "Two Su-22Ms take off from Ghurdabiya, near Sirte.", None),)),
}

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
}
