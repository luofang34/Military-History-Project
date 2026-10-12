"""The Sorpe: McCarthy's and Brown's runs along the crest."""
from ledger import Dispute, Moment, Record

from .names import DB, EDITOR, LOG, ORB, WP  # noqa: F401

MOMENTS = {
    "mccarthy-release": Moment(
        "McCarthy's attack", "AJ-T", "00:46",
        (Record(ORB, "McCarthy attacks along the crest at 0046 after nine dummy runs, dropping "
                "from 30 ft without spin; the dam holds.", "00:46"),)),
    "brown-release": Moment(
        "Brown's attack", "AJ-F", "03:14",
        (Record(ORB, "Brown attacks the Sorpe from 60 ft at 0314 after marking it with "
                "incendiaries; the crest holds.", "03:14"),)),
}

DISPUTES = {
    "mccarthy-arrival": Dispute(
        "McCarthy's arrival at the Sorpe", "AJ-T",
        (Record(DB, "Flying as fast as he could, McCarthy made up 13 or 14 minutes by the time he "
                "reached the Sorpe at 0015", "00:15", quote=True),
         Record(LOG, "Target Z", "00:30", label="Navigator's log, page 3", quote=True),
         Record(DB, "He recorded the time of arrival at Target Z as 0030", "00:30", quote=True,
                label="Foster on MacLean's log")),
        "00:30", "The log's own time, as the blog later reads it too. Ten approaches from about "
        "00:32, once across from the Möhne side, to the 00:46 release take 90 s each, which the "
        "blog also works out (\"not much more than 90 seconds\") and a tight circuit allows.",
        at="00:30"),
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
    "sorpe-geometry": Dispute(
        "The Sorpe run", "SORPE",
        (Record(WP, "the approach was made along the length of the dam, not at right angles over "
                "the reservoir", quote=True),
         Record(ORB, "detailed to fly from left to right at about 30 degrees with the mine "
                "bouncing up to the dam face", quote=True, label=EDITOR),
         Record(WP, "led over a church steeple in the village of Langscheid", quote=True),
         Record(DB, "The approach involved flying over the small town of Langscheid, which had "
                "a prominent church steeple", quote=True)),
        "Along the crest, unspun; McCarthy in over Langscheid's steeple",
        "McCarthy's own report of \"the run along the Dam\" (ORB). His crew came in over the "
        "church of St. Antonius, Langscheid, 320 m to the lake side of the crest line, at some "
        "30-40° to the crest, as the editor's note has it, and turned onto it before the dam.",
        shown="00:46"),
}
