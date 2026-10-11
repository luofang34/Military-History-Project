"""The reconstruction under construction: tracks, the evidence behind each stretch of them,
the mines, reported conditions, and the anchors the build checks hold the tracks to."""
from dataclasses import dataclass, field

from manoeuvre import upkeep
from track import Track


@dataclass
class Release:
    code: str
    target: str
    point: tuple
    aim: tuple
    at_ms: int
    spun: bool
    late: bool


@dataclass
class Plan:
    tracks: dict = field(default_factory=dict)
    phases: dict = field(default_factory=dict)
    mines: dict = field(default_factory=dict)
    mine_owners: dict = field(default_factory=dict)
    releases: list = field(default_factory=list)
    conditions: list = field(default_factory=list)
    landed: dict = field(default_factory=dict)
    lost: dict = field(default_factory=dict)
    flood: Track = None

    def phase(self, code, at_ms, source, bound_m):
        """From `at_ms` on, `code`'s fixes rest on `source` with horizontal bound `bound_m`."""
        self.phases.setdefault(code, []).append((int(at_ms), source, bound_m))

    def source_for(self, code, at_ms):
        current = ("reconstruction-route", 5000.0)
        for start, source, bound in sorted(self.phases.get(code, [])):
            if start <= at_ms:
                current = (source, bound)
        return current

    def changes(self, code):
        """Times at which `code`'s evidence source changes."""
        out, current = [], "reconstruction-route"
        for start, source, _ in sorted(self.phases.get(code, [])):
            if source != current:
                out.append(start)
                current = source
        return out

    def condition(self, source, entity, at_ms, condition):
        self.conditions.append((source, entity, int(at_ms), condition))

    def drop(self, code, target, release, aim, at_ms, bounces, end_m=None, spun=True,
             late=False):
        """Records a release and builds its mine's track."""
        mine = f"UPKEEP {code}"
        self.releases.append(Release(code, target, release, aim, at_ms, spun, late))
        self.mines[mine] = upkeep(release, aim, at_ms, bounces, end_m=end_m, spun=spun)
        self.mine_owners[mine] = code
        return self.mines[mine]
