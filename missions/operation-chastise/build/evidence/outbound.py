"""The flight out: take-offs, the routes and the losses before the targets."""
from ledger import Dispute, Moment, Record

from .names import DB, EDITOR, LOG, ORB, WP  # noqa: F401

MOMENTS = {
    "first-take-off": Moment(
        "The first take-off", None, "21:28",
        (Record(ORB, "First take-off 2128; the second wave leaves Scampton singly from 21:28 to "
                "21:31.", "21:28"),)),
    "gibson-take-off": Moment(
        "Gibson's take-off", "AJ-G", "21:39",
        (Record(ORB, "Gibson, Hopgood and Martin take off in a vic at 2139.", "21:39"),)),
    "munro-hit": Moment(
        "Munro hit at Vlieland", "AJ-W", "22:54",
        (Record(ORB, "Light flak at Vlieland hits AJ-W about 2254 and knocks out the intercom; "
                "Munro turns for home with his mine.", "22:54"),)),
    "byers-loss": Moment(
        "Byers's loss", "AJ-K", "22:57",
        (Record(DB, "Byers, off track over Texel, is shot down by flak at 2257 and falls into the "
                "Waddenzee; all seven are killed.", "22:57"),)),
    "barlow-loss": Moment(
        "Barlow's loss", "AJ-E", "23:50",
        (Record(DB, "Barlow hits high-tension cables at Haldern at 2350 and crashes; all seven "
                "are killed.", "23:50"),)),
    "astell-loss": Moment(
        "Astell's loss", "AJ-B", "00:15",
        (Record(DB, "Astell flies into high-tension cables near Marbeck at 0015.", "00:15"),)),
}

DISPUTES = {
    "mccarthy-delay": Dispute(
        "McCarthy's late take-off", "AJ-T",
        (Record(ORB, "Had trouble with his compass and took off 20 mins. late.", "22:01",
                quote=True),
         Record(WP, "took off in the reserve aircraft 34 minutes late", quote=True),
         Record(DB, "AJ-T eventually took to the air some 33 minutes later than their scheduled "
                "departure time", quote=True)),
        "22:01", "The ORB's own UP time.", at="22:01"),
    "mccarthy-route-out": Dispute(
        "McCarthy's route to the Sorpe", "AJ-T",
        (Record(LOG, "Stavoren a/c Harderwijk; Harderwijk a/c Doesburg; Doesburg a/c Rees; Rees "
                "a/c Lake; Lake a/c Ahlen; Ahlen a/c Target X; Target X a/c Target Z",
                label="Navigator's log, page 3, its legs in order"),
         Record(WP, "Formation No. 2 flew further north, cutting over Vlieland and crossing the "
                "IJsselmeer", quote=True),
         Record(WP, "before joining the first route near Wesel", quote=True)),
        "The northern route by Doesburg to Rees, then the lakes, Ahlen and the Möhne",
        "The log's own legs. Rees, where it joins the southern route, lies near Wesel; Target X, "
        "the Möhne, is where it turns for the Sorpe, placed 2 km short of the dam.",
        shown="00:20"),
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
