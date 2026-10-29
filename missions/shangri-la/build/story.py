"""Audience notes and an authored camera table; all authoring times use the ship clock."""
from geography import DURATION, clock
from pacing import after_viewing, with_beats

# start, end, viewing seconds, camera target, zoom, pitch, move seconds, intent, shows, note, source
SHOTS = [
    ('07:30', '07:38', 18, (146.5, 35.5), 4.5, 0, 0,
     'Establish the carrier force far east of Japan before discovery.', ['HORNET', 'TOKYO'],
     '18 April 1942. Sixteen Army B-25s and eighty men ride aboard Hornet. Their plan: strike Japan, then fly on to Chinese airfields. The screen clock is Japan time; ship reports run one hour ahead.', 'doolittle'),
    ('07:38', '08:00', 18, 'HORNET', 10.0, 25, 3,
     'Close on the ships as a Japanese picket forces the decision to launch.', ['HORNET', 'ENTERPRISE', 'NASHVILLE'],
     'The Japanese picket No. 23 Nittō Maru has seen the force. Nashville opens fire; the warning cannot be recalled. Halsey must protect his carriers. The bombers will leave much farther from Japan than planned.', 'hornet'),
    ('08:00', '08:20', 16, 'HORNET', 11.0, 35, 2,
     'Hold on Hornet while the crews prepare and the carrier turns into wind.', ['HORNET'],
     'The order reaches Hornet at 07:00 Japan time. Lashings come off and crews start their engines. Added fuel tanks and weight reductions give the bombers a chance of reaching China.', 'hornet'),
    ('08:20', '08:21', 10, 'B25-01', 11.5, 25, 0,
     'Follow Doolittle off the deck and into the open Pacific.', ['B25-01', 'HORNET'],
     'Doolittle is away. His own report puts take-off at 08:20 ship time; Hornet records 08:25.', 'doolittle-personal'),
    ('08:21', '09:19', 18, 'HORNET', 8.8, 10, 3,
     'Pull back to the departure stream as the other crews launch separately.', ['HORNET'],
     'The aircraft leave one by one. Each carries five men. They cannot return to land on Hornet; the carrier force will retire east while the bombers continue west.', 'doolittle'),
    ('09:19', '09:27', 10, 'B25-16', 9.2, 20, 0,
     'Show Farrow, the last bomber, clearing the retiring carriers.', ['B25-16', 'HORNET'],
     'Farrow’s crew launches last. All sixteen are airborne. The naval reports place the final take-off one or two minutes later.', 'enterprise'),
    ('09:27', '12:50', 14, 'B25-01', 5.3, 0, 4,
     'Open the scale of the ocean crossing without holding the quiet transit.', ['B25-01'],
     'Hours over the Pacific. Low flying reduces the chance of detection, but navigation and fuel are unforgiving. These paths join reported anchors; they are not recorded flight tracks.', 'doolittle-personal'),
    ('12:50', '13:25', 14, 'B25-01', 8.3, 15, 3,
     'Follow the lead aircraft to landfall north of its intended course.', ['B25-01'],
     'Doolittle reaches the coast north of his intended approach. He turns toward Tokyo from the north. Training aircraft and fighters are visible, but the raid retains much of its surprise.', 'doolittle-personal'),
    ('13:25', '13:32', 18, 'B25-01', 10.3, 25, 2,
     'Tighten on the lead bombing pass over Tokyo.', ['B25-01'],
     'At about 12:30 Japan time, Doolittle drops incendiaries over Tokyo’s industrial districts. The aircraft then returns to low altitude and heads toward the sea.', 'doolittle-personal'),
    ('13:32', '13:39', 14, 'B25-04', 9.8, 20, 0,
     'Cut to Holstrom offshore: a crew unable to complete its attack.', ['B25-04'],
     'Holstrom meets fighters with an inoperative turret. He jettisons his bombs offshore and turns away. The replay places this episode approximately; his attack minute is not established.', 'aaf-summary'),
    ('13:39', '14:05', 20, (139.8, 35.65), 8.6, 0, 0,
     'Re-establish the dispersed attacks around Tokyo, not a massed bomber formation.', ['TOKYO'],
     'Other crews strike factories, oil and power facilities across Tokyo. Bombs also fall among homes. These are reported target districts; smoke seen by crews cannot establish the full damage.', 'aaf-summary'),
    ('14:05', '14:32', 18, (139.95, 35.55), 8.8, 10, 2,
     'Shift southeast to Greening and Bower’s reported industrial targets.', ['YOKOHAMA'],
     'Greening attacks a site he identifies as a refinery east of Tokyo. Bower bombs the Yokohama area. Their intended targets and the places they report hitting are not always the same.', 'aaf-summary'),
    ('14:32', '14:48', 18, 'B25-13', 10.3, 25, 0,
     'Cut to the documented Yokosuka pass and follow McElroy out.', ['B25-13'],
     'McElroy attacks Yokosuka naval yard at about 13:40 Japan time. His crew reports a crane and a ship in the building slips hit. The replay does not turn that report into a confirmed sinking.', 'mcelroy'),
    ('14:48', '15:16', 12, (136.05, 34.9), 7.0, 0, 0,
     'Cut west to the aircraft assigned beyond the Tokyo region.', ['NAGOYA', 'KOBE'],
     'The western aircraft continue toward Nagoya and Kobe. Osaka appeared in planning, but the checked accounts put Hilger and Farrow at Nagoya and Smith at Kobe.', 'aaf-summary'),
    ('15:16', '15:28', 16, 'B25-14', 10.2, 20, 0,
     'Follow Hilger across his Nagoya target area at the reported attack time.', ['B25-14'],
     'Hilger reports four incendiary attacks at 14:20 Japan time: barracks, oil storage, an arsenal and aircraft works. Farrow also attacks Nagoya; his detailed contemporary report is unavailable.', 'hilger-personal'),
    ('15:28', '15:52', 18, 'B25-15', 9.7, 20, 0,
     'Cut to Smith at Kobe, completing the western attacks.', ['B25-15'],
     'Smith attacks Kobe’s waterfront and aircraft industry. The raid kills civilians as well as damaging industrial sites. Its overall military damage is limited; its psychological effect will be much larger.', 'aaf-summary'),
    ('15:52', '17:10', 16, 'B25-01', 6.4, 0, 3,
     'Pull out along the southwest escape route toward the East China Sea.', ['B25-01'],
     'Fifteen bombers are making for China. A helpful tailwind extends their reach. Doolittle’s navigator records passing near Yakushima; the other routes are approximate corridors.', 'doolittle-personal'),
    ('17:10', '19:35', 18, 'B25-08', 6.4, 0, 0,
     'Cut north to York’s separate flight to Soviet territory.', ['B25-08'],
     'York turns toward the Soviet Union because of fuel consumption. He lands near Vladivostok. The USSR is neutral toward Japan: his five-man crew is interned, not immediately sent home.', 'nhhc'),
    ('19:35', '20:50', 18, (121.0, 29.6), 7.0, 0, 0,
     'Return to the Chinese coast as the weather closes in.', ['NINGBO', 'QUZHOU'],
     'Rain, cloud and darkness hide the Chinese coast. Secrecy and the early launch have also disrupted preparations at Chuchow—modern Quzhou. The crews cannot make the planned refuelling landing.', 'aaf-history'),
    ('20:50', '21:25', 20, (120.2, 29.5), 6.8, 0, 2,
     'Show the coastal and inland separation as Lawson, Hoover and Doolittle come down.', ['NINGBO', 'QUZHOU'],
     'Lawson ditches and is badly injured. Hoover makes a forced landing. Doolittle’s crew parachutes into the mountains. Chinese villagers, soldiers and others shelter the survivors and help them escape.', 'doolittle'),
    ('21:25', '22:18', 20, (120.4, 28.7), 7.0, 0, 2,
     'Widen across the recovery region to place the losses in China.', ['QUZHOU', 'NINGBO'],
     'Hallmark ditches off the coast; Dieter and Fitzmaurice drown. Faktor dies after Gray’s bailout. Eight airmen from Hallmark’s and Farrow’s crews will fall into Japanese hands.', 'afmc'),
    ('22:18', '23:01', 20, (118.6, 28.7), 7.3, 0, 0,
     'Resolve the final aircraft losses across Zhejiang and Jiangxi.', ['QUZHOU', 'SHANGRAO'],
     'The remaining China-bound aircraft are abandoned or wrecked. Fifteen aircraft are lost in China; one is impounded in the USSR. Sixty-four airmen evade capture in China, aided by their rescuers.', 'crews'),
    ('23:01', '23:05', 23, (118.8, 28.8), 6.5, 0, 3,
     'Hold the region for the later human consequences, explicitly outside the raid-day clock.', ['QUZHOU'],
     'Aftermath, 1942–45. Japan executes Hallmark, Farrow and Spatz in October 1942; Meder dies in captivity in 1943. Four prisoners survive to liberation. In China, the subsequent Japanese campaign brings massacres and biological warfare; the often-cited 250,000 deaths is an uncertain estimate.', 'nhhc'),
    ('23:05', '23:10', 20, (130.0, 33.0), 4.0, 0, 4,
     'End at regional scale, connecting the secret launch, American morale and the cost in China.', ['TOKYO', 'QUZHOU'],
     'On 21 April, Roosevelt says the bombers came from “our new secret base at Shangri-La!” The name conceals Hornet. The raid lifts American morale and strengthens support for Japan’s Midway operation; it did not originate that plan.', 'fdr'),
]


def pacing():
    base = [(clock(a), clock(b), (clock(b) - clock(a)) / (seconds * 1000))
            for a, b, seconds, *_ in SHOTS]
    # Give the take-off and the two precisely timed passes additional viewing weight.
    beats = [(clock('08:20'), clock('08:21'), 5),
             (clock('13:28'), clock('13:32'), 12),
             (clock('14:38'), clock('14:43'), 14)]
    return with_beats(base, beats)


def document():
    pace = pacing()
    cameras, intents = [], {}
    for a, b, _, target, zoom, pitch, move, intent, shows, _, _ in SHOTS:
        start, end = clock(a), clock(b)
        aim = ({'kind': 'entity', 'value': target} if isinstance(target, str)
               else {'kind': 'point', 'value': {'lon': target[0], 'lat': target[1]}})
        cameras.append({'start_ms': start, 'end_ms': end, 'target': aim, 'zoom': zoom,
                        'pitch': pitch, 'bearing': 0, 'orbit_deg_s': 0,
                        'transition_ms': after_viewing(pace, start, move) - start})
        intents[str(start)] = {'intent': intent, 'shows': shows}
    chapters = [('A one-way mission', '07:30'), ('Launch early', '08:00'),
                ('Across the Pacific', '09:27'), ('Japan under attack', '13:25'),
                ('China or the Soviet Union', '15:52'), ('The human cost', '20:50')]
    return {'format': 'sokoly-presentation', 'version': 1, 'id': 'default',
            'name': 'Shangri-La', 'operation': 'shangri-la',
            'chapters': [{'title': t, 'at_ms': clock(a), 'available_ms': clock(a)} for t, a in chapters],
            'camera_track': cameras,
            'playback_track': [{'start_ms': a, 'end_ms': b, 'speed': s} for a, b, s in pace],
            'extensions': {'shot_intents': intents}}


def annotate(em):
    for a, b, _, _, _, _, _, _, _, note, source in SHOTS:
        em.note(source, None, clock(a), clock(b), note, 'reported', [])
