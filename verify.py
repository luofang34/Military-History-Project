#!/usr/bin/env python3
"""Check what the App's loader does not enforce.

Every second of each operation needs exactly one playback cue and one camera
cue in its default presentation, and a cue that follows an entity must find a
valid fix for its whole span; otherwise the authored camera stalls. A map on
which nothing moves may play for at most MAX_STILL_VIEWING_S, every event must
lie within the operation, and every source an event cites must be declared. Every shot
states its intent and what it shows, plays long enough to register, arrives by a cut or a
visible move, and holds no longer than a viewer stays with one picture. With a viewer
binary, its frame report must show each shot's focus and promised entities in frame, and
every briefing note readable before it leaves the screen. Reconstructed tracks must hand
over between sources 1 ms apart, and the order of battle must resolve. The App itself
validates the schema.
"""
import bisect
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import parse_qs, urljoin, urlsplit

root = Path(__file__).resolve().parent
sys.path.insert(0, str(root / "tools"))
import composition as composition_tool  # noqa: E402


def fixes_by_entity(events):
    spans = defaultdict(list)
    for e in events:
        if e["payload"]["kind"] != "position":
            continue
        # An open-ended fix holds until the next one; inf keeps the tuples orderable.
        end = e["valid_until_ms"]
        end = float("inf") if end is None else end
        spans[e["entity"]].append((e["observed_ms"], end, e["payload"]["data"] is not None))
    for entity in spans:
        spans[entity].sort()
    return spans


def located(spans, at):
    i = bisect.bisect_right(spans, (at, float("inf"), True)) - 1
    if i < 0:
        return False
    start, end, present = spans[i]
    return present and at < end


def joins_across_sources(events):
    """The App joins consecutive fixes only within one source, so where a reconstructed path
    changes source while the earlier fix still holds, the handover must be 1 ms apart; a
    longer one freezes the entity on the earlier fix. A fix that expires first is a gap."""
    by_entity = defaultdict(list)
    for e in events:
        if e["payload"]["kind"] == "position":
            by_entity[e["entity"]].append(e)
    for entity, fixes in by_entity.items():
        fixes.sort(key=lambda e: e["observed_ms"])
        for a, b in zip(fixes, fixes[1:]):
            joined = a["payload"]["data"] is not None and b["payload"]["data"] is not None
            until = a["valid_until_ms"]
            holds = until is None or until >= b["observed_ms"]
            if (joined and holds and a["source"]["id"] != b["source"]["id"]
                    and b["observed_ms"] - a["observed_ms"] > 1):
                yield entity, a["observed_ms"]


def broken_parents(entities):
    """Parents that name no declared entity, or chains that loop; the App rejects both."""
    parent = {e["id"]: e.get("parent") for e in entities}
    for entity, up in parent.items():
        if up is not None and up not in parent:
            yield f"{entity}: parent {up} is not declared"
        seen, at = {entity}, up
        while at is not None and at in parent:
            if at in seen:
                yield f"{entity}: order of battle loops through {at}"
                break
            seen.add(at)
            at = parent[at]


MAX_STILL_VIEWING_S = 6.0


def still_stretches(events, presentation, duration, sources):
    """Stretches of the operation in which nothing on the map moves, with their viewing time.
    A still map holds the viewer for at most MAX_STILL_VIEWING_S; a briefing stays readable
    after the action resumes. Motion is counted only where the App draws it: between two
    fixes of one source that declares a motion model, within its max_gap_ms, while the
    earlier fix still holds."""
    model = {s["id"]: s.get("max_gap_ms") for s in sources if s.get("motion")}
    fixes = defaultdict(list)
    for e in events:
        if e["payload"]["kind"] == "position":
            fixes[e["entity"]].append(e)
    moving = []
    for track in fixes.values():
        track.sort(key=lambda e: e["observed_ms"])
        for a, b in zip(track, track[1:]):
            pa, pb = a["payload"]["data"], b["payload"]["data"]
            start, end = a["observed_ms"], b["observed_ms"]
            source = a["source"]["id"]
            gap = model.get(source)
            holds = a["valid_until_ms"] is None or a["valid_until_ms"] >= end
            if (pa is not None and pb is not None and source == b["source"]["id"]
                    and source in model and (gap is None or end - start <= gap) and holds
                    and pa["point"] != pb["point"] and end - start > 1):
                moving.append((start, end))
    moving.sort()
    still, t = [], 0
    for a, b in moving:
        if a > t:
            still.append((t, a))
        t = max(t, b)
    if t < duration:
        still.append((t, duration))
    pace = presentation["playback_track"]
    for a, b in still:
        viewing = sum(max(0, min(b, c["end_ms"]) - max(a, c["start_ms"])) / c["speed"]
                      for c in pace) / 1000
        yield a, b, viewing


MIN_SHOT_S = 1.5  # a shot shorter than this flashes past before it registers
MIN_MOVE_S = 0.8  # a move between shots shorter than this jumps; make it a cut or a move
MAX_HOLD_S = 45.0  # a settled shot held longer than this wants a new angle or a faster pace


def shot_timing(story):
    """Each shot's length, move and settled hold against MIN_SHOT_S, MIN_MOVE_S and
    MAX_HOLD_S, in seconds of viewing."""
    pace = story["playback_track"]
    for c in story["camera_track"]:
        start, end = c["start_ms"], c["end_ms"]
        settles = start + c["transition_ms"]
        move = composition_tool.viewing_between(pace, start, settles)
        hold = composition_tool.viewing_between(pace, settles, end)
        if move + hold < MIN_SHOT_S:
            yield f"shot at {start} ms plays {move + hold:.1f} s, under {MIN_SHOT_S} s"
        if 0 < move < MIN_MOVE_S:
            yield f"shot at {start} ms moves in {move:.2f} s; cut or take {MIN_MOVE_S} s"
        if hold > MAX_HOLD_S:
            yield f"shot at {start} ms holds {hold:.0f} s, over {MAX_HOLD_S:.0f} s"


def unstated_intents(story, entities):
    """Every shot states what it is for and which declared entities it shows, under the
    presentation's shot_intents extension keyed by its start_ms, and no intent names a shot
    that does not exist. Only a shot held on a place may show no entity. The frame report
    checks that each shot keeps the entities it names in frame."""
    stated = composition_tool.intents(story)
    targets = {str(c["start_ms"]): c["target"]["kind"] for c in story["camera_track"]}
    starts = set(targets)
    declared = {e["id"] for e in entities}
    for start in sorted(starts, key=int):
        promise = stated.get(start)
        if not isinstance(promise, dict) or not str(promise.get("intent", "")).strip():
            yield f"shot at {start} ms states no intent"
        elif not promise.get("shows") and targets[start] == "entity":
            yield f"shot at {start} ms follows an entity but names nothing it shows"
        else:
            for entity in sorted(set(promise["shows"]) - declared):
                yield f"shot at {start} ms shows {entity}, which is not declared"
    for start in sorted(set(stated) - starts, key=int):
        yield f"intent for {start} ms names no shot"


APP = None


def composition(mission, app):
    """Framing and reading problems from the viewer's own frame report
    (tools/composition.py)."""
    return composition_tool.findings(mission, app)


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
    problems.extend(broken_parents(op["entities"]))
    for e in events:
        if not 0 <= e["observed_ms"] <= duration:
            problems.append(f"event {e['id']} at {e['observed_ms']} ms lies outside 0–{duration}")
            break
    declared = {s["id"] for s in op["sources"]}
    for source in sorted({e["source"]["id"] for e in events} - declared):
        problems.append(f"events cite source {source}, which operation.json does not declare")
    for entity, fixes in joins_across_sources(events):
        problems.append(f"{entity}: fix at {fixes} joins a fix from another source")
    for a, b, viewing in still_stretches(events, story, duration, op["sources"]):
        if viewing > MAX_STILL_VIEWING_S:
            problems.append(f"nothing moves from {a} to {b} ms but it plays for {viewing:.0f} s")
    for track in ("camera_track", "playback_track"):
        for c in story[track]:
            if not 0 <= c["start_ms"] < c["end_ms"] <= duration:
                problems.append(f"{track} cue {c['start_ms']}–{c['end_ms']} leaves 0–{duration}")
    for a, b in zip(story["camera_track"], story["camera_track"][1:]):
        if a["end_ms"] != b["start_ms"]:
            problems.append(f"camera gap or overlap at {a['end_ms']}")
    problems.extend(unstated_intents(story, op["entities"]))
    problems.extend(shot_timing(story))
    reading = None
    if APP:
        try:
            framing, reading = composition(mission, APP)
            problems.extend(framing + reading)
        except composition_tool.NoReport as error:
            print(f"{mission.name}: composition skipped, {error}", file=sys.stderr)
    viewing = sum((c["end_ms"] - c["start_ms"]) / c["speed"]
                  for c in story["playback_track"]) / 1000
    for problem in problems[:40]:
        print(f"{mission.name}: {problem}", file=sys.stderr)
    print(f"{mission.name}: {len(events)} events, {len(op['entities'])} entities, "
          f"{len(story['camera_track'])} shots, viewing {viewing:.0f} s"
          + (", composition checked" if reading is not None else ""))
    return not problems


def catalog_lists_every_mission():
    """Each mission folder appears in catalog.json under its folder name, and nothing else."""
    catalog = json.loads((root / "catalog.json").read_text())
    listed = {m["package"] for m in catalog["missions"]}
    present = {f"missions/{m.name}" for m in (root / "missions").iterdir() if m.is_dir()}
    for missing in sorted(present - listed):
        print(f"catalog.json does not list {missing}", file=sys.stderr)
    for stale in sorted(listed - present):
        print(f"catalog.json lists missing {stale}", file=sys.stderr)
    return listed == present


class LaunchLinkParser(HTMLParser):
    """Read the accessible replay link, also used by the automatic launcher."""

    def __init__(self):
        super().__init__()
        self.href = None

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "a" and attributes.get("id") == "launch":
            self.href = attributes.get("href")


def front_matter(text):
    """Jekyll front matter as a dict of `key: value` lines; empty without front matter."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    fields = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return fields
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip()
    return {}


def replay_links_match_catalog():
    """Keep each public launcher inside its mission folder, published at /<id>/, and
    connected to its catalogued operation package."""
    catalog = json.loads((root / "catalog.json").read_text())
    origin = f"https://{(root / 'CNAME').read_text().strip()}/"
    viewer = urlsplit(catalog["viewer"])
    problems = []
    for mission in catalog["missions"]:
        if (root / mission["id"]).exists():
            problems.append(f"{mission['id']}: launch page belongs in {mission['package']}/")
        path = root / mission["package"] / "index.html"
        if not path.is_file():
            problems.append(f"{mission['id']}: missing public replay page")
            continue
        text = path.read_text()
        if front_matter(text).get("permalink") != f"/{mission['id']}/":
            problems.append(f"{mission['id']}: replay page is not published at /{mission['id']}/")
        link = LaunchLinkParser()
        link.feed(text)
        target = urlsplit(link.href or "")
        options = parse_qs(target.query, keep_blank_values=True)
        if (target.scheme, target.netloc, target.path) != (viewer.scheme, viewer.netloc, viewer.path):
            problems.append(f"{mission['id']}: replay link does not use the catalog viewer")
        if options.get("operation") != [urljoin(origin, mission["package"])]:
            problems.append(f"{mission['id']}: replay link does not open its published package")
        if "recorded-path" not in options:
            problems.append(f"{mission['id']}: replay link does not enable the story camera")
    for problem in problems:
        print(problem, file=sys.stderr)
    return not problems


def agents_guide_holds():
    """AGENTS.md names only files that exist, in the repository or in every mission, and
    constants that exist; Pages leaves the guide unpublished, and no CLAUDE.md displaces it."""
    guide = (root / "AGENTS.md").read_text()
    missions = [m for m in (root / "missions").iterdir() if m.is_dir()]
    problems = []
    for name in re.findall(r"`([\w./-]+\.(?:py|json|md|yml))`", guide):
        if not (root / name).exists() and not all((m / name).exists() for m in missions):
            problems.append(f"AGENTS.md names {name}, which does not exist")
    sources = (root / "verify.py").read_text() + (root / "tools" / "composition.py").read_text()
    for constant in re.findall(r"`([A-Z][A-Z_]+)`", guide):
        if not re.search(rf"^{constant} = ", sources, re.M):
            problems.append(f"AGENTS.md names {constant}, which verify.py and "
                            f"tools/composition.py do not define")
    config = (root / "_config.yml").read_text()
    if not re.search(r"^\s*- AGENTS\.md$", config, re.M):
        problems.append("_config.yml does not exclude AGENTS.md from Pages")
    if (root / "CLAUDE.md").exists():
        problems.append("CLAUDE.md exists; Claude Code would read it instead of AGENTS.md")
    for problem in problems:
        print(problem, file=sys.stderr)
    return not problems


if __name__ == "__main__":
    APP = composition_tool.app_binary()
    print(f"composition: {APP}" if APP else
          "composition: skipped, no viewer binary (set SOKOLY_APP or build Sokoly-App --release)")
    ok = all([check(m) for m in sorted((root / "missions").iterdir()) if m.is_dir()])
    ok = catalog_lists_every_mission() and ok
    ok = replay_links_match_catalog() and ok
    ok = agents_guide_holds() and ok
    sys.exit(0 if ok else 1)
