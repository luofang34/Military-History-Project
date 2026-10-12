"""The pilots' fate and the clearance that came after the kills."""
from ledger import Dispute, Record
from geometry import FE102, NIMITZ, SU_LEAD, SU_WING

from .names import COOPER, DVIDS, REPRINT, SASSER, STANIK, TAPE, UPI, UPI_20, WAPO

MOMENTS = {
}

DISPUTES = {
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
