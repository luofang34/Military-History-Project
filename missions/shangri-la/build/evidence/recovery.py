"""Losses and recovery; later consequences have no invented raid-day timestamp."""
from ledger import Dispute, Moment, Record
from crews import CREWS

MOMENTS = {
    'mcelroy-bailout': Moment('McElroy’s crew bails out', 'B25-13', '22:45', (
        Record('mcelroy', 'Crew bailed out at 2245; Williams injured his knee.', '22:45'),)),
    'hilger-bailout': Moment('Hilger orders his crew to jump', 'B25-14', '22:20', (
        Record('hilger-personal', 'At 22:20, an estimated position over Chuchow and about 40 gallons remaining; ordered crew out.', '22:20'),)),
}
DISPUTES = {
    'doolittle-bailout': Dispute('Doolittle’s crew abandons its bomber', 'B25-01', (
        Record('doolittle-personal', 'Pilot gives 21:20 ship time.', '21:20'),
        Record('doolittle-personal', 'Navigator gives 21:15–21:20.', '21:15', latest='21:20')),
        '21:20 ship / 20:20 Japan',
        'Use the pilot’s time at the end of the navigator’s five-minute interval; no second-level accuracy is claimed.',
        at='21:20'),
    'hallmark-loss-location': Dispute('Confused early reports of Hallmark’s fate', 'B25-06', (
        Record('doolittle', 'Initial information placed Hallmark near Nanchang/Poyang and explicitly warned it was unreliable.'),
        Record('crews', 'Crew 6 ditched; three captured.'),
        Record('wikipedia', 'Hallmark’s bomber ditched off Wenzhou. Dieter and Fitzmaurice drowned.')),
        'Wenzhou coastal area, 80 km bound',
        'Use the later coastal account; do not map the unconfirmed Poyang report as a crash site.', shown='22:00'),
    'farrow-loss-location': Dispute('Confused early reports of Farrow’s fate', 'B25-16', (
        Record('doolittle', 'Places Farrow near Shipu and warns that accounts of his and Hallmark’s crews may be confused.'),
        Record('crews', 'All five of Farrow’s crew became prisoners.')),
        'Shipu region, 80 km bound', 'This is a recovery region, not a precise bailout or capture coordinate.', shown='23:00'),
    'chinese-airfield-preparations': Dispute('Why the intended landing was not available', None, (
        Record('doolittle-personal', 'Could not raise Chuchow by radio; cloud and darkness prevented a landing.'),
        Record('aaf-history', 'Secrecy restricted Chinese information; fields expected arrivals later, and Chiang resisted using Chuchow.')),
        'Weather, fuel, disrupted timing and incomplete coordination',
        'The immediate crew experience and the official planning history explain different parts of the failure; '
        'do not blame it solely on weather or portray Chinese assistance as absent.', shown='20:10'),
    'chinese-reprisal-toll': Dispute('Deaths in the Zhejiang–Jiangxi campaign', None, (
        Record('scott', 'Estimates a quarter-million deaths; documents massacres, destruction and biological warfare.'),
        Record('nhhc', 'Attributes 250,000 to Chiang Kai-shek and Chennault; says the real total is unknown.')),
        'An estimated 250,000, with the total uncertain',
        'This describes the subsequent 1942 campaign, not deaths on 18 April or a count of people who directly helped airmen. '
        'No raid-day timestamp is assigned.'),
}
for crew in CREWS:
    if crew.number in (1, 13, 14):
        continue
    name = crew.pilot.split()[-1].lower()
    action = 'lands in the Soviet Union' if crew.number == 8 else 'loses the aircraft in China'
    DISPUTES[name + '-recovery'] = Dispute(f'{crew.pilot} {action}', crew.id,
        (Record('crews', f'{crew.serial}: {crew.outcome}; {crew.survivors} survived the flight, '
                         f'{crew.captured} subsequently captured by Japan.'),),
        crew.finish + ' ship time, approximate',
        'Outcome is documented; the terminal minute and regional coordinate are reconstruction. '
        'Bailout symbols disappear rather than drawing an invented crash descent.', at=crew.finish, outside=True)
