"""What the crews attacked, distinct from what their bombs actually destroyed."""
from ledger import Dispute, Moment, Record
from crews import CREWS

MOMENTS = {
    'doolittle-attack': Moment('Doolittle bombs Tokyo', 'B25-01', '13:30', (
        Record('doolittle-personal', 'Dropped first bomb at 1:30 (ship time).', '13:30', quote=True),)),
    'mcelroy-attack': Moment('McElroy attacks Yokosuka naval yard', 'B25-13', '14:40', (
        Record('mcelroy', 'Bombs dropped about 1440; a crane and ship in the slips were reported hit.', '14:40'),)),
    'hilger-attack': Moment('Hilger attacks Nagoya', 'B25-14', '15:20', (
        Record('hilger-personal', 'Attack at 15:20, explicitly zone minus ten; four incendiary targets.', '15:20'),)),
}
DISPUTES = {
    'damage-assessment': Dispute('Reported hits and the raid’s material effect', None, (
        Record('doolittle', 'Initial assessment claimed damage exceeded expectations.'),
        Record('aaf-summary', 'Pilot observations describe explosions and fires, including residential districts.'),
        Record('wikipedia', 'Postwar count: 87 killed, 151 seriously injured and more than 311 lightly injured in Japan.')),
        'Local destruction and civilian deaths; limited overall military damage',
        'Aircrew claims are not a surveyed damage assessment. No destroyed target or confirmed fighter-kill symbols are drawn.',
        shown='15:45'),
    'greening-target': Dispute('What Greening bombed', 'B25-11', (
        Record('greening', 'Reported an oil refinery and storage tanks.'),
        Record('aaf-summary', 'Identifies a reported refinery near Sakura; Yokohama primary not reached.')),
        'A broad district east of Tokyo, with 40 km uncertainty',
        'The identification is a crew report; no exact refinery footprint is asserted. This uncertainty also covers the route to it.',
        shown='14:10'),
    'watson-target': Dispute('Watson’s target identification', 'B25-09', (
        Record('aaf-summary', 'Tokyo Gas and Electric; the same target was also reported as a tank and truck factory.'),),
        'Tokyo industrial district, not an identified building',
        'The summary itself records competing identifications. Use a 40 km bound.', shown='14:00'),
}
for crew in CREWS:
    if crew.number in (1, 13, 14):
        continue
    name = crew.pilot.split()[-1].lower()
    source = 'doolittle' if crew.number in (6, 16) else 'aaf-summary'
    says = crew.objective + '; no precise attack clock adopted from this account.'
    if crew.number == 16:
        source = 'crews'
        says = 'Farrow attacked Nagoya; no contemporary pilot report survives in the checked compilation.'
    DISPUTES[name + '-attack'] = Dispute(
        ('Holstrom jettisons his bombs' if crew.number == 4 else f'{crew.pilot} over the target area'),
        crew.id, (Record(source, says),), crew.attack + ' ship time, approximate',
        'An editorial placement within the raid, constrained by the launch, destination and feasible transit. '
        'The route and minute are reconstructed; this does not establish a bomb impact location.',
        at=crew.attack, outside=True)
