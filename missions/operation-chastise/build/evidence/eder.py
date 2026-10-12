"""The Eder: the attacks, the breach and the flood."""
from ledger import Dispute, Moment, Record

from .names import DB, EDITOR, LOG, ORB, WP  # noqa: F401

MOMENTS = {
    "shannon-release": Moment(
        "Shannon's attack", "AJ-L", "01:39",
        (Record(ORB, "Shannon attacks at 0139; the mine bounces twice and explodes, with no "
                "visible result.", "01:39"),)),
}

DISPUTES = {
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
    "eder-flood": Dispute(
        "The Eder flood down the valley", "EDER FLOOD",
        (Record("dewiki-eder", "In der Folge ergoss sich eine 6 bis 8 m hohe Flutwelle durch das "
                "untere Edertal nach Fritzlar, Wabern und Felsberg", quote=True),
         Record("geschichtskreis-wabern", "Um 5.30 Uhr traf die Flutwelle ein", "05:30",
                quote=True)),
        "05:30", "Wabern's arrival is the one time found below the dam; the front runs there "
        "from the breach at an even pace through Affoldern, Bergheim, Wega and Fritzlar.",
        at="05:30"),
}
