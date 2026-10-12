#!/usr/bin/env python3
"""Builds the Operation Vengeance reconstruction (18 April 1943).

Run from anywhere; writes this mission's operation.json and events.jsonl beside build/,
and the story in presentations/default.json. Fixed sites and anchor times are sourced; flight
paths between anchors are reconstructions whose `bound_m` states the horizontal
uncertainty. The build fails if an aircraft leaves its type's speeds, a wreck strays from
its site, or an estimate in build/evidence.py falls outside its records without saying why.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[2] / "tools"))
import checks  # noqa: E402
import engagement  # noqa: E402
import facts  # noqa: E402
import ledger  # noqa: E402
import presentation  # noqa: E402
import routes  # noqa: E402
from track import Emitter  # noqa: E402
from evidence import DISPUTES  # noqa: E402
from sites import (OP, L, DURATION, BETTYS, ZEROS, YAMAMOTO, UGAKI,  # noqa: E402
                   CRASH_T1_323, DITCH_T1_326, FIXED, entities, unix_ms)


# Times at which `evidence_for` changes source; each source's fixes join only to its own.
SOURCE_CHANGES = [L(t) for t in ("07:31:00", "08:08:30", "09:34:00", "09:42:30")]

TOKYO = {"kind": "fixed", "seconds": 9 * 3600,
         "source": "Imperial Japanese Navy records kept Tokyo time (UTC+9)"}
RECONSTRUCTED = {"motion": "great_circle", "max_gap_ms": DURATION}
SOURCES = [
    {"id": "reconstruction-fighter-two-departure", "name": "P-38 departure reconstruction",
     **RECONSTRUCTED},
    {"id": "reconstruction-p38-route", "name": "P-38 route reconstruction", **RECONSTRUCTED},
    {"id": "reconstruction-lakunai-departure", "name": "Lakunai departure reconstruction",
     "zone": TOKYO, **RECONSTRUCTED},
    {"id": "reconstruction-japanese-route", "name": "Japanese route reconstruction",
     "zone": TOKYO, **RECONSTRUCTED},
    {"id": "reconstruction-engagement", "name": "Engagement choreography", **RECONSTRUCTED},
    {"id": "reconstruction-egress", "name": "Egress reconstruction", **RECONSTRUCTED},
    {"id": "13th-fighter-command-report", "name": "13th Fighter Command interception report"},
    {"id": "macr-599-609", "name": "Missing Air Crew Reports 599 and 609"},
    {"id": "pacific-wrecks", "name": "Pacific Wrecks"},
    {"id": "pacific-wrecks-2656", "name": "Pacific Wrecks: G4M1 2656 (T1-323)"},
    {"id": "pacific-wrecks-t1-326", "name": "Pacific Wrecks: G4M1 T1-326"},
    {"id": "yanagiya-interview", "name": "Yanagiya Kenji interview", "zone": TOKYO},
    {"id": "ja-wikipedia-kaigun-ko-jiken", "name": "海軍甲事件 (ja.wikipedia)", "zone": TOKYO},
    {"id": "ja-wikipedia-sugita", "name": "杉田庄一 (ja.wikipedia)", "zone": TOKYO},
    {"id": "pacific-wrecks-hine", "name": "Pacific Wrecks: P-38G Hine"},
    {"id": "pacific-wrecks-ballale", "name": "Pacific Wrecks: Ballale Airfield"},
    {"id": "historynet-lehr-hine",
     "name": "Dick Lehr, \"What Happened to Operation Vengeance Wingman Raymond K. Hine\", "
     "HistoryNet"},
    {"id": "jacar-204-kokutai-18-april",
     "name": "第二〇四海軍航空隊 戦闘行動調書, 18 April 1943 (JACAR C08051654600)", "zone": TOKYO},
    {"id": "yanagiya-yoshimura",
     "name": "Yanagiya Kenji, interviewed in Yoshimura Akira, 戦史の証言者たち", "zone": TOKYO},
    {"id": "wikipedia-operation-vengeance", "name": "Operation Vengeance (en.wikipedia)"},
    {"id": "wikipedia-kukum", "name": "Kukum Field (en.wikipedia)"},
    {"id": "wikipedia-lakunai", "name": "Lakunai Airfield (en.wikipedia)"},
    {"id": "wikipedia-kahili", "name": "Kahili Airfield (en.wikipedia)"},
    {"id": "decrypt-ntf131755", "name": "US Navy decrypt of JN-25 message NTF131755"},
    {"id": "historynet-death-by-p38", "name": "HistoryNet, \"Death by P-38\""},
    {"id": "warfare-history-network-ames",
     "name": "Roger Ames, via Warfare History Network, \"Killing Yamamoto\""},
    {"id": "afm-grant", "name": "Rebecca Grant, \"Magic and Lightning\", Air & Space Forces "
     "Magazine"},
    {"id": "afm-haulman", "name": "Daniel Haulman, \"The Man Who Shot Down Yamamoto\", "
     "Air & Space Forces Magazine"},
    {"id": "barber-v-widnall", "name": "Barber v. Widnall, 78 F.3d 1419 (9th Cir. 1996)"},
    {"id": "reconstruction-estimate",
     "name": "Replay estimates where sources disagree (build/evidence.py)"},
]
NAMES = {s["id"]: s["name"] for s in SOURCES}


def evidence_for(entity, t):
    """(source id, horizontal bound in metres) for a reconstructed fix."""
    japanese = entity in BETTYS or entity in ZEROS
    if t >= L("09:42:30"):
        return "reconstruction-egress", 30_000.0
    if t >= L("09:34:00"):
        return "reconstruction-engagement", 1500.0
    if japanese:
        if t < L("08:08:30"):
            return "reconstruction-lakunai-departure", 800.0
        return "reconstruction-japanese-route", 5000.0 if t >= L("09:22:00") else 30_000.0
    if t < L("07:31:00") or entity in ("MOORE", "MCLANAHAN"):
        return "reconstruction-fighter-two-departure", 500.0
    return "reconstruction-p38-route", 5000.0 if t >= L("09:28:00") else 20_000.0


def emit_track(em, entity, track, final_valid, until=None):
    """One fix per waypoint; the App joins them along great circles, as the track is built.

    Where the evidence source changes, the earlier source reports the position 1 ms
    before, so neither source's path is extended by the other's. With `until`, the
    track's last fix is 1 ms before that time and stays valid to it.
    """
    stop = min(track.end if until is None else until - 1, DURATION)
    times = {w.at_ms for w in track.waypoints if track.start <= w.at_ms <= stop}
    times |= {track.start, stop}
    times |= {t for change in SOURCE_CHANGES if track.start < change <= stop
              for t in (change - 1, change)}
    times = sorted(times)
    last = until if until is not None else final_valid
    for t, nxt in zip(times, times[1:] + [None]):
        point, alt = track.at(t)
        source, bound = evidence_for(entity, t)
        em.fix(source, entity, t, point, alt, bound, last if nxt is None else nxt,
               "reconstructed", [])


REPORT_13FC = "13th-fighter-command-report"


def endings(em, tracks):
    """Known wreck sites persist; missing aircraft and untracked escorts become gaps."""
    em.fix("pacific-wrecks-2656", YAMAMOTO, L("09:38:00"), CRASH_T1_323, 0, 100.0, None,
           "reported", [], reference="wreck")
    em.fix("pacific-wrecks-t1-326", UGAKI, L("09:39:20"), DITCH_T1_326, 0, 500.0, None,
           "reported", [], reference="ditching")
    # Damage as reported: Barber's astern hits, Holmes's attack off Moila Point, debris
    # from T1-326 holing Barber, and Hine trailing smoke (Pacific Wrecks, MACR 609).
    for source, entity, at, condition in [
        ("pacific-wrecks-2656", YAMAMOTO, "09:37:00", "damaged"),
        ("pacific-wrecks-2656", YAMAMOTO, "09:38:00", "destroyed"),
        ("pacific-wrecks-t1-326", UGAKI, "09:38:20", "damaged"),
        ("pacific-wrecks-t1-326", UGAKI, "09:39:20", "destroyed"),
        ("pacific-wrecks", "BARBER", "09:38:55", "damaged"),
        (REPORT_13FC, "LANPHIER", "09:38:40", "damaged"),
        ("macr-599-609", "HINE", "09:41:36", "damaged"),
    ]:
        em.condition(source, entity, L(at), condition, "reported", [])
    hine_end = tracks["HINE"].end
    em.gap("macr-599-609", "HINE", hine_end + 1, None, "reported", [])
    for zero in ZEROS:
        if zero != "OKAZAKI":  # landed at Ballale; his final fix persists
            em.gap("reconstruction-engagement", zero, tracks[zero].end + 1, None,
                   "reconstructed", [])
    em.note("yanagiya-interview", None, L("09:42:00"), L("09:52:00"),
            "Escort tracks end here. All six Zeros survived: Okazaki landed at Ballale with "
            "engine trouble, the rest at Buin; Yanagiya, last down, about 10:20.",
            "reported", [])
    return hine_end


def main():
    out = HERE.parent
    out.mkdir(parents=True, exist_ok=True)
    tracks, lead, p38_speed = routes.p38_tracks()
    japanese, betty_kmh = routes.japanese_tracks()
    tracks.update(japanese)
    engagement.engagement(tracks, lead)
    em = Emitter(OP)
    open_ended = {"MCLANAHAN", "MOORE", "OKAZAKI"}
    for entity, track in tracks.items():
        final = None if entity in open_ended else track.end + 1
        if track.end >= DURATION:
            final = DURATION + 1
        # The sourced wreck fix takes over exactly when the reconstructed flight ends.
        until = track.end if entity in (YAMAMOTO, UGAKI) else None
        emit_track(em, entity, track, final, until)
    hine_end = endings(em, tracks)
    checks.all(tracks, hine_end)
    for id_, _, _, _, point, bound, source in FIXED:
        em.fix(source, id_, 0, point, 0.0, bound, None, "reported", [], reference="site")
    presentation.annotations(em, NAMES)
    em.write(out / "events.jsonl")
    op = {
        "format": "sokoly-operation",
        "version": 4,
        "id": OP,
        "name": "Operation Vengeance",
        "duration_ms": DURATION,
        "time_origin": (
            "18 April 1943 07:24:30 Henderson Field time (UTC+11), the clock of the 13th "
            "Fighter Command interception report; Japanese records use Tokyo time (UTC+9)"),
        "time": {
            "range": {"start": 0, "end": DURATION},
            "anchor": {
                "at": 0,
                "unix_ms": unix_ms(),
                "source": ("13th Fighter Command 'Fighter Interception' report, 18 Apr 1943: "
                           "take-off 0725, interception 0935 Henderson Field time"),
                "source_scale": "utc",
                "uncertainty_ms": 60_000,
                "resolution_ms": 60_000,
                "original_calendar": "1943-04-18 Henderson Field time (UTC+11)",
            },
            "zone": {
                "kind": "fixed",
                "seconds": 11 * 3600,
                "source": ("US forces in the Solomons kept Henderson Field time (UTC+11); "
                           "tzdb Pacific/Bougainville gives the Japanese occupation clock"),
            },
        },
        "captured_availability": False,
        "sources": SOURCES,
        "entities": entities(),
        "media_archive": None,
    }
    (out / "operation.json").write_text(json.dumps(op, indent=2, ensure_ascii=False) + "\n")
    story = presentation.document(OP)
    (out / "presentations").mkdir(exist_ok=True)
    (out / "presentations" / "default.json").write_text(
        json.dumps(story, indent=2, ensure_ascii=False) + "\n")
    viewing = sum((c["end_ms"] - c["start_ms"]) / c["speed"]
                  for c in story["playback_track"]) / 1000
    ledger.write_readme(out / "README.md", DISPUTES, NAMES, "vengeance.py")
    facts.write_mission(out, OP, DISPUTES, L)
    print(f"{len(em.events)} events; P-38 route {p38_speed * 3.6:.0f} km/h, "
          f"Betty route {betty_kmh:.0f} km/h; viewing {viewing:.0f} s; {checks.summary(tracks)}")


if __name__ == "__main__":
    main()
