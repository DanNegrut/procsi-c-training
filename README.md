# PROCSI C Training: two-week summer camp

Materials for a two-week summer camp (Mon Jul 6 to Fri Jul 17, 2026) that introduces
computer-novice undergrads to the command line, git, Python, an AI assistant, Blender,
Onshape, what it means to "simulate" (a sliding block via forward Euler), PyChrono, and
RAG with chrono-rag.

The camp runs hands-off: each morning the instructor briefs the day's topic and a concrete
target, then the teams (freshly drafted each day by 5 captains) work self-directed with
Claude as their tutor. Late each afternoon every team gives a friendly ~10-minute talk on
how far they got and what they learned, closing with a "quote or joke of the day." No
grades, no quizzes. Only the last Friday is the State Street send-off.

## Layout

```
schedule.qmd     # student-facing overview deck (published to Quarto Pub)
theme.scss       # shared UW-Madison Badger-red theme, used by every deck
days/            # the instructor's morning briefing decks, one per working day
  _brief-template.qmd
  day-02-command-line.qmd ... day-09-rag.qmd
starters/        # tiered starter material handed to teams (days 6 to 8)
notes/           # source notes (brainstorming, day-by-day scratch)
_quarto.yml      # minimal project so one render builds everything
```

## Render and publish (Windows)

Quarto is installed but not on PATH, so prepend its bin directory for the session:

```powershell
$env:Path = "C:\Program Files\Quarto\bin;" + $env:Path
quarto render                              # builds schedule + all day decks
quarto preview schedule.qmd                # live preview while editing
quarto publish quarto-pub schedule.qmd     # publish the schedule (first run is interactive)
```

The first `quarto publish` creates `_publish.yml`, which records the Quarto Pub URL so
later publishes re-target the same link. Built `*.html` output is gitignored.
