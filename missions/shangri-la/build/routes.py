"""Geographic routes constrained by documented anchors, with no simulated combat claims."""
from geography import LAUNCH, YAKUSHIMA, DURATION, clock
from track import Track, destination, distance_m, offset


def fleet():
    hornet = Track().add(0, destination(LAUNCH, 90, 18_520), 0)
    hornet.add(clock('08:00'), LAUNCH, 0)
    turn = destination(LAUNCH, 310, 22 * 1852 * 81 / 60)
    hornet.add(clock('09:21'), turn, 0)
    hornet.add(clock('09:27'), destination(turn, 90, 25 * 1852 * 0.1), 0)
    hornet.add(DURATION, destination(turn, 90, 25 * 1852 * (13 + 49 / 60)), 0)
    return {'HORNET': hornet, 'ENTERPRISE': hornet.shifted(6000, -3000),
            'NASHVILLE': hornet.shifted(-5000, 5000)}


def flight(crew, carrier):
    launch, attack, finish = map(clock, (crew.launch, crew.attack, crew.finish))
    start, _ = carrier.at(launch)
    track = Track().add(launch, start, 20)
    track.add(launch + 60_000, destination(start, 280, 3500), 100)
    if crew.number == 1:
        track.add(clock('13:00'), (140.666667, 36.333333), 61)
    elif crew.number in (14, 15, 16):
        track.add(clock('13:50'), (140.4, 34.8), 100)
    else:
        coast_time = attack - (10 if crew.number in (4, 11) else 20) * 60_000
        point = (140.6, 35.8) if crew.number != 4 else (140.6, 34.9)
        track.add(coast_time, point, 100)
    # A district-scale pass, not a precision bomb trajectory. Heights are AGL, as the schema requires.
    track.add(attack - 120_000, offset(crew.target, 6500, 1000), 450)
    track.add(attack, crew.target, 400 if crew.number != 4 else 23)
    track.add(attack + 120_000, offset(crew.target, -6500, -1000), 100)
    if crew.number == 8:
        track.add(clock('16:00'), (137.0, 38.0), 1500)
        track.add(finish - 60_000, offset(crew.endpoint, 4000, -2000), 300)
        track.add(finish, crew.endpoint, 0)
    else:
        yak_time = clock('17:00') if crew.number == 1 else max(clock('17:20'), attack + 150 * 60_000)
        track.add(yak_time, offset(YAKUSHIMA, crew.number * 1500, crew.number * 1000), 150)
        coast = (122.333333, 29.666667) if crew.number == 1 else (122.0, crew.endpoint[1])
        inland_ms = max(60_000, round(distance_m(coast, crew.endpoint) / 85 * 1000))
        coastal_time = clock('20:10') if crew.number == 1 else finish - inland_ms
        track.add(coastal_time, coast, 180)
        terminal_alt = 2438 if crew.outcome == 'bailout' else 0
        track.add(finish, crew.endpoint, terminal_alt)
    return track


def build(crews):
    tracks = fleet()
    for crew in crews:
        tracks[crew.id] = flight(crew, tracks['HORNET'])
    return tracks
