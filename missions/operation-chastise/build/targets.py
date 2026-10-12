"""The attacks, from arrival in each target's holding circuit to departure for home.

Release times are the ORB's (Maltby's 00:49 from his navigator's log, the ORB's "0139" being
Shannon's time copied). Circuits are left-hand, as B.976 orders, and run tangent into each
dam's run. Dummy-run counts follow the crews' accounts; their times are spaced evenly between
arrival and release and are not sourced. Each run's geometry is reconstructed from the dam's
crest and the accounts quoted in the README.
"""
import math

from evidence import time_of
from manoeuvre import RELEASE_M, RUN_ALT_M, alongside, attack_run, circuit_to, go, turn
from sites import (EDER, EDER_RUN, ENNEPE, HAMMERBERG, L, MOHNE, MOHNE_RUN, POWER_STATION,
                   SHORE_M, SORPE, SORPE_AXIS, WALDECK)
from track import MPH, bearing_deg, destination, distance_m

HOLD_ALT_M = 200.0

# Möhne: runs down the lake on 323°, toward the water face, with a climbing turn to port.
MOHNE_RELEASE = destination(MOHNE, MOHNE_RUN + 180, RELEASE_M)
MOHNE_START = destination(MOHNE_RELEASE, MOHNE_RUN + 180, 4500)

# Eder: over Waldeck castle toward the Hammerberg spit, a 90° turn to port onto the dam, and a
# steep climbing turn to starboard to clear the hill beyond it.
EDER_RELEASE = destination(EDER, EDER_RUN + 180, RELEASE_M)
EDER_DIVE = bearing_deg(WALDECK, HAMMERBERG)
EDER_START = destination(WALDECK, EDER_DIVE + 180, 2000)
EDER_LINED_UP_M = 500.0
EDER_LINED_UP = destination(EDER_RELEASE, EDER_RUN + 180, EDER_LINED_UP_M)

# Sorpe: along the crest from over Langscheid, at the lowest practicable height and 180 mph,
# the mine dropped unspun near the middle of the crest on the water side.
SORPE_RUN = SORPE_AXIS
SORPE_SPEED = 180 * MPH
SORPE_WATER = destination(SORPE, SORPE_AXIS + 90, 20)
SORPE_RELEASE = destination(SORPE_WATER, SORPE_RUN + 180, 110)
SORPE_START = destination(SORPE_RELEASE, SORPE_RUN + 180, 1500)
# McCarthy's crew flew in over the steeple of St. Antonius, Langscheid (sorpe-geometry), which
# stands 320 m to the lake side of the crest line, and turned onto the crest before the dam.
STEEPLE = (7.95528, 51.35465)  # OpenStreetMap
SORPE_NW_END = (7.964935, 51.353015)  # OpenStreetMap, the dam's outline
# Onto the crest line, through the release, 150 m before the dam's north-west end, so the run
# is straight along the whole crest.
CREST_LINE_IN = destination(SORPE_RELEASE, SORPE_RUN + 180,
                            distance_m(SORPE_NW_END, SORPE_RELEASE) + 150)
STEEPLE_IN = bearing_deg(STEEPLE, CREST_LINE_IN)
STEEPLE_START = destination(STEEPLE, STEEPLE_IN + 180, 400)

# Ennepe: Townsend reported his run on 355° magnetic; the run here is perpendicular to the
# crest, from the lake to the south.
ENNEPE_RUN = 1.0
ENNEPE_RELEASE = destination(ENNEPE, ENNEPE_RUN + 180, RELEASE_M)
ENNEPE_START = destination(ENNEPE_RELEASE, ENNEPE_RUN + 180, 3000)


def T(clock):
    return L(clock)


def mohne_run(plan, code, release_at, radius=3000, release_m=RELEASE_M, **kw):
    """Holding circuit, then a run from MOHNE_START released `release_m` short of the dam at
    `release_at`; returns the release point."""
    track = plan.tracks[code]
    lead_in = 4500 + RELEASE_M - release_m
    start_at = release_at - (lead_in / (220 * MPH)) * 1000
    circuit_to(track, MOHNE_START, MOHNE_RUN, radius, start_at - 1, HOLD_ALT_M)
    plan.phase(code, track.end - 1, "reconstruction-target", 400.0)
    # A late release keeps the run's line, so it reaches the water as far before the dam.
    shore = SHORE_M["MÖHNE"] + RELEASE_M - release_m
    return attack_run(track, MOHNE, MOHNE_RUN, release_at, shore, release_m=release_m,
                      lead_in_m=lead_in, **kw)


def escort(plan, code, leader, release_at, side_m, radius):
    """Holds, then flies beside `leader`'s run drawing the flak."""
    track = plan.tracks[code]
    lead = plan.tracks[leader]
    join_at = release_at - 25_000
    p, _ = lead.shifted(side_m, 120).at(join_at)
    circuit_to(track, destination(p, MOHNE_RUN + 180, 600), MOHNE_RUN, radius, join_at - 6000,
               HOLD_ALT_M)
    alongside(track, lead, release_at, side_m)
    go(track, [(None, destination(MOHNE, MOHNE_RUN - 30, 2500), 150)], 330)


def mohne(plan):
    """Gibson's dummy run and attack, then Hopgood, Martin, Young and Maltby under his control,
    Gibson and Martin flying beside the later runs (Maltby: Gibson to starboard, Martin to port;
    the sides on Martin's and Young's runs are not recorded)."""
    m = plan.drop
    mohne_run(plan, "AJ-G", T("00:21:30"))  # dummy run through the flak
    m("AJ-G", "MÖHNE", mohne_run(plan, "AJ-G", T("00:28")), MOHNE, T("00:28"), 3,
      end_m=55.0)
    # Hopgood, hit on the run-in, releases late: the mine bounces over the parapet onto the
    # power station, and the burning Lancaster climbs to about 500 ft and falls near Ostönnen.
    hopgood = T(time_of("hopgood-release"))
    rel = mohne_run(plan, "AJ-M", hopgood, radius=3200, release_m=150.0, pull_up_m=900.0)
    plan.condition("orb-617", "AJ-M", hopgood - 10_000, "damaged")
    m("AJ-M", "MÖHNE", rel, POWER_STATION, hopgood, 2, end_m=0.0, late=True)
    m("AJ-P", "MÖHNE", mohne_run(plan, "AJ-P", T("00:38"), radius=3400), MOHNE,
      T("00:38"), 3, end_m=18.0)
    escort(plan, "AJ-G", "AJ-P", T("00:38"), 180, 3000)
    # The ORB: 20 mm fire from the dam holes the starboard outer tank on the run.
    plan.condition("orb-617", "AJ-P", T("00:38"), "damaged")
    young = T(time_of("young-release"))
    m("AJ-A", "MÖHNE", mohne_run(plan, "AJ-A", young, radius=3800), MOHNE, young, 3)
    escort(plan, "AJ-G", "AJ-A", young, -200, 3000)
    escort(plan, "AJ-P", "AJ-A", young, 200, 3400)
    maltby = T(time_of("maltby-release"))
    m("AJ-J", "MÖHNE", mohne_run(plan, "AJ-J", maltby, radius=4200, climb_turn=-90),
      MOHNE, maltby, 4)
    escort(plan, "AJ-G", "AJ-J", maltby, 200, 3000)
    escort(plan, "AJ-P", "AJ-J", maltby, -200, 3400)
    # Gibson closes on the wall and sees the breach; the codeword goes at 00:56.
    near = destination(MOHNE, MOHNE_RUN + 180, 1500)
    circuit_to(plan.tracks["AJ-G"], near, MOHNE_RUN, 2000, T("00:53:30"), 250)
    go(plan.tracks["AJ-G"], [(T("00:54:00"), destination(MOHNE, MOHNE_RUN - 90, 800), 250)], 0)
    turn_toward(plan.tracks["AJ-G"], EDER)
    for code, radius, leave in [("AJ-L", 4600, "00:56:30"), ("AJ-Z", 5000, "00:56:30"),
                                ("AJ-N", 5400, "00:56:30"), ("AJ-J", 4200, "00:56"),
                                ("AJ-P", 3400, "00:56")]:
        circuit_to(plan.tracks[code], MOHNE_START, MOHNE_RUN, radius, T(leave),
                   HOLD_ALT_M + 50)
    circuit_to(plan.tracks["AJ-A"], MOHNE_START, MOHNE_RUN, 3800, T("00:57:00"),
               HOLD_ALT_M + 50)


def eder_run(plan, code, release_at, radius):
    track = plan.tracks[code]
    v = 220 * MPH
    lined_up_at = release_at - EDER_LINED_UP_M / v * 1000
    hammer_at = lined_up_at - distance_m(HAMMERBERG, EDER_LINED_UP) / v * 1000
    castle_at = hammer_at - distance_m(WALDECK, HAMMERBERG) / v * 1000
    start_at = castle_at - 2000 / v * 1000
    circuit_to(track, EDER_START, EDER_DIVE, radius, start_at, 330)
    plan.phase(code, start_at - 1, "reconstruction-target", 400.0)
    track.add(castle_at, WALDECK, 300.0)  # 1,000 ft over the castle, diving
    track.add(hammer_at, HAMMERBERG, 30.0)
    # Lined up on the wall before the release, not turning onto it at the release.
    track.add(lined_up_at, EDER_LINED_UP, RUN_ALT_M)
    track.add(release_at, EDER_RELEASE, RUN_ALT_M)
    over = destination(EDER, EDER_RUN, 150)
    track.add(release_at + (RELEASE_M + 150) / v * 1000, over, RUN_ALT_M + 15)
    turn(track, EDER_RUN, 45, 1800, v, 320.0)
    return EDER_RELEASE


def eder(plan):
    """Shannon's dummy runs and attack, Maudslay's, then Knight's breach; Gibson and Young
    circle over Waldeck castle in the left-hand orbit."""
    for code, at in [("AJ-G", "01:10"), ("AJ-A", "01:10:30"), ("AJ-L", "01:11"),
                     ("AJ-Z", "01:11:30"), ("AJ-N", "01:12")]:
        plan.phase(code, plan.tracks[code].end + 1, "reconstruction-route", 3000.0)
        go(plan.tracks[code], [(T(at), destination(EDER_START, 60, 3000), 400)], 0)
    for at in ("01:20", "01:25", "01:30", "01:34"):
        eder_run(plan, "AJ-L", T(at), 1500)
    plan.drop("AJ-L", "EDER", eder_run(plan, "AJ-L", T("01:39"), 1500), EDER,
              T("01:39"), 2, end_m=40.0)
    maudslay = T(time_of("maudslay-release"))
    eder_run(plan, "AJ-Z", maudslay - 240_000, 1700)
    rel = eder_run(plan, "AJ-Z", maudslay, 1700)
    plan.drop("AJ-Z", "EDER", destination(rel, EDER_RUN, 160), EDER, maudslay + 2000,
              1, end_m=0.0, late=True)
    plan.condition("orb-617", "AJ-Z", maudslay + 8000, "damaged")
    knight = T(time_of("eder-breach"))
    eder_run(plan, "AJ-N", knight - 240_000, 1900)
    plan.drop("AJ-N", "EDER", eder_run(plan, "AJ-N", knight, 1900), EDER, knight, 3)
    for code, radius, leave in [("AJ-G", 2600, T("01:55:30")), ("AJ-A", 3000, T("01:55")),
                                ("AJ-L", 1500, T("01:55:40")), ("AJ-Z", 1700, maudslay + 150_000),
                                ("AJ-N", 1900, T("01:56"))]:
        circuit_to(plan.tracks[code], EDER_START, EDER_DIVE, radius, leave, 330)


def turn_toward(track, point, mps=72.0, bank_deg=30.0):
    """Turns the shorter way from the track's heading onto the bearing of `point`, flown as
    an arc, before the leg that follows."""
    a, b = track.waypoints[-2], track.waypoints[-1]
    heading = bearing_deg(a.point, b.point)
    need = (bearing_deg(b.point, point) - heading + 180) % 360 - 180
    radius = mps ** 2 / (9.81 * math.tan(math.radians(bank_deg)))
    turn(track, heading, need, radius * math.radians(abs(need)), mps, b.alt_m)


def sorpe_run(plan, code, release_at, alt, radius=1300, exit_m=900, steeple=False):
    """A run along the crest released at `release_at`, then a climbing turn to port
    `exit_m` beyond the dam; with `steeple`, flown in over Langscheid's church onto the
    crest at its north-west end."""
    track = plan.tracks[code]
    if steeple:
        legs = [STEEPLE, CREST_LINE_IN, SORPE_RELEASE]
        lengths = [distance_m(STEEPLE_START, STEEPLE), distance_m(STEEPLE, CREST_LINE_IN),
                   distance_m(CREST_LINE_IN, SORPE_RELEASE)]
        start, heading = STEEPLE_START, STEEPLE_IN
    else:
        legs, lengths, start, heading = [SORPE_RELEASE], [1500.0], SORPE_START, SORPE_RUN
    start_at = release_at - sum(lengths) / SORPE_SPEED * 1000
    circuit_to(track, start, heading, radius, start_at, 250, mps=78)
    plan.phase(code, start_at - 1, "reconstruction-target", 400.0)
    at = start_at
    for point, length in zip(legs, lengths):
        at += length / SORPE_SPEED * 1000
        track.add(release_at if point == SORPE_RELEASE else at, point,
                  alt if point != STEEPLE else alt + 40)
    beyond = destination(SORPE, SORPE_RUN, exit_m)
    over = distance_m(SORPE_RELEASE, beyond)
    track.add(release_at + over / SORPE_SPEED * 1000, beyond, alt + 30)
    turn(track, SORPE_RUN, -60, exit_m, SORPE_SPEED, 220.0)
    return SORPE_RELEASE


def sorpe(plan, code, dummies, release, alt, radius=1300, exit_m=900, steeple=False):
    """Dummy runs at `dummies` (clock times or operation ms), then the release."""
    for at in dummies:
        sorpe_run(plan, code, at if isinstance(at, int) else T(at), alt, radius, exit_m,
                  steeple)
    rel = sorpe_run(plan, code, T(release), alt, radius, exit_m, steeple)
    plan.drop(code, "SORPE", rel, SORPE_WATER, T(release), 0, spun=False)


def ennepe_run(plan, release_at):
    """Townsend's circuit over the misty hills, then a run on the Ennepe released at
    `release_at`; returns the release point."""
    track = plan.tracks["AJ-O"]
    start_at = release_at - 3000 / (220 * MPH) * 1000
    circuit_to(track, ENNEPE_START, ENNEPE_RUN, 2000, start_at, 250)
    plan.phase("AJ-O", start_at - 1, "reconstruction-target", 400.0)
    return attack_run(track, ENNEPE, ENNEPE_RUN, release_at, SHORE_M["ENNEPE"], lead_in_m=3000)


def ennepe(plan):
    """Townsend searches the misty hills after the 02:26 order and drops on his third run
    (ORB: "Mine dropped accurately on third attempt")."""
    for at in ("03:27", "03:32"):
        ennepe_run(plan, T(at))
    rel = ennepe_run(plan, T("03:37"))
    plan.drop("AJ-O", "ENNEPE", rel, ENNEPE, T("03:37"), 2, end_m=30.0)
