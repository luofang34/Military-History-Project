"""The decisive releases, each shot as a sequence of its own.

The wide shot of a dam shows where an attack comes from; at the moment that decides it the
story cuts in behind the attacker, selected so its panel shows the height of the run, then
rides the mine to the wall, orbits the dam through the burst, and pulls back out.
"""
from pacing import viewing_between
from sites import EDER_RUN, MOHNE_RUN

CHASE_MS = 20_000  # behind the attacker before release: the last mile of the run
AFTER_MS = 30_000  # orbiting the dam once the mine has gone
# Close behind the attacker; the dam, far ahead and lifted by the ground it stands on, comes
# into frame only on the mine's ride.
CHASE_ZOOM, CHASE_PITCH = 15.6, 60
MIN_BACK_S = 3.0  # a pull-back shorter than this in viewing folds into the orbit
# Knight's run turns onto the Eder late, past the Hammerberg spit; behind him any earlier,
# the dam is not yet ahead.
CHASE_FOR = {"AJ-N": 12_000}

# (attacker, dam, run heading, chase intent, mine intent, burst intent, pull-back intent)
DROPS = [
    ("AJ-G", "MÖHNE", MOHNE_RUN,
     "Behind Gibson down the lake, the first attack of the night, held at 60 ft by the "
     "spotlights.",
     "Ride Gibson's mine as it skips toward the wall.",
     "Round the dam as the mine bursts short and the water rises.",
     "Back out over the lake while the water settles for the next attack."),
    ("AJ-J", "MÖHNE", MOHNE_RUN,
     "Behind Maltby on the run that decides the Möhne, Gibson and Martin flanking him.",
     "Ride Maltby's mine to the wall.",
     "Round the dam as the wall gives way.",
     "Back out over the breach."),
    ("AJ-N", "EDER", EDER_RUN,
     "Behind Knight, the last mine in the first wave, as he turns onto the Eder.",
     "Ride Knight's mine to the wall.",
     "Round the Eder as it breaks.",
     "Back out over the Eder valley."),
]


def releases(plan):
    """{attacker: (release ms, mine track)} for the drops in DROPS."""
    at = {r.code: r.at_ms for r in plan.releases}
    return {code: (at[code], plan.mines[f"UPKEEP {code}"]) for code, *_ in DROPS}


def chase_ms(code):
    return CHASE_FOR.get(code, CHASE_MS)


def windows(plan):
    """(release, end of orbit) ms of each drop sequence."""
    return [(release, mine.end + AFTER_MS) for release, mine in releases(plan).values()]


def sequence(f, plan, code, base_end, base):
    """Adds the drop sequence for `code` to framer `f`, then the rest of its wide shot until
    `base_end` with `base(start, end, intent)`."""
    attacker, dam, heading, chase, ride, burst, back = next(d for d in DROPS if d[0] == code)
    release, mine = releases(plan)[code]
    mine_id = f"UPKEEP {code}"
    landed = mine.end
    orbit_end = landed + AFTER_MS
    if viewing_between(f.pacing, orbit_end, base_end) < MIN_BACK_S:
        orbit_end = base_end
    f.view(release - chase_ms(code), release, {"intent": chase, "shows": [attacker]},
           attacker, CHASE_ZOOM, CHASE_PITCH, heading, move=0, focus=attacker)
    f.view(release, landed, {"intent": ride, "shows": [mine_id, dam]}, mine_id, 16.4, 60,
           heading, move=0.8)
    f.view(landed, orbit_end, {"intent": burst, "shows": [dam]}, dam, 15.4, 55, heading,
           orbit=1.5, move=1)
    if orbit_end < base_end:
        base(orbit_end, base_end, back)
