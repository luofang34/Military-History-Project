"""Behavioral guardrails for identity, chronology, plausible flight and terminal outcomes."""
from geography import ANCHOR, DURATION, clock
from track import distance_m


def validate(crews, tracks, moments, disputes):
    if len(crews) != 16 or len({c.serial for c in crews}) != 16:
        raise ValueError('The raid requires sixteen distinct B-25s')
    if [c.number for c in crews] != list(range(1, 17)):
        raise ValueError('Aircraft must remain in documented take-off order')
    if sum(c.survivors for c in crews) != 77 or sum(c.captured for c in crews) != 8:
        raise ValueError('Reconcile 80 airmen: 3 flight deaths, 8 Japanese prisoners, 5 Soviet internees')
    if sum(c.outcome == 'internment' for c in crews) != 1:
        raise ValueError('Only York’s aircraft landed in the USSR')
    if [clock(c.launch) for c in crews] != sorted(clock(c.launch) for c in crews):
        raise ValueError('Launch order must advance')
    for crew in crews:
        path = tracks[crew.id]
        if path.start != clock(crew.launch) or path.end != clock(crew.finish):
            raise ValueError(f'{crew.id}: route endpoints disagree with evidence anchors')
        if not path.start < clock(crew.attack) < path.end <= DURATION:
            raise ValueError(f'{crew.id}: impossible chronology')
        for a, b in zip(path.waypoints, path.waypoints[1:]):
            speed = distance_m(a.point, b.point) / ((b.at_ms - a.at_ms) / 1000)
            if not 30 <= speed <= 150:
                raise ValueError(f'{crew.id}: implausible segment speed {speed:.1f} m/s')
        if distance_m(path.at(clock(crew.attack))[0], crew.target) > 1:
            raise ValueError(f'{crew.id}: attack anchor missed')
        prefix = crew.pilot.split()[-1].lower()
        for event in ('launch', 'attack', 'bailout' if crew.number in (1, 13, 14) else 'recovery'):
            key = 'last-launch' if crew.number == 16 and event == 'launch' else f'{prefix}-{event}'
            if key not in moments and key not in disputes:
                raise ValueError(f'{crew.id}: missing permanent evidence key for {event}')
    if ANCHOR + clock('08:20') != -874374000000:
        raise ValueError('08:20 ship must be 1942-04-17 22:20 UTC / 18 April 07:20 Japan')
