#!/usr/bin/env python3
"""Builds the Battle of Taierzhuang, part I: the defence and fall of Tengxian, 14–18 March 1938.

Run from anywhere; writes this mission's operation.json and events.jsonl beside build/, and
the story in presentations/default.json. Times and places are sourced; the moves between them
are reconstructions whose `bound_m` states the horizontal uncertainty. The build fails if a
unit outpaces the marches of 1938, a battery leaves the place its range fan is drawn from, or an
estimate in build/evidence/ falls outside its records without saying why.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[2] / "tools"))
import checks  # noqa: E402
import facts  # noqa: E402
import graphics  # noqa: E402
import ledger  # noqa: E402
import moves  # noqa: E402
import shots  # noqa: E402
import story  # noqa: E402
from evidence import DISPUTES, MOMENTS  # noqa: E402
from sites import (CHINESE, CST_S, DURATION, FIXED, JAPANESE, OP, L, unix_ms)  # noqa: E402
from track import Emitter  # noqa: E402

CLOCK = {"kind": "fixed", "seconds": CST_S,
         "source": "China's coastal standard time, UTC+8; the Japanese 10th Infantry's report "
                   "is read on it (build/evidence/, japanese-clock)"}
RECONSTRUCTED = {"motion": "great_circle", "max_gap_ms": DURATION, "zone": CLOCK}
SOURCES = [
    {"id": "reconstruction-chinese", "name": "Chinese units' moves, reconstructed",
     **RECONSTRUCTED},
    {"id": "reconstruction-japanese", "name": "Japanese units' moves, reconstructed",
     **RECONSTRUCTED},
    {"id": "reconstruction-guns", "name": "Japanese batteries' range fans, reconstructed",
     "zone": CLOCK},
    {"id": "reconstruction-railway", "name": "The Tianjin–Pukou railway of 1938",
     "zone": CLOCK},
    {"id": "reconstruction-estimate",
     "name": "Replay estimates where sources disagree (build/evidence/)", "zone": CLOCK},
    {"id": "jacar-10i-report-11", "name": "歩兵第十聯隊 滕縣附近戦闘詳報 第十一號 (JACAR C11111170200)",
     "zone": CLOCK},
    {"id": "jacar-seya-orders", "name": "瀬谷支隊命令, 別紙 (JACAR C11111170300)", "zone": CLOCK},
    {"id": "jacar-10i-casualties", "name": "歩兵第十聯隊死傷表, 3月15日–18日 (JACAR C11111170700)"},
    {"id": "jiang-2015", "name": "姜克實「日本軍の史料から見る滕県作戦の実記録」, 文化共生学研究 14 (2015)"},
    {"id": "jiang-withdrawal", "name": "姜克實「坂本、瀬谷支隊の台児庄撤退の経緯 ─1938年4月」, "
     "岡山大学文学部紀要 64"},
    {"id": "senshi-sosho-89", "name": "戦史叢書 89 『支那事変陸軍作戦〈2〉』 (1976)"},
    {"id": "krzzjn-jiehe", "name": "「滕县作战之界河附近的战斗 3月14-15日」, 抗日战争纪念网 (2018)"},
    {"id": "krzzjn-sfh18", "name": "萨沙「国军的雷神之锤——抗战中的sFH18 150毫米榴弹炮」, 抗日战争纪念网 "
     "(2018)"},
    {"id": "zhwiki-tengxian", "name": "滕县保卫战 (zh.wikipedia)"},
    {"id": "zhwiki-wang-mingzhang", "name": "王銘章 (zh.wikipedia)"},
    {"id": "zhwiki-sfh18", "name": "SFH 18榴彈砲 (zh.wikipedia)"},
    {"id": "tengxian-gazetteer", "name": "《滕县志》 (中华书局, 1990)"},
    {"id": "xuecheng-gazetteer", "name": "《薛城区志》"},
    {"id": "rmzxw-2020", "name": "郑学富, 人民政协网 (2020)"},
    {"id": "rmzxw-2025", "name": "蔡永飞「滕县保卫战中的张宣武」, 人民政协网 (2025)"},
    {"id": "qq-yang-jintao", "name": "杨津涛「中、日战报为何差距四十倍？」, 腾讯 (2019)"},
    {"id": "nationalist-decree-1938", "name": "國民政府 褒揚令, 6 April 1938"},
    {"id": "osm", "name": "OpenStreetMap"},
]
JAPANESE_IDS = {id_ for id_, *_ in JAPANESE}


def evidence_for(entity, at):
    """(source id, horizontal bound in metres) for a reconstructed fix: within 2 km on the march,
    within 100 m once the fighting is at the walls."""
    source = "reconstruction-japanese" if entity in JAPANESE_IDS else "reconstruction-chinese"
    at_walls = L("16 11:00") <= at and entity not in ("63 REGT", "ARMOUR", "731 REGT",
                                                      "125 DIV", "379 BDE", "381 BDE")
    return source, 100.0 if at_walls else 2000.0


def emit_track(em, entity, track, until):
    times = [w.at_ms for w in track.waypoints]
    for i, at in enumerate(times):
        nxt = times[i + 1] if i + 1 < len(times) else until
        source, bound = evidence_for(entity, at)
        point, _ = track.at(at)
        em.fix(source, entity, at, point, 0.0, bound, nxt, "reconstructed", [],
               reference="ground")
    if until is not None:
        em.gap(evidence_for(entity, until)[0], entity, until, None, "reconstructed", [])


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
    tracks, conditions, escaped = moves.plan()
    checks.all(tracks, DURATION)
    em = Emitter(OP)
    for entity, track in tracks.items():
        until = L(escaped[entity]) + 1 if entity in escaped else None
        emit_track(em, entity, track, until)
    for id_, _, _, point, bound, source in FIXED:
        em.fix(source, id_, 0, point, 0.0, bound, None, "reported", [], reference="site")
    for entity, at, condition in conditions:
        em.condition("reconstruction-estimate", entity, L(at), condition, "reconstructed", [])
    graphics.emit(em)
    story.annotations(em)
    undeclared = {e["source"]["id"] for e in em.events} - {s["id"] for s in SOURCES}
    if undeclared:
        raise ValueError(f"events cite undeclared sources: {sorted(undeclared)}")
    em.write(out / "events.jsonl")
    op = {
        "format": "sokoly-operation",
        "version": 4,
        "id": OP,
        "name": "Battle of Taierzhuang, I: Tengxian",
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
    doc = story.document(OP, cues, intents)
    (out / "presentations").mkdir(exist_ok=True)
    (out / "presentations" / "default.json").write_text(
        json.dumps(doc, indent=2, ensure_ascii=False) + "\n")
    ledger.write_readme(out / "README.md", DISPUTES, {s["id"]: s["name"] for s in SOURCES},
                        "taierzhuang.py", MOMENTS)
    facts.write_mission(out, OP, {**MOMENTS, **DISPUTES}, L)
    viewing = sum((c["end_ms"] - c["start_ms"]) / c["speed"] for c in doc["playback_track"])
    print(f"{len(em.events)} events, {len(cues)} shots; viewing {viewing / 1000:.0f} s; "
          f"{checks.summary(tracks)}")


if __name__ == "__main__":
    main()
