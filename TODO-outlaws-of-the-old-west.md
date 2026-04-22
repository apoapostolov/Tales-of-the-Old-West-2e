# TODO - Outlaws of the Old West

## Current Focus

- Convert FL2e mercenary-band management into a ToOW2e outlaw-band appendix that strengthens long-form outlaw campaigns without importing FL2e's heavier campaign machinery.
- Canonical system owner: `/home/apoapostolov/git-public/Tales-of-the-Old-West-2e/proposals/proposal-fl2e-grafts-and-outlaws-plan.md`
- Current manuscript draft: `/home/apoapostolov/git-public/Tales-of-the-Old-West-2e/corebook/11-outlaws-of-the-old-west.md`
- Current research memo: `/home/apoapostolov/git-public/Tales-of-the-Old-West-2e/proposals/proposal-outlaw-reality-and-town-resource-tieins.md`

## Scope And Boundaries

- Owns the design, research plan, drafting plan, and future manuscript production path for `Chapter 11 / Appendix A: Outlaws of the Old West`.
- Owns identification of low-overhead FL2e systems that can be cleanly grafted onto ToOW2e.
- Owns integration planning against ToOW2e town, outfit, compadre, reputation, bounty, and seasonal systems.
- Does not own final historical research in this pass.
- Does not own final manuscript prose in this pass.
- Does not own a full port of `Forbidden Lands 2e` mercenary rules.
- Does not own mass-combat, host command, or other heavy FL2e-only mechanics unless later research proves a small fragment is essential.

## Active Prompt Queue

### [ ] Prompt 1 — Lock the outlaw appendix design spine

Finalize the minimum rule loop for outlaw-band play so later research is targeted and does not bloat the appendix.

Context:

- ToOW2e is intentionally lighter than FL2e.
- The appendix must plug into existing ToOW2e systems instead of becoming a parallel game.
- The current planning proposal is the canonical draft design note for this epic.

Inputs:

- `proposals/proposal-fl2e-grafts-and-outlaws-plan.md`
- `corebook/02-your-player-character.md`
- `corebook/06-life-in-the-old-west.md`
- `corebook/08-campaigns-in-the-old-west.md`
- `/home/apoapostolov/git-public/Forbidden-Lands-2e/corebook/12-mercenaries-of-forbidden-lands.md`

Outputs:

- A short follow-up design memo that locks:
- gang scale tiers
- gang cohesion model
- notable gang member model
- wanted escalation model
- job / score structure
- hideout upkeep scope

Validation:

- Every chosen mechanic must map to an existing ToOW2e term or chapter.
- Every rejected FL2e mechanic must be named explicitly if it presents a likely future temptation to overbuild.
- `npx -y markdownlint-cli2 --fix TODO-outlaws-of-the-old-west.md proposals/proposal-fl2e-grafts-and-outlaws-plan.md`

Delegation notes:

- Keep the appendix playable with minimal bookkeeping.
- Prefer seasonal consequences over daily accounting.
- Use ToOW2e names wherever possible.

### [ ] Prompt 2 — Research outlaw-band reality by subsystem

Run structured research across multiple later prompts so each historical question ends in direct design consequences rather than loose notes.

Context:

- This appendix will require heavy historical grounding.
- Research needs to be split so each pass has a clear output and does not blur into drafting.

Inputs:

- Prompt 1 locked design spine
- likely external historical sources gathered in future prompts

Outputs:

- one memo each for:
- gang composition and leadership
- outlaw earnings, loot division, and supply pressure
- wanted systems, posses, bounty hunters, and federal escalation
- hideouts, movement, seasonality, and survival
- score types by region and target class

Validation:

- Each research memo ends with `Design Implications`.
- Each memo distinguishes documented history from design inference.
- Each memo states what should be excluded from the manuscript to preserve playability.

Delegation notes:

- Research should be period-focused on the 1870s Old West first, with later decades used only when directly illuminating 1873-era play.
- Favor practical realities over cinematic myth unless the manuscript intentionally wants the myth layer.

### [x] Prompt 2A — Proposal on outlaw reality and light town/resource tie-ins

Write a research memo answering two linked questions:

- what western outlaw realities are still missing from the current outlaw loop
- how outlaw play can tie lightly into settlement and resource logic without importing full FL2e weight

Inputs:

- `proposals/proposal-fl2e-grafts-and-outlaws-plan.md`
- `corebook/11-outlaws-of-the-old-west.md`
- `corebook/02-your-player-character.md`
- `corebook/06-life-in-the-old-west.md`
- `corebook/08-campaigns-in-the-old-west.md`
- `/home/apoapostolov/git-public/Forbidden-Lands-2e/corebook/08-journeys.md`
- `/home/apoapostolov/git-public/Forbidden-Lands-2e/corebook/09-the-stronghold.md`
- `/home/apoapostolov/git-public/Forbidden-Lands-2e/corebook/12-mercenaries-of-forbidden-lands.md`
- external historical sources on rustling, hideouts, marshals, and private enforcement

Outputs:

- `/home/apoapostolov/git-public/Tales-of-the-Old-West-2e/proposals/proposal-outlaw-reality-and-town-resource-tieins.md`

Validation:

- must end in concrete design recommendations
- must clearly reject heavy imports that do not fit `Tales`
- must separate historical finding from rules inference

### [x] Prompt 3 — Create the appendix skeleton

Create the future chapter shell for `Outlaws of the Old West` once Prompt 1 is locked and at least the first research memos exist.

Context:

- The chapter should be executable as a manuscript project, not just a concept.

Inputs:

- Prompt 1 design memo
- Prompt 2 research outputs
- `proposals/proposal-fl2e-grafts-and-outlaws-plan.md`

Outputs:

- a markdown chapter skeleton with section headings, integration notes, and placeholders for tables, examples, and sidebars

Validation:

- Section order should teach play from basic to advanced.
- The appendix must be optional and self-explanatory.
- The skeleton must call out direct integration points with existing ToOW2e chapters.

Delegation notes:

- Do not write final prose yet.
- Avoid long placeholder text dumps; use short intent notes.

### [x] Prompt 4 — Draft the minimum viable outlaw loop

Write the first playable manuscript pass for the appendix's core loop.

Context:

- This is the first real drafting pass and should stay tightly scoped.

Inputs:

- chapter skeleton from Prompt 3
- approved design spine
- research memos from Prompt 2

Outputs:

- draft sections for:
- what this appendix is
- the outlaw band
- recruitment and loyalty
- scores and jobs
- wanted men

Validation:

- Rules must read as ToOW2e manuscript prose, not design-note prose.
- Every rule should produce clear table behavior.
- No section should assume heavy tracking infrastructure that the book has not already taught.

Delegation notes:

- This is a good prompt for one coordinator plus up to two focused workers:
- one discovery / source cross-check worker
- one drafting worker
- coordinator handles integration and final pass

### [x] Prompt 5 — Draft hideout life, upkeep, and collapse

Expand the appendix from minimum viable play into a durable long-campaign subsystem.

Context:

- This pass adds between-job and seasonal persistence.

Inputs:

- Prompt 4 draft
- Prompt 2 research on seasonality, hideouts, and outlaw economics

Outputs:

- draft sections for:
- shares, supplies, and hideout upkeep
- hideout life
- consequences and collapse

Validation:

- Must integrate with `Turn of the Season` rather than overwrite it.
- Must not create a second town-development game for outlaws.
- Must make failure states playable rather than campaign-ending by default.

Delegation notes:

- Emphasize pressure, scarcity, and movement.
- Keep accounting abstract unless a detail produces meaningful drama.

### [ ] Prompt 6 — Build examples, tables, and premade bands

Add the support material that makes the appendix usable at the table.

Context:

- Once the rules are stable, support material should teach tone and usage.

Inputs:

- Prompts 4 and 5 drafts
- research memos

Outputs:

- one worked example of an outlaw season
- notable gang member templates
- premade outlaw bands
- core reference tables for jobs, wanted escalation, and gang troubles

Validation:

- Examples must demonstrate actual play decisions, not just summarize rules.
- Premade bands must feel grounded in the Old West rather than fantasy-company logic in western clothes.

Delegation notes:

- Premade bands should vary by region, social makeup, and criminal method.
- Avoid turning every gang into a celebrity gang.

### [ ] Prompt 7 — Run final integration and manuscript audit

Audit the appendix against the rest of ToOW2e before any release-quality pass.

Context:

- This is the anti-bloat and anti-contradiction pass.

Inputs:

- full appendix draft
- `corebook/02-your-player-character.md`
- `corebook/03-rolling-the-bones.md`
- `corebook/05-conflict-and-damage.md`
- `corebook/06-life-in-the-old-west.md`
- `corebook/08-campaigns-in-the-old-west.md`

Outputs:

- an integration audit memo or revision pass that confirms:
- terms are consistent
- money scales make sense
- reputation consequences align with existing systems
- compadres and gang members do not overlap confusingly
- seasonal timing is coherent

Validation:

- zero unresolved terminology conflicts
- zero silent contradictions with money, reputation, or seasonal rules
- `npx -y markdownlint-cli2 --fix TODO-outlaws-of-the-old-west.md`

Delegation notes:

- This is a strong candidate for parallel validation agents if subagents are explicitly requested later.
- Keep findings concrete and file-linked.

## Working Rules

- Canonical source rule: treat `proposals/proposal-fl2e-grafts-and-outlaws-plan.md` as the live planning anchor for this epic until manuscript drafting begins.
- Canonical chapter rule: when drafting starts, update the chapter file in place and keep proposal notes upstream rather than scattering competing design docs.
- Derived artifact rule: tables and reusable roll structures should be regenerated from canonical draft material if a generation workflow appears later; do not hand-edit derived outputs without necessity.
- Safety rule: do not overwrite or restructure existing ToOW2e chapter numbering without an explicit integration decision recorded in the decision log.
- Research boundary rule: historical research must be separated from manuscript drafting, and each research pass must end with design implications and exclusions.
- Prompt completeness rule: every future prompt in this file should state canonical inputs, outputs, validation, and non-goals before execution.
- Constant pushing rule: once one prompt is complete and the next is unblocked, continue immediately rather than stopping between phases.
- Cleanup rule: if this TODO becomes crowded, remove completed prompt dumps from the active queue first; archive only if explicitly useful.
- Markdown rule: run `npx -y markdownlint-cli2 --fix <file>` after editing any markdown.

## Decision Log

- 2026-04-22: Treat FL2e mercenary rules as source material, not as a chapter to port wholesale.
- 2026-04-22: The outlaw appendix must remain lighter than FL2e and integrate with ToOW2e's town, outfit, reputation, and seasonal systems.
- 2026-04-22: The immediate deliverables for this pass are a proposal and an execution-ready TODO, not final manuscript text.

## Risks And Blockers

- Biggest design risk: importing too much FL2e bookkeeping and losing ToOW2e's lighter feel.
- Biggest research risk: relying on cinematic outlaw tropes where 1870s realities would produce stronger and more original rules.
- Structural risk: `compadres`, generic gang members, and notable gang members could overlap unless their roles are defined sharply.
- Structural risk: outlaw hideout play could accidentally compete with the town-development loop instead of productively pressuring it.
- No active blocker at this stage.

## Template

Use this structure when a new major undertaking becomes the active queue in this file:

```md
# TODO - <Project Name>

## Current Focus

- epic name and one-sentence mission
- explicit canonical file or system owner

## Scope And Boundaries

- what this pass owns
- what this pass explicitly does not own

## Active Prompt Queue

### [ ] Prompt 1 — <goal>

Short prompt description.

Context:

- canonical files, systems, and assumptions this prompt depends on

Inputs:

- exact files, commands, or upstream prompts to inspect before acting

Outputs:

- expected file or system result

Validation:

- tests, lint, preview commands, or manual checks

Delegation notes:

- constraints, non-goals, and implementation guidance needed for a cheaper executor to finish safely

### [ ] Prompt 1A — <sub-goal>

Use sub-prompts when a prompt needs to be split without hiding partial
completion.

Dependencies:

- parent prompt or upstream prerequisite if applicable

Completed output:

- concrete finished deliverable

## Working Rules

- canonical source
- derived outputs
- rollback or safety notes
- prompt completeness and delegation readiness
- constant pushing when context allows
- cleanup removes completed prompts from the active TODO first; optional
  archiving happens separately, after removal, in `TODO_ARCHIVE.md` or a
  project-specific archive

## Decision Log

- YYYY-MM-DD: important scope or design decision

## Risks And Blockers

- open risk
- explicit blocker if present
```
