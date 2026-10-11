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

`python3 verify.py` is the gate before every commit. Each mission's line must end
"composition checked"; "composition skipped" means the binary lacks `--frame-report` and the
shots were not checked.

## Adding a mission

1. Create `missions/<id>/` with its generator in `build/`, its README and an `index.html` whose
   front matter sets `permalink: /<id>/` and whose launch link opens the package on
   `history.sokoly.app` with `recorded-path`. Add it to `catalog.json`. Packages must not use
   Git LFS: Pages serves LFS pointers, not content.
2. Evidence. Keep every source's account as recorded in `build/evidence.py`, using
   `tools/ledger.py`; the ledger writes the README's dispute tables. Quote sources verbatim,
   offensive words included, with at most a short critical note. Keep a reconstruction or an
   estimate apart from the records, with its basis. Disputes stay in the code base; the
   replay shows at most a one-line `brief` per dispute.
3. Story. The replay is for a general audience. Briefing notes say what is happening now, in
   a sentence or three, and must be readable in the viewing time they are on screen.
4. Shots. List the camera as a table in which every shot has an intent (what the viewer
   should take from it) and the entities it shows; the generator writes both into the
   presentation's `shot_intents` extension. Pace the story with `tools/pacing.py`, slowing
   only through the moments that matter (`with_beats`), and give moves in seconds of viewing.

## Judging the story without screenshots

    python3 tools/composition.py missions/<id>

prints, from the viewer's own projection of every half second of viewing: viewing seconds per
chapter, and for each shot its intent, length, whether it arrives by cut or move, the change
in zoom and pitch, where its focus sits, whether each entity it promises is in frame, what
moves on screen, the symbols drawn, and the briefing it carries. Read it as an editor would:

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
Passing them does not make the story good. Take a screenshot only for what the report cannot
show: terrain under low-flying symbols (the report flags its lift) or a crowded frame.

## Git

Both repositories are GitButler workspaces: make commits and branches with `but`. Open one PR
per issue. Merge stacked PRs in this repository with
`gh api -X PUT repos/luofang34/Military-History-Project/pulls/<n>/merge-async -f merge_method=rebase`
and poll the returned status.
