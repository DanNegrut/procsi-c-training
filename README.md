# PROCSI C Training: two-week summer camp

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

`_publish.yml` records the Posit Connect Cloud content id, so every publish updates the
same content. Two URLs exist: the owner dashboard (connect.posit.cloud/dan-negrut/...,
prompts visitors to log in) and the public share link to give participants:
<https://019f3df6-2e06-666d-2df7-384391ce794d.share.connect.posit.cloud/>.
Note: Quarto Pub is deprecated and closed to new accounts; Posit Connect Cloud is its
successor. Built `*.html` output is gitignored.
