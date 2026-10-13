#!/usr/bin/env python3
"""Builds the Battle of Taierzhuang, 14 March – 1 April 1938: the defence and fall of Tengxian, the
road south to the Grand Canal, and the battle for the town and its guns.

Run from anywhere; writes this mission's operation.json and events.jsonl beside build/, and the
story in presentations/default.json. Times and places are sourced; the moves between them are
reconstructions whose `bound_m` states the horizontal uncertainty. Each part of the story is a
package (tengxian/, siege/) whose checks fail the build if a unit outpaces the marches of 1938, a
battery leaves the place its range fan is drawn from, a round flies further than its gun could
throw it, or an estimate in build/evidence/ falls outside its records without saying why.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[2] / "tools"))
import facts  # noqa: E402
import ledger  # noqa: E402
import shots  # noqa: E402
import story  # noqa: E402
from clock import DURATION, OP, L, unix_ms  # noqa: E402
from evidence import DISPUTES, MOMENTS  # noqa: E402
from siege import checks as siege_checks, fire, graphics as siege_graphics  # noqa: E402
from siege import moves as siege_moves, sites as siege_sites  # noqa: E402
from sources import CLOCK, SOURCES  # noqa: E402
from tengxian import checks as tengxian_checks, graphics as tengxian_graphics  # noqa: E402
from tengxian import moves as tengxian_moves, sites as tengxian_sites  # noqa: E402
from track import Emitter, Track, distance_m  # noqa: E402

JAPANESE_IDS = {id_ for id_, *_ in tengxian_sites.JAPANESE + siege_sites.JAPANESE}
SIEGE_IDS = {id_ for id_, *_ in siege_sites.CHINESE + siege_sites.JAPANESE}
TENGXIAN_MARCH = {"63 REGT", "ARMOUR", "731 REGT", "125 DIV", "379 BDE", "381 BDE"}


def evidence_for(entity, at):
    """(source id, horizontal bound in metres) for a reconstructed fix: at Tengxian within 2 km on
    the march and 100 m once the fighting is at the walls; at Taierzhuang within 500 m, the
    Chinese 15 cm battery, whose position no record gives, within 3 km."""
    source = "reconstruction-japanese" if entity in JAPANESE_IDS else "reconstruction-chinese"
    if entity in SIEGE_IDS:
        return source, 3000.0 if entity == "SFH" else 500.0
    at_walls = L("16 11:00") <= at and entity not in TENGXIAN_MARCH
    return source, 100.0 if at_walls else 2000.0


def emit_track(em, entity, track, until):
    source, _ = evidence_for(entity, track.waypoints[0].at_ms)
    times = [w.at_ms for w in track.waypoints]
    for i, at in enumerate(times):
        nxt = times[i + 1] if i + 1 < len(times) else until
        point, _ = track.at(at)
        em.fix(source, entity, at, point, 0.0, evidence_for(entity, at)[1], nxt,
               "reconstructed", [], reference="ground")
    if until is not None:
        em.gap(source, entity, until, None, "reconstructed", [])


def entities():
    rows = []
    for sites in (tengxian_sites, siege_sites):
        for id_, name, sidc, kind, parent in sites.CHINESE + sites.JAPANESE:
            row = {"id": id_, "sidc": sidc, "camera": False, "name": name, "kind": kind}
            if parent:
                row["parent"] = parent
            rows.append(row)
        rows += [{"id": id_, "sidc": sidc, "camera": False, "name": name, "kind": "site"}
                 for id_, sidc, name, *_ in sites.FIXED]
    return rows


def plan():
    """Every entity's track, the conditions it takes and when it leaves the map, and each
    part's tracks alone, for its summary."""
    tracks, ends = {}, {}
    t_tracks, t_conditions, t_ends = tengxian_moves.plan()
    tengxian_checks.all(t_tracks, tengxian_sites.END)
    s_tracks, s_conditions, s_ends = siege_moves.plan()
    siege_checks.all(s_tracks, siege_sites.END)
    for entity in t_tracks:
        if entity not in s_tracks:
            ends[entity] = L(t_ends[entity]) + 1 if entity in t_ends else tengxian_sites.END + 1
    ends.update({e: L(at) + 1 for e, at in s_ends.items()})
    tracks.update(t_tracks)
    for entity, track in s_tracks.items():
        tracks[entity] = joined(t_tracks[entity], track) if entity in t_tracks else track
    return tracks, t_conditions + s_conditions, ends, t_tracks, s_tracks


def joined(first, then):
    """One track from a unit's Tengxian track and its later one, which must start where and
    after the first leaves it."""
    last, start = first.waypoints[-1], then.waypoints[0]
    if distance_m(last.point, start.point) > 1 or start.at_ms < last.at_ms:
        raise ValueError(f"a track does not take up at {last.point}, {last.at_ms} ms")
    track = Track()
    for w in first.waypoints + then.waypoints[1:]:
        track.add(w.at_ms, w.point, 0.0)
    return track


def main():
    out = HERE.parent
    tracks, conditions, ends, t_tracks, s_tracks = plan()
    em = Emitter(OP)
    for entity, track in tracks.items():
        emit_track(em, entity, track, ends.get(entity))
    for sites in (tengxian_sites, siege_sites):
        for id_, _, _, point, bound, source in sites.FIXED:
            em.fix(source, id_, 0, point, 0.0, bound, None, "reported", [], reference="site")
    for entity, at, condition in conditions:
        em.condition("reconstruction-estimate", entity, L(at), condition, "reconstructed", [])
    tengxian_graphics.emit(em)
    siege_graphics.emit(em)
    fire.emit(em)
    story.annotations(em)
    undeclared = {e["source"]["id"] for e in em.events} - {s["id"] for s in SOURCES}
    if undeclared:
        raise ValueError(f"events cite undeclared sources: {sorted(undeclared)}")
    em.write(out / "events.jsonl")
    op = {
        "format": "sokoly-operation",
        "version": 4,
        "id": OP,
        "name": story.NAME,
        "duration_ms": DURATION,
        "time_origin": ("14 March 1938 04:00 UTC+8, when the Japanese 10th Infantry set out "
                        "from Tangcun; Japanese and Chinese records are read on this clock"),
        "time": {
            "range": {"start": 0, "end": DURATION},
            "anchor": {
                "at": 0,
                "unix_ms": unix_ms(),
                "source": ("krzzjn, from the 10th and 63rd Infantry's reports: the right column "
                           "left Tangcun at 04:00 on 14 March"),
                "source_scale": "utc",
                "uncertainty_ms": 3_600_000,
                "resolution_ms": 60_000,
                "original_calendar": "1938-03-14 UTC+8",
            },
            "zone": CLOCK,
        },
        "captured_availability": False,
        "sources": SOURCES,
        "entities": entities(),
        "media_archive": None,
    }
    (out / "operation.json").write_text(json.dumps(op, indent=2, ensure_ascii=False) + "\n")
    cues, intents = shots.camera()
    doc = story.document(OP, cues, intents, L)
    (out / "presentations").mkdir(exist_ok=True)
    (out / "presentations" / "default.json").write_text(
        json.dumps(doc, indent=2, ensure_ascii=False) + "\n")
    ledger.write_readme(out / "README.md", DISPUTES, {s["id"]: s["name"] for s in SOURCES},
                        "taierzhuang.py", MOMENTS)
    facts.write_mission(out, OP, {**MOMENTS, **DISPUTES}, L)
    viewing = sum((c["end_ms"] - c["start_ms"]) / c["speed"] for c in doc["playback_track"])
    print(f"{len(em.events)} events, {len(cues)} shots; viewing {viewing / 1000:.0f} s; "
          f"{tengxian_checks.summary(t_tracks)}; {siege_checks.summary(s_tracks)}")


if __name__ == "__main__":
    main()
