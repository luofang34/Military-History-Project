#!/usr/bin/env python3
"""Builds the Operation Chastise reconstruction (16/17 May 1943).

Run from anywhere; writes this mission's operation.json and events.jsonl beside build/, and
the story in presentations/default.json. Times and fixed sites are sourced; flight paths
between them are reconstructions whose `bound_m` states the horizontal uncertainty. The build
fails if a Lancaster leaves the type's speed envelope, a release misses the briefed height
and range, a loss strays from its crash site, or a camera shot loses its subject.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[2] / "tools"))
import checks  # noqa: E402
import ledger  # noqa: E402
import flights  # noqa: E402
import shots  # noqa: E402
import story  # noqa: E402
from sites import CRASH, DURATION, FIXED, OP, entities, unix_ms  # noqa: E402
from track import Emitter  # noqa: E402

RECONSTRUCTED = {"motion": "great_circle", "max_gap_ms": DURATION}
SOURCES = [
    {"id": "reconstruction-route", "name": "Route reconstruction (B.976 turning points)",
     **RECONSTRUCTED},
    {"id": "reconstruction-target", "name": "Target-area choreography", **RECONSTRUCTED},
    {"id": "reconstruction-airfield", "name": "Scampton take-off and landing reconstruction",
     **RECONSTRUCTED},
    {"id": "reconstruction-upkeep", "name": "Upkeep bounce choreography", **RECONSTRUCTED},
    {"id": "reconstruction-flood", "name": "Möhne flood front through the sourced towns",
     **RECONSTRUCTED},
    {"id": "reconstruction-estimate",
     "name": "Replay estimates where sources disagree (build/evidence.py)"},
    {"id": "orb-617", "name": "617 Squadron Operations Record Book, AIR 27/2128"},
    {"id": "nav-log-aj-t", "name": "AJ-T navigator's log (Dambusters Blog transcription)"},
    {"id": "asn", "name": "Aviation Safety Network wikibase"},
    {"id": "wikipedia-gibson", "name": "Guy Gibson (en.wikipedia)"},
    {"id": "order-b976", "name": "5 Group Operation Order B.976 (IBCC 10501, 33688)"},
    {"id": "gibson-eca", "name": "Guy Gibson, Enemy Coast Ahead (1946)"},
    {"id": "dambustersblog", "name": "Charles Foster, Dambusters Blog"},
    {"id": "lwl-moehne", "name": "LWL Westfälische Geschichte: Möhnekatastrophe"},
    {"id": "dewiki-moehne", "name": "Möhnekatastrophe (de.wikipedia)"},
    {"id": "dewiki-eder", "name": "Edertalsperre (de.wikipedia)"},
    {"id": "hinks-2010", "name": "Hinks, Heitefuss & Chrimes, The Dambusters Revisited (2010)"},
    {"id": "wikipedia-chastise", "name": "Operation Chastise (en.wikipedia)"},
    {"id": "rafm-podcast", "name": "RAF Museum, The Dams Raid (transcript)"},
    {"id": "osm", "name": "OpenStreetMap dam and site geometry"},
    {"id": "wikipedia-scampton", "name": "RAF Scampton (en.wikipedia)"},
    {"id": "wikipedia-st-vincents", "name": "St Vincents Hall, Grantham (en.wikipedia)"},
]


def emit_track(em, entity, track, source_for, final_valid, until=None, changes=()):
    """One fix per waypoint; the App joins them along great circles, as they were built, but
    only within one source. At each time in `changes`, where the evidence source changes, the
    earlier source reports the position 1 ms before and the later one at the change, so
    neither source's path is extended by the other's. With `until`, the last fix is 1 ms
    before it."""
    stop = DURATION if until is None else until - 1
    times = {w.at_ms for w in track.waypoints if 0 <= w.at_ms <= stop}
    times |= {t for c in changes if track.start < c <= stop for t in (c - 1, c)}
    if until is not None:
        times.add(stop)
    times = sorted(times)
    for i, at in enumerate(times):
        valid = times[i + 1] if i + 1 < len(times) else final_valid
        source, bound = source_for(entity, at)
        point, alt = track.at(at)
        em.fix(source, entity, at, point, alt, bound, valid, "reconstructed", [])


def main():
    out = HERE.parent
    plan = flights.build()
    checks.all(plan)
    em = Emitter(OP)
    for code, track in plan.tracks.items():
        if code in plan.lost:
            # The flight ends 1 ms before the loss, where the reported crash site takes over.
            loss = plan.lost[code]
            emit_track(em, code, track, plan.source_for, loss, until=loss,
                       changes=plan.changes(code))
            site, bound, _ = CRASH[code]
            em.fix("dambustersblog", code, loss, site, 0.0, bound, None, "reported", [],
                   reference="wreck")
        else:
            emit_track(em, code, track, plan.source_for, None, changes=plan.changes(code))
    for mine, track in plan.mines.items():
        emit_track(em, mine, track, lambda *_: ("reconstruction-upkeep", 30.0), track.end + 1)
        em.gap("reconstruction-upkeep", mine, track.end + 1, None, "reconstructed", [])
    flood = plan.flood
    emit_track(em, "MÖHNE FLOOD", flood, lambda *_: ("reconstruction-flood", 1500.0),
               DURATION + 1)
    for id_, _, _, _, point, bound, source in FIXED:
        em.fix(source, id_, 0, point, 0.0, bound, None, "reported", [], reference="site")
    for source, entity, at, condition in plan.conditions:
        em.condition(source, entity, at, condition, "reported", [])
    story.annotations(em, {s["id"]: s["name"] for s in SOURCES})
    undeclared = {e["source"]["id"] for e in em.events} - {s["id"] for s in SOURCES}
    if undeclared:
        raise ValueError(f"events cite undeclared sources: {sorted(undeclared)}")
    em.write(out / "events.jsonl")
    op = {
        "format": "sokoly-operation",
        "version": 4,
        "id": OP,
        "name": "Operation Chastise",
        "duration_ms": DURATION,
        "time_origin": ("16 May 1943 21:25 British Double Summer Time (UTC+2), the clock of "
                        "617 Squadron's Operations Record Book; German summer time was also "
                        "UTC+2"),
        "time": {
            "range": {"start": 0, "end": DURATION},
            "anchor": {
                "at": 0,
                "unix_ms": unix_ms(),
                "source": ("617 Squadron ORB, 16/17 May 1943: first take-off 2128, last "
                           "landing 0615"),
                "source_scale": "utc",
                "uncertainty_ms": 60_000,
                "resolution_ms": 60_000,
                "original_calendar": "1943-05-16 British Double Summer Time (UTC+2)",
            },
            "zone": {
                "kind": "fixed",
                "seconds": 2 * 3600,
                "source": ("tzdb: Europe/London BDST and Europe/Berlin CEST were both UTC+2 "
                           "on 16/17 May 1943"),
            },
        },
        "captured_availability": False,
        "sources": SOURCES,
        "entities": entities(plan.mine_owners),
        "media_archive": None,
    }
    (out / "operation.json").write_text(json.dumps(op, indent=2, ensure_ascii=False) + "\n")
    ledger.write_readme(out / "README.md", {s["id"]: s["name"] for s in SOURCES})
    shot_list = shots.shots(plan)
    doc = story.document(OP, shot_list)
    (out / "presentations").mkdir(exist_ok=True)
    (out / "presentations" / "default.json").write_text(
        json.dumps(doc, indent=2, ensure_ascii=False) + "\n")
    viewing = sum((c["end_ms"] - c["start_ms"]) / c["speed"] for c in doc["playback_track"])
    print(f"{len(em.events)} events, {len(shot_list)} shots; viewing {viewing / 1000:.0f} s; "
          f"{checks.summary(plan)}")


if __name__ == "__main__":
    main()
