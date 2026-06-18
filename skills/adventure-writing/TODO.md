# TODO — Adventure Writing Skill

This is the execution-ready planning queue for the adventure-writing skill
library (references, templates, examples, learnings). Optimized for a strong
planner + cheaper executor workflow.

## Current Focus

- Maintenance and expansion of the adventure-writing skill library
- Canonical owner: `skills/adventure-writing/SKILL.md`

## Scope And Boundaries

- **Owns:** references/ (26 files), templates/ (4 files), examples/ (3 files),
  learnings/ (README + per-adventure files)
- **Does not own:** the adventures themselves (`03-adventures/`),
  corebook content, western-writing skill

## Active Prompt Queue

Start active entries at `Prompt 1`. Add `Prompt 1A`, `Prompt 1B`, etc. only
when a single deliverable needs to be split without hiding partial completion.

<!-- Add new prompts below this line -->

## Decision Log

- 2026-06-18: Reset TODO from completed build phases; skill library is fully
  built (26 references, 4 templates, 3 examples, learnings system). New work
  goes in the Active Prompt Queue above.

## Risks And Blockers

- No active blockers

---

**Notes**:
- The full working rules, prompt granularity guidance, subagent delegation
  rules, and rationale live in `dev/TODO_MANAGEMENT.md` (in the shared defaults
  repo at `c:\git\defaults`).
- When a new reference, template, exemplar, or learnings entry is identified,
  add a prompt above, build the file, wire it into `SKILL.md`, then mark it
  done.
- Run `npx -y markdownlint-cli2 --fix TODO.md` after edits.

