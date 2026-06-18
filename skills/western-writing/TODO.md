# TODO — Western Writing Skill

This is the execution-ready planning queue for the western-writing skill
library (references, knowledge, examples). Optimized for a strong planner +
cheaper executor workflow.

## Current Focus

- Maintenance and expansion of the western-writing skill library
- Canonical owner: `skills/western-writing/SKILL.md`

## Scope And Boundaries

- **Owns:** references/ (13 files — how to write), knowledge/ (26 files — what
  to write about), examples/ (scenes.md — 27 worked exemplars)
- **Does not own:** corebook prose, adventure text, adventure-writing skill,
  illustration prompts

## Active Prompt Queue

Start active entries at `Prompt 1`. Add `Prompt 1A`, `Prompt 1B`, etc. only
when a single deliverable needs to be split without hiding partial completion.

<!-- Add new prompts below this line -->

## Decision Log

- 2026-06-18: Reset TODO from completed build phases; skill library is fully
  built (13 references, 26 knowledge modules, 1 examples file with 27
  exemplars). New work goes in the Active Prompt Queue above.

## Risks And Blockers

- No active blockers

---

**Notes**:
- The full working rules, prompt granularity guidance, subagent delegation
  rules, and rationale live in `dev/TODO_MANAGEMENT.md` (in the shared defaults
  repo at `c:\git\defaults`).
- When a new reference, knowledge, or example module is identified, add a
  prompt above, build the file (header, subject, before/after rewrites,
  cross-references), wire it into `SKILL.md`, then mark it done.
- Run the anti-AI pass (`references/anti-ai-patterns.md`) on any new prose
  examples.
- Run `npx -y markdownlint-cli2 --fix todo.md` after edits.

