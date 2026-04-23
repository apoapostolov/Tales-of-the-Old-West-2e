# Learnings — Table-Sourced Knowledge

This folder holds what the table teaches. Not theory. Not
design principles borrowed from blogs. What actually happened
when real players touched a real adventure.

Every entry in this folder is grounded in a specific session
of a specific adventure. Generalizations that aren't grounded
here are not learnings; they're opinions. Those belong in the
reference files.

## When to create an entry

After completing step 17 of the workflow (feedback triage),
create or update a learnings file if the session produced at
least one bucket-B finding: a pattern to avoid or replicate in
_future_ adventures that is not yet documented in the reference
files.

Do not create entries for:

- Bucket-A findings (fix the current adventure's text — don't
  file them here, apply them directly to the adventure).
- Bucket-C findings (preference mismatches — the players wanted
  a different kind of adventure; no structural learning exists).

## File naming

One file per adventure. All entries from multiple playtests of
the same adventure accumulate in the same file.

```
learnings/[adventure-slug].md
```

Examples:

```
learnings/yellowstone-line.md
learnings/the-cooper-mine.md
learnings/iron-cold-session-0.md
```

Use lowercase, hyphens, no spaces.

## Entry format

Each entry in a learnings file follows this structure:

```markdown
## [Adventure Title] — [Session Date YYYY-MM-DD]

**Pattern observed**: One sentence describing what happened at
the table.

**What went wrong / right**: One to three sentences describing
the specific mechanic, scene, NPC, or clue that produced the
pattern.

**Learning**: The generalized rule this session taught, stated
as a principle that applies to future adventures, not just this
one.

**Apply to**: Which reference file this learning suggests
updating, OR which future adventure should inherit this
principle first.

**Status**: `OPEN` (not yet graduated) / `GRADUATED` (folded
into reference file — see note below).
```

## The graduation threshold

A learning **graduates** when:

- The same pattern has appeared in two or more separate
  sessions (same adventure or different adventures), or
- The pattern directly contradicts or extends a rule in an
  existing reference file.

When a learning graduates:

1. Update the relevant reference file with the new or corrected
   rule.
2. Note the session evidence in the reference file's revision
   notes (or a brief inline comment: "confirmed by table play,
   [adventure slug], [date]").
3. Mark the entry in this file as `[GRADUATED → references/filename.md]`.

## Examples

The following are illustrative examples using placeholder
adventure names. Real entries replace these as adventures are
playtested.

---

## The Cooper Mine — 2025-06-14

**Pattern observed**: Players skipped the Vickers NPC entirely
in Arc I and never recovered the route-forgery subplot.

**What went wrong**: Vickers was the sole carrier for the
route-forgery clue in Arc I. The players bypassed the saloon
scene where he appeared and did not return until Arc III, by
which point the clue was moot.

**Learning**: No critical fact should have a single carrier in
the first arc. Arc I carriers are the most likely to be skipped
because players have not yet mapped the adventure space.
Distribute Arc I facts across at least two locations and two
NPC types (one stationary, one mobile).

**Apply to**: `references/clue-discipline.md` — add a note on
carrier distribution by arc, with Arc I requiring the highest
density.

**Status**: OPEN

---

## The Cooper Mine — 2025-06-14

**Pattern observed**: The interrogation scene with Aldermoor ran
20 minutes over schedule because the players kept trying options
the text hadn't anticipated.

**What went wrong**: The scene entry listed two pivot points.
Both were formal (a document shown, a name dropped). Players
kept trying physical intimidation and environment manipulation.
The GM had to improvise because the text hadn't addressed those
routes.

**Learning**: Social encounter entries need a third pivot point
from an unanticipated approach category (physical, environmental,
or emotional) in addition to the two designed pivots. Players
always attempt the approach the author didn't write.

**Apply to**: `references/social-encounters.md` — add a
requirement for a third "unexpected approach" pivot point in
every social encounter entry.

**Status**: OPEN

---

## Iron Cold — 2025-09-02

**Pattern observed**: The horror read-aloud for the crypt scene
landed flat. Players joked through it.

**What went wrong**: The read-aloud was four sentences, two of
which named the emotional register ("dread hung over the room,"
"an unnatural silence"). Players heard the mood-naming and
tuned out.

**Learning**: Horror read-aloud must never name the mood. The
same principle from `references/read-aloud.md` (mood-naming
anti-pattern) applies with greater force in horror. In horror,
named mood becomes comedy. Specific sensory detail that implies
the wrong is more durable.

**Apply to**: `references/horror-design.md` (when created) —
add explicit note that the mood-naming anti-pattern from
`read-aloud.md` is fatal in horror context, not merely weak.

**Status**: OPEN

---

## How this folder grows

At the start of the skill's life, this folder is empty except
for this README. That is correct. Learnings are earned, not
invented. The examples above are placeholders that will be
replaced or supplemented by real session data as adventures
are playtested.

After three to five adventures have been run and their learnings
filed here, a graduation pass should be run: review all OPEN
entries, identify which have two or more corroborating instances
across different adventures, and graduate them into the
appropriate reference files.

The goal is a feedback loop: reference files teach design →
adventures are built → sessions are played → learnings are
filed → reference files improve → the next adventure is better.

That loop is the bible's engine.

## Cross-adventure pattern detection

A single learning entry is one data point. A pattern is multiple
entries from different adventures pointing at the same structural
issue.

At three-month intervals, run a cross-adventure scan:

1. Open every learnings file in this folder.
2. Group OPEN entries by which reference file they point to.
3. For any reference file with two or more OPEN entries pointing
   at it, those learnings have crossed the graduation threshold.
   Update the reference file and mark the entries graduated.
4. For any reference file with five or more OPEN entries pointing
   at it across multiple adventures, the reference itself may
   need a structural revision rather than an incremental update.
   Treat as a major revision; document the change in the
   reference file's revision notes.

The scan is the mechanism by which table experience compounds
into the bible. Without periodic scans, learnings accumulate as
trivia rather than improving the next adventure's design.

## What does not belong here

For clarity, learnings files are not:

- A general design diary. If the thought is not grounded in a
  specific session, it is not a learning.
- A complaint log. Player frustration that is not actionable for
  future adventure design is not a learning. (Bucket-C feedback
  belongs in your private notes, not here.)
- A theoretical position. "I think clue distribution should be
  more redundant" is not a learning. "In the Cooper Mine session,
  one carrier was insufficient and the players missed it" is.
- A polished essay. Learnings are short, specific, and
  diagnostic. The format above is sufficient. Do not expand into
  prose unless the pattern genuinely requires it.
