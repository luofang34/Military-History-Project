"""The head-on pass, the missiles and the two kills."""
from ledger import Dispute, Moment, Record
from geometry import FE102, NIMITZ, SU_LEAD, SU_WING

from .names import ACIG, COOPER, CRUISE, RATNER, REPRINT, STANIK, TAPE, UPI, WAPO

MOMENTS = {
    "tally-ho": Moment(
        "The F-14s see the Su-22s", "FE102", "07:15:54",
        (Record(TAPE, "8 miles.", None, quote=True),
         Record(STANIK, "Tally-ho: two Fitters in welded wing, under 500 ft apart.", None))),
    "atoll-shot": Moment(
        "The Libyan lead fires", "AA2-ATOLL", "07:16:23",
        (Record(STANIK, "The Libyan lead fires one AA-2 Atoll head-on from about 300 m; it passes "
                "under 102 and misses.", None),)),
    "kleemann-shot": Moment(
        "Kleemann fires", "AIM9-102", "07:17:18",
        (Record(STANIK, "Kleemann waits for the Fitter to clear the sun, then fires one AIM-9L.",
                None),)),
    "wingman-down": Moment(
        "The Su-22 wingman is shot down", "SU22-WING", "07:17:21",
        (Record(TAPE, "Affimative.[garbled] shot one of them down.", None, quote=True),)),
    "muczynski-shot": Moment(
        "Muczynski fires", "AIM9-107", "07:17:50",
        (Record(STANIK, "Muczynski fires one AIM-9L from about 1,000 yd.", None),)),
    "leader-down": Moment(
        "The Su-22 leader is shot down", "SU22-LEAD", "07:17:53",
        (Record(TAPE, "Fox 2 kill from music.", None, quote=True),)),
}

DISPUTES = {
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
}
