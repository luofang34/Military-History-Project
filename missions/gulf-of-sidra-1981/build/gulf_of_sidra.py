#!/usr/bin/env python3
"""Builds the Gulf of Sidra reconstruction (19 August 1981).

Run from anywhere; writes this mission's operation.json and events.jsonl beside build/, and
the story in presentations/default.json. The build fails if the closure stops matching the
Biddle tape's range calls, or if any camera shot would lose one of its subjects.
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[2] / "tools"))
import camera  # noqa: E402
import coast  # noqa: E402
import geometry as g  # noqa: E402
import story  # noqa: E402
from track import Emitter  # noqa: E402

OP = "gulf-of-sidra-1981"
ANCHOR_MS = int(datetime(1981, 8, 19, 5, 0, tzinfo=timezone.utc).timestamp() * 1000)
DURATION = story.DURATION
TRIPOLI = {"kind": "fixed", "seconds": 2 * 3600,
           "source": "tzdb Africa/Tripoli: UTC+2 (EET) with no DST in August 1981"}
RECONSTRUCTED = {"motion": "great_circle", "max_gap_ms": DURATION}
SOURCES = [
    {"id": "reconstruction-transit", "name": "Su-22 launch and climb reconstruction",
     **RECONSTRUCTED},
    {"id": "reconstruction-cap", "name": "F-14 CAP and vector reconstruction", **RECONSTRUCTED},
    {"id": "reconstruction-engagement", "name": "Engagement choreography (tape ranges)",
     **RECONSTRUCTED},
    {"id": "reconstruction-carrier", "name": "Nimitz from the 123 nm DME call"},
    {"id": "reconstruction-s3a", "name": "S-3A orbit and Buster North reconstruction",
     **RECONSTRUCTED},
    {"id": "biddle-tape", "name": "USS Biddle CIC audio (relative times)", "zone": TRIPOLI},
    {"id": "upi-1981", "name": "UPI wire reports, 19-20 Aug 1981"},
    {"id": "stanik-1996", "name": "Stanik, Naval Aviation News, 1996", "zone": TRIPOLI},
    {"id": "baugher-thirdseries21", "name": "Joe Baugher, third-series serials"},
    {"id": "dvids-2022", "name": "DVIDS: Fast Eagles made history over the Gulf of Sidra"},
    {"id": "cooper-acig", "name": "Tom Cooper, Libyan Air Wars and ACIG", "zone": TRIPOLI},
    {"id": "ratner-yale-1984", "name": "Ratner, Yale Journal of International Law, 1984"},
    {"id": "francioni-syracuse", "name": "Francioni, Syracuse Journal of International Law"},
    {"id": "natural-earth-10m", "name": "Natural Earth 10 m coastline"},
    {"id": "wapo-1981", "name": "Washington Post, 20 Aug 1981 (Pentagon briefing)"},
    {"id": "nimitz-cruise-book", "name": "USS Nimitz 1980-82 cruise book"},
    {"id": "sanders-2012", "name": "Sanders, 'Bait and Switch in Libya', Air & Space, 2012"},
    {"id": "sasser-biddle", "name": "Lt Mike Sasser, USS Biddle account"},
]


def entity(id_, sidc, name, kind, parent=None, quantity=None):
    e = {"id": id_, "sidc": sidc, "camera": False, "name": name, "kind": kind}
    if quantity:
        e["quantity"] = quantity
    if parent:
        e["parent"] = parent
    return e


# Formations carry no fixes; the viewer draws their members as one symbol when they overlap.
ENTITIES = [
    entity("FAST EAGLE", "SFAPMFF--------", "Fast Eagle section, VF-41", "formation",
           quantity=2),
    entity("FITTER PAIR", "SHAPMFF--------", "Su-22 pair, 1022 Sqn", "formation", quantity=2),
    entity(g.FE102, "SFAPMFF--------", "FE102 Kleemann / Venlet", "F-14A", "FAST EAGLE"),
    entity(g.FE107, "SFAPMFF--------", "FE107 Muczynski / Anderson", "F-14A", "FAST EAGLE"),
    entity(g.SU_LEAD, "SHAPMFF--------", "Su-22 lead", "Su-22M3", "FITTER PAIR"),
    entity(g.SU_WING, "SHAPMFF--------", "Su-22 wingman", "Su-22M3", "FITTER PAIR"),
    entity(g.AA2, "SHAPWMAA-------", "AA-2 Atoll", "AA-2"),
    entity(g.AIM_102, "SFAPWMAA-------", "AIM-9L (102)", "AIM-9L"),
    entity(g.AIM_107, "SFAPWMAA-------", "AIM-9L (107)", "AIM-9L"),
    entity(g.NIMITZ, "SFSPCLCV-------", "USS Nimitz", "CVN-68"),
    entity(g.S3A, "SFAPMFS--------", "Diamond Cutter 702", "S-3A"),
    entity(g.LOD_W, "SUGPUCI--------", "Line of Death, west", "32°30'N at the coast"),
    entity(g.LOD_E, "SUGPUCI--------", "Line of Death, east", "32°30'N at the coast"),
]


def evidence(entity_id, at):
    """(source, horizontal bound in metres) for a reconstructed fix."""
    if entity_id in g.MISSILES:
        return "reconstruction-engagement", 300.0
    if entity_id == g.S3A:
        return "reconstruction-s3a", 30_000.0
    if at >= g.T15:
        return "reconstruction-engagement", 1500.0
    if entity_id in (g.FE102, g.FE107):
        return "reconstruction-cap", 10_000.0
    return "reconstruction-transit", 20_000.0


def emit_track(em, entity_id, track, step_ms, final_valid):
    """Fixes on a regular grid plus every waypoint, so launches and hits land exactly."""
    end = track.end
    times = set(range(track.start, end + 1, step_ms)) | {end}
    times |= {w.at_ms for w in track.waypoints}
    if track.start < g.T15 <= end:
        times |= {g.T15 - 1, g.T15}
    times = sorted(times)
    for i, at in enumerate(times):
        valid = times[i + 1] if i + 1 < len(times) else final_valid
        source, bound = evidence(entity_id, at)
        point, alt = track.at(at)
        reference = "wreck" if valid is None else "aircraft"
        em.fix(source, entity_id, at, point, alt, bound, valid, "reconstructed", [],
               reference=reference)


def emit(em, tracks, shots_of_missiles):
    for flier in (g.FE102, g.FE107, g.S3A):
        emit_track(em, flier, tracks[flier], 15_000, DURATION + 1)
    for su in (g.SU_LEAD, g.SU_WING):
        emit_track(em, su, tracks[su], 15_000, None)  # the last fix is where it hits the sea
    for missile, track in shots_of_missiles.items():
        emit_track(em, missile, track, 250, track.end + 1)
        em.gap("reconstruction-engagement", missile, track.end + 1, None, "reconstructed", [])
    for hit, su in [(g.HIT_WING_S, g.SU_WING), (g.HIT_LEAD_S, g.SU_LEAD)]:
        em.condition("biddle-tape", su, g.s_ms(hit), "destroyed", "reported", [])
    for entity_id, point, bound, source, provenance, reference in g.statics(tracks):
        # 1 ms, not 0: verify.py samples on a 250 ms grid and cannot order open-ended fixes
        # that start exactly on it.
        em.fix(source, entity_id, 1, point, 0.0, bound, None, provenance, [],
               reference=reference)


def check_shore(tracks):
    """The S-3A stays outside Libya's 12 nm territorial sea (Wikipedia: its racetrack was
    inside the claimed line but outside 12 nm), and the merge stays about 60 statute miles,
    52 nm, from land (Pentagon briefing). Fails the build otherwise."""
    s3a = tracks[g.S3A]
    nearest = min(coast.nm_to_shore(s3a.at(at)[0]) for at in range(0, DURATION + 1, 5000))
    if nearest < 12.5:
        raise ValueError(f"S-3A comes within {nearest:.1f} nm of the shore")
    merge = coast.nm_to_shore(g.MERGE)
    if not 50.0 <= merge <= 60.0:
        raise ValueError(f"merge is {merge:.1f} nm from the shore; the briefing says about 52")
    return nearest, merge


def main():
    out = HERE.parent
    tracks = g.aircraft()
    g.check_ranges(tracks)
    tracks[g.S3A] = g.s3a()
    s3a_shore, merge_shore = check_shore(tracks)
    missiles = g.missiles(tracks)
    fixed = {e: p for e, p, *_ in g.statics(tracks)}
    shot_list = camera.shots({**tracks, **missiles}, fixed, story.t, DURATION)
    em = Emitter(OP)
    emit(em, tracks, missiles)
    story.annotations(em)
    em.write(out / "events.jsonl")
    op = {
        "format": "sokoly-operation",
        "version": 4,
        "id": OP,
        "name": "Gulf of Sidra incident, 19 August 1981",
        "duration_ms": DURATION,
        "time_origin": ("19 August 1981 07:00 Tripoli time (UTC+2), the Libyan clock of the "
                        "launch report; US wire times are Pentagon times converted from Zulu"),
        "time": {
            "range": {"start": 0, "end": DURATION},
            "anchor": {
                "at": 0,
                "unix_ms": ANCHOR_MS,
                "source": ("Libyan account: Su-22s sent at 7 AM; Biddle tape: contact at "
                           "about 07:15; Pentagon: shootdowns 0520Z"),
                "source_scale": "utc",
                "uncertainty_ms": 900_000,
                "resolution_ms": 60_000,
                "original_calendar": "1981-08-19 Tripoli time (UTC+2)",
            },
            "zone": TRIPOLI,
        },
        "captured_availability": False,
        "sources": SOURCES,
        "entities": ENTITIES,
        "media_archive": None,
    }
    (out / "operation.json").write_text(json.dumps(op, indent=2, ensure_ascii=False) + "\n")
    doc = story.document(OP, shot_list)
    (out / "presentations").mkdir(exist_ok=True)
    (out / "presentations" / "default.json").write_text(
        json.dumps(doc, indent=2, ensure_ascii=False) + "\n")
    viewing = sum((c["end_ms"] - c["start_ms"]) / c["speed"] for c in doc["playback_track"])
    ranges = ", ".join(f"{g.separation_nm(tracks, g.FE102, g.SU_LEAD, g.s_ms(s)):.1f}"
                       for s, _ in g.RANGE_CALLS)
    print(f"{len(em.events)} events, {len(shot_list)} shots; viewing {viewing / 1000:.0f} s; "
          f"tape ranges {ranges} nm; S-3A >= {s3a_shore:.1f} nm and merge {merge_shore:.1f} nm "
          f"from shore")


if __name__ == "__main__":
    main()
