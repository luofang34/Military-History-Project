#!/usr/bin/env python3
"""What each shot of a mission's story shows, from the viewer's own frame report.

Runs `sokoly-app --operation MISSION --frame-report` (the binary named by $SOKOLY_APP, or the
release build in ../Sokoly-App-main, which must be newer than its checkout), which projects
every entity with the viewer's globe projection every half second of viewing. For each camera cue it prints its stated intent, how
long it plays and how it arrives, where the focus and each promised entity sit in the frame,
what moves on screen, the symbols drawn (folded into formations as on screen), and how much
briefing text appears against the viewing time there is to read it; with viewing seconds per
chapter. Reading this is enough to judge a shot without a screenshot.

    python3 tools/composition.py missions/operation-vengeance

Findings, also returned by `findings()` for verify.py:
- framing: after its transition, a located focus leaves the frame or comes within EDGE of its
  border (a focus with no position, such as an aircraft after it was last seen, is noted);
- promise: an entity the shot's intent says it shows never comes near the frame while the
  shot holds, or is inside it less than SHOWN of the time it is near;
- reading: a briefing note leaves the screen before a viewer reading at READ_CPS, who reads
  first whichever note on screen leaves soonest, has read it; or more than PANEL_CHARS are on
  screen at once.
"""
import datetime as dt
import heapq
import json
import os
import subprocess
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

EDGE = 0.03  # of the frame: a symbol's half-width at the default window size
READ_CPS = 20.0  # characters per second of comfortable reading
PANEL_CHARS = 900  # what the briefing panel shows at the default window size before scrolling
REPO = Path(__file__).resolve().parents[1]


# The detached origin/main worktree AGENTS.md has the viewer built in; a checkout another
# session is changing would judge the shots by unreleased code.
MAIN = REPO.parent / "Sokoly-App-main"


class StaleBinary(Exception):
    """The default viewer binary is older than the checkout it is built from."""


def app_binary():
    """The viewer binary to report with, or None."""
    named = os.environ.get("SOKOLY_APP")
    if named:
        if not Path(named).is_file():
            raise FileNotFoundError(f"SOKOLY_APP names {named}, which is not a file")
        return Path(named)
    built = MAIN / "target" / "release" / "sokoly-app"
    if not built.is_file():
        return None
    checked_out = subprocess.run(["git", "-C", str(MAIN), "log", "-1", "--format=%ct"],
                                 capture_output=True, text=True, check=True).stdout
    if built.stat().st_mtime < int(checked_out):
        raise StaleBinary(f"{built} is older than {MAIN}'s checkout; rebuild it (AGENTS.md)")
    return built


class NoReport(Exception):
    """The viewer binary is a build without --frame-report."""


class ReportFailed(Exception):
    """The viewer binary has the option but could not write the report."""


def frame_report(mission, app):
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "frames.json"
        run = subprocess.run([str(app), "--operation", str(mission), "--frame-report", str(out)],
                             capture_output=True, text=True)
        if run.returncode != 0:
            said = (run.stderr or run.stdout).strip().splitlines()[-1:]
            if any("unknown option --frame-report" in line for line in said):
                raise NoReport(f"{app} has no --frame-report")
            raise ReportFailed(f"{app} failed on {mission.name}: {said}")
        return json.loads(out.read_text())


def clock(op):
    """Formats operation milliseconds as the operation's local clock."""
    anchor = op["time"]["anchor"]
    zone = dt.timezone(dt.timedelta(seconds=op["time"]["zone"]["seconds"]))

    def fmt(ms):
        t = dt.datetime.fromtimestamp((anchor["unix_ms"] + ms - anchor["at"]) / 1000, zone)
        return t.strftime("%H:%M:%S")
    return fmt


def viewing_between(pacing, a, b):
    return sum(max(0, min(b, c["end_ms"]) - max(a, c["start_ms"])) / c["speed"]
               for c in pacing) / 1000


def viewing_at(pacing, ms):
    """Viewing seconds from the start of the story to operation time `ms`."""
    return viewing_between(pacing, 0, ms)


def unread(pacing, briefs):
    """(appears ms, characters left unread) for each note that leaves the screen before a
    reader at READ_CPS has read it, reading first whichever note on screen leaves soonest;
    up to a second's reading may be missed."""
    queue = sorted((viewing_at(pacing, a), viewing_at(pacing, b), a, chars)
                   for a, b, chars in briefs)
    pending, out, now, k = [], [], 0.0, 0
    while k < len(queue) or pending:
        if not pending:
            now = max(now, queue[k][0])
        while k < len(queue) and queue[k][0] <= now:
            shown, gone, start, chars = queue[k]
            heapq.heappush(pending, [gone, start, float(chars)])
            k += 1
        gone, start, left = pending[0]
        until = min(gone, queue[k][0] if k < len(queue) else gone)
        read = min(left, max(0.0, until - now) * READ_CPS)
        now += read / READ_CPS
        pending[0][2] -= read
        if pending[0][2] <= 0.5:
            heapq.heappop(pending)
        elif now >= gone - 1e-9:
            heapq.heappop(pending)
            if pending_left(left - read):
                out.append((start, int(left - read)))
        if read == 0 and pending and pending[0][0] <= now:
            gone, start, left = heapq.heappop(pending)
            if pending_left(left):
                out.append((start, int(left)))
    return out


def pending_left(chars):
    """Whether unread characters exceed a second's reading."""
    return chars > READ_CPS


def notes(events):
    """(appears ms, ends ms, characters) for every briefing note."""
    out = []
    for e in events:
        if e["payload"]["kind"] == "annotation":
            end = e["valid_until_ms"] if e["valid_until_ms"] is not None else e["observed_ms"]
            out.append((e["observed_ms"], end, len(e["payload"]["data"])))
    return out


def framed(seen):
    """Whether a projected entity lies inside the frame, clear of its border."""
    return EDGE <= seen["x"] <= 1 - EDGE and EDGE <= seen["y"] <= 1 - EDGE


INTENTS = "shot_intents"  # presentation extension: what each shot is for, by its start_ms
SHOWN = 0.9  # of the settled samples in which an entity a shot shows has a position


def intents(story):
    """Each camera cue's {"intent": what it is for, "shows": entity ids it must keep in
    frame}, keyed by its start_ms as a string."""
    return story.get("extensions", {}).get(INTENTS, {})


def promise_lines(at, cue, settled, shows, names):
    """(lines, problems) checking a shot's promise against the frame: every entity it shows
    comes near the frame at some point once the camera settles (the report lists only
    entities within its margin), and is inside it in at least SHOWN of those samples."""
    lines, problems = [], []
    for entity in shows:
        seen = [e for s in settled for e in s["entities"] if e["id"] == entity]
        name = names.get(entity, entity)
        if not seen:
            lines.append(f"    shows {name}: never near the frame while the shot holds")
            problems.append(f"shot {at(cue['start_ms'])} promises {name}, which never comes "
                            f"near the frame while it holds")
            continue
        share = sum(framed(e) for e in seen) / len(seen)
        lines.append(f"    shows {name}: in frame {100 * share:.0f}% of the {len(seen)} of "
                     f"{len(settled)} samples it is near it")
        if share < SHOWN:
            problems.append(f"shot {at(cue['start_ms'])} promises {name}, in frame only "
                            f"{100 * share:.0f}% of the time it is near it")
    return lines, problems


def shot_head(at, pacing, cue, before, names):
    """The shot's timing, how it arrives from the previous shot, and its focus."""
    start, end = cue["start_ms"], cue["end_ms"]
    settles = min(end, start + cue["transition_ms"])
    move = viewing_between(pacing, start, settles)
    hold = viewing_between(pacing, settles, end)
    arrive = "cut" if cue["transition_ms"] == 0 else f"move {move:.1f} s"
    zoom, pitch = f"zoom {cue['zoom']:.1f}", f"pitch {cue['pitch']:.0f}"
    if before is not None:
        zoom += f" ({cue['zoom'] - before['zoom']:+.1f})"
        pitch += f" ({cue['pitch'] - before['pitch']:+.0f})"
    focus = cue.get("focus")
    return (f"{at(start)}–{at(end)}  {move + hold:5.1f} s viewing, {arrive}, hold {hold:.1f} s"
            f"  {zoom}  {pitch}"
            + (f"  focus {names.get(focus, focus)}" if focus else ""))


def focus_lines(at, cue, settled, names):
    """(lines, framing problems) for where the shot's focus sits once the camera settles."""
    focus = cue.get("focus")
    if not focus:
        return [], []
    lines, problems = [], []
    where = [next((e for e in s["entities"] if e["id"] == focus), None) for s in settled]
    placed = [(s, e) for s, e in zip(settled, where) if e]
    if placed:
        xs = [e["x"] for _, e in placed]
        ys = [e["y"] for _, e in placed]
        inside = [e for _, e in placed if framed(e)]
        lines.append(f"    focus in frame {100 * len(inside) / len(placed):.0f}%  "
                     f"x {min(xs):.2f}–{max(xs):.2f}  y {min(ys):.2f}–{max(ys):.2f}  "
                     f"travels {max(max(xs) - min(xs), max(ys) - min(ys)):.2f} of the frame")
    gone = next((s for s, e in zip(settled, where) if e is None), None)
    if gone:
        lines.append(f"    focus has no position from {at(gone['at_ms'])}")
    for s, e in zip(settled, where):
        if e and not framed(e):
            problems.append(f"{at(s['at_ms'])}: shot {at(cue['start_ms'])} loses its focus "
                            f"{names.get(focus, focus)} (x {e['x']:.2f} y {e['y']:.2f})")
            break
    return lines, problems


def chapter_lines(story, pacing, at):
    """Viewing seconds per chapter, so the story's pace reads on one screen."""
    chapters = sorted(story.get("chapters", []), key=lambda c: c["at_ms"])
    ends = [c["at_ms"] for c in chapters[1:]] + [max(c["end_ms"] for c in pacing)]
    lines = ["chapters:"]
    for chapter, end in zip(chapters, ends):
        viewing = viewing_between(pacing, chapter["at_ms"], end)
        lines.append(f"    {at(chapter['at_ms'])}  {viewing:5.1f} s  {chapter['title']}")
    return lines


def summarise(mission, report):
    """(lines of text, framing problems, reading problems) for one mission."""
    op = json.loads((mission / "operation.json").read_text())
    story = json.loads((mission / "presentations" / "default.json").read_text())
    events = [json.loads(line) for line in (mission / "events.jsonl").read_text().splitlines()]
    names = {e["id"]: e.get("name") or e["id"] for e in op["entities"]}
    at = clock(op)
    pacing = story["playback_track"]
    briefs = notes(events)
    purpose = intents(story)
    by_cue = defaultdict(list)
    for s in report["samples"]:
        if s["cue"] is not None:
            by_cue[s["cue"]].append(s)
    lines, problems, reading = chapter_lines(story, pacing, at), [], []
    before = None
    for index, cue in enumerate(story["camera_track"]):
        samples = by_cue.get(index, [])
        if samples:
            lines.append(shot_head(at, pacing, cue, before, names))
            stated = purpose.get(str(cue["start_ms"]), {})
            lines.append(f"    intent: {stated.get('intent', '(none stated)')}")
            settled = [s for s in samples
                       if s["at_ms"] >= cue["start_ms"] + cue["transition_ms"]]
            shown, lost = focus_lines(at, cue, settled, names)
            # A shot that is all move promises what it arrives at.
            kept, broken = promise_lines(at, cue, settled or samples[-1:],
                                         stated.get("shows", []), names)
            lines.extend(shown + kept)
            lines.extend(motion_lines(settled, cue.get("focus"), names))
            problems.extend(lost + broken)
            lines.extend(content_lines(cue, samples, briefs))
            peak = max(s["briefing_chars"] for s in samples)
            if peak > PANEL_CHARS:
                reading.append(f"{at(cue['start_ms'])}: {peak} characters of briefing on "
                               f"screen at once, more than the panel's {PANEL_CHARS}")
        before = cue
    for start, left in unread(pacing, briefs):
        reading.append(f"{at(start)}: a note leaves the screen with {left} characters unread "
                       f"at {READ_CPS:.0f} a second")
    return lines, problems, reading


def motion_lines(settled, focus, names):
    """How far the symbol that moves most across the settled frame travels, other than the
    focus: a followed aircraft stays centred, so this is what shows motion on screen."""
    paths = defaultdict(list)
    for s in settled:
        for e in s["entities"]:
            if e["id"] != focus and framed(e):
                paths[e["id"]].append((e["x"], e["y"]))
    travel = {k: max(max(x for x, _ in p) - min(x for x, _ in p),
                     max(y for _, y in p) - min(y for _, y in p)) for k, p in paths.items()}
    if not travel:
        return ["    nothing else in frame"]
    most = max(travel, key=travel.get)
    return [f"    on screen, {names.get(most, most)} travels {travel[most]:.2f} of the frame"]


def content_lines(cue, samples, briefs):
    """What the shot draws, how far terrain could shift it, and the briefing it carries."""
    drawn = sorted({label for s in samples for _, label in s["drawn"]})
    lift = max((e["lift"] for s in samples for e in s["entities"]), default=0.0)
    lines = [f"    drawn: {', '.join(drawn[:12])}{' …' if len(drawn) > 12 else ''}"]
    if lift > 0.05:
        lines.append(f"    terrain: 100 m of ground would lift symbols {lift:.2f} of the frame")
    new = sum(c for a, _, c in briefs if cue["start_ms"] <= a < cue["end_ms"])
    peak = max(s["briefing_chars"] for s in samples)
    lines.append(f"    briefing: {new} new characters, up to {peak} on screen")
    return lines


def findings(mission, app):
    """(framing problems, reading problems) for `mission`, from the viewer binary `app`."""
    _, framing, reading = summarise(mission, frame_report(mission, app))
    return framing, reading


def main():
    app = app_binary()
    if app is None:
        sys.exit("no viewer binary: set SOKOLY_APP or build Sokoly-App with --release")
    for arg in sys.argv[1:]:
        mission = Path(arg).resolve()
        try:
            report = frame_report(mission, app)
        except NoReport as error:
            sys.exit(str(error))
        lines, framing, reading = summarise(mission, report)
        print(f"# {mission.name}")
        print("\n".join(lines))
        for problem in framing:
            print(f"FRAMING {problem}")
        for problem in reading:
            print(f"READING {problem}")


if __name__ == "__main__":
    main()
