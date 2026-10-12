"""Operation Vengeance's evidence, in the form tools/ledger.py describes: its key moments and its
disputed facts, one module per part of the morning. Each source's record is compared with the
cited pages and, for the 13th Fighter Command report, with its scanned typescript; a dispute
also holds the replay's estimate. Record times are Henderson Field time (UTC+11); Japanese
records keep Tokyo time (UTC+9) in their own words.
"""
import ledger

from . import departure, hine, interception, route

PARTS = (departure, route, interception, hine,)
MOMENTS = ledger.merge(part.MOMENTS for part in PARTS)
DISPUTES = ledger.merge(part.DISPUTES for part in PARTS)
if set(MOMENTS) & set(DISPUTES):
    raise ValueError(f"evidence keys {sorted(set(MOMENTS) & set(DISPUTES))} are both a moment "
                     f"and a dispute")
