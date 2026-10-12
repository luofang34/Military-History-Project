"""Operation Chastise's evidence, in the form tools/ledger.py describes: its key moments and its
disputed facts, one module per part of the night. Each source's record is compared with the
ORB transcript, Enemy Coast Ahead, Hinks et al. and the cited web pages; a dispute also holds
the replay's estimate. The flight plans read the estimates from here, so revising one is a
one-line change and a rebuild.
"""
import ledger

from . import eder, home, mohne, outbound, reserve, sorpe

PARTS = (outbound, mohne, sorpe, eder, reserve, home)
MOMENTS = ledger.merge(part.MOMENTS for part in PARTS)
DISPUTES = ledger.merge(part.DISPUTES for part in PARTS)
if set(MOMENTS) & set(DISPUTES):
    raise ValueError(f"evidence keys {sorted(set(MOMENTS) & set(DISPUTES))} are both a moment "
                     f"and a dispute")


def time_of(key):
    """The estimate's clock time for a dispute that sets a time."""
    return ledger.time_of(DISPUTES, key)
