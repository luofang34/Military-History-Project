#!/usr/bin/env python3
"""Builds the reconstruction of John Brown's raid on Harpers Ferry (16–18 October 1859).

Run from anywhere; writes this mission's operation.json and events.jsonl beside build/, and
the story in presentations/default.json. Times and places are sourced; the moves between them
are reconstructions whose `bound_m` states the horizontal uncertainty. The build fails if anyone
outpaces the roads or the railroad of 1859, if someone dies away from where the sources put it,
or if an estimate in build/evidence/ falls outside its records without saying why.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[2] / "tools"))
import checks  # noqa: E402
import facts  # noqa: E402
import ledger  # noqa: E402
import moves  # noqa: E402
import shots  # noqa: E402
import story  # noqa: E402
from evidence import DISPUTES, MOMENTS  # noqa: E402
from sites import DURATION, FIXED, LMT_S, OP, WIRES, L, entities, unix_ms  # noqa: E402
from track import Emitter  # noqa: E402

CLOCK = {"kind": "fixed", "seconds": LMT_S,
         "source": "Harpers Ferry local mean time, 77°43′47″ W; towns kept their own time "
                   "in 1859"}
RECONSTRUCTED = {"motion": "great_circle", "max_gap_ms": DURATION, "zone": CLOCK}
SOURCES = [
    {"id": "reconstruction-raiders", "name": "The raiders' moves, reconstructed",
     **RECONSTRUCTED},
    {"id": "reconstruction-opponents", "name": "The militia's and the marines' moves, "
     "reconstructed", **RECONSTRUCTED},
    {"id": "reconstruction-railroad", "name": "Trains on the B&O, reconstructed",
     **RECONSTRUCTED},
    {"id": "reconstruction-estimate",
     "name": "Replay estimates where sources disagree (build/evidence/)", "zone": CLOCK},
    {"id": "anderson-1861", "name": "Osborne P. Anderson, A Voice from Harper's Ferry (1861)"},
    {"id": "mason-report", "name": "Senate Select Committee (Mason) Report on the Harper's "
     "Ferry Invasion (1860), with its testimony"},
    {"id": "lee-report", "name": "R. E. Lee to the Adjutant General, 19 October 1859 (Mason "
     "Report, Appendix 1)"},
    {"id": "greene-1885", "name": "Israel Green, \"The Capture of John Brown\", North American "
     "Review (1885)"},
    {"id": "daingerfield-1885", "name": "John E. P. Daingerfield, \"John Brown at Harper's "
     "Ferry\", Century (1885)"},
    {"id": "villard-1910", "name": "Oswald Garrison Villard, John Brown 1800–1859 (1910)"},
    {"id": "hinton-1894", "name": "Richard J. Hinton, John Brown and His Men (1894), with "
     "Cook's confession"},
    {"id": "dewitt-1859", "name": "The Life, Trial and Execution of Captain John Brown (De Witt, "
     "1859), with Phelps's testimony at the trial"},
    {"id": "drew-1860", "name": "Thomas Drew, The John Brown Invasion (1860), reprinting the "
     "Baltimore papers"},
    {"id": "shepherdstown-register", "name": "Shepherdstown Register, 22 October 1859"},
    {"id": "hungerford-1928", "name": "Edward Hungerford, The Story of the Baltimore & Ohio "
     "Railroad (1928)"},
    {"id": "doc-y", "name": "Correspondence relating to the Insurrection at Harper's Ferry "
     "(Maryland Senate Document Y, 1860): the B&O's telegrams", "zone": CLOCK},
    {"id": "bo-annual-report-1859", "name": "Thirty-third Annual Report of the Baltimore and "
     "Ohio Railroad (1859)"},
    {"id": "douglass-life", "name": "Frederick Douglass, Life and Times of Frederick Douglass"},
    {"id": "nps-raid", "name": "National Park Service, \"John Brown's Raid\" (timeline)"},
    {"id": "nps-history-series", "name": "National Park Service History Series, John Brown's "
     "Raid (1973)"},
    {"id": "wikipedia-raid", "name": "John Brown's raid on Harpers Ferry (en.wikipedia)"},
    {"id": "hmdb-151957", "name": "\"In Memoriam\" plaque at the Kennedy Farm (HMdb 151957)"},
    {"id": "nhl-kennedy-farm", "name": "National Historic Landmark nomination, Kennedy Farm "
     "(1973)"},
    {"id": "nrhp", "name": "National Register of Historic Places: Beall-Air; Allstadt House"},
    {"id": "osm", "name": "OpenStreetMap: the ruins and sites of 1859"},
]
OPPONENTS = {"CITIZENS", "JEFFERSON GUARDS", "BOTTS COMPANY", "IRWIN PARTY",
             "MARTINSBURG COMPANY", "FREDERICK MILITIA", "BALTIMORE MILITIA", "MARINES",
             "STORMING PARTY", "LEE", "STUART"}


def evidence_for(entity, at):
    """(source id, horizontal bound in metres) for a reconstructed fix."""
    if entity == "EXPRESS":
        return "reconstruction-railroad", 300.0 if at < L("17 07:05") else 3000.0
    if entity in OPPONENTS:
        town = at >= L("17 23:40") or entity in ("CITIZENS", "IRWIN PARTY", "STORMING PARTY")
        return "reconstruction-opponents", 60.0 if town else 1500.0
    if entity in ("HAZLETT", "O ANDERSON") and at >= L("17 17:30"):
        return "reconstruction-raiders", 1000.0
    return "reconstruction-raiders", 60.0 if L("16 22:30") <= at else 300.0


def emit_track(em, entity, track, until):
    """One fix per waypoint, each valid until the next; the last holds to the end, or to
    `until` where the man escapes, after which there is a gap."""
    times = [w.at_ms for w in track.waypoints]
    for i, at in enumerate(times):
        nxt = times[i + 1] if i + 1 < len(times) else until
        source, bound = evidence_for(entity, at)
        point, _ = track.at(at)
        em.fix(source, entity, at, point, 0.0, bound, nxt, "reconstructed", [],
               reference="ground")
    if until is not None:
        em.gap(evidence_for(entity, until)[0], entity, until, None, "reconstructed", [])


def main():
    out = HERE.parent
    tracks, conditions, escaped = moves.plan()
    checks.all(tracks)
    em = Emitter(OP)
    for entity, track in tracks.items():
        until = L(escaped[entity]) + 1 if entity in escaped else None
        emit_track(em, entity, track, until)
    for id_, _, _, _, point, bound, source in FIXED:
        em.fix(source, id_, 0, point, 0.0, bound, None, "reported", [], reference="site")
    for id_, _, point in WIRES:
        em.fix("reconstruction-estimate", id_, 0, point, 0.0, 1500.0, None, "reconstructed", [],
               reference="site")
    for entity, at, condition in conditions:
        em.condition("reconstruction-estimate", entity, L(at), condition, "reconstructed", [])
    story.annotations(em)
    undeclared = {e["source"]["id"] for e in em.events} - {s["id"] for s in SOURCES}
    if undeclared:
        raise ValueError(f"events cite undeclared sources: {sorted(undeclared)}")
    em.write(out / "events.jsonl")
    op = {
        "format": "sokoly-operation",
        "version": 4,
        "id": OP,
        "name": "John Brown's raid on Harpers Ferry",
        "duration_ms": DURATION,
        "time_origin": ("16 October 1859 14:30 Harpers Ferry local mean time (UTC−5:10:55), "
                        "Sunday afternoon at the Kennedy farm, when Brown gave his orders; "
                        "records' times are as each writer's town kept them"),
        "time": {
            "range": {"start": 0, "end": DURATION},
            "anchor": {
                "at": 0,
                "unix_ms": unix_ms(),
                "source": ("Anderson (1861): the eleven orders on the afternoon of Sunday 16 "
                           "October, the march at eight that evening"),
                "source_scale": "utc",
                "uncertainty_ms": 600_000,
                "resolution_ms": 60_000,
                "original_calendar": "1859-10-16 Harpers Ferry local mean time",
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
    doc = story.document(OP, cues, intents)
    (out / "presentations").mkdir(exist_ok=True)
    (out / "presentations" / "default.json").write_text(
        json.dumps(doc, indent=2, ensure_ascii=False) + "\n")
    ledger.write_readme(out / "README.md", DISPUTES, {s["id"]: s["name"] for s in SOURCES},
                        "harpers_ferry.py", MOMENTS)
    facts.write_mission(out, OP, {**MOMENTS, **DISPUTES}, L)
    viewing = sum((c["end_ms"] - c["start_ms"]) / c["speed"] for c in doc["playback_track"])
    print(f"{len(em.events)} events, {len(cues)} shots; viewing {viewing / 1000:.0f} s; "
          f"{checks.summary(tracks)}")


if __name__ == "__main__":
    main()
