#!/usr/bin/env python3
"""What each shot of a mission's story shows, from the viewer's own frame report.

Runs `sokoly-app --operation MISSION --frame-report` (the binary named by $SOKOLY_APP, or a
release build beside this repository), which projects every entity with the viewer's globe
projection every half second of viewing. For each camera cue it prints where the focus sits
in the frame, the symbols drawn (folded into formations as on screen), and how much briefing
text appears against the viewing time there is to read it.

    python3 tools/composition.py missions/operation-vengeance

Findings, also returned by `findings()` for verify.py:
- framing: after its transition, a located focus leaves the frame or comes within EDGE of its
  border (a focus with no position, such as an aircraft after it was last seen, is noted);
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


def app_binary():
    """The viewer binary to report with, or None."""
    named = os.environ.get("SOKOLY_APP")
    if named:
        if not Path(named).is_file():
            raise FileNotFoundError(f"SOKOLY_APP names {named}, which is not a file")
        return Path(named)
    built = REPO.parent / "Sokoly-App" / "target" / "release" / "sokoly-app"
    return built if built.is_file() else None


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


def summarise(mission, report):
    """(lines of text, framing problems, reading problems) for one mission."""
    op = json.loads((mission / "operation.json").read_text())
    story = json.loads((mission / "presentations" / "default.json").read_text())
    events = [json.loads(line) for line in (mission / "events.jsonl").read_text().splitlines()]
    names = {e["id"]: e.get("name") or e["id"] for e in op["entities"]}
    at = clock(op)
    pacing = story["playback_track"]
    briefs = notes(events)
    late = unread(pacing, briefs)
    by_cue = defaultdict(list)
    for s in report["samples"]:
        if s["cue"] is not None:
            by_cue[s["cue"]].append(s)
    lines, problems, reading = [], [], []
    for index, cue in enumerate(story["camera_track"]):
        samples = by_cue.get(index, [])
        viewing = viewing_between(pacing, cue["start_ms"], cue["end_ms"])
        if not samples:
            continue
        head = (f"{at(cue['start_ms'])}–{at(cue['end_ms'])}  {viewing:5.1f} s viewing  "
                f"zoom {cue['zoom']:.1f} pitch {cue['pitch']:.0f}")
        focus = cue.get("focus")
        lines.append(head + (f"  focus {names.get(focus, focus)}" if focus else ""))
        settled = [s for s in samples if s["at_ms"] >= cue["start_ms"] + cue["transition_ms"]]
        if focus:
            where = [next((e for e in s["entities"] if e["id"] == focus), None) for s in settled]
            placed = [(s, e) for s, e in zip(settled, where) if e]
            inside = [e for _, e in placed if framed(e)]
            if placed:
                xs = [e["x"] for _, e in placed]
                ys = [e["y"] for _, e in placed]
                lines.append(f"    focus in frame {100 * len(inside) / len(placed):.0f}%  "
                             f"x {min(xs):.2f}–{max(xs):.2f}  y {min(ys):.2f}–{max(ys):.2f}")
            gone = next((s for s, e in zip(settled, where) if e is None), None)
            if gone:
                lines.append(f"    focus has no position from {at(gone['at_ms'])}")
            for s, e in zip(settled, where):
                if e and not framed(e):
                    problems.append(f"{at(s['at_ms'])}: shot {at(cue['start_ms'])} loses its "
                                    f"focus {names.get(focus, focus)} (x {e['x']:.2f} "
                                    f"y {e['y']:.2f})")
                    break
        drawn = sorted({label for s in samples for _, label in s["drawn"]})
        lift = max((e["lift"] for s in samples for e in s["entities"]), default=0.0)
        lines.append(f"    drawn: {', '.join(drawn[:12])}{' …' if len(drawn) > 12 else ''}")
        if lift > 0.05:
            lines.append(f"    terrain: 100 m of ground would lift symbols {lift:.2f} of the frame")
        new = sum(c for a, _, c in briefs if cue["start_ms"] <= a < cue["end_ms"])
        peak = max(s["briefing_chars"] for s in samples)
        lines.append(f"    briefing: {new} new characters, up to {peak} on screen")
        if peak > PANEL_CHARS:
            reading.append(f"{at(cue['start_ms'])}: {peak} characters of briefing on screen "
                           f"at once, more than the panel's {PANEL_CHARS}")
    for start, left in late:
        reading.append(f"{at(start)}: a note leaves the screen with {left} characters unread "
                       f"at {READ_CPS:.0f} a second")
    return lines, problems, reading


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
