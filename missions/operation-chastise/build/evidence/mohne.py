"""The Möhne: the attacks, its defences and its breach."""
from ledger import Dispute, Moment, Record

from .names import DB, EDITOR, LOG, ORB, WP  # noqa: F401

MOMENTS = {
    "gibson-release": Moment(
        "Gibson's attack", "AJ-G", "00:28",
        (Record(ORB, "Gibson attacks first at 60 ft at 0028; the mine explodes short of the wall.",
                "00:28"),)),
    "hopgood-loss": Moment(
        "Hopgood's loss", "AJ-M", "00:34",
        (Record(ORB, "AJ-M, hit on the run-in, crashes near Ostönnen at 0034; two of the crew "
                "survive as prisoners.", "00:34"),)),
    "martin-release": Moment(
        "Martin's attack", "AJ-P", "00:38",
        (Record(ORB, "Martin attacks at 0038 with Gibson alongside; the mine bursts short.",
                "00:38"),)),
    "mohne-breach": Moment(
        "The Möhne breaks", "MÖHNE", "00:49",
        (Record("dewiki-moehne", "Die Bombe explodierte um 0:49 Uhr in der Mitte der Mauer und "
                "riss die Staumauer auf etwa 30 m Breite auf.", "00:49", quote=True),
         Record("lwl-moehne", "Erst beim sechsten Anflug gelang es einer Lancaster um 00.49 Uhr, "
                "die Staumauer zu zerstören.", "00:49", quote=True))),
    "neheim-flood": Moment(
        "The Möhne flood reaches Neheim", "MÖHNE FLOOD", "01:20",
        (Record("dewiki-moehne", "The flood reaches Neheim at 0120.", "01:20"),)),
}

DISPUTES = {
    "hopgood-release": Dispute(
        "Hopgood's attack", "AJ-M",
        (Record(ORB, "Was seen to be hit by flak on the run-up and to have an engine on fire. He "
                "overshot with his mine", quote=True),
         Record(ORB, "crashed near the dam power house and exploded at 0034hrs", "00:34",
                quote=True, label=f"{EDITOR}, across a page break after \"power\""),
         Record("lwl-moehne", "Der deutschen Flak auf den Türmen gelang es immerhin, einen der "
                "Bomber auf dem Zielanflug über dem Möhnesee abzuschießen", quote=True)),
        "00:32:50", "No source times the release. It follows Gibson's 00:28 by B.976's three "
        "minutes for the water and leaves about a minute for the burning climb to Ostönnen.",
        at="00:32:50", outside=True),
    "young-release": Dispute(
        "Young's attack", "AJ-A",
        (Record(ORB, "Was seen to make an accurate attack with his mine", quote=True),),
        "00:43", "No source read times it; it falls between Martin's 00:38 and Maltby's 00:49 "
        "at B.976's spacing, and secondary accounts give 00:43.", at="00:43", outside=True),
    "maltby-release": Dispute(
        "Maltby's attack", "AJ-J",
        (Record(ORB, "MOHNE DAM. 1 Mine. 60ft. 0139 hrs.", "01:39", quote=True),
         Record(DB, "Gibson told Maltby to go ahead at 0048.", "00:48", quote=True),
         Record(DB, "at 0050 wireless operator Antony Stone radioed ‘Goner 78A’"
                " back to Grantham.", "00:50", quote=True),
         Record("lwl-moehne", "Erst beim sechsten Anflug gelang es einer Lancaster um 00.49 Uhr, "
                "die Staumauer zu zerstören.", "00:49", quote=True),
         Record("dewiki-moehne", "Die Bombe explodierte um 0:49 Uhr in der Mitte der Mauer und "
                "riss die Staumauer auf etwa 30 m Breite auf.", "00:49", quote=True)),
        "00:49", "The ORB's 0139 repeats Shannon's Eder time on the next sheet; the breach was "
        "signalled at 00:56 and Maltby landed at 03:11.", at="00:49"),
    "martin-mine": Dispute(
        "Martin's mine", "AJ-P",
        (Record(ORB, "Mine burst about 20 yds. short.", "00:38", quote=True),
         Record(WP, "Mine missed the target.", quote=True)),
        "Bursts 18 m short", "The ORB's distance; Wikipedia agrees it missed.", shown="00:38"),
    "mohne-flak": Dispute(
        "Möhne flak", "MÖHNE FLAK",
        (Record("lwl-moehne", "nur noch sechs 2-cm-Flakgeschütze der 3. Batterie leichte "
                "Flakabteilung 840, die zur Flakgruppe Dortmund gehörte.", quote=True),
         Record("lwl-moehne", "Die Sologeschütze hatten ihre Stellungen am Ende der Sperrmauer, "
                "unterhalb der Talsperre und auf den zwei Türmen bezogen.", quote=True),
         Record(ORB, "There were between seven and ten light flak guns around the target",
                quote=True)),
        "Six guns, one battery at the dam", "The German record of the defending battery.",
        shown="00:17"),
    "release-speed": Dispute(
        "Release speed", None,
        (Record("order-b976", "the height of attack is to be 60 feet and the ground speed 220 "
                "m.p.h.", quote=True),
         Record(WP, "at an air speed of 240 mph (390 km/h)", quote=True),
         Record("gibson-eca", "we were being dragged along at four miles a minute", quote=True)),
        "220 mph", "The operation order's figure.", shown="00:28"),
}
