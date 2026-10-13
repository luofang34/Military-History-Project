"""Tuesday 18 October: Stuart's summons and the marines' assault on the engine house."""
from ledger import Dispute, Record

from .names import DEWITT, GREENE, LEE, MASON, NPS, VILLARD, WP

MOMENTS = {}

DISPUTES = {
    "engine-house-stormed": Dispute(
        "When the marines stormed the engine house and took Brown", "BROWN",
        (Record(GREENE, "At half-past six in the morning Colonel Lee gave me orders to select a "
                "detail of twelve men for a storming party", "18 06:30", quote=True),
         Record(WP, "At 6:30 AM Lee began the attack", "18 06:30", quote=True),
         Record(VILLARD, "At sunrise, when Lieutenant Stuart gave his signal", quote=True),
         Record(DEWITT, "Shortly after 7 o'clock, Lieutenant E.B. Stuart … advanced to parley",
                "18 07:00", quote=True),
         Record(NPS, "7:00 am Brown refuses to surrender to Lt. J.E.B. Stuart.", "18 07:00",
                quote=True),
         Record(MASON, "about half-past seven o'clock on Tuesday morning", "18 07:30",
                quote=True, label="Lewis W. Washington, of his delivery"),
         Record(LEE, "The whole was over in a few minutes.", quote=True),
         Record(GREENE, "the whole fight had not lasted over three minutes.", quote=True)),
        "Stuart at the door at 6:58, the doors broken in at 7:02 and Brown cut down a minute "
        "later", "Greene's half past six is his order to pick the storming party, before the "
        "summons; the papers and the Park Service put the summons at about seven, and "
        "Washington was out by half past.", at="18 07:00",
        brief="When the marines went in is disputed, from half past six to after seven; the "
              "replay sends Stuart to the door just before seven."),
}
