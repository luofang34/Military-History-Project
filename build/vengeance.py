#!/usr/bin/env python3
"""Builds the Operation Vengeance reconstruction (18 April 1943).

Run from anywhere; writes missions/operation-vengeance/{operation.json,events.jsonl}.
Fixed sites and anchor times are sourced; flight paths between anchors are
reconstructions whose `bound_m` states the horizontal uncertainty.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import engagement  # noqa: E402
import presentation  # noqa: E402
import routes  # noqa: E402
from track import Emitter  # noqa: E402
from sites import (OP, L, DURATION, ENGAGED, BETTYS, ZEROS, P38S, YAMAMOTO, UGAKI,  # noqa: E402
                   CRASH_T1_323, DITCH_T1_326, entities, unix_ms)


# (from, until, interval for followed/engaged aircraft, interval for the rest) in ms.
# Intervals keep on-screen motion to a few pixels per update at each shot's zoom and speed.
SAMPLING = [
    ("07:24:30", "07:28:30", 500, 500),
    ("07:28:30", "07:31:00", 2000, 2000),
    ("07:31:00", "07:35:30", 1000, 1000),
    ("07:35:30", "07:38:00", 1000, 2000),
    ("07:38:00", "08:04:30", 2000, 10_000),
    ("08:04:30", "08:08:30", 500, 10_000),
    ("08:08:30", "09:28:00", 2000, 10_000),
    ("09:28:00", "09:32:00", 1000, 1000),
    ("09:32:00", "09:34:00", 500, 1000),
    ("09:34:00", "09:35:40", 500, 2000),
    ("09:35:40", "09:38:10", 200, 2000),
    ("09:38:10", "09:39:40", 300, 2000),
    ("09:39:40", "09:42:30", 500, 2000),
    # Egress shot follows Mitchell at zoom 9.5; every P-38 in frame moves ~1 px per update.
    ("09:42:30", "09:56:00", 1000, 10_000),
    ("09:56:00", "10:05:00", 2000, 10_000),
]
FOLLOWED = {"MITCHELL", "MOORE", "MCLANAHAN", "T1-323 YAMAMOTO"}
JAPANESE_DEPARTURE = ("08:04:30", "08:08:30")


def step_for(entity, t):
    """Sampling interval: dense only where the camera is close or following.

    The Japanese formation shares one interval during transit so its members update
    together while the camera follows T1-323; differing rates read as escorts creeping
    back and snapping forward.
    """
    if (entity in BETTYS or entity in ZEROS) and L("08:08:30") <= t < L("09:32:00"):
        return 3000
    for start, until, close, other in SAMPLING:
        if L(start) <= t < L(until):
            dense = entity in FOLLOWED or (entity in ENGAGED and "09:32" <= start < "09:42:30")
            if start >= "09:42:30":
                dense = entity in P38S
            if (start, until) == JAPANESE_DEPARTURE:
                dense = entity in BETTYS or entity in ZEROS
            if entity in ("HOLMES", "HINE") and "09:34:40" <= start < "09:37:40":
                dense = False
            return close if dense else other
    return 10_000


def evidence_for(entity, t):
    """(source id, horizontal bound in metres) for a reconstructed fix."""
    japanese = entity in BETTYS or entity in ZEROS
    if t >= L("09:42:30"):
        return "reconstruction-egress", 30_000.0
    if t >= L("09:34:00"):
        return "reconstruction-engagement", 1500.0
    if japanese:
        if t < L("08:08:30"):
            return "reconstruction-lakunai-departure", 800.0
        return "reconstruction-japanese-route", 5000.0 if t >= L("09:22:00") else 30_000.0
    if t < L("07:31:00") or entity in ("MOORE", "MCLANAHAN"):
        return "reconstruction-fighter-two-departure", 500.0
    return "reconstruction-p38-route", 5000.0 if t >= L("09:28:00") else 20_000.0


def emit_track(em, entity, track, final_valid, until=None):
    """Samples on a shared time grid so aircraft in one formation update in the same frame.
    With `until`, the last fix stays valid to that time instead of sampling the end point."""
    t = track.start
    stop = min(track.end if until is None else until, DURATION)
    while True:
        step = step_for(entity, t)
        nxt = min((t // step + 1) * step, stop) if t < stop else None
        if until is not None and nxt == stop:
            nxt = None
        point, alt = track.at(t)
        if nxt is not None:
            # Hold one fix across stationary spans (parked or stopped aircraft).
            following = [w for w in track.waypoints if w.at_ms > t]
            if following and following[0].point == point and following[0].alt_m == alt:
                nxt = min(following[0].at_ms, stop)
        source, bound = evidence_for(entity, t)
        last = until if until is not None else final_valid
        em.fix(source, entity, t, point, alt, bound, nxt if nxt is not None else last,
               "reconstructed", [])
        if nxt is None:
            return
        t = nxt


REPORT_13FC = "13th-fighter-command-report"


def endings(em, tracks):
    """Known wreck sites persist; missing aircraft and untracked escorts become gaps."""
    em.fix("pacific-wrecks-2656", YAMAMOTO, L("09:38:00"), CRASH_T1_323, 0, 100.0, None,
           "reported", [], reference="wreck")
    em.fix("pacific-wrecks-t1-326", UGAKI, L("09:39:20"), DITCH_T1_326, 0, 500.0, None,
           "reported", [], reference="ditching")
    # Damage as reported: Barber's astern hits, Holmes's attack off Moila Point, debris
    # from T1-326 holing Barber, and Hine trailing smoke (Pacific Wrecks, MACR 609).
    for source, entity, at, condition in [
        ("pacific-wrecks-2656", YAMAMOTO, "09:37:00", "damaged"),
        ("pacific-wrecks-2656", YAMAMOTO, "09:38:00", "destroyed"),
        ("pacific-wrecks-t1-326", UGAKI, "09:38:20", "damaged"),
        ("pacific-wrecks-t1-326", UGAKI, "09:39:20", "destroyed"),
        ("pacific-wrecks", "BARBER", "09:38:55", "damaged"),
        (REPORT_13FC, "LANPHIER", "09:38:40", "damaged"),
        ("macr-599-609", "HINE", "09:40:00", "damaged"),
    ]:
        em.condition(source, entity, L(at), condition, "reported", [])
    hine_end = tracks["HINE"].end
    em.gap("macr-599-609", "HINE", hine_end + 1, None, "reported", [])
    for zero in ZEROS:
        if zero != "OKAZAKI":  # landed at Ballale; his final fix persists
            em.gap("reconstruction-engagement", zero, tracks[zero].end + 1, None,
                   "reconstructed", [])
    em.note("yanagiya-interview", "TSUJINOUE", L("09:42:00"), L("09:52:00"),
            "Escort tracks end here. All six Zeros survived: Okazaki landed at Ballale with "
            "engine trouble, the rest at Buin; Yanagiya, last down, about 10:20.",
            "reported", [])
    return hine_end


def main():
    out = Path(__file__).resolve().parent.parent / "missions" / OP
    out.mkdir(parents=True, exist_ok=True)
    tracks, lead, p38_speed = routes.p38_tracks()
    japanese, betty_kmh = routes.japanese_tracks()
    tracks.update(japanese)
    engagement.engagement(tracks, lead)
    em = Emitter(OP)
    open_ended = {"MCLANAHAN", "MOORE", "OKAZAKI"}
    for entity, track in tracks.items():
        final = None if entity in open_ended else track.end + 1
        if track.end >= DURATION:
            final = DURATION + 1
        # The sourced wreck fix takes over exactly when the reconstructed flight ends.
        until = track.end if entity in (YAMAMOTO, UGAKI) else None
        emit_track(em, entity, track, final, until)
    hine_end = endings(em, tracks)
    assert hine_end > L("09:41:10"), "the HINE camera cue must end while he is still tracked"
    presentation.annotations(em)
    em.write(out / "events.jsonl")
    op = {
        "format": "sokoly-operation",
        "version": 3,
        "id": OP,
        "name": "Operation Vengeance",
        "duration_ms": DURATION,
        "time_origin": (
            "18 April 1943 07:24:30 Henderson Field time (UTC+11), the clock of the 13th "
            "Fighter Command interception report; Japanese records use Tokyo time (UTC+9)"),
        "time": {
            "range": {"start": 0, "end": DURATION},
            "anchor": {
                "at": 0,
                "unix_ms": unix_ms(),
                "source": ("13th Fighter Command 'Fighter Interception' report, 18 Apr 1943: "
                           "take-off 0725, interception 0935 Henderson Field time"),
                "source_scale": "utc",
                "uncertainty_ms": 60_000,
                "resolution_ms": 60_000,
                "original_calendar": "1943-04-18 Henderson Field time (UTC+11)",
            },
            "zone": {
                "kind": "fixed",
                "seconds": 11 * 3600,
                "source": ("US forces in the Solomons kept Henderson Field time (UTC+11); "
                           "tzdb Pacific/Bougainville gives the Japanese occupation clock"),
            },
        },
        "captured_availability": False,
        "entities": entities(),
        "media_archive": None,
        **presentation.operation_presentation(),
    }
    (out / "operation.json").write_text(json.dumps(op, indent=2, ensure_ascii=False) + "\n")
    viewing = sum((c["end_ms"] - c["start_ms"]) / c["speed"] for c in op["playback_track"]) / 1000
    print(f"{len(em.events)} events; P-38 route {p38_speed * 3.6:.0f} km/h, "
          f"Betty route {betty_kmh:.0f} km/h; viewing {viewing:.0f} s")


if __name__ == "__main__":
    main()
