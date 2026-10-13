#!/usr/bin/env python3
"""Builds the Battle of Taierzhuang, part II: the artillery battle at the canal, 30 March –
1 April 1938.

Run from anywhere; writes this mission's operation.json and events.jsonl beside build/, and
the story in presentations/default.json. Times and places are sourced; the moves between them
are reconstructions whose `bound_m` states the horizontal uncertainty. The build fails if a
battery leaves the place its range fan is drawn from, a round flies further than its gun could
throw it, a unit outpaces the marches of 1938, or an estimate in build/evidence/ falls outside
its records without saying why.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[2] / "tools"))
import checks  # noqa: E402
import facts  # noqa: E402
import fire  # noqa: E402
import graphics  # noqa: E402
import ledger  # noqa: E402
import moves  # noqa: E402
import shots  # noqa: E402
import story  # noqa: E402
from evidence import DISPUTES, MOMENTS  # noqa: E402
from sites import (CHINESE, CST_S, DURATION, FIXED, JAPANESE, OP, L, unix_ms)  # noqa: E402
from track import Emitter  # noqa: E402

CLOCK = {"kind": "fixed", "seconds": CST_S,
         "source": "China's coastal standard time, UTC+8, which the Japanese reports name "
                   "(「時刻ハ西部標準時トス」)"}
RECONSTRUCTED = {"motion": "great_circle", "max_gap_ms": DURATION, "zone": CLOCK}
SOURCES = [
    {"id": "reconstruction-chinese", "name": "Chinese units' moves, reconstructed",
     **RECONSTRUCTED},
    {"id": "reconstruction-japanese", "name": "Japanese units' moves, reconstructed",
     **RECONSTRUCTED},
    {"id": "reconstruction-fire", "name": "Fire missions, from the Japanese reports' times",
     **RECONSTRUCTED},
    {"id": "reconstruction-guns", "name": "Batteries' range fans, reconstructed", "zone": CLOCK},
    {"id": "reconstruction-railway", "name": "The Taierzhuang branch railway of 1938",
     "zone": CLOCK},
    {"id": "reconstruction-estimate",
     "name": "Replay estimates where sources disagree (build/evidence/)", "zone": CLOCK},
    {"id": "jacar-63i-taierzhuang",
     "name": "歩兵第六十三聯隊 台児庄攻略戦闘詳報 (JACAR C11111252700–C11111254100)",
     "zone": CLOCK},
    {"id": "jacar-10i-report-13",
     "name": "歩兵第十聯隊 臺兒庄附近戦闘詳報 第十三號 (JACAR C11111171800–C11111172200)",
     "zone": CLOCK},
    {"id": "jacar-sas-report",
     "name": "臨SAS戦詳第一號 臺兒庄附近ノ戰鬪詳報, 第二軍臨時野戰重砲兵中隊 "
             "(JACAR C11111730100–C11111731000)", "zone": CLOCK},
    {"id": "jacar-ohashi",
     "name": "大橋武夫「支那事変初期 北支における十五榴部隊を中心とする砲兵戦史資料」 "
             "(JACAR C11111729600, C11111729700)", "zone": CLOCK},
    {"id": "jiang-2017", "name": "姜克實「台児庄作戦の概観」, 岡山大学大学院社会文化科学研究科紀要 43 "
     "(2017)"},
    {"id": "senshi-sosho-89", "name": "戦史叢書 89 『支那事変陸軍作戦〈2〉』 (1976)"},
    {"id": "krzzjn-sfh18", "name": "萨沙「国军的雷神之锤——抗战中的sFH18 150毫米榴弹炮」, 抗日战争纪念网 "
     "(2018)"},
    {"id": "zhwiki-sfh18", "name": "SFH 18榴彈砲 (zh.wikipedia)"},
    {"id": "enwiki-taierzhuang", "name": "Battle of Taierzhuang (en.wikipedia)"},
    {"id": "jawiki-taierzhuang", "name": "台児荘の戦い (ja.wikipedia)"},
    {"id": "zhwiki-taierzhuang-site", "name": "台儿庄大战旧址 (zh.wikipedia)"},
    {"id": "osm", "name": "OpenStreetMap"},
]
JAPANESE_IDS = {id_ for id_, *_ in JAPANESE}


def emit_track(em, entity, track, until):
    source = "reconstruction-japanese" if entity in JAPANESE_IDS else "reconstruction-chinese"
    bound = 3000.0 if entity == "SFH" else 500.0
    times = [w.at_ms for w in track.waypoints]
    for i, at in enumerate(times):
        nxt = times[i + 1] if i + 1 < len(times) else until
        point, _ = track.at(at)
        em.fix(source, entity, at, point, 0.0, bound, nxt, "reconstructed", [],
               reference="ground")
    if until is not None:
        em.gap(source, entity, until, None, "reconstructed", [])


def entities():
    rows = []
    for id_, name, sidc, kind, parent in CHINESE + JAPANESE:
        row = {"id": id_, "sidc": sidc, "camera": False, "name": name, "kind": kind}
        if parent:
            row["parent"] = parent
        rows.append(row)
    rows += [{"id": id_, "sidc": sidc, "camera": False, "name": name, "kind": "site"}
             for id_, sidc, name, *_ in FIXED]
    return rows


def main():
    out = HERE.parent
    tracks, conditions, ends = moves.plan()
    checks.all(tracks, DURATION)
    em = Emitter(OP)
    for entity, track in tracks.items():
        until = L(ends[entity]) + 1 if entity in ends else None
        emit_track(em, entity, track, until)
    for id_, _, _, point, bound, source in FIXED:
        em.fix(source, id_, 0, point, 0.0, bound, None, "reported", [], reference="site")
    for entity, at, condition in conditions:
        em.condition("reconstruction-estimate", entity, L(at), condition, "reconstructed", [])
    graphics.emit(em)
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
        "name": "Battle of Taierzhuang, II: the guns at the canal",
        "duration_ms": DURATION,
        "time_origin": ("30 March 1938 01:30 UTC+8, as the Chinese night attack sets out from "
                        "the station; the Japanese reports are kept on this clock"),
        "time": {
            "range": {"start": 0, "end": DURATION},
            "anchor": {
                "at": 0,
                "unix_ms": unix_ms(),
                "source": ("the 63rd Infantry's and the Type 96 company's reports, whose "
                           "entries are timed on UTC+8"),
                "source_scale": "utc",
                "uncertainty_ms": 600_000,
                "resolution_ms": 60_000,
                "original_calendar": "1938-03-30 UTC+8",
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
                        "taierzhuang_guns.py", MOMENTS)
    facts.write_mission(out, OP, {**MOMENTS, **DISPUTES}, L)
    viewing = sum((c["end_ms"] - c["start_ms"]) / c["speed"] for c in doc["playback_track"])
    print(f"{len(em.events)} events, {len(cues)} shots; viewing {viewing / 1000:.0f} s; "
          f"{checks.summary(tracks)}")


if __name__ == "__main__":
    main()
