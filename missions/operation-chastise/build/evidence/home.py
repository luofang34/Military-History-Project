"""The flight home and the landings."""
from ledger import Dispute, Moment, Record

from .names import DB, EDITOR, LOG, ORB, WP  # noqa: F401

MOMENTS = {
    "maudslay-loss": Moment(
        "Maudslay's loss", "AJ-Z", "02:36",
        (Record(DB, "Maudslay is shot down by flak at Klein-Netterden, near Emmerich, at 0236; "
                "all are killed.", "02:36"),)),
    "gibson-landing": Moment(
        "Gibson lands", "AJ-G", "04:15",
        (Record(WP, "Gibson lands at Scampton at 0415.", "04:15"),)),
    "last-landing": Moment(
        "The last landing", "AJ-O", "06:15",
        (Record(ORB, "Last landing 0615: Townsend, the last back, crosses Holland in daylight.",
                "06:15"),)),
}

DISPUTES = {
    "young-loss": Dispute(
        "Young's loss", "AJ-A",
        (Record("asn", "02:57", "02:57", quote=True, label="Time"),
         Record(ORB, "\"Dinghy\" Young's Lancaster was shot down by flak North of Ijmuiden at "
                "0258 (Castricum aan Zee) killing all the crew.", "02:58", quote=True,
                label=EDITOR)),
        "02:58", "The ORB editor's note; the two differ by a minute.", at="02:58"),
    "mccarthy-route-home": Dispute(
        "McCarthy's route home", "AJ-T",
        (Record(LOG, "Target Z a/c Target X; Target X a/c Ahlen; Ahlen a/c Lake; Lake a/c Rees; "
                "Rees a/c Doesburg; Doesburg a/c Harderwijk; Harderwijk a/c Stavoren; Wall; "
                "Island Vlieland; Mablethorpe", label="Navigator's log, page 3, its legs in order"),
         Record(DB, "they simply backtracked along their outbound course", quote=True),
         Record(DB, "McCarthy set course for home, but went via the Möhne, having heard over the "
                "radio that it had been breached.", quote=True),
         Record(DB, "ending up over the heavily defended town of Hamm.", quote=True,
                label="Foster on MacLean")),
        "The outbound legs reversed, off course over Hamm between Ahlen and the lakes",
        "The log reverses its outbound legs and names no Hamm; its Ahlen to Rees leg, 00:59 to "
        "01:32, takes half as long again as the same leg out, room for the deviation both blog "
        "posts describe. Times are the log's legible ones. The log crosses the English coast "
        "at Mablethorpe about 03:02 and is over base at 03:18; the replay, with no circuit of "
        "Scampton before the 03:23 landing (ORB), crosses about 03:11.", shown="00:59"),
}
