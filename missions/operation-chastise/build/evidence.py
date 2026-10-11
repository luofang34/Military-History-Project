"""Operation Chastise's disputed facts, in the form tools/ledger.py describes: each source's
record, compared with the ORB transcript, Enemy Coast Ahead, Hinks et al. and the cited web
pages, and the replay's estimate. The flight plans read the estimates from here, so revising
one is a one-line change and a rebuild.
"""
import ledger
from ledger import Dispute, Record

ORB = "orb-617"
DB = "dambustersblog"
WP = "wikipedia-chastise"
EDITOR = "ORB editor's note"

DISPUTES = {
    "mccarthy-arrival": Dispute(
        "McCarthy's arrival at the Sorpe", "AJ-T",
        (Record(DB, "Flying as fast as he could, McCarthy made up 13 or 14 minutes by the time he "
                "reached the Sorpe at 0015", "00:15", quote=True),
         Record("nav-log-aj-t", "Target Z 0030", "00:30", label="Navigator's log",
                checked=False)),
        "00:15", "The blog's reading of the log; ten runs ending in the 00:46 release (ORB) "
        "cannot be flown from 00:30 within a Lancaster's holding speeds.", at="00:15"),
    "mccarthy-runs": Dispute(
        "McCarthy's runs at the Sorpe", "AJ-T",
        (Record(DB, "on the tenth approach, he managed to make a near perfect run, getting down "
                "to about 30 feet", quote=True),
         Record(WP, "McCarthy made nine attempted bombing runs before Johnson was satisfied",
                quote=True),
         Record("gibson-eca", "They had both made twelve dummy runs and had dropped their mines "
                "along the lip of the concrete", quote=True)),
        "Nine dummy runs, release on the tenth",
        "Two accounts agree on ten approaches; Gibson was not at the Sorpe.", shown="00:46"),
    "mccarthy-delay": Dispute(
        "McCarthy's late take-off", "AJ-T",
        (Record(ORB, "Had trouble with his compass and took off 20 mins. late.", "22:01",
                quote=True),
         Record(WP, "took off in the reserve aircraft 34 minutes late", quote=True),
         Record(DB, "AJ-T eventually took to the air some 33 minutes later than their scheduled "
                "departure time", quote=True)),
        "22:01", "The ORB's own UP time.", at="22:01"),
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
    "maudslay-release": Dispute(
        "Maudslay's attack", "AJ-Z",
        (Record(ORB, "Diverted from the Mohne to the Eder Dam, attacked first and registered a "
                "direct hit, but no result was seen.", "01:39", quote=True, label="Shannon"),
         Record(ORB, "The mine overshot and struck the parapet, detonating instantaneously.",
                quote=True, label="Maudslay"),
         Record(ORB, "Was the third aircraft to attack the Eder Dam.", quote=True, label="Knight"),
         Record(DB, "At 0157, some twenty minutes after they had dropped their mine, wireless "
                "operator Alden Cottam sent a ‘Goner 28B’ message back to base", "01:57",
                quote=True)),
        "01:45", "Keeps the ORB's order, after Shannon's 01:39 and before Knight's mine (about "
        "01:52, eder-breach), with B.976's three minutes either side; \"some twenty minutes\" "
        "before 01:57 would put it at about 01:37, before Shannon's.", at="01:45"),
    "eder-breach": Dispute(
        "Eder breach", "EDER",
        (Record("lwl-moehne", "Etwa eine Stunde später, um 01.37 Uhr, wurde auch dieser Staudamm "
                "zerstört.", "01:37", quote=True),
         Record("dewiki-eder", "Am 17. Mai 1943 kurz vor 2 Uhr nachts wurde die Ederstaumauer bei "
                "einem Angriff", quote=True),
         Record("wikipedia-gibson", "At 01:54, Hutchinson signalled the breach and then "
                "confirmed it.", "01:54", quote=True),
         Record(WP, "The final bomb of the formation, from Knight's aircraft (N for Nut), "
                "breached the dam.", quote=True)),
        "01:52", "On Knight's attack, two minutes before the signal; LWL's 01:37 comes before "
        "Shannon's 01:39 release in the ORB.", at="01:52"),
    "burpee-loss": Dispute(
        "Burpee's loss", "AJ-S",
        (Record("asn", "01:53", "01:53", quote=True, label="Time"),
         Record(ORB, "Shot down at 0200 immediately south of Gilze-Rijen (Netherlands) on way "
                "to target.", "02:00", quote=True, label=EDITOR)),
        "02:00", "The ORB editor's note; the two differ by seven minutes.", at="02:00"),
    "ottley-loss": Dispute(
        "Ottley's loss", "AJ-C",
        (Record(DB, "At 0231, Group sent the code word “Gilbert” to AJ-C, and the signal was "
                "acknowledged.", "02:31", quote=True),
         Record(DB, "The second signal was not acknowledged, indicating that AJ-C had met its "
                "fate at about 0231.", "02:31", quote=True),
         Record(DB, "Ken Brown, flying AJ-F a few minutes behind, reported seeing him hit the "
                "ground at 0235.", "02:35", quote=True)),
        "02:35", "Brown's sighting, the one direct observation.", at="02:35"),
    "young-loss": Dispute(
        "Young's loss", "AJ-A",
        (Record("asn", "02:57", "02:57", quote=True, label="Time"),
         Record(ORB, "\"Dinghy\" Young's Lancaster was shot down by flak North of Ijmuiden at "
                "0258 (Castricum aan Zee) killing all the crew.", "02:58", quote=True,
                label=EDITOR)),
        "02:58", "The ORB editor's note; the two differ by a minute.", at="02:58"),
    "townsend-target": Dispute(
        "Townsend's target", "AJ-O",
        (Record(ORB, "ENNEPE DAM. 1 Mine. 60ft. 0337 hrs.", "03:37", quote=True),
         Record(ORB, "Post war research proves that Townsend attacked not the Ennerpe Dam but the "
                "Bever Dam nearby to the North West instead.", quote=True, label=EDITOR),
         Record("hinks-2010", "Sweetman (2002) makes a strong case that the fourth dam attacked "
                "was the Bever Dam", quote=True)),
        "The Ennepe, as reported", "Townsend's own report; the dams' coordinates put the Bever "
        "11 km south of the Ennepe, not north-west.", shown="03:37",
        brief="Townsend reported attacking the Ennepe dam; post-war research suggests it was "
        "the Bever dam nearby."),
    "martin-mine": Dispute(
        "Martin's mine", "AJ-P",
        (Record(ORB, "Mine burst about 20 yds. short.", "00:38", quote=True),
         Record(WP, "Mine missed the target.", quote=True)),
        "Bursts 18 m short", "The ORB's distance; Wikipedia agrees it missed.", shown="00:38"),
    "sorpe-geometry": Dispute(
        "The Sorpe run", "SORPE",
        (Record(WP, "the approach was made along the length of the dam, not at right angles over "
                "the reservoir", quote=True),
         Record(ORB, "detailed to fly from left to right at about 30 degrees with the mine "
                "bouncing up to the dam face", quote=True, label=EDITOR)),
        "Along the crest, unspun", "McCarthy's own report of \"the run along the Dam\" (ORB).",
        shown="00:46"),
    "release-speed": Dispute(
        "Release speed", None,
        (Record("order-b976", "the height of attack is to be 60 feet and the ground speed 220 "
                "m.p.h.", quote=True),
         Record(WP, "at an air speed of 240 mph (390 km/h)", quote=True),
         Record("gibson-eca", "we were being dragged along at four miles a minute", quote=True)),
        "220 mph", "The operation order's figure.", shown="00:28"),
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
    "serials": Dispute(
        "Serials of AJ-A and AJ-T", None,
        (Record(ORB, "ED. 877G. (A)", quote=True, label="Young's sheet"),
         Record("asn", "ED877 was hit by Flak", quote=True, label="Young's loss, whose "
                "registration field reads ED887"),
         Record(ORB, "Lancaster III ED 923 G. (T)", quote=True, label="McCarthy's sheet"),
         Record(DB, "McCarthy flew the spare ED825/G.", checked=False)),
        "ED887/G and ED825/G", "The usual identifications of the aircraft flown; the ORB "
        "transcript's serials disagree.", shown="21:47"),
}


def time_of(key):
    """The estimate's clock time for a dispute that sets a time."""
    return ledger.time_of(DISPUTES, key)
