#!/usr/bin/env python3
"""Generate Shangri-La, its evidence tables, stable facts and content manifest."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[2] / 'tools'))
import checks
import content
import facts
import ledger
import routes
import story
from crews import CREWS
from evidence import MOMENTS, DISPUTES
from evidence.sources import SOURCES, NAMES
from geography import ANCHOR, DURATION, JAPAN, OP, SHIP, SITES, clock
from track import Emitter


def entities():
    aircraft = [{'id': c.id, 'name': f'{c.number:02d} {c.pilot.split()[-1]} · {c.serial}',
                 'sidc': 'SFAPMFB--------', 'kind': 'B-25B', 'camera': False} for c in CREWS]
    ships = [{'id': id_, 'name': name, 'sidc': sidc, 'kind': kind, 'camera': False}
             for id_, name, sidc, kind in [
                 ('HORNET', 'USS Hornet (CV-8)', 'SFSPCLCV-------', 'aircraft carrier'),
                 ('ENTERPRISE', 'USS Enterprise (CV-6)', 'SFSPCLCV-------', 'aircraft carrier'),
                 ('NASHVILLE', 'USS Nashville (CL-43)', 'SFSPCLCC-------', 'cruiser')]]
    places = [{'id': key, 'name': key.title(), 'sidc': 'SUGP-----------',
               'kind': 'geographic reference', 'camera': False} for key in SITES]
    return aircraft + ships + places


def emit_tracks(em, tracks):
    for entity, track in tracks.items():
        crew = next((c for c in CREWS if c.id == entity), None)
        times = sorted({w.at_ms for w in track.waypoints} | set(range(track.start, track.end, 300_000)))
        for i, at in enumerate(times):
            end = times[i + 1] if i + 1 < len(times) else (DURATION + 1 if crew is None or crew.number == 8 else at + 1)
            point, alt = track.at(at)
            bound = 40_000 if crew is None else (80_000 if at >= clock('19:00') else 40_000)
            em.fix('reconstruction', entity, at, point, alt, bound, end, 'reconstructed', [],
                   reference='ship' if crew is None else 'aircraft')
        if crew and crew.number != 8:
            em.gap('reconstruction', entity, track.end + 1, None, 'reconstructed', [])
    for entity, point in SITES.items():
        em.fix('reconstruction', entity, 0, point, 0, 15_000, None, 'reconstructed', [], reference='site')


def write_readme(out):
    ledger.write_readme(out / 'README.md', DISPUTES, NAMES, 'shangri_la.py', MOMENTS)
    text = (out / 'README.md').read_text()
    rows = ['| No. | Aircraft | Pilot | Launch (ship) | Attack / release | End of flight |',
            '| --- | --- | --- | --- | --- | --- |']
    rows += [f'| {c.number} | {c.serial} | {c.pilot} | {c.launch} | {c.objective} | {c.outcome} |' for c in CREWS]
    shots = ['| Ship time | Intent | Entities promised |', '| --- | --- | --- |']
    shots += [f'| {a}–{b} | {intent} | {", ".join(shows)} |'
              for a, b, _, _, _, _, _, intent, shows, _, _ in story.SHOTS]
    for marker, body in [('crew table', rows), ('camera table', shots),
                         ('sources', [f'- {NAMES[key]}' for key, _, _ in SOURCES])]:
        start, end = f'<!-- {marker} -->', f'<!-- end {marker} -->'
        head, rest = text.split(start)
        _, tail = rest.split(end)
        text = head + start + '\n' + '\n'.join(body) + '\n' + end + tail
    (out / 'README.md').write_text(text)


def main():
    out = HERE.parent
    tracks = routes.build(CREWS)
    ledger.check(DISPUTES, clock)
    ledger.check_moments(MOMENTS, clock)
    checks.validate(CREWS, tracks, MOMENTS, DISPUTES)
    em = Emitter(OP)
    emit_tracks(em, tracks)
    story.annotate(em)
    em.write(out / 'events.jsonl')
    sources = [{'id': key, 'name': name, 'zone': SHIP} for key, name, _ in SOURCES]
    sources.append({'id': 'reconstruction', 'name': 'Approximate routes and regional anchors; see mission method',
                    'motion': 'great_circle', 'max_gap_ms': DURATION, 'zone': SHIP})
    operation = {'format': 'sokoly-operation', 'version': 4, 'id': OP, 'name': 'Shangri-La',
                 'duration_ms': DURATION,
                 'time_origin': '18 April 1942, 06:30 Japan / 07:30 ship time (UTC+10). All tracks reconstructed.',
                 'time': {'range': {'start': 0, 'end': DURATION}, 'zone': JAPAN,
                          'anchor': {'at': 0, 'unix_ms': ANCHOR, 'source': 'Enterprise action report: zone minus ten',
                                     'source_scale': 'utc', 'uncertainty_ms': 300_000, 'resolution_ms': 60_000,
                                     'original_calendar': '1942-04-18 07:30 naval zone minus ten (UTC+10)'}},
                 'captured_availability': False, 'sources': sources, 'entities': entities(), 'media_archive': None}
    (out / 'operation.json').write_text(json.dumps(operation, indent=2, ensure_ascii=False) + '\n')
    presentation = story.document()
    (out / 'presentations/default.json').write_text(json.dumps(presentation, indent=2, ensure_ascii=False) + '\n')
    write_readme(out)
    facts.write_mission(out, OP, {**MOMENTS, **DISPUTES}, clock)
    content.write(out)
    viewing = sum((c['end_ms'] - c['start_ms']) / c['speed'] / 1000 for c in presentation['playback_track'])
    print(f'Shangri-La: {len(em.events)} events, {len(CREWS)} aircraft, {len(MOMENTS) + len(DISPUTES)} facts, '
          f'{len(story.SHOTS)} shots, {viewing:.1f} viewing seconds')


if __name__ == '__main__':
    main()
