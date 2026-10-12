#!/usr/bin/env python3
"""The fact layer: every mission's sourced facts under ids that never change, filed by when and
where they happened, so a link to a fact outlives every regeneration of the views that show it.

A fact is a key moment or a dispute of a mission's build/evidence/: what each source records,
and for a dispute the reading the replay adopts. Its key, `<mission>/<evidence key>`, is written
once and never carries the
adopted time, which a later reading may revise; its id is the UUIDv5 of the key under NAMESPACE.
A fact that must be renamed or merged keeps its old id in facts/aliases.json, old id to new.
facts/published.json lists every id the layer has ever held; building the layer only adds to
it, and the check fails while a listed id is neither a fact nor an alias of one, so a renamed
key cannot silently break the links already shared.

Each mission generator writes its facts to missions/<id>/facts.jsonl and rebuilds the layer:

    facts/<yyyy>/<mm>/<dd>/<tile>.jsonl   each fact, by the UTC day of its adopted time and the
                                          z4 map tile of its entity then ("global" without one)
    facts/index/<hh>.json                 id -> where it is filed and where a view shows it,
                                          sharded by the id's first two hex digits

A file over BIN_BYTES fails the check, so a denser layer splits its days by hour before it is
too large to fetch. history.sokoly.app/f/?id=<id> resolves a link through the index: it opens
the fact's view LEAD_S before the fact, or, for a fact with no time of its own, when the view
shows it, or else the view's page.

    python3 tools/facts.py
"""
import datetime as dt
import json
import math
import sys
import uuid
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
LAYER = REPO / "facts"
# The ids' namespace: as permanent as the ids themselves, which verify.py pins.
NAMESPACE = uuid.UUID("4049086a-ec06-42e4-8b6d-96836ee28e9f")
TILE_ZOOM = 4  # 16 x 16 tiles, about 2,500 km across at mid latitudes
BIN_BYTES = 4_000_000
LEAD_S = 5.0  # seconds of operation time a link opens before its fact
SHARD = 2  # hex digits of the id that name its index shard
NEAR_MS = 300_000  # how close a moment's entity must have an event in its view


def fact_id(key):
    return str(uuid.uuid5(NAMESPACE, key))


def mission_facts(mission, entries, clock):
    """The facts of `mission`'s moments and disputes, with operation times from `clock`."""
    def ms(at):
        return None if at is None else clock(at)
    return [{
        "key": f"{mission}/{key}",
        "kind": "dispute" if hasattr(d, "estimate") else "moment",
        "entity": d.entity,
        "at_ms": ms(d.at),
        "shown_ms": ms(getattr(d, "shown", None)),
        "title": d.title,
        "reading": getattr(d, "estimate", None),
        "basis": getattr(d, "basis", None),
        "records": [{"source": r.source, "says": r.says, "at": r.at, "latest": r.latest,
                     "quote": r.quote, "label": r.label, "checked": r.checked}
                    for r in d.records],
    } for key, d in entries.items()]


def write_mission(out, mission, entries, clock):
    """Writes the facts of `mission`'s moments and disputes beside its package in `out`, then
    rebuilds the layer."""
    lines = [json.dumps(f, ensure_ascii=False) for f in mission_facts(mission, entries, clock)]
    (out / "facts.jsonl").write_text("\n".join(lines) + "\n")
    write(build())


def tile(lon, lat):
    n = 2 ** TILE_ZOOM
    lat = max(-85.0511, min(85.0511, lat))
    x = int((lon + 180) / 360 * n) % n
    y = int((1 - math.asinh(math.tan(math.radians(lat))) / math.pi) / 2 * n)
    return f"z{TILE_ZOOM}-{x}-{min(n - 1, y)}"


def located(events, entity, at_ms):
    """Where `entity` was at `at_ms`: its last fix by then, else its first."""
    fixes = sorted((e["observed_ms"], e["payload"]["data"]["point"]) for e in events
                   if e["entity"] == entity and e["payload"]["kind"] == "position"
                   and (e["payload"]["data"] or {}).get("point"))
    if not fixes:
        return None
    before = [p for t, p in fixes if at_ms is None or t <= at_ms]
    return (before or [fixes[0][1]])[-1]


def view_facts(mission):
    """`mission`'s facts, each with its id, UTC time, file and the view's place for it."""
    path = mission / "facts.jsonl"
    if not path.exists():
        return []
    op = json.loads((mission / "operation.json").read_text())
    anchor = op["time"]["anchor"]
    events = [json.loads(line) for line in (mission / "events.jsonl").read_text().splitlines()]
    out = []
    for f in (json.loads(line) for line in path.read_text().splitlines() if line):
        at = f["at_ms"] if f["at_ms"] is not None else f["shown_ms"]
        when = None if at is None else anchor["unix_ms"] + at - anchor["at"]
        point = located(events, f["entity"], at) if f["entity"] else None
        out.append({**f, "id": fact_id(f["key"]), "utc_ms": when,
                    "bin": bin_path(when, point), "view": op["id"],
                    "view_s": None if at is None else at / 1000})
    return out


def bin_path(utc_ms, point):
    """Where a fact is filed: its UTC day and map tile, relative to the layer."""
    place = tile(point["lon"], point["lat"]) if point else "global"
    if utc_ms is None:
        return f"undated/{place}.jsonl"
    day = dt.datetime.fromtimestamp(utc_ms / 1000, dt.timezone.utc)
    return f"{day:%Y/%m/%d}/{place}.jsonl"


def aliases():
    path = LAYER / "aliases.json"
    return json.loads(path.read_text()) if path.exists() else {}


def published():
    path = LAYER / "published.json"
    return json.loads(path.read_text()) if path.exists() else []


def every_fact(root=REPO):
    return [f for m in sorted((root / "missions").iterdir()) if m.is_dir()
            for f in view_facts(m)]


def build(root=REPO):
    """{relative path: text} of the whole layer, from every mission's facts."""
    facts = every_fact(root)
    seen = {}
    for f in facts:
        if f["id"] in seen:
            raise ValueError(f"fact {f['key']} has the id of {seen[f['id']]}")
        seen[f["id"]] = f["key"]
    files, index = {}, {}
    for f in sorted(facts, key=lambda f: (f["utc_ms"] is None, f["utc_ms"] or 0, f["key"])):
        record = {k: v for k, v in f.items() if k not in ("bin", "at_ms", "shown_ms")}
        files.setdefault(f["bin"], []).append(json.dumps(record, ensure_ascii=False))
        index.setdefault(f["id"][:SHARD], {})[f["id"]] = {
            "key": f["key"], "file": f["bin"], "view": f["view"], "view_s": f["view_s"],
            "lead_s": LEAD_S if f["at_ms"] is not None else 0.0}
    for old, new in aliases().items():
        index.setdefault(old[:SHARD], {})[old] = {"alias": new}
    layer = {path: "\n".join(lines) + "\n" for path, lines in files.items()}
    for shard, entries in index.items():
        layer[f"index/{shard}.json"] = json.dumps(dict(sorted(entries.items())), indent=1,
                                                  ensure_ascii=False) + "\n"
    return layer


KEPT = ("aliases.json", "published.json")  # written by hand, or only ever added to


def write(layer, root=REPO):
    """Replaces the layer's built files with `layer`, keeping its aliases, and adds the ids
    it holds to the published ones."""
    ids = sorted(set(published()) | {f["id"] for f in every_fact(root)})
    for path in LAYER.rglob("*"):
        if path.is_file() and path.name not in KEPT:
            path.unlink()
    for path in sorted(LAYER.rglob("*"), reverse=True):
        if path.is_dir() and not any(path.iterdir()):
            path.rmdir()
    for rel, text in layer.items():
        (LAYER / rel).parent.mkdir(parents=True, exist_ok=True)
        (LAYER / rel).write_text(text)
    (LAYER / "published.json").write_text(json.dumps(ids, indent=1) + "\n")


def unplayed(mission):
    """Moments of `mission` whose entity the view lacks, or shows nothing of near the moment."""
    path = mission / "facts.jsonl"
    if not path.exists():
        return []
    op = json.loads((mission / "operation.json").read_text())
    known = {e["id"] for e in op["entities"]}
    times = {}
    for line in (mission / "events.jsonl").read_text().splitlines():
        e = json.loads(line)
        times.setdefault(e["entity"], []).append(e["observed_ms"])
    problems = []
    for f in (json.loads(line) for line in path.read_text().splitlines() if line):
        if f.get("kind") != "moment" or f["entity"] is None:
            continue
        if f["entity"] not in known:
            problems.append(f"moment {f['key']} is about {f['entity']}, not in the view")
        elif not any(abs(t - f["at_ms"]) <= NEAR_MS for t in times.get(f["entity"], [])):
            problems.append(f"moment {f['key']}: the view shows nothing of {f['entity']} "
                            f"within {NEAR_MS // 60_000} min of it")
    return problems


def check(root=REPO):
    """Problems with the layer: built files out of date, aliases that do not resolve, or a
    file too large to fetch."""
    problems = [p for m in sorted((root / "missions").iterdir()) if m.is_dir()
                for p in unplayed(m)]
    layer = build(root)
    built = {str(p.relative_to(LAYER)): p.read_text() for p in LAYER.rglob("*")
             if p.is_file() and p.name not in KEPT}
    if built != layer:
        stale = sorted(set(built) ^ set(layer) | {k for k in layer if built.get(k) != layer[k]})
        problems.append(f"facts/ is not what the missions' facts build ({stale[:3]}); run "
                        f"python3 tools/facts.py")
    live = {f["id"] for f in every_fact(root)}
    for unlisted in sorted(live - set(published())):
        problems.append(f"fact {unlisted} is not in facts/published.json; run "
                        f"python3 tools/facts.py")
    for gone in sorted(set(published()) - live - set(aliases())):
        problems.append(f"published fact {gone} is gone; restore its key, or add it to "
                        f"facts/aliases.json with the fact it became")
    for old, new in aliases().items():
        seen = {old}
        while new not in live:
            if new in seen or new not in aliases():
                problems.append(f"alias {old} does not resolve to a fact")
                break
            seen.add(new)
            new = aliases()[new]
        if old in live:
            problems.append(f"alias {old} is also a fact's id")
    for rel, text in layer.items():
        if len(text.encode()) > BIN_BYTES:
            problems.append(f"facts/{rel} holds {len(text.encode())} bytes, over {BIN_BYTES}")
    return problems


if __name__ == "__main__":
    write(build())
    problems = check()
    for problem in problems:
        print(problem, file=sys.stderr)
    sys.exit(1 if problems else 0)
