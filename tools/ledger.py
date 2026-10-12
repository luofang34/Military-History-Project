"""The evidence ledger: what each source records, kept apart from the replay's estimate.

A mission's build/evidence/ holds its key moments and its disputes, one module per part of the
story, each with MOMENTS and DISPUTES that `merge` joins. A moment is something that happened
on which the sources agree, to within MOMENT_SPREAD_MS; where they do not, it is a dispute,
whose estimate the replay adopts. Both are facts of the shared layer (tools/facts.py), so the
moments a viewer may want to link to belong here, not only the disputed ones.

A dispute lists each source's record, whose `says` is the
source's exact words where `quote` is set and otherwise paraphrases, and the replay's estimate
with its basis. A record whose content was relayed but could not be compared with the source (a
scanned image, an unavailable page) has `checked` unset and is shown as unchecked. The mission
README's conflicts table is generated from the list, which stays in the code base for future
study and correction; the replay shows viewers only a dispute's `brief`.
"""
from dataclasses import dataclass

MOMENT_SPREAD_MS = 120_000  # how far a moment's records' times may lie from its own


@dataclass(frozen=True)
class Record:
    source: str
    says: str
    at: str = None  # the clock time the record itself gives; None if it gives none
    latest: str = None  # with a range, its end
    quote: bool = False  # `says` is the source's exact words
    label: str = None  # whose words or which part of the source, outside the quotation
    checked: bool = True  # compared with the source itself

    def text(self):
        said = f"“{self.says}”" if self.quote else self.says
        said = f"{self.label}: {said}" if self.label else said
        return said if self.checked else f"Unchecked relay, not compared with the source: {said}"


@dataclass(frozen=True)
class Dispute:
    title: str
    entity: str
    records: tuple
    estimate: str  # what the replay uses
    basis: str
    at: str = None  # the estimate's clock time, when it is a time
    outside: bool = False  # the estimate lies outside the records' times, as `basis` explains
    shown: str = None  # when a dispute that is not about a time is shown
    brief: str = None  # one plain sentence for viewers, where the dispute changes what is shown

    def when(self):
        return self.at or self.shown


@dataclass(frozen=True)
class Moment:
    title: str
    entity: str
    at: str  # the clock time the records agree on
    records: tuple

    def when(self):
        return self.at


def merge(parts):
    """The entries of `parts` (dicts of moments or disputes) in order, each key once."""
    merged = {}
    for part in parts:
        for key, entry in part.items():
            if key in merged:
                raise ValueError(f"evidence key {key} is defined twice")
            merged[key] = entry
    return merged


def check_moments(moments, clock):
    """Every record of a moment that gives a time lies within MOMENT_SPREAD_MS of it."""
    for key, m in moments.items():
        if not m.records:
            raise ValueError(f"moment {key} has no record")
        for r in m.records:
            for t in (r.at, r.latest):
                if t and abs(clock(t) - clock(m.at)) > MOMENT_SPREAD_MS:
                    raise ValueError(f"moment {key} at {m.at}: {r.source} records {t}; a "
                                     f"disagreement is a dispute")


def check(disputes, clock):
    """A timed estimate lies within its records' times, or says why not. `clock` turns a
    record's clock time into operation milliseconds."""
    for key, d in disputes.items():
        if d.at is None:
            continue
        times = [clock(t) for r in d.records for t in (r.at, r.latest) if t]
        inside = bool(times) and min(times) <= clock(d.at) <= max(times)
        if inside == d.outside:
            raise ValueError(f"evidence {key}: estimate {d.at} is "
                             f"{'inside' if inside else 'outside'} its records' times, but "
                             f"outside={d.outside}")


def time_of(disputes, key):
    """The estimate's clock time for a dispute that sets a time."""
    at = disputes[key].at
    if at is None:
        raise KeyError(f"dispute {key} does not estimate a time")
    return at


def emit(em, disputes, clock, estimate_source, shown_ms=120_000):
    """Each dispute's audience note, where it has one, as a reconstructed note under
    `estimate_source`. The replay is for a general audience: the records and the basis stay
    in build/evidence/ and the README's table, not on screen."""
    for d in disputes.values():
        if d.brief:
            at = max(0, clock(d.when()))
            em.note(estimate_source, d.entity, at, at + shown_ms, d.brief, "reconstructed", [])


END = "<!-- end of evidence ledger -->"


def _cell(text):
    return text.replace("|", "\\|")


def table(disputes, names):
    rows = ["| Dispute | Records (source: what it says) | Replay estimate and basis |",
            "| --- | --- | --- |"]
    for key, d in disputes.items():
        records = "<br>".join(f"{names[r.source]}: {r.text()}" for r in d.records)
        rows.append(f"| {_cell(d.title)} (`{key}`) | {_cell(records)} | "
                    f"**{_cell(d.estimate)}**. {_cell(d.basis)} |")
    return "\n".join(rows)


def moment_table(moments, names):
    rows = ["| Moment | Records (source: what it says) | Time |", "| --- | --- | --- |"]
    for key, m in moments.items():
        records = "<br>".join(f"{names[r.source]}: {r.text()}" for r in m.records)
        rows.append(f"| {_cell(m.title)} (`{key}`) | {_cell(records)} | {m.at} |")
    return "\n".join(rows)


def write_readme(path, disputes, names, generator, moments=None):
    """Writes the ledger into the README between its marker comments, so the README's
    conflicts and key moments always show what build/evidence/ holds. `generator` names the
    build script."""
    start = f"<!-- evidence ledger: generated by build/{generator} from build/evidence/ -->"
    text = path.read_text()
    head, rest = text.split("<!-- evidence ledger: generated by", 1)
    _, tail = rest.split(END, 1)
    body = table(disputes, names)
    if moments:
        body += "\n\nKey moments, on which the sources agree:\n\n" + moment_table(moments, names)
    path.write_text(f"{head}{start}\n{body}\n{END}{tail}")
