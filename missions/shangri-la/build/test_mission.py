#!/usr/bin/env python3
"""Regression tests exercise the generated replay and reject materially misleading changes."""
import copy
import json
import sys
import unittest
from dataclasses import replace
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[2] / 'tools'))
import checks
import facts
import routes
import story
from crews import CREWS
from evidence import MOMENTS, DISPUTES
from geography import ANCHOR, DURATION, clock
from shangri_la import emit_tracks
from track import Emitter


class MissionTests(unittest.TestCase):
    def setUp(self):
        self.tracks = routes.build(CREWS)

    def validate(self, crews=None, tracks=None):
        checks.validate(crews or CREWS, tracks or self.tracks, MOMENTS, DISPUTES)

    def test_complete_aircraft_and_outcomes(self):
        self.validate()
        self.assertEqual(64, sum(c.survivors - c.captured for c in CREWS if c.number != 8))
        self.assertEqual([8], [c.number for c in CREWS if c.outcome == 'internment'])
        self.assertEqual(3, sum(c.outcome == 'ditching' for c in CREWS))

    def test_ship_time_is_east_of_utc_and_japan(self):
        utc = datetime.fromtimestamp((ANCHOR + clock('08:20')) / 1000, timezone.utc)
        self.assertEqual('1942-04-17T22:20:00+00:00', utc.isoformat())
        op = json.loads((HERE.parent / 'operation.json').read_text())
        local = (op['time']['anchor']['unix_ms'] + clock('08:20')) / 1000 + op['time']['zone']['seconds']
        self.assertEqual('1942-04-18 07:20', datetime.fromtimestamp(local, timezone.utc).strftime('%Y-%m-%d %H:%M'))

    def test_wrong_identity_and_casualty_total_fail(self):
        for change in (replace(CREWS[0], serial=CREWS[1].serial), replace(CREWS[0], survivors=4)):
            with self.subTest(change=change), self.assertRaises(ValueError):
                self.validate([change] + CREWS[1:])

    def test_impossible_flight_segment_fails(self):
        altered = copy.deepcopy(self.tracks)
        altered['B25-01'].waypoints[1].point = (0, 0)
        with self.assertRaisesRegex(ValueError, 'speed'):
            self.validate(tracks=altered)

    def test_no_aircraft_before_launch_or_after_bailout(self):
        em = Emitter('shangri-la')
        emit_tracks(em, self.tracks)
        for crew in CREWS:
            positions = sorted((e for e in em.events if e['entity'] == crew.id and e['payload']['kind'] == 'position'),
                               key=lambda e: e['observed_ms'])
            with self.subTest(crew=crew.number):
                self.assertEqual(clock(crew.launch), positions[0]['observed_ms'])
                if crew.number == 8:
                    self.assertEqual(DURATION + 1, positions[-1]['valid_until_ms'])
                    self.assertEqual(0, positions[-1]['payload']['data']['agl_m'])
                else:
                    self.assertIsNone(positions[-1]['payload']['data'])
                    self.assertEqual(clock(crew.finish) + 1, positions[-1]['observed_ms'])

    def test_later_campaign_has_no_false_raid_day(self):
        rows = facts.view_facts(HERE.parent)
        row = next(f for f in rows if f['id'] == facts.fact_id('shangri-la/chinese-reprisal-toll'))
        self.assertIsNone(row['utc_ms'])
        self.assertTrue(row['bin'].startswith('undated/'))

    def test_authored_story_covers_whole_day_and_preserves_anchors(self):
        doc = story.document()
        for name in ('camera_track', 'playback_track'):
            cues = doc[name]
            self.assertEqual(0, cues[0]['start_ms'])
            self.assertEqual(DURATION, cues[-1]['end_ms'])
            self.assertTrue(all(a['end_ms'] == b['start_ms'] for a, b in zip(cues, cues[1:])))
        self.assertEqual((140.666667, 36.333333), self.tracks['B25-01'].at(clock('13:00'))[0])
        self.assertEqual((122.333333, 29.666667), self.tracks['B25-01'].at(clock('20:10'))[0])
        self.assertEqual('13:30', MOMENTS['doolittle-attack'].at)
        self.assertEqual('15:20', MOMENTS['hilger-attack'].at)


if __name__ == '__main__':
    unittest.main()
