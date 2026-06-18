# Quiet Title — Design Learnings

This file holds the structural learnings surfaced while
designing the _Quiet Title_ adventure
(`03-adventures/01-quiet-title.md`). Per the
`learnings/README.md` discipline, these are grounded in the
specific work of building one adventure, then generalized
into principles for the next one.

_Quiet Title_ was designed before the sandbox-structure and
levers-and-fallbacks reference modules existed. Several of
the entries below were the _evidence_ that those modules
were needed; they have now graduated into the reference
files. Entries marked `[GRADUATED]` are folded into the
named reference; the entry remains here as the record of
the table-side discovery.

---

## Quiet Title — design pass, 2026

**Pattern observed:** The first draft of the adventure was
a branching three-act chapter with one central prize (the
field book), structurally identical to _Yellowstone Line_
wearing different clothes. It worked but felt like a
railroad wearing a sandbox's hat.

**What went wrong:** The adventure claimed sandbox
structure (multiple goals, multiple solutions) but actually
ran on a single critical path. The "what if they break it"
section was a patch list, not a doctrine. The factions were
reactive, not clock-driven. The whole design collapsed if
the party refused the field book.

**Learning:** A branching chapter is not a sandbox. The
sandbox is a distinct structure requiring: a lever menu
(many sufficient routes, none mandatory), faction clocks
that advance on time without the party, an entry-point
menu (multiple valid first sessions), and shortcut
_doctrine_ (true consequences, never resets). Without all
four, the adventure is a chapter with sandbox flavor.

**Apply to:** New reference file `references/sandbox-structure.md`.
The four properties became its definition of the sandbox.

**Status:** `[GRADUATED → references/sandbox-structure.md]`

---

## Quiet Title — design pass, 2026

**Pattern observed:** The single most useful design
artifact produced for the adventure was the "Truth Survives
the Holder" table — a per-NPC map of where each load-bearing
truth migrates on death, flight, or bribery.

**What went right:** Building the table forced recognition
of hidden single-point failures. Three NPCs who "carried"
the whole plot were revealed to have no fallback; the table
made the author add one. The table is also the fastest
runtime reference at the table when an NPC dies unexpectedly.

**Learning:** Every adventure, chapter or sandbox, should
carry a truth-survives-the-holder table for its load-bearing
NPCs. It is the action-layer equivalent of the three-clue
rule for information. Building it is a design audit;
running it is a runtime safety net.

**Apply to:** New reference file `references/levers-and-fallbacks.md`,
"The truth-survives-the-holder table." The pattern also
appears in _Yellowstone Line_ as inline prose; the
formalization as a table is the QT contribution.

**Status:** `[GRADUATED → references/levers-and-fallbacks.md]`

---

## Quiet Title — design pass, 2026

**Pattern observed:** The social scenes only landed once
each principal was given three distinct player-approach
tiers — please, intuit, offend — each with its own
consequence-track shift.

**What went right:** The "please" tier alone produced flat
scenes (do the obvious thing, get the obvious reward).
Adding "intuit" — a deeper read unlocked by understanding
the NPC's actual concern (the graves, not the lawsuit) —
rewarded players who listened rather than players who
rolled. Adding "offend" with a named track cost gave the
scene real stakes.

**Learning:** Social scenes need at least three pivot tiers
per NPC: the obvious pleasing approach, the deeper
intuitive approach that requires reading the NPC, and the
offending approach with a named cost. Two tiers produce a
social roll with flavor text. Three tiers produce a scene
that rewards engagement.

**Apply to:** `references/social-encounters.md` — consider
adding the please/intuit/offend three-tier model as a
concrete implementation of the pivot-point mechanic.

**Status:** OPEN

---

## Quiet Title — design pass, 2026

**Pattern observed:** Separating the historical
authenticity material into a companion document
(`01B-historical-facts-and-authenticity.md`) rather than
inline notes kept the adventure playable while letting the
grounding go deep.

**What went right:** The Maxwell Grant's real history,
surveyor's trade, plaza life, and mercury poisoning were
too substantial for inline notes (which would have
overwhelmed the adventure text) and too valuable to omit.
The companion document carries the depth; the adventure
carries the play. A GM reads the treatise once and runs
from the adventure repeatedly.

**Learning:** Adventures built on substantial real-world
grounding (a political economy, a technical trade, a
documented atrocity) earn a separate authenticity
companion, not inline notes. The threshold: if the
grounding would run more than ~2000 words, it belongs in a
sidecar. Inline notes suit a single real event behind a
fictional scene; sidecars suit a whole real world behind
a fictional one.

**Apply to:** `references/historical-grounding.md` — add
guidance on the inline-vs-sidecar decision and the
"real/invented ledger" as a recommended section of the
sidecar.

**Status:** OPEN

---

## Quiet Title — design pass, 2026

**Pattern observed:** The faction clocks only generated
real pressure when they were allowed to _collide_ in the
same week, not serialized.

**What went right:** The directive "When two clocks collide,
let them" produced the adventure's best sessions in
design — a week where the Company's chain crew re-marks the
line _and_ the camp raids an assay wagon forces the party
to choose which fire to fight. Serializing the collisions
(one per week, in order) would have flattened the pressure
into a queue.

**Learning:** Faction clocks must be allowed to collide,
not serialized. The collision — two or more clocks firing
in the same unit of time — is where the sandbox's pressure
is highest and the party's choices are hardest. Build for
collision; do not smooth it away.

**Apply to:** `references/clocks-and-timers.md` and
`references/sandbox-structure.md`. The collision rule is
now stated explicitly in both.

**Status:** `[GRADUATED → references/sandbox-structure.md]`

---

## Quiet Title — design pass, 2026

**Pattern observed:** The split-party had to be designed
_for_, not against. Treating the split as the campaign's
natural shape (two riders to the camp, two to the court,
one in the plaza) produced better sessions than discouraging
it.

**What went right:** The sandbox's fixed nodes are real
enough to sustain half a party each. Cutting between groups
"like a western cuts between riders on different trails"
gave the table a cinematic rhythm and let each subgroup's
choices land on the other's table. Fighting the split would
have produced a frustrated table and a stalled session.

**Learning:** A sandbox with real nodes supports a split
party naturally; design for it. The split-party test
("can you run it?") is a core sandbox audit item. The
technique of cutting between groups is film editing applied
to tabletop pacing.

**Apply to:** `references/sandbox-structure.md`, "The
split-party test." This is a sandbox-specific concern;
chapters generally cannot support a split because the track
is single.

**Status:** `[GRADUATED → references/sandbox-structure.md]`

---

## Quiet Title — design pass, 2026

**Pattern observed:** Writing the "When the Party Shortcuts
the Plot" section _before_ finishing the arcs forced the
design to become a real sandbox. Writing it _after_ would
have produced patches bolted onto a chapter.

**What went right:** Drafting the eleven shortcut answers
(expose the field book early, kill Hadley, ride for Santa
Fe, burn the book, split the party, sit still, unite the
factions, triple-deal, etc.) revealed where the adventure
was secretly still a chapter. Each shortcut that initially
had no answer exposed a hidden critical path; fixing the
answer meant adding a lever or a clock, which made the
sandbox richer.

**Learning:** The shortcut-doctrine section is not a
post-draft safety check; it is a _design driver_. Drafting
it early exposes the adventure's hidden railroads. If a
shortcut has no true consequence, the adventure is a
chapter in disguise; redesign until every shortcut opens
a road rather than closing one.

**Apply to:** `references/sandbox-structure.md` and the
sandbox audit (the shortcut test is now a core audit item).
Consider promoting this to `references/anti-railroad.md`
as a general audit technique, since shortcuts expose
railroads in chapters too.

**Status:** OPEN (candidate for `anti-railroad.md`)

---

## How this file grows

_Quiet Title_ has not yet been playtested at a live table;
these entries are _design-pass learnings_ (what building
the adventure taught), not _table learnings_ (what running
it taught). The distinction matters: design learnings can
graduate into reference files immediately, as several
above have; table learnings require the feedback loop in
`learnings/README.md` (run → debrief → triage → file).

When _Quiet Title_ is run at a table, add table-learned
entries below the design-pass entries, dated by session.
Table learnings supersede design-pass assumptions where
they conflict — the table is the final authority.
