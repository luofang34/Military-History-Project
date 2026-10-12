# Working on the Military History Project

Codex and Claude Code both read this file; keep the instructions here, not in a CLAUDE.md,
which Claude Code would read instead of it.

Each mission under `missions/<id>/` is a replayable operation package (`operation.json`,
`events.jsonl`, `presentations/default.json`) written by its generator in `build/`, with a
README of method, anchors, disputes and sources, and an `index.html` launch page. Shared
helpers are in `tools/`. Never edit a generated file by hand; change the generator and rerun it
(`python3 missions/<id>/build/<generator>.py`).

## The viewer build

The composition checks run the Sokoly viewer headless. Build it from Sokoly-App's `origin/main`
in a detached worktree of its own, not in a checkout another session is working in:

    git -C ../Sokoly-App fetch origin
    # Once; afterwards `git -C ../Sokoly-App-main checkout --detach origin/main` updates it.
    git -C ../Sokoly-App worktree add --detach ../Sokoly-App-main origin/main
    cargo build --release --locked -p sokoly-app --manifest-path ../Sokoly-App-main/Cargo.toml
    export SOKOLY_APP="$(cd ../Sokoly-App-main && pwd)/target/release/sokoly-app"

`tools/composition.py` uses that build unless `$SOKOLY_APP` names another, and refuses one older
than its checkout. `python3 verify.py` is the gate before every commit. Each mission's line
must end "composition checked"; "composition skipped" means the binary lacks `--frame-report`
and the shots were not checked, and "terrain skipped" that it lacks `--terrain-tiles` and the
shots were judged at sea level.

## Adding a mission

1. Create `missions/<id>/` with its generator in `build/`, its README and an `index.html` whose
   front matter sets `permalink: /<id>/` and whose launch link opens the package on
   `history.sokoly.app` with `recorded-path`. Add it to `catalog.json`. Packages must not use
   Git LFS: Pages serves LFS pointers, not content.
2. Evidence. Keep every source's account as recorded in `build/evidence/`, one module per
   part of the story, using `tools/ledger.py`; the ledger writes the README's tables. Record
   each key moment a viewer may want to link to (a take-off, an attack, a loss, a kill) as a
   `Moment`, and each fact the sources disagree on as a `Dispute` with the replay's estimate
   and its basis. Quote sources verbatim, offensive words included, with at most a short
   critical note. Disputes stay in the code base; the replay shows at most a one-line `brief`
   per dispute. A moment's or dispute's key is also its fact's permanent key (see Facts and
   links): name it for what happened, never for its time.
3. Story. The replay is for a general audience. Briefing notes say what is happening now, in
   a sentence or three, and must be readable in the viewing time they are on screen.
4. Shots. List the camera as a table in which every shot has an intent (what the viewer
   should take from it) and the entities it shows; the generator writes both into the
   presentation's `shot_intents` extension. Pace the story with `tools/pacing.py`, slowing
   only through the moments that matter (`with_beats`), and give moves in seconds of viewing.

## Facts and links

Every moment and dispute in a mission's `build/evidence/` is also a fact of the shared layer in `facts/`,
built by `tools/facts.py` when the mission's generator runs. A fact's id is fixed by its key,
`<mission>/<dispute key>`, so `https://history.sokoly.app/f/?id=<id>` keeps opening the moment it
names however the view is regenerated. `facts/published.json` lists every id the layer has
held, and building the layer only adds to it. Never rename a published dispute key: if a fact
must be renamed or merged, add its old id to `facts/aliases.json`, old to new. `verify.py`
fails when `facts/` is stale, when an alias does not resolve, or when a published id is
neither a fact nor an alias of one.

## Judging the story without screenshots

    python3 tools/composition.py missions/<id>

prints, from the viewer's own projection of every half second of viewing: viewing seconds per
chapter, and for each shot its intent, length, whether it arrives by cut or move, the change
in zoom and pitch, where its focus sits, whether each entity it promises is in frame, what
moves on screen, the symbols drawn, the briefing it carries, how far the camera stands above
the ground, and through a photograph's tour how long the photograph shows and how far the
camera jumps when the story takes it back. Read it as an editor would:

- Does each shot do what its intent says, and is that worth the time it takes?
- Two shots in a row with the same subjects and framing are one shot: merge them, or give
  the second a new angle or scale that its intent explains.
- Establish wide, go close for the decisive moment, pull back to resolve. A cut suits a
  parallel action elsewhere; a move suits following the same action.
- Where nothing new happens and no note is being read, play faster. Where the decisive
  moment happens, slow down, and make sure the frame shows it.
- Compare the chapters' viewing seconds: the story's weight should sit on its events.

`verify.py` enforces only the floors: every shot states an intent and keeps its promised
entities in frame (`SHOWN` in `tools/composition.py`), plays at least `MIN_SHOT_S`, arrives
by a cut or a move of at least `MIN_MOVE_S`, and holds no longer than `MAX_HOLD_S`; every note
is readable before it leaves; the focus stays in frame.
Passing them does not make the story good. Close shots stand on the ground the viewer draws
for them: the report fetches the DEM tiles they need into `TERRAIN_CACHE`, outside the
repository, and counts a promised symbol hidden by the ground in front of it as out of frame.
The camera must stay above the ground, and no promised symbol may stand where no DEM is
known. Wide shots are still projected at sea level; there the report flags how far ground
could lift a symbol. Take a screenshot only for what the report cannot show: a crowded frame,
or ground the report could not read.
The report replays the authored cameras, not the viewer's own navigation state: after a change
to how the viewer moves its camera, take screenshots of close shots, starting with `--at` on
one, since the viewer then hands its startup camera to the story without a frame between.
A screenshot taken with `--at` shows the story camera only once the viewer has handed it
back; one whose bar still reads "Recorded path in 1s" is not the story's frame.

## Git

Both repositories are GitButler workspaces: make commits and branches with `but`. Open one PR
per issue. Merge stacked PRs in this repository with
`gh api -X PUT repos/luofang34/Military-History-Project/pulls/<n>/merge-async -f merge_method=rebase`
and poll the returned status. In Sokoly-App, merging a PR with `--delete-branch` closes every PR
stacked on its branch; retarget those onto `main` before the base branch is deleted.
