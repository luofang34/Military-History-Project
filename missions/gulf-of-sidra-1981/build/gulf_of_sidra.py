#!/usr/bin/env python3
"""Builds the Gulf of Sidra reconstruction (19 August 1981).

Run from anywhere; writes this mission's operation.json and events.jsonl beside build/,
and the story in presentations/default.json. Times are the Libyan clock (UTC+2): the Biddle
tape's relative times are anchored at 15:00 (07:15). Positions are reconstructed inside the
range calls and bearings the tape gives; no source publishes coordinates for the fight.
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[2] / "tools"))
import story  # noqa: E402
from track import Emitter, Track  # noqa: E402

OP = "gulf-of-sidra-1981"
ANCHOR_MS = int(datetime(1981, 8, 19, 5, 0, tzinfo=timezone.utc).timestamp() * 1000)
DURATION = story.DURATION
TRIPOLI = {"kind": "fixed", "seconds": 2 * 3600,
           "source": "tzdb Africa/Tripoli: UTC+2 (EET) with no DST in August 1981"}
RECONSTRUCTED = {"motion": "great_circle", "max_gap_ms": DURATION}
SOURCES = [
    {"id": "reconstruction-transit", "name": "Su-22 launch and climb reconstruction",
     **RECONSTRUCTED},
    {"id": "reconstruction-cap", "name": "F-14 CAP racetrack and vector reconstruction",
     **RECONSTRUCTED},
    {"id": "reconstruction-engagement", "name": "Engagement choreography (tape ranges)",
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
]

GHURDABIYA = (16.61167, 31.06056)  # Wikipedia / ICAO HLGD
LOD_WEST = (14.60, 32.50)  # 32°30′N where the line meets the coast (computed, Natural Earth)
LOD_EAST = (20.48, 32.50)

SU_LEAD, SU_WING = "SU22-LEAD", "SU22-WING"
FE102, FE107 = "FE102", "FE107"
AA2, AIM_102, AIM_107 = "AA2-ATOLL", "AIM9-102", "AIM9-107"
LOD_W, LOD_E = "LOD-WEST", "LOD-EAST"
ALT_SU, ALT_F102, ALT_F107 = 6100.0, 6100.0, 6700.0
ENTITIES = [
    {"id": FE102, "sidc": "SFAPMFF--------", "camera": False,
     "name": "FE102 Kleemann / Venlet", "kind": "F-14A VF-41, BuNo 160403 (secondary sources)"},
    {"id": FE107, "sidc": "SFAPMFF--------", "camera": False,
     "name": "FE107 Muczynski / Anderson", "kind": "F-14A VF-41, BuNo 160390 (secondary sources)"},
    {"id": SU_LEAD, "sidc": "SHAPMFF--------", "camera": False,
     "name": "Su-22 lead", "kind": "Su-22M3, 1022 Sqn (Zintani per Cooper; unconfirmed)"},
    {"id": SU_WING, "sidc": "SHAPMFF--------", "camera": False,
     "name": "Su-22 wingman", "kind": "Su-22M3, 1022 Sqn (Jafari per Cooper; unconfirmed)"},
    {"id": AA2, "sidc": "SHAPWMAA-------", "camera": False,
     "name": "AA-2 Atoll", "kind": "Fired by Su-22 lead, missed (US account)"},
    {"id": AIM_102, "sidc": "SFAPWMAA-------", "camera": False,
     "name": "AIM-9L", "kind": "Fired by FE102 at the Su-22 wingman"},
    {"id": AIM_107, "sidc": "SFAPWMAA-------", "camera": False,
     "name": "AIM-9L", "kind": "Fired by FE107 at the Su-22 lead"},
    {"id": LOD_W, "sidc": "SUGPUCI--------", "camera": False,
     "name": "Line of Death, west", "kind": "32°30′N meets the coast, 14.60°E"},
    {"id": LOD_E, "sidc": "SUGPUCI--------", "camera": False,
     "name": "Line of Death, east", "kind": "32°30′N meets the coast, 20.48°E"},
]


def t(clock):
    """Operation milliseconds from 07:00 Tripoli time; `MM:SS` is minutes and seconds."""
    m, s = clock.split(":")
    return (int(m) * 60 + int(s)) * 1000


def tracks():
    """Geometry from the tape: 20 mi at 15:15, 8 mi at 15:54, 6 mi at 16:03, merge ~16:20."""
    su_lead = (Track().add(0, GHURDABIYA, 0).add(t("10:00"), (16.95, 31.62), 3000)
               .add(t("15:00"), (17.10, 32.00), ALT_SU)
               .add(t("16:00"), (17.15, 32.13), ALT_SU)
               .add(t("16:31"), (17.20, 32.22), ALT_SU)
               .add(t("16:45"), (17.14, 32.27), ALT_SU)
               .add(t("17:53"), (17.00, 32.40), 5800.0)
               .add(t("17:58"), (16.99, 32.41), 0.0))
    su_wing = (Track().add(0, (16.62, 31.07), 0).add(t("10:00"), (16.97, 31.66), 3000)
               .add(t("15:00"), (17.12, 32.02), ALT_SU)
               .add(t("16:00"), (17.18, 32.11), ALT_SU)
               .add(t("16:45"), (17.26, 32.14), ALT_SU)
               .add(t("17:21"), (17.36, 32.04), 5800.0)
               .add(t("17:26"), (17.365, 32.035), 0.0))
    f102 = (Track().add(0, (18.10, 33.40), ALT_F102).add(t("06:00"), (17.90, 33.10), ALT_F102)
            .add(t("09:00"), (17.75, 32.95), ALT_F102).add(t("12:00"), (17.55, 32.70), ALT_F102)
            .add(t("15:00"), (17.30, 32.45), ALT_F102).add(t("16:31"), (17.24, 32.30), ALT_F102)
            .add(t("17:00"), (17.30, 32.20), ALT_F102).add(t("17:21"), (17.345, 32.06), ALT_F102)
            .add(t("18:30"), (17.60, 32.50), ALT_F102).add(t("19:10"), (17.85, 32.65), ALT_F102)
            .add(t("25:00"), (17.90, 32.90), ALT_F102))
    f107 = (Track().add(0, (18.20, 33.50), ALT_F107).add(t("06:00"), (18.00, 33.20), ALT_F107)
            .add(t("09:00"), (17.90, 33.05), ALT_F107).add(t("12:00"), (17.65, 32.80), ALT_F107)
            .add(t("15:00"), (17.36, 32.48), ALT_F107).add(t("16:31"), (17.30, 32.40), ALT_F107)
            .add(t("17:20"), (17.10, 32.36), ALT_F107).add(t("17:53"), (17.03, 32.37), ALT_F107)
            .add(t("18:30"), (17.50, 32.70), ALT_F107).add(t("19:10"), (17.75, 32.75), ALT_F107)
            .add(t("25:00"), (17.95, 33.00), ALT_F107))
    return {SU_LEAD: su_lead, SU_WING: su_wing, FE102: f102, FE107: f107}


def missile_tracks(all_tracks):
    """Each missile starts where its shooter is at launch and ends where its target is at
    impact, at the same altitude, so the hit reads on screen. The AA-2 misses on purpose."""
    lead, wing = all_tracks[SU_LEAD], all_tracks[SU_WING]
    f102, f107 = all_tracks[FE102], all_tracks[FE107]
    launch_102, launch_107 = t("17:11"), t("17:43")
    hit_102, hit_107 = t("17:21"), t("17:53")
    track = Track()
    p, a = lead.at(t("16:31"))
    track.add(t("16:31"), p, a)
    track.add(t("16:38"), (17.30, 32.38), ALT_F102)
    aim102 = Track()
    p, a = f102.at(launch_102)
    aim102.add(launch_102, p, a)
    p, a = wing.at(hit_102)
    aim102.add(hit_102, p, a)
    aim107 = Track()
    p, a = f107.at(launch_107)
    aim107.add(launch_107, p, a)
    p, a = lead.at(hit_107)
    aim107.add(hit_107, p, a)
    return {AA2: track, AIM_102: aim102, AIM_107: aim107}

def evidence(entity, at):
    """(source, horizontal bound in metres) for a reconstructed fix."""
    if entity in (AA2, AIM_102, AIM_107):
        return "reconstruction-engagement", 300.0
    if at >= t("15:00"):
        return "reconstruction-engagement", 1500.0
    if entity in (FE102, FE107):
        return "reconstruction-cap", 10_000.0
    return "reconstruction-transit", 20_000.0


def emit_track(em, entity, track, step_ms, end_ms, final_valid):
    """Fixes on a regular grid plus every waypoint, so each aircraft is exactly where its
    waypoints put it at the moments that matter (launch, impact, the split at 15:00)."""
    split = t("15:00")
    times = set(range(0, end_ms + 1, step_ms)) | {end_ms, split - 1, split}
    times |= {w.at_ms for w in track.waypoints if w.at_ms <= end_ms}
    times = sorted(x for x in times if 0 <= x <= end_ms)
    for i, at in enumerate(times):
        valid = times[i + 1] if i + 1 < len(times) else final_valid
        source, bound = evidence(entity, at)
        point, alt = track.at(at)
        em.fix(source, entity, at, point, alt, bound, valid, "reconstructed", [])

def wreck(em, entity, track, at, point):
    """A splash or crash site that persists after the aircraft is gone; not sourced to a point."""
    em.fix("reconstruction-engagement", entity, at, point, 0.0, 800.0, None,
           "reconstructed", [], reference="wreck")


def emit_aircraft(em, all_tracks):
    emit_track(em, FE102, all_tracks[FE102], 15_000, DURATION, DURATION + 1)
    emit_track(em, FE107, all_tracks[FE107], 15_000, DURATION, DURATION + 1)
    emit_track(em, SU_LEAD, all_tracks[SU_LEAD], 15_000, t("17:57"), t("17:58") + 1)
    emit_track(em, SU_WING, all_tracks[SU_WING], 15_000, t("17:25"), t("17:26"))
    wreck(em, SU_WING, all_tracks[SU_WING], t("17:26") + 1, (17.365, 32.035))
    wreck(em, SU_LEAD, all_tracks[SU_LEAD], t("17:58") + 1, (16.99, 32.41))


def emit_missiles(em, missiles):
    """Missiles are fixed every 250 ms; they end with a gap so the viewer drops them."""
    for entity, track in missiles.items():
        end = track.end
        times = sorted(set(range(track.start, end + 1, 250)) | {end})
        for i, at in enumerate(times):
            valid = times[i + 1] if i + 1 < len(times) else end + 1
            point, alt = track.at(at)
            em.fix("reconstruction-engagement", entity, at, point, alt, 300.0, valid,
                   "reconstructed", [])
        em.gap("reconstruction-engagement", entity, end + 1, None, "reconstructed", [])

def emit_conditions(em):
    """The Biddle tape reports the kills; each aircraft is damaged on the hit, then destroyed."""
    for entity, hit, down in [(SU_WING, "17:21", "17:26"), (SU_LEAD, "17:53", "17:58")]:
        em.condition("biddle-tape", entity, t(hit), "damaged", "reported", [])
        em.condition("biddle-tape", entity, t(down), "destroyed", "reported", [])


def emit_lod_endpoints(em):
    """Static reported markers for where the 32°30′N line meets the coast, for the map."""
    for entity, point in [(LOD_W, LOD_WEST), (LOD_E, LOD_EAST)]:
        em.fix("natural-earth-10m", entity, 1, point, 0.0, 500.0, None, "reported", [],
               reference="coast")


def main():
    out = HERE.parent
    out.mkdir(parents=True, exist_ok=True)
    all_tracks = tracks()
    em = Emitter(OP)
    emit_aircraft(em, all_tracks)
    emit_missiles(em, missile_tracks(all_tracks))
    emit_conditions(em)
    emit_lod_endpoints(em)
    story.annotations(em, t)
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
    doc = story.document(OP, t, all_tracks)
    (out / "presentations").mkdir(exist_ok=True)
    (out / "presentations" / "default.json").write_text(
        json.dumps(doc, indent=2, ensure_ascii=False) + "\n")
    viewing = sum((c["end_ms"] - c["start_ms"]) / c["speed"] for c in doc["playback_track"])
    print(f"{len(em.events)} events; viewing {viewing / 1000:.0f} s")


if __name__ == "__main__":
    main()
