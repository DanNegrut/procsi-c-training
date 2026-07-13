# ProCSI C Training: two-week summer camp

Materials for a two-week summer camp (Mon Jul 13 to Fri Jul 24, 2026) that introduces
computer-novice undergrads to the command line, Python, an AI assistant, Blender,
Onshape, what it means to "simulate" (a sliding brick via forward Euler), PyChrono, and RAG with chrono-rag.

The camp runs hands-off: each morning the instructor briefs the day's topic and a concrete
target, then the teams (freshly drafted each day by 5 captains) work self-directed with
Claude as their tutor. Late each afternoon every team gives a friendly ~10-minute talk on
how far they got and what they learned, opening or closing with a "quote of the day." No
grades, no quizzes. Only the last Friday is the State Street send-off.

## Layout

```
schedule.qmd     # student-facing overview deck (published to Posit Connect Cloud)
theme.scss       # shared UW-Madison Badger-red theme, used by every deck
days/            # the instructor's morning briefing decks, one per working day
  _brief-template.qmd
  day-02-command-line.qmd ... day-09-rag.qmd
starters/        # tiered starter material handed to teams (days 6 to 8)
notes/           # source notes (brainstorming)
_quarto.yml      # minimal project so one render builds everything
```

## Render and publish (Windows)

```powershell
quarto render                              # builds schedule + all day decks
quarto preview schedule.qmd                # live preview while editing
quarto publish posit-connect-cloud schedule.qmd   # publish the schedule
```

Each `_publish.yml` (repo root for the schedule, `days/` for the briefs) records the
Posit Connect Cloud content ids, so every publish updates the same links. The
`danPublishQuarto` bash helper (in `~/.bashrc`) wraps this: run `danPublishQuarto all`
at the repo root to republish everything non-interactively.
Note: Quarto Pub is deprecated and closed to new accounts; Posit Connect Cloud is its
successor. Built `*.html` output is gitignored.

## Published decks (public share links)

The owner-dashboard URLs (connect.posit.cloud/dan-negrut/...) prompt visitors to log
in; give participants these share links instead:

| Deck | Share link |
|------|-----------|
| Schedule | <https://019f3df6-2e06-666d-2df7-384391ce794d.share.connect.posit.cloud/> |
| Day 2, command line | <https://019f5d3f-765a-7cdd-4f3d-2e89be3fec19.share.connect.posit.cloud/> |
| Day 3, Python and conda | <https://019f5d3f-c1f2-e076-e6a3-0d22d7731181.share.connect.posit.cloud/> |
| Day 4, Blender | <https://019f5d40-0b22-46b4-b2e9-c2bc67ed24d0.share.connect.posit.cloud/> |
| Day 5, Onshape to Blender | <https://019f5d40-77c3-ffa1-9a4b-47417f4c6e41.share.connect.posit.cloud/> |
| Day 6, sliding brick | <https://019f5d40-aa29-ba42-338a-7c58402d51d3.share.connect.posit.cloud/> |
| Day 7, brick movie | <https://019f5d40-e9b6-e707-c6f8-7eab621ff2ae.share.connect.posit.cloud/> |
| Day 8, PyChrono | <https://019f5d41-2cdf-51b7-4a6e-73e875e10ed4.share.connect.posit.cloud/> |
| Day 9, RAG | <https://019f5d41-6eaf-3b09-4076-8ab7c8d84395.share.connect.posit.cloud/> |
