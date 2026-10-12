"""The Gulf of Sidra incident's evidence, in the form tools/ledger.py describes: its key moments
and its disputed facts, one module per part. Each source's record is compared with the fetched
text of the cited page; a dispute also holds the replay's estimate. Record times are Tripoli
time (UTC+2); the Biddle tape's times are relative to its start and are given in its own words.
Stanik is read from The Aviation Geek Club's reprint, and Cooper's Libyan Air Wars from the
extracts The Aviation Geek Club and Warrior Maven print.
"""
import ledger

from . import aftermath, engagement, setting

PARTS = (setting, engagement, aftermath,)
MOMENTS = ledger.merge(part.MOMENTS for part in PARTS)
DISPUTES = ledger.merge(part.DISPUTES for part in PARTS)
if set(MOMENTS) & set(DISPUTES):
    raise ValueError(f"evidence keys {sorted(set(MOMENTS) & set(DISPUTES))} are both a moment "
                     f"and a dispute")
