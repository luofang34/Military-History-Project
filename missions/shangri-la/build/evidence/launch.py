"""Detection and launches: source clocks are retained as ship time (UTC+10)."""
from ledger import Dispute, Moment, Record
from crews import CREWS

MOMENTS = {
    'nashville-opens-fire': Moment('Nashville opens fire on the Japanese picket', 'NASHVILLE', '07:55', (
        Record('hornet', 'Nashville opened fire at 0755; Enterprise aircraft also attacked the vessel.', '07:55'),)),
    'launch-order': Moment('Halsey orders the Army bombers launched', 'HORNET', '08:00', (
        Record('hornet', 'Received the task-force commander’s launch order at 0800.', '08:00'),)),
    'fleet-retirement': Moment('The carrier force turns east', 'HORNET', '09:27', (
        Record('enterprise', 'Force commenced retirement eastward at 0927, 25 knots.', '09:27'),)),
}
DISPUTES = {
    'launch-distance': Dispute('Distances to Japan use different reference points and units', 'HORNET', (
        Record('doolittle', 'Gives the launch as approximately 824 statute miles east of central Tokyo.'),
        Record('enterprise', 'Describes the first launch as approximately 650 miles from Tokyo.')),
        'Use the geographic fixes, not a distance ring',
        'Doolittle’s navigator coordinate is about 1,231 km from the Tokyo district used here. '
        'It does not exactly reproduce either prose distance; coast versus city and nautical versus statute miles matter.',
        shown='08:00'),
    'picket-contact': Dispute('When the picket was sighted', 'HORNET', (
        Record('hornet', 'Patrol craft sighted at 0738, bearing 220°, 20,000 yards.', '07:38'),
        Record('enterprise', 'Patrol vessel sighted at 0744, bearing 221°, 10,000 yards.', '07:44'),
        Record('wikipedia', 'Identifies the sighting vessel as No. 23 Nittō Maru.')),
        '07:38 ship / 06:38 Japan', 'Use Hornet’s first sighting; the ships had different viewpoints.',
        at='07:38'),
    'doolittle-launch': Dispute('Doolittle’s launch time', 'B25-01', (
        Record('doolittle-personal', 'Take off at 8:20 A.M. ship time.', '08:20', quote=True),
        Record('hornet', 'First B-25 launched at 0825.', '08:25'),
        Record('enterprise', 'First bomber launched at 0820.', '08:20')),
        '08:20 ship / 07:20 Japan', 'The pilot and Enterprise agree; retain Hornet’s five-minute difference.',
        at='08:20'),
    'launch-position': Dispute('The offshore launch position', 'HORNET', (
        Record('hornet', '0800 position: 35°26′N, 153°27′E.'),
        Record('doolittle-personal', 'Navigator gives take-off at 35°43′N, 153°25′E.')),
        'Hornet’s 0800 fix, followed by a reconstructed 22-knot turn into wind',
        'The latitude difference is about 31 km; use a 40 km horizontal bound. Neither point is an exact deck trajectory.',
        shown='08:00'),
    'last-launch': Dispute('Farrow leaves last', 'B25-16', (
        Record('doolittle', 'Farrow’s 40-2268 took off at 9:19 a.m. ship time.', '09:19'),
        Record('hornet', 'Last bomber launched at 0920.', '09:20'),
        Record('enterprise', 'Last bomber off at 0921.', '09:21')),
        '09:19 ship / 08:19 Japan', 'Use the individual aircraft account; naval completion reports differ by one or two minutes.',
        at='09:19'),
}
# The compiled aircraft list supplies the coherent order; conflicting individual reports stay visible.
CONFLICTS = {
    2: ('hornet', 'Second plane seven minutes after the first at 0825.', '08:32'),
    10: ('joyce', 'The transcription gives 08:05, explicitly zone minus ten.', '08:05'),
    11: ('greening', 'Time of take-off 0855 Hornet time.', '08:55'),
    12: ('bower', 'Time of take-off 0910.', '09:10'),
    13: ('mcelroy', 'Personal report gives 0900.', '09:00'),
    14: ('hilger', 'Mission report gives 09:13; personal report gives 09:15.', '09:13'),
}
for crew in CREWS[1:-1]:
    key = crew.pilot.split()[-1].lower() + '-launch'
    record = Record('doolittle', f'{crew.serial}: take-off {crew.launch} ship time.', crew.launch)
    if crew.number in CONFLICTS:
        source, says, at = CONFLICTS[crew.number]
        records = (record, Record(source, says, at))
        if crew.number == 14:
            records += (Record('hilger-personal', 'Take-off made at 09:15.', '09:15'),)
        DISPUTES[key] = Dispute(f'{crew.pilot} launches', crew.id, records, crew.launch + ' ship time',
            'Use the compiled aircraft sequence consistently. Individual timings are not silently corrected; '
            'Joyce’s 08:05 would precede the lead aircraft and is unusable as a sequence anchor.', at=crew.launch)
    else:
        MOMENTS[key] = Moment(f'{crew.pilot} launches', crew.id, crew.launch, (record,))
