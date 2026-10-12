"""Build checks: the reconstruction must keep to the sources it is built from.

- Every airborne leg of 1 s or more stays within its type's speeds as Wikipedia's
  specifications give them: P-38 169–666 km/h (P-38L stall and top speed), G4M1 at most
  428 km/h, A6M2 110–533 km/h. Legs on the ground are only held to the upper bound.
- T1-323's last fix is its wreck and T1-326's its ditching, each where the sources put it.
- Hine is still tracked until the camera stops following him.
- Each timed estimate in build/evidence/ lies within its records' times, or is flagged as
  lying outside them with its reason.
"""
import ledger
import presentation
from evidence import DISPUTES, MOMENTS
from sites import BETTYS, CRASH_T1_323, DITCH_T1_326, L, P38S, UGAKI, YAMAMOTO, ZEROS
from track import distance_m

ENVELOPE_KMH = {"P-38": (169.0, 666.0), "G4M1": (0.0, 428.0), "A6M2": (110.0, 533.0)}
TYPE = {**{e: "P-38" for e in P38S}, **{e: "G4M1" for e in BETTYS},
        **{e: "A6M2" for e in ZEROS}}


def speeds(tracks):
    """Per type: (slowest airborne leg, fastest leg), each as (km/h, entity, ms)."""
    out = {}
    for entity, track in tracks.items():
        kind = TYPE[entity]
        slow, fast = out.get(kind, ((1e9, None, None), (0.0, None, None)))
        for a, b in zip(track.waypoints, track.waypoints[1:]):
            dt = (b.at_ms - a.at_ms) / 1000
            if dt < 1:
                continue
            kmh = distance_m(a.point, b.point) / dt * 3.6
            if kmh > fast[0]:
                fast = (kmh, entity, a.at_ms)
            if min(a.alt_m, b.alt_m) > 1 and kmh < slow[0]:
                slow = (kmh, entity, a.at_ms)
        out[kind] = (slow, fast)
    return out


def check_speeds(tracks):
    for kind, ((slow, s_who, s_at), (fast, f_who, f_at)) in speeds(tracks).items():
        lo, hi = ENVELOPE_KMH[kind]
        if slow < lo:
            raise ValueError(f"{s_who} flies {slow:.0f} km/h at {s_at} ms, below the {kind}'s "
                             f"{lo:.0f}")
        if fast > hi:
            raise ValueError(f"{f_who} flies {fast:.0f} km/h at {f_at} ms, above the {kind}'s "
                             f"{hi:.0f}")


def check_anchors(tracks):
    for entity, site, what in ((YAMAMOTO, CRASH_T1_323, "wreck"),
                               (UGAKI, DITCH_T1_326, "ditching")):
        end = tracks[entity].waypoints[-1].point
        if distance_m(end, site) > 50:
            raise ValueError(f"{entity} ends {distance_m(end, site):.0f} m from its {what}")


def check_camera_follow(hine_end):
    """Hine is tracked until the last shot that follows him ends."""
    cues = [c for c in presentation.camera()[0] if c.get("focus") == "HINE"]
    last = max(c["end_ms"] for c in cues)
    if hine_end < last:
        raise ValueError(f"Hine's track ends at {hine_end} ms, before his shot ends at {last}")


def all(tracks, hine_end):  # noqa: A001 - the module's one entry point, called as checks.all
    ledger.check(DISPUTES, L)
    ledger.check_moments(MOMENTS, L)
    check_speeds(tracks)
    check_anchors(tracks)
    check_camera_follow(hine_end)


def summary(tracks):
    return ", ".join(f"{kind} {slow[0]:.0f}–{fast[0]:.0f} km/h"
                     for kind, (slow, fast) in speeds(tracks).items())
