"""The story camera: one shot per beat, contiguous from the start to the end of the record.

Every shot is fitted to its subjects by `framing.Framer`; subjects are Lancasters, mines, the
flood front, fixed sites, or the run-in points that frame an attack.
"""
from framer import Framer
from sites import CRASH, DURATION, FIXED, HAMMERBERG, L, NEHEIM_CAMP, WALDECK
from targets import ENNEPE_START, MOHNE_START, SORPE_START

POINTS = {
    "MÖHNE RUN-IN": MOHNE_START, "SORPE RUN-IN": SORPE_START, "ENNEPE RUN-IN": ENNEPE_START,
    "WALDECK": WALDECK, "HAMMERBERG": HAMMERBERG, "NEHEIM": NEHEIM_CAMP,
    "OSTÖNNEN": CRASH["AJ-M"][0], "CASTRICUM": CRASH["AJ-A"][0], "HALDERN": CRASH["AJ-E"][0],
}


def lifetimes(plan):
    out = {}
    for code, track in plan.tracks.items():
        out[code] = (track.start, track.end if code in plan.lost else DURATION)
    for mine, track in plan.mines.items():
        out[mine] = (track.start, track.end)
    out["MÖHNE FLOOD"] = (plan.flood.start, DURATION)
    return out


def shots(plan):
    fixed = {id_: point for id_, _, _, _, point, _, _ in FIXED}
    fixed.update(POINTS)
    tracks = {**plan.tracks, **plan.mines, "MÖHNE FLOOD": plan.flood}
    f = Framer(tracks, fixed, lifetimes(plan))

    def s(start, end, subjects, follow=None, pitch=0, **kw):
        a = start if isinstance(start, int) else L(start)
        b = end if isinstance(end, int) else L(end)
        return f.shot(a, b, subjects, follow, pitch, **kw)

    s(0, "21:27:30", ["SCAMPTON", "MÖHNE", "EDER", "SORPE"], transition=0)
    s("21:27:30", "21:32", ["SCAMPTON", "AJ-E", "AJ-W", "AJ-K", "AJ-H"], pitch=40,
      transition=4000)
    s("21:32", "21:38", ["AJ-E", "AJ-W", "AJ-K", "AJ-H"], "AJ-E", 20, pad_km=4)
    s("21:38", "21:41", ["SCAMPTON", "AJ-G", "AJ-M", "AJ-P"], pitch=40, pad_km=1.5)
    s("21:41", "21:46", ["AJ-G", "AJ-M", "AJ-P"], "AJ-G", 30, pad_km=2)
    s("21:46", "21:49", ["SCAMPTON", "AJ-A", "AJ-J", "AJ-L"], pitch=40, pad_km=1.5)
    s("21:49", "21:58", ["AJ-A", "AJ-J", "AJ-L"], "AJ-A", 30, pad_km=2)
    s("21:58", "22:02", ["SCAMPTON", "AJ-Z", "AJ-B", "AJ-N", "AJ-T"], pitch=40, pad_km=1.5)
    s("22:02", "22:50", ["AJ-G", "AJ-E", "SCAMPTON"], transition=20_000)
    s("22:50", "23:03", ["AJ-W", "AJ-K", "AJ-H", "AJ-E"], pitch=25, transition=15_000)
    s("23:03", "23:46", ["AJ-G", "AJ-A", "AJ-Z"], "AJ-G", 20, pad_km=10, transition=30_000)
    s("23:46", "23:52", ["AJ-E", "HALDERN"], pitch=40, pad_km=3, transition=10_000)
    s("23:52", "00:12", ["AJ-G", "AJ-A"], "AJ-G", 25, pad_km=8, transition=20_000)
    s("00:12", "00:17", ["AJ-B", "AJ-Z", "AJ-N"], pitch=35, pad_km=2, transition=8000)
    s("00:17", "00:27", ["MÖHNE", "AJ-G", "AJ-M", "AJ-P", "AJ-A", "AJ-J", "AJ-L"], pitch=35,
      transition=15_000)
    s("00:27", "00:31", ["MÖHNE", "MÖHNE RUN-IN"], pitch=50, pad_km=0.8, transition=8000)
    s("00:31", "00:35", ["MÖHNE", "MÖHNE RUN-IN", "OSTÖNNEN"], pitch=45, transition=6000)
    s("00:35", "00:44", ["MÖHNE", "MÖHNE RUN-IN"], pitch=50, pad_km=0.8, transition=6000)
    s("00:44", "00:47", ["SORPE", "SORPE RUN-IN"], pitch=50, pad_km=1.0, transition=4000)
    s("00:47", "00:50", ["MÖHNE", "MÖHNE RUN-IN"], pitch=50, pad_km=0.8, transition=4000)
    s("00:50", "00:56:30", ["MÖHNE", "MÖHNE FLOOD", "NEHEIM"], pitch=40, pad_km=1.0,
      transition=8000)
    s("00:56:30", "01:18", ["AJ-G", "AJ-L", "AJ-Z", "AJ-N", "AJ-A"], "AJ-G", 25, pad_km=4,
      transition=20_000)
    s("01:18", "01:37", ["EDER", "WALDECK", "AJ-L"], pitch=45, pad_km=0.8, transition=15_000)
    s("01:37", "01:47", ["EDER", "WALDECK", "HAMMERBERG"], pitch=50, pad_km=1.2,
      transition=6000)
    s("01:47", "01:54", ["EDER", "WALDECK", "HAMMERBERG"], pitch=50, pad_km=1.2,
      transition=4000)
    s("01:54", "02:24", ["AJ-G", "AJ-A", "AJ-Z", "AJ-N", "AJ-L", "MÖHNE FLOOD"],
      transition=30_000)
    s("02:24", "02:38", ["AJ-C", "AJ-Z", "AJ-O", "AJ-Y", "AJ-F"], pitch=20, transition=20_000)
    s("02:38", "02:56", ["AJ-A"], "AJ-A", 30, pad_km=8, transition=15_000)
    s("02:56", "03:00", ["AJ-A", "CASTRICUM"], pitch=35, pad_km=2, transition=6000)
    s("03:00", "03:08", ["AJ-F", "SORPE", "AJ-Y"], "AJ-F", 20, transition=15_000)
    s("03:08", "03:16", ["SORPE", "SORPE RUN-IN"], pitch=50, pad_km=1.0, transition=8000)
    s("03:16", "03:25", ["AJ-O", "ENNEPE"], "AJ-O", 30, pad_km=2, transition=10_000)
    s("03:25", "03:39", ["ENNEPE", "ENNEPE RUN-IN"], pitch=50, pad_km=1.0, transition=8000)
    s("03:39", "05:25", ["AJ-O", "AJ-F", "AJ-Y", "SCAMPTON"], transition=40_000)
    s("05:25", "06:12", ["AJ-O"], "AJ-O", 25, pad_km=15, transition=30_000)
    s("06:12", DURATION, ["SCAMPTON", "AJ-O"], pitch=40, pad_km=2, transition=10_000)
    return f.shots
