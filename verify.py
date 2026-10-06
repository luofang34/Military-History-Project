#!/usr/bin/env python3
"""Check presentation coverage that the App's loader does not enforce.

Every second of each operation needs exactly one playback cue and one camera
cue in its default presentation, and a cue that follows an entity must find a
valid fix for its whole span; otherwise the authored camera stalls. The App
itself validates the schema.
"""
import bisect
import json
import sys
from collections import defaultdict
from pathlib import Path

root = Path(__file__).resolve().parent


def fixes_by_entity(events):
    spans = defaultdict(list)
    for e in events:
        if e["payload"]["kind"] != "position":
            continue
        end = e["valid_until_ms"]
        spans[e["entity"]].append((e["observed_ms"], end, e["payload"]["data"] is not None))
    for entity in spans:
        spans[entity].sort()
    return spans


def located(spans, at):
    i = bisect.bisect_right(spans, (at, float("inf"), True)) - 1
    if i < 0:
        return False
    start, end, present = spans[i]
    return present and (end is None or at < end)


def check(mission):
    op = json.loads((mission / "operation.json").read_text())
    story = json.loads((mission / "presentations" / "default.json").read_text())
    events = [json.loads(line) for line in (mission / "events.jsonl").read_text().splitlines()]
    problems = []
    spans = fixes_by_entity(events)
    duration = op["duration_ms"]
    for at in range(0, duration, 250):
        cams = [c for c in story["camera_track"] if c["start_ms"] <= at < c["end_ms"]]
        paces = [c for c in story["playback_track"] if c["start_ms"] <= at < c["end_ms"]]
        if len(cams) != 1 or len(paces) != 1:
            problems.append(f"t={at}: {len(cams)} camera and {len(paces)} playback cues")
            continue
        target = cams[0]["target"]
        if target["kind"] == "entity" and not located(spans.get(target["value"], []), at):
            problems.append(f"t={at}: camera target {target['value']} has no fix")
    for a, b in zip(story["camera_track"], story["camera_track"][1:]):
        if a["end_ms"] != b["start_ms"]:
            problems.append(f"camera gap or overlap at {a['end_ms']}")
    viewing = sum((c["end_ms"] - c["start_ms"]) / c["speed"] for c in story["playback_track"]) / 1000
    for problem in problems[:20]:
        print(f"{mission.name}: {problem}", file=sys.stderr)
    print(f"{mission.name}: {len(events)} events, {len(op['entities'])} entities, "
          f"{len(story['camera_track'])} shots, viewing {viewing:.0f} s")
    return not problems


if __name__ == "__main__":
    ok = all([check(m) for m in sorted((root / "missions").iterdir()) if m.is_dir()])
    sys.exit(0 if ok else 1)
