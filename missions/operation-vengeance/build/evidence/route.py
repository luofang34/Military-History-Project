"""The P-38s' route to Bougainville."""
from ledger import Dispute, Record

from .names import AMES, GRANT, HN, REPORT, SCAN, WP

MOMENTS = {
}

DISPUTES = {
    "route-length": Dispute(
        "Length of the P-38 route", "MITCHELL",
        (Record(REPORT, "the flight went 410 miles over the circuitous all-water route",
                quote=True, label=SCAN),
         Record(REPORT, "a 435 mile interception by land planes largely over water", quote=True,
                label=SCAN),
         Record(AMES, "the longest combat mission yet flown (420 miles)", quote=True),
         Record(GRANT, "Two-and-half-hours later, the Lightnings had flown for 494 miles.",
                quote=True),
         Record(WP, "This roundabout approach was plotted and measured to be about 600 miles "
                "(970 km).", quote=True)),
        "About 435 mi", "The report's summary figure, which Pacific Wrecks repeats.",
        shown="08:20"),
    "final-turn": Dispute(
        "The final turn", "MITCHELL",
        (Record(HN, "At 0925, less than 20 miles off Bougainville, they made their final turn "
                "to the northeast", "09:25", quote=True),),
        "09:18, 56 mi out", "At the route's 215 mph a turn at 09:25 lies about 32 mi from the "
        "09:34 interception, not under 20; the replay keeps the stated speed and sighting time.",
        at="09:18", outside=True),
}
