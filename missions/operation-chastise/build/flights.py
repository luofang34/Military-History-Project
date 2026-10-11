"""Every Lancaster's night, from the ORB's take-off minute to its landing minute or its loss.

Legs between sourced anchors are flown at constant ground speed along the planned routes; the
anchors are the ORB's times, the navigators' logs and the loss times quoted in the README.
The first wave flew in vics of three, the others singly.
"""
import targets
from evidence import time_of
import waypoints as w
from manoeuvre import CIRCUIT_ALT_M, FINAL, between, circuit_to, go, land, take_off
from plan import Plan
from sites import (CRASH, FRONDENBERG, GUNNE, HIMMELPFORTEN, L, LANDED, MOHNE, NEHEIM_CAMP,
                   NIEDERENSE, SCHWERTE, TAKE_OFF, WICKEDE)
from track import Track, bearing_deg, distance_m

ENGLAND = {w.WEST_RAYNHAM, w.WAINFLEET, w.NORTH_COAST_OUT}
SEA = {w.ZERO, w.NORTH_ZERO, w.NORTH_SEA_EXIT, w.VLIELAND_GAP, w.STAVOREN, w.AFSLUITDIJK,
       w.VLIELAND}
SLOTS = [(0, 0), (-110, -90), (110, -90)]  # (right m, ahead m) in a vic

# Loss times: the ORB's notes, dambustersblog and the crews' logs (see the README).
LOSS = {"AJ-K": "22:57", "AJ-E": "23:50", "AJ-B": "00:15", "AJ-M": "00:34",
        "AJ-S": time_of("burpee-loss"), "AJ-C": time_of("ottley-loss"), "AJ-Z": "02:36",
        "AJ-A": time_of("young-loss")}


def alt(point):
    if point == FINAL:
        return CIRCUIT_ALT_M
    if point == w.OSTONNEN_CLIMB:
        return 150.0
    if point in ENGLAND or point == w.SOUTHWOLD:
        return 150.0 if point == w.SOUTHWOLD else 300.0
    return 18.0 if point in SEA else 40.0


def depart(plan, code, slot=0):
    at = L(TAKE_OFF[code])
    plan.tracks[code] = take_off(at, slot)
    plan.phase(code, 0, "reconstruction-airfield", 1000.0)
    plan.phase(code, at + 80_000, "reconstruction-route", 5000.0)
    return plan.tracks[code]


def fly(plan, code, points, arrive):
    """Constant speed through `points`, reaching the last at clock time `arrive`."""
    return between(plan.tracks[code], points, L(arrive), [alt(p) for p in points])


def onward(plan, code, points, kmh):
    go(plan.tracks[code], [(None, p, alt(p)) for p in points], kmh)


def home(plan, code, points):
    """Flies `points` at constant speed to the final approach and lands at the ORB's minute."""
    plan.phase(code, plan.tracks[code].end + 1, "reconstruction-route", 5000.0)
    track = plan.tracks[code]
    landing = L(LANDED[code])
    points = list(points) + [FINAL]
    between(track, points, landing - 120_000, [alt(p) for p in points])
    plan.phase(code, landing - 120_000, "reconstruction-airfield", 1000.0)
    land(track, landing)
    plan.landed[code] = landing


def lose(plan, code, via=()):
    """Flies `via` at constant speed and reaches the crash site at the loss time."""
    site, _, _ = CRASH[code]
    track = plan.tracks[code]
    between(track, list(via) + [site], L(LOSS[code]), [alt(p) for p in via] + [0.0])
    plan.lost[code] = L(LOSS[code])
    plan.condition("dambustersblog", code, L(LOSS[code]), "destroyed")


def vic(plan, codes, route, arrive, split, abeam=None):
    """A section in vic: the leader flies `route` to `arrive`, the others hold their slots
    until `split`. With `abeam` = (index, clock), the leader is timed to that route point and
    keeps the same speed beyond it."""
    lead = depart(plan, codes[0])
    if abeam:
        i, at = abeam
        v = fly(plan, codes[0], route[:i + 1], at)
        onward(plan, codes[0], route[i + 1:], v * 3.6)
    else:
        fly(plan, codes[0], route, arrive)
    for slot, code in enumerate(codes[1:], start=1):
        own = depart(plan, code, slot)
        after = own.end + 60_000
        for wp in lead.shifted(*SLOTS[slot]).waypoints:
            if after < wp.at_ms <= L(split):
                own.add(wp.at_ms, wp.point, wp.alt_m)
    return lead


def wave_one(plan):
    route = [w.WEST_RAYNHAM] + w.SOUTH_OUT
    vic(plan, ["AJ-G", "AJ-M", "AJ-P"], route, "00:13", "00:13")
    plan.condition("dambustersblog", "AJ-M", time_at(plan.tracks["AJ-M"], w.HALTERN_LAKES),
                   "damaged")
    vic(plan, ["AJ-A", "AJ-J", "AJ-L"], route, "00:24", "00:24")
    # Maudslay's section is placed abeam Marbeck at 00:15, when Knight's wireless operator
    # logged Astell going down; it keeps that speed to the Möhne.
    marbeck = route.index(w.HALTERN_LAKES)
    route3 = route[:marbeck] + [w.MARBECK_ABEAM] + route[marbeck:]
    lead = vic(plan, ["AJ-Z", "AJ-B", "AJ-N"], route3, None, "00:40",
               abeam=(marbeck, "00:15"))
    astell = plan.tracks["AJ-B"]
    lagging = time_at(lead, w.ROOSENDAAL) + 60_000  # after the canal turn
    astell.waypoints = [p for p in astell.waypoints if p.at_ms < lagging]
    for wp in lead.shifted(-700, -800).waypoints:
        if lagging <= wp.at_ms < L("00:12"):
            astell.add(wp.at_ms, wp.point, wp.alt_m)
    lose(plan, "AJ-B")


def time_at(track, point):
    """The time `track` passes closest to `point`."""
    return min((distance_m(wp.point, point), wp.at_ms) for wp in track.waypoints)[1]


def wave_two(plan):
    out = [w.NORTH_COAST_OUT, w.NORTH_ZERO, w.VLIELAND_GAP]
    for code in ("AJ-E", "AJ-W", "AJ-K", "AJ-H", "AJ-T"):
        depart(plan, code)
    lose(plan, "AJ-E", out + [w.STAVOREN, w.HARDERWIJK, w.DOESBURG])
    fly(plan, "AJ-W", out, "22:54")
    plan.condition("orb-617", "AJ-W", L("22:54"), "damaged")
    home(plan, "AJ-W", [w.NORTH_ZERO, w.NORTH_COAST_OUT])
    lose(plan, "AJ-K", out[:2] + [w.TEXEL_NORTH])
    fly(plan, "AJ-H", out, "22:59")
    go(plan.tracks["AJ-H"], [(L("23:01"), w.RICE_SEA, 0.0)], 0)
    plan.condition("orb-617", "AJ-H", L("23:01"), "damaged")
    home(plan, "AJ-H", [w.VLIELAND_GAP, w.NORTH_ZERO, w.NORTH_COAST_OUT])
    mccarthy_out(plan)


# McCarthy's legs and the times his navigator logged at each turn (mccarthy-route-out,
# mccarthy-route-home), at constant speed between them.
MCCARTHY_OUT = [
    ([w.NORTH_COAST_OUT, w.NORTH_ZERO, w.VLIELAND_GAP, w.STAVOREN], "23:26:30"),
    ([w.HARDERWIJK], "23:37:30"), ([w.DOESBURG], "23:49:30"), ([w.REES], "23:57"),
    ([w.HALTERN_LAKES], "00:10"), ([w.AHLEN], "00:20"), ([w.MOHNE_TURN], "00:27"),
]
MCCARTHY_HOME = [
    ([w.MOHNE_TURN], "00:54"), ([w.AHLEN], "00:59"), ([w.HAMM, w.HALTERN_LAKES, w.REES], "01:32"),
    ([w.DOESBURG], "01:37"), ([w.HARDERWIJK], "01:46"), ([w.STAVOREN], "01:57"),
    ([w.AFSLUITDIJK, w.VLIELAND], "02:06"),
]


# Ten approaches between the 00:30 arrival and the 00:46 release (mccarthy-arrival), the
# first once he has crossed from the Möhne side to the start of the run: 90 s apart, as the
# blog works out from the log. That leaves room only for a tight circuit, pulling up soon
# after the crest; the ORB has a hill at either end of the run.
MCCARTHY_FIRST, MCCARTHY_RUN_MS = "00:32:30", 90_000
MCCARTHY_CIRCUIT_M, MCCARTHY_EXIT_M = 700, 400


def mccarthy_out(plan):
    for points, at in MCCARTHY_OUT:
        fly(plan, "AJ-T", points, at)
    fly(plan, "AJ-T", [w.SORPE_NORTH], time_of("mccarthy-arrival"))


def mccarthy_home(plan):
    """Circles the Sorpe after the release until the log's 00:51 "Target Z a/c Target X", then
    flies its homeward legs."""
    track = plan.tracks["AJ-T"]
    circuit_to(track, w.SORPE_NORTH, bearing_deg(w.SORPE_NORTH, w.MOHNE_TURN), 1300,
               L("00:51"), 250.0)
    plan.phase("AJ-T", track.end + 1, "reconstruction-route", 5000.0)
    for points, at in MCCARTHY_HOME:
        fly(plan, "AJ-T", points, at)
    home(plan, "AJ-T", [w.NORTH_ZERO, w.NORTH_COAST_OUT])


def wave_three(plan):
    for code in ("AJ-C", "AJ-S", "AJ-F", "AJ-O", "AJ-Y"):
        depart(plan, code)
    out = w.SOUTH_OUT
    lose(plan, "AJ-S", out[:out.index(w.GILZE_SOUTH) + 1])
    lose(plan, "AJ-C", out[:out.index(w.AHSEN) + 1])
    fly(plan, "AJ-F", out[:out.index(w.AHLEN) + 1] + [w.SORPE_NORTH], "02:48")
    fly(plan, "AJ-O", out[:out.index(w.AHSEN) + 1], "02:38")
    fly(plan, "AJ-O", [w.ENNEPE_SEARCH], "02:52")
    fly(plan, "AJ-Y", out[:out.index(w.AHSEN) + 1] + [w.ANDERSON_TURN], "03:10")
    plan.phase("AJ-Y", L("02:20"), "reconstruction-route", 20_000.0)


def returns(plan):
    """Return routes as the planned-routes map numbers them; Shannon's is not known and is
    placed on Knight's."""
    lose(plan, "AJ-M", [w.OSTONNEN_CLIMB])
    home(plan, "AJ-J", w.RETURN_1[:-1])
    home(plan, "AJ-P", w.RETURN_1[:-1])
    lose(plan, "AJ-Z", [w.REES])
    lose(plan, "AJ-A", [MOHNE, w.HARDERWIJK])
    home(plan, "AJ-G", [MOHNE] + w.RETURN_3[:-1])
    home(plan, "AJ-N", w.RETURN_2[:-1])
    home(plan, "AJ-L", w.RETURN_2[:-1])
    mccarthy_home(plan)
    home(plan, "AJ-F", [MOHNE] + w.RETURN_1[:-1])
    home(plan, "AJ-O", w.RETURN_1[1:-1])
    home(plan, "AJ-Y", [w.DULMEN, w.REES, w.GOCH, w.BEEK, w.ROOSENDAAL, w.SCHELDT, w.ZERO,
                        w.SOUTHWOLD])


def flood():
    """The Möhne flood front through the towns whose times de.wikipedia gives: the breach at
    00:49, Neheim 01:20, Wickede about 02:00, Fröndenberg about 03:00, Schwerte 05:15."""
    t = Track().add(L("00:49:10"), MOHNE, 0)
    between(t, [GUNNE, HIMMELPFORTEN, NIEDERENSE, NEHEIM_CAMP], L("01:20"), [0] * 4)
    t.add(L("02:00"), WICKEDE, 0)
    t.add(L("03:00"), FRONDENBERG, 0)
    t.add(L("05:15"), SCHWERTE, 0)
    return t


def damage(plan):
    """Each target's reported state once the mine that changed it has gone off: the Möhne
    and the Eder breached (no longer able to hold their water, "destroyed" in MIL-STD-2525),
    the Sorpe's crest crumbled but holding, the Möhne power station wrecked by Hopgood's
    mine."""
    burst = {code: plan.mines[f"UPKEEP {code}"].end for code in ("AJ-J", "AJ-N", "AJ-T", "AJ-M")}
    plan.condition("dewiki-moehne", "MÖHNE", burst["AJ-J"], "destroyed")
    plan.condition("dewiki-eder", "EDER", burst["AJ-N"], "destroyed")
    plan.condition("orb-617", "SORPE", burst["AJ-T"], "damaged")
    plan.condition("orb-617", "MÖHNE POWER STATION", burst["AJ-M"], "destroyed")


def build():
    plan = Plan()
    wave_one(plan)
    wave_two(plan)
    wave_three(plan)
    targets.mohne(plan)
    targets.eder(plan)
    # McCarthy drops on his tenth run (evidence: mccarthy-runs); Brown makes seven runs,
    # marks the mist with incendiaries, and drops on the eighth.
    targets.sorpe(plan, "AJ-T", [L(MCCARTHY_FIRST) + k * MCCARTHY_RUN_MS for k in range(9)],
                  "00:46", 30 * 0.3048, radius=MCCARTHY_CIRCUIT_M, exit_m=MCCARTHY_EXIT_M)
    targets.sorpe(plan, "AJ-F", ["02:51", "02:54", "02:57", "03:00", "03:03", "03:06",
                                 "03:09"], "03:14", 60 * 0.3048)
    targets.ennepe(plan)
    damage(plan)
    returns(plan)
    plan.flood = flood()
    return plan
