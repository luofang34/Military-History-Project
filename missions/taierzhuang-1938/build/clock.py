"""The operation's clock: China's coastal standard time, UTC+8, from 04:00 on 14 March 1938, when
the Japanese 10th Infantry set out from Tangcun, to the evening of 1 April.

Both sides' records are read on it: the Chinese as written, the Japanese because their reports
say so (「時刻ハ西部標準時トス」) and their sunrise and sunset fit it (the japanese-clock dispute).
"""
import datetime as dt

OP = "taierzhuang-1938"
CST_S = 8 * 3600
LOCAL = dt.timezone(dt.timedelta(seconds=CST_S))
START = dt.datetime(1938, 3, 14, 4, 0, tzinfo=LOCAL)


def L(clock):
    """Operation milliseconds for `DD HH:MM[:SS]` on the UTC+8 clock: a day from the 10th on is
    in March 1938, an earlier one in April."""
    day, hms = clock.split(" ")
    parts = [float(p) for p in hms.split(":")]
    h, m, s = (parts + [0.0])[:3]
    month = 3 if int(day) >= 10 else 4
    t = dt.datetime(1938, month, int(day), int(h), int(m), tzinfo=LOCAL) \
        + dt.timedelta(seconds=s)
    return int(round((t - START).total_seconds() * 1000))


def unix_ms():
    return int(START.timestamp() * 1000)


def clock(ms_):
    """`DD HH:MM:SS` for operation milliseconds, the inverse of L."""
    t = START + dt.timedelta(milliseconds=ms_)
    return f"{t.day} {t:%H:%M:%S}"


DURATION = L("1 19:05")
