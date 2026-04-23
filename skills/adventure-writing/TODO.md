# TODO - Adventure Writing Skill Expansion

This TODO drives the expansion of `skills/adventure-writing` from a
12-reference structural bible into a full design bible covering the
complete lifecycle: research → design → draft → playtest → feedback →
learnings. Modeled on research from adventure-writing practice in Call
of Cthulhu, historical RPGs, node-based design theory, and sandbox
methodology.

## Current Focus

- Expand the adventure-writing skill into a comprehensive adventure
  design bible with coverage of investigation design, horror design,
  location design, social encounters, scope calibration, the full
  research pipeline, and a closed feedback loop with learnings.
- Canonical owner: `skills/adventure-writing/SKILL.md` plus all
  files under `skills/adventure-writing/`.

## Scope And Boundaries

- **Owns:** New reference files, new templates, learnings folder
  infrastructure, and SKILL.md enhancements.
- **Does not own:** Existing 12 reference files (architecture,
  scene-design, npcs, factions-and-tracks, clue-discipline,
  pacing-and-arcs, dilemmas, combat-encounters, endings-and-sandbox,
  historical-grounding, anti-railroad, read-aloud) — these are
  complete and should not be edited unless a specific correction is
  identified.
- **Does not own:** Any corebook chapters or supplement content.

## Working Rules

- Execution-ready rule: every active prompt is documented so a
  capable executor can perform the work without relying on hidden
  planner context.
- Canonical source rule: all new files live under
  `skills/adventure-writing/`. File paths are stated per prompt.
- Safety rule: no existing reference files are modified by this
  TODO. SKILL.md is modified only by the designated prompt.
- Prompt granularity: each prompt produces one deliverable file
  or one targeted SKILL.md edit.
- After completing any prompt, immediately update SKILL.md's library
  index to add the new file. (The SKILL.md enhancement prompt covers
  the full batch update; individual prompts do not need to update it.)

---

## Active Prompt Queue

### Prompt 1 — SKILL.md: Research + Feedback Pipeline Enhancement [ ]

**Goal:** Extend SKILL.md with a Phase 0 (scope + research) prepended
to the 14-step workflow, a Phase 3 (playtest → feedback → learnings)
appended, and updated library entries for all planned new files.

**File:** `skills/adventure-writing/SKILL.md`

**Inputs:** Current SKILL.md (read before editing).

**Changes:**

1. [ ] After the line `Use this order when drafting a fresh adventure.
Skipping a step produces the failure modes...` and before step 1,
       insert two new steps:
   - [ ] **Step 0a — Set scope before drafting.** One-shot / campaign
         chapter / mini-campaign. Set a word target and session count.
         See `references/scope-and-format.md`.
   - [ ] **Step 0b — Run the research pipeline.** Primary sources,
         setting bibles, period grounding, worldbuilding verification.
         Do not draft until the world can answer six research questions.
         See `references/research-pipeline.md`.
         Renumber the existing steps 1-14 as steps 1-14 (no renumbering
         needed; steps 0a/0b are prepended as a Phase 0 block).

2. [ ] After the current step 14, add a Phase 3 block:
   - [ ] **Step 15 — Playtest.** Run the adventure at a live table or
         arrange a controlled playtest. Take notes; do not intervene.
         See `references/playtesting.md`.
   - [ ] **Step 16 — Collect structured feedback.** Run the post-session
         debrief 24 hours after the game. Use the feedback form. See
         `references/feedback-collection.md` and
         `templates/feedback-form.md`.
   - [ ] **Step 17 — Triage and file learnings.** Categorize feedback
         into: (a) fixes to this adventure, (b) patterns to avoid in
         future adventures, (c) patterns to replicate. File (b) and (c)
         in `learnings/`. See `learnings/README.md`.

3. [ ] In the library section, add a new "**Phase 0: Process**" subsection
       with entries for all files listed in Prompts 2–4.

4. [ ] Add a new "**learnings/**" subsection pointing to
       `learnings/README.md`.

5. [ ] In "How to use this bible", add:
   - [ ] Entry 10: For an investigation or mystery adventure, load
         `references/investigation-structure.md` and
         `references/node-based-design.md`.
   - [ ] Entry 11: For a horror adventure, load
         `references/horror-design.md`.
   - [ ] Entry 12: For a one-shot, load `references/scope-and-format.md`
         and `templates/one-shot-skeleton.md`.
   - [ ] Entry 13: After every live session, run steps 15–17.

**Validation:** SKILL.md should contain all 17 workflow steps, library
entries for all planned files, and a learnings/ section.

---

### Prompt 2 — Phase 0: `references/scope-and-format.md` [ ]

**Goal:** Document the scope-setting discipline that precedes all
drafting. Covers format decisions, structural constraints, and common
scope failures.

**File:** `skills/adventure-writing/references/scope-and-format.md`

**Content to include:**

- **One-shot design constraints**: single session, self-contained arc,
  compressed cast (4-6 NPCs max), one central dilemma, no consequence
  ledger spanning sessions. Typical word count 3,000-6,000.
- **Campaign chapter design constraints**: feeds forward and backward,
  uses the full consequence ledger, carries open threads, introduces
  at most two new factions, assumes 2-4 sessions. Typical word count
  6,000-12,000.
- **Mini-campaign (2-4 chapter arc)**: bridging structure. How chapters
  hand off consequences, NPCs, and open threads.
- **Scope failure modes**: scope creep (writing for every contingency),
  scope poverty (skipping robustness clauses to stay small).
- **Session length calibration**: 3h vs 4h vs full-day session, scene
  density per session type.
- **Format decisions**: pre-generated characters vs. open cast,
  handouts (when to include, what constitutes a handout vs. boxed text),
  maps (when a map earns its place vs. clutters the table).
- **The minimum viable adventure**: the smallest design that can
  function at the table. One pressure, two factions, six NPCs, one
  dilemma, two endings.
- **Closing checklist**: six questions to answer before moving from
  scope to research.

---

### Prompt 3 — Phase 0: `references/research-pipeline.md` [ ]

**Goal:** A systematic workflow for researching an adventure before
drafting. Covers primary sources, period anchors, worldbuilding
verification, and when to stop researching.

**File:** `skills/adventure-writing/references/research-pipeline.md`

**Content to include:**

- **The six research questions**: (1) What is the political/power
  situation? (2) What are people fighting over economically? (3) What
  technology and communication reality exists? (4) Who is being
  displaced or exploited? (5) What does daily work look like for the
  people in this adventure? (6) What happened here in the year or two
  before the adventure opens?
- **Source hierarchy**: primary sources (period documents, diaries,
  newspapers) → secondary historical works → setting bibles → invented
  (for fantasy/sci-fi). Distinguish between researching texture vs.
  inventing events.
- **Worldbuilding verification for fantasy/sci-fi**: even invented
  worlds must pass the six questions. Map the world's equivalent
  political situation, economy, technology, displaced people, work,
  and recent history.
- **The research register format**: a short working document (one
  page max) answering the six questions for this specific adventure.
  Keep it. Quote from it in historical notes.
- **When to stop**: when you can answer all six questions in two
  sentences each, you have enough. More research after this point
  delays drafting without improving the adventure.
- **Research anti-patterns**: paralysis (researching instead of
  drafting), lecturing (importing research as prose), period purity
  (refusing to invent when research would be blocking).
- **Lean-period research for fantasy**: minimum viable worldbuilding
  to satisfy the six questions when the setting bible is thin.
- **Cross-reference with historical-grounding.md**: this file covers
  _process_ (what to do before drafting); `historical-grounding.md`
  covers _application_ (how grounding appears on the page).

---

### Prompt 4 — Phase 3: `references/playtesting.md` [ ]

**Goal:** How to run a controlled playtest: what to observe, what not
to do, how to take notes, when to intervene, and what constitutes a
useful vs. useless playtest.

**File:** `skills/adventure-writing/references/playtesting.md`

**Content to include:**

- **What playtesting is for**: surfacing structural failures that
  cannot be found on the page — dead clues, gated information, pacing
  collapse, NPCs who don't land.
- **Playtest types**: (a) solo read-aloud pass (author reads while
  another person listens), (b) live table playtest, (c) blind playtest
  (another GM runs from the text alone without author present).
  Each has different signal value; blind is highest.
- **The observer role**: the author's job during a live playtest is
  to observe and take notes, not to fill in gaps or explain the text.
  If you explain, it means the text failed.
- **What to observe and note**: (1) Where the players stop and look
  confused — the text didn't provide enough orientation. (2) Where
  they ignore your designed branches and do something else. (3) Where
  they roll when the chapter didn't intend a roll. (4) Where they
  move faster or slower than the pacing assumed. (5) Which NPCs land
  and which are ignored.
- **The intervention threshold**: intervene only to prevent session
  death (total stall with no visible path). Never explain an NPC's
  motivation or add information the chapter didn't supply. Stalls are
  data.
- **Note format during play**: shorthand notation. Mark scene number +
  what happened + "F" (faster than expected), "S" (slower), "Ø"
  (skipped), "?" (player confusion), "!" (unexpected player move).
- **Timing**: run the playtest at a live table before publishing. For
  major revisions, run a second pass. For a one-shot, a single live
  playtest is sufficient.
- **Pre-playtest checklist**: the text is complete, you have pre-gen
  characters if needed, you have printed/shareable handouts, you know
  which scene you want to observe most carefully.
- **Setting expectations with players**: tell players this is a draft,
  not a finished product. Ask them to play naturally. Ask them not to
  give feedback during the session — hold it for the debrief.
- **Blind playtest protocol**: hand the GM the document. Do not
  explain anything beforehand. Observe as a player. Note every moment
  the GM pauses to search the text or makes a ruling that the text
  should have covered.

---

### Prompt 5 — Phase 3: `references/feedback-collection.md` [ ]

**Goal:** Structured post-session debrief protocol. How to collect
actionable feedback from players and GM, how to resist defensive
responses, and how to convert raw feedback to usable learnings.

**File:** `skills/adventure-writing/references/feedback-collection.md`

**Content to include:**

- **Timing**: collect written or verbal feedback 12-24 hours after
  the session, not immediately after. Players and author are both tired
  and emotionally reactive right after a session. A night's sleep
  separates enjoyment from critique.
- **The debrief structure**: a short structured conversation or written
  form with five questions. See `templates/feedback-form.md` for
  the blank form.
- **The five questions**: (1) Which moment in the session would you
  most want to play again? (2) Which moment do you wish had gone
  differently? (3) Was there anything you couldn't figure out or
  wanted more information about? (4) What did you want to do that the
  adventure didn't support? (5) What would you tell another player
  before running this adventure?
- **How to listen**: take notes; do not defend. A player saying "I
  couldn't figure out Vane's motivation" is not a complaint about your
  writing — it is data that the motivation is undersupported. Treat
  every piece of feedback as a data point, not a verdict.
- **The feedback triage**: after collecting all feedback, sort into
  three buckets: (A) structural failures — fix in this adventure
  before publishing, (B) author learnings — patterns to file in
  `learnings/` for future adventures, (C) preference mismatches —
  players wanted a different kind of adventure. Bucket C doesn't
  require a fix.
- **Red flags in feedback**: if multiple players flag the same
  moment, it is structural, not preferential. If a clue is described
  as "hard to find" by more than one player, it needs a carrier added.
  If an NPC is described as "flat" or "confusing," revise to the
  five-sentence template.
- **What to do with author-learnings**: file them to `learnings/` with
  the adventure title, session date, and the lesson. See
  `learnings/README.md`.
- **Protecting the author**: negative feedback is professional data.
  If feedback stings, wait another 24 hours before reading the notes
  again. The goal is not to defend the adventure; it is to make the
  next one better.

---

### Prompt 6 — Phase 3: `templates/feedback-form.md` [ ]

**Goal:** A printable/shareable post-session feedback questionnaire.
Clean, short, and respecting player time.

**File:** `skills/adventure-writing/templates/feedback-form.md`

**Content to include:**

- Title block: adventure name, session date, GM name.
- Five player questions (see Prompt 5's five questions) with space
  for written answers.
- Two GM-specific questions: (1) Was the text sufficient to run from
  without author input? If not, which sections needed clarification?
  (2) Were there any moments where you improvised because the chapter
  didn't cover the situation?
- One rating scale: "Would you recommend this adventure to another GM?
  Y / N / With notes."
- One open field: "Anything else the author should know."
- Brief framing note at the top: "This is a draft. Your honest
  answers help make the final adventure better. There are no wrong
  answers."

---

### Prompt 7 — `learnings/README.md` [ ]

**Goal:** Document the learnings folder system — its purpose, format,
and how to create and use learning entries.

**File:** `skills/adventure-writing/learnings/README.md`

**Content to include:**

- **Purpose**: a persistent record of what was learned from live table
  play. Not a general RPG theory file. Each entry is grounded in a
  specific session of a specific adventure.
- **When to create an entry**: after completing the feedback triage
  (step 17 in the workflow), file one entry per adventure per playtest
  that yields a bucket-B author learning.
- **Entry format**:

  ```
  ## [Adventure Title] — [Session Date]

  **Pattern observed**: one sentence.
  **What went wrong / right**: one to three sentences.
  **Learning**: the generalized rule this session taught.
  **Applied to**: which reference file this learning improves or which
  future adventure it affects.
  ```

- **Naming convention**: `learnings/[adventure-slug].md`. One file
  per adventure, multiple entries per file as playtests accumulate.
- **The feedback loop**: learnings discovered here should eventually
  be folded into the matching reference file when enough evidence
  accumulates. Mark mature learnings with `[GRADUATED]` and note
  which reference file they were folded into.
- **What learnings are not**: general opinions, system preferences, or
  taste disputes. Learnings are observed structural patterns from real
  sessions.
- **Examples** (2-3 illustrative entries using invented adventure
  names as placeholders).

---

### Prompt 8 — `references/investigation-structure.md` [ ]

**Goal:** A dedicated reference for mystery and investigation adventure
design, extending beyond `clue-discipline.md` to cover the full arc
of an investigation: structure, suspect webs, revelation pacing, the
clue-vs-conclusion distinction, and verification mechanics.

**File:** `skills/adventure-writing/references/investigation-structure.md`

**Content to include:**

- **Investigation vs. sandbox**: investigation adventures have a
  factual target (what happened); sandbox adventures have a situational
  target (what will happen). The difference is in how truth is managed.
- **The crime-scene reconstruction method**: design the crime from the
  perpetrator's point of view before designing the investigation.
  Write a step-by-step account of what the antagonist did. Every step
  leaves residue — evidence, witnesses, behavioral changes.
- **Suspect webs**: a relationship diagram with the perpetrator at the
  center and witnesses, adjacent suspects, partial witnesses, and false
  leads at the periphery. Each node has: what they know, what they'll
  say freely, what requires pressure, what they'll never say.
- **Clues vs. conclusions**: clues are sensory, observable facts.
  Conclusions are player theories. The adventure supplies clues. The
  players supply conclusions. Never embed the solution in the clue
  text itself.
- **Observable vs. deducible clues**: observable clues are directly
  visible (a stain, a letter, a wound pattern); deducible clues require
  interpretation (the stain is the wrong color for the story to be
  true). Both are valid; label them clearly in the design notes.
- **Escalating timelines in investigations**: a countdown of villain
  actions, victim deterioration, or public pressure. Advances when
  players spend time, rest, or fail loudly. Creates tradeoffs.
- **Node-based investigation design**: see `references/node-based-design.md`.
  Summary: each scene in an investigation is a node with: entry conditions,
  clues available, suspect behavior, exit paths, and what changes when
  the players act.
- **Red herrings**: how to plant false leads without cheating. A red
  herring must be falsifiable — the players can disprove it by
  investigation, not by GM fiat.
- **The open-loop ending**: investigations can end without a full
  conviction. The players may have the truth but lack legal proof.
  The chapter's ending handles both the "proof enough" and
  "no admissible evidence" states.
- **Horror and investigation**: how investigation design changes when
  the truth is cosmically dangerous to know. See also
  `references/horror-design.md`.
- **Audit checklist**: 8-point investigation audit.

---

### Prompt 9 — `references/node-based-design.md` [ ]

**Goal:** A reference for node-based scenario design — an alternative
structural model to the three-act arc that suits investigations,
dungeon-crawls, and non-linear exploration equally well. Based on
Alexandrian node theory and practical sandbox methodology.

**File:** `skills/adventure-writing/references/node-based-design.md`

**Content to include:**

- **What a node is**: a scene, location, or encounter the PCs interact
  with. Each node contains information, choices, and entry/exit paths.
- **Node types**: information nodes (clue delivery), decision nodes
  (moral or practical choice), encounter nodes (NPC or conflict), hub
  nodes (from which the party can reach multiple others).
- **Designing backward**: start with the final node (the reckoning
  or revelation) and work backward, placing the clues needed to reach
  each prior node.
- **Floating clues**: critical information that is not locked to one
  node but can surface at any node where it is plausible. When players
  skip or miss a node, floating clues appear at the next relevant
  node.
- **The quantum problem**: floating clues work because information
  travels; the adventure never retcons what the players saw, only what
  they haven't reached yet.
- **Chokepoints**: nodes that every branch must pass through, used
  sparingly. A chokepoint is acceptable only when it is a revelation
  the adventure cannot function without.
- **Exit design**: every node that is not the final node has at least
  two exit paths leading to different next nodes.
- **Linear node chain as railroad detection**: if your node map is
  A → B → C → D with no alternatives, you have a railroad. Minimum
  viable branching: each major node has at least two exits.
- **The relationship map**: a visual diagram showing all nodes and
  their connections. Draw it before drafting. Any node with only one
  exit is a bottleneck — fix it or justify it as a chokepoint.
- **When to use node design vs. three-act arc**: node design suits
  investigations and spatial exploration; three-act arc suits journey
  and pressure narratives. They can be combined: use three-act arc for
  pacing rhythm and node design for scene structure within each act.
- **Node density per session**: a 3-hour session can visit 4-7 nodes.
  Designing 8-12 nodes per session block provides player agency without
  overwhelming the author.

---

### Prompt 10 — `references/horror-design.md` [ ]

**Goal:** A dedicated reference for horror and dread in adventure
design. System-agnostic. Covers tension architecture, the unseen, the
reveal economy, cosmic horror vs. gothic horror vs. survival horror,
and how horror pacing differs from action pacing.

**File:** `skills/adventure-writing/references/horror-design.md`

**Content to include:**

- **What horror requires**: the reader (and later the player) must
  _care_ about the characters before the threat arrives. Horror without
  investment is spectacle.
- **Three horror modes**: (1) Gothic — the horror is old, personal,
  and architectural (the house, the family, the bloodline). (2) Cosmic
  — the horror is inhuman, vast, and indifferent. Knowledge is the
  wound. (3) Survival — the horror is immediate, mortal, and material.
  The threat can be killed but not easily.
- **The unseen principle**: fear is maximized when the threat is
  implied, not shown. The adventure supplies evidence, aftermath, and
  sounds; the players' imaginations construct the monster. Revealing
  the monster too early is the most common horror design error.
- **The reveal economy**: a horror adventure has one or two major
  reveals. Each reveal costs some of the dread. Budget them.
  Front-load dread; back-load reveals.
- **Tension architecture**: a tension arc that rises and falls, not
  a flat high-tension plateau. Moments of (apparent) safety amplify
  the next horror beat. Camp scenes can be used as relief that
  darkens.
- **Cost mechanics (system-agnostic)**: the horror adventure imposes
  costs for proximity to the unnatural: sanity damage, corruption,
  resource depletion, NPC loss. These costs must be _felt_, not only
  tracked. Design the fiction of what the cost looks like.
- **The human antagonist in horror**: the most frightening horror
  adventures layer a human threat beneath the supernatural one. A
  cultist with a recognizable motive is more disturbing than a
  faceless monster.
- **Dread vs. shock**: dread accumulates slowly. Shock is momentary.
  Good horror adventures engineer dread; shocks amplify it but cannot
  replace it.
- **Horror pacing**: slower than action pacing. More silence, more
  description of the mundane before the rupture, more time spent with
  NPCs who will suffer. See `references/pacing-and-arcs.md`.
- **The safety toolkit**: content warnings, session zero calibration
  for horror content, X-card protocol. System-agnostic. The author
  notes in the GM section what content the adventure contains and
  recommends calibration before running.
- **Horror read-aloud**: tighter than action read-aloud. Shorter
  sentences, more specific sensory details, longer silences.
  See `references/read-aloud.md`.
- **Anti-patterns**: jump scares in text form (ineffective without
  timing), gore as substitute for dread, revealing the monster too
  early, giving the players a weapon that cleanly solves the threat.

---

### Prompt 11 — `references/antagonist-design.md` [ ]

**Goal:** Deep antagonist and villain construction beyond the faction
Want/Method/View triplet. Covers motivation archaeology, the
mirror-protagonist principle, antagonist competence, and how to make
antagonists feel inevitable rather than arbitrary.

**File:** `skills/adventure-writing/references/antagonist-design.md`

**Content to include:**

- **The antagonist is not the villain**: the antagonist is the
  character or force whose interest most directly opposes the party's
  current action. A railroad company can be an antagonist without a
  named villain.
- **Motivation archaeology**: work backward from the antagonist's
  current action to the chain of decisions that made it inevitable.
  The chain should be at least three steps deep. If you can't answer
  "why are they doing this _now_?" the antagonist is arbitrary.
- **The mirror-protagonist principle**: the most resonant antagonists
  share a core value or desire with the party but pursue it through
  destructive means. Both the party and the antagonist want security;
  only one of them is burning people's homes for it.
- **Antagonist competence**: a competent antagonist adapts. If the
  party exposes their agent in Scene 2, they deploy a different agent
  by Scene 4. The antagonist has a response tree, not a fixed plan.
- **Antagonist hierarchy**: separate the visible instrument (the
  hired gun the party fights) from the organizing interest (the
  faction funding the hire) from the structural force (the
  economic/political pressure that makes the hire inevitable). All
  three tiers should be visible in the adventure by Arc III.
- **Antagonist presence before confrontation**: the antagonist's work
  is visible in consequences, not in person. Burned ranches, missing
  people, forged documents, bribes. The party feels the antagonist
  long before they meet them.
- **Antagonist perspective in the GM notes**: write one paragraph from
  the antagonist's point of view explaining why what they are doing
  is necessary and justified. This paragraph is not in the adventure
  text; it is in the GM notes. It makes the antagonist real to the GM.
- **Sympathetic antagonists and lost sympathy**: how to build an
  antagonist who is understandable through Arc I and unforgivable by
  Arc III. What action converts understanding to condemnation.
- **When the antagonist wins**: some end-states require the antagonist
  to succeed. The adventure must survive an antagonist victory with
  narrative weight. See `references/endings-and-sandbox.md`.
- **The antagonist's exit**: arrest, death, escape, or converted.
  Each exit has different sandbox consequences. All four should be
  possible, none required.

---

### Prompt 12 — `references/location-design.md` [ ]

**Goal:** Keyed location design — the art of writing a specific place
(building, camp, dungeon, ship, wilderness stretch) so that a GM can
navigate it spatially, discover its secrets, and have the location
feel real without a detailed map being mandatory.

**File:** `skills/adventure-writing/references/location-design.md`

**Content to include:**

- **What keyed location design is**: numbering or naming specific
  rooms, areas, or zones in a location and writing a short entry for
  each. Each entry is a self-contained scene seed.
- **The location entry format**: (1) What is immediately visible (one
  line), (2) What requires investigation (one to two lines), (3) Who
  or what is present and behaving how, (4) What exits exist,
  (5) One threat or opportunity tied to this space.
- **Environmental storytelling**: the location tells its own history
  through what is present, damaged, missing, or wrong. A room with
  a locked chest and a burned carpet tells a story. The GM reads the
  room; the players read the GM's description.
- **Density calibration**: how many entries per location type.
  A manor house: 8-15 entries. A ship: 6-10. A camp: 4-6.
  A wilderness stretch: landmark-based (one entry per named feature,
  not per acre).
- **The three-zone rule**: every interesting location has a public
  zone (safe, open, visible), a private zone (restricted, watched,
  or dangerous), and a hidden zone (secret, requiring effort to
  reach). Secrets concentrate in the hidden zone.
- **Secret placement**: put secrets in the hidden zone and in the
  private zone as partial truths. The public zone confirms the lie
  the antagonist is telling.
- **NPC placement in locations**: where each NPC physically is at
  the location's "default" state, before player action changes it.
  Movement is driven by player interaction and NPC motivation, not
  by scene triggers.
- **The living location**: a location should change between the
  party's visits. If the party leaves and returns, what changed? Who
  moved? What was removed? What was added?
- **Mapless design**: when a visual map is not available, the GM
  navigates using exit descriptions in each entry. "The east door
  leads to Entry 4 (the scullery). The back stairs lead to Entry 7
  (the locked study)." The party can map it themselves.
- **Dungeon vs. social vs. wilderness locations**: how location entry
  format adjusts for combat-focused vs. investigation-focused vs.
  travel-focused locations.

---

### Prompt 13 — `references/social-encounters.md` [ ]

**Goal:** Social scene design as a distinct encounter type. Covers
negotiation beats, persuasion structures, how social scenes generate
consequences without combat, and the kill list for social scene
anti-patterns.

**File:** `skills/adventure-writing/references/social-encounters.md`

**Content to include:**

- **What a social encounter is**: any scene where the primary agency
  is verbal or relational rather than physical. The party's choices
  are who to talk to, what to reveal, what to ask, and what to offer.
- **Social encounter grammar**: adapts the scene grammar from
  `references/scene-design.md`. Read-aloud is shorter (the NPC's
  opening line or posture). Ground truth adds what the NPC knows and
  what they want from this conversation. NPC behavior entry names
  the NPC's opening stance and two or three pivot points that shift
  their stance.
- **Pivot points**: specific things the party can say, reveal, or
  offer that change an NPC's stance. A pivot point is not a single
  correct answer — it is a threshold. "If the party demonstrates
  knowledge of the route forgery, this NPC's defensiveness cracks."
  Multiple approaches can reach the same pivot.
- **Stakes in social encounters**: social encounters that carry no
  consequence are filler. Every social encounter should shift at least
  one consequence track, reveal at least one piece of truth, or open
  or close at least one path.
- **Pressure as design tool**: social encounters under time pressure
  (a guard patrol is coming, the NPC has to leave in five minutes)
  generate the same tension as combat. Time limits enforce decision.
- **The social roll and fail-forward**: when a social roll fails, the
  NPC does not simply refuse. They respond to the failed approach with
  a counteroffer, a demand, a warning, or an escalation. Social
  failure is never a dead end.
- **NPCs with competing social agendas**: a scene with three NPCs who
  want different things from the party is richer than a one-on-one
  interview. Each NPC reacts to what the others reveal.
- **Interrogation scenes**: distinct from negotiation. The party has
  power; the NPC has information. The design challenge is: what is
  the limit of coercion, and what does going past the limit cost?
- **Social dilemmas**: every major social encounter should have at
  least one no-clean-option moment. The party cannot both tell NPC A
  the truth and protect NPC B.
- **Anti-patterns**: the monologue dump (an NPC gives a speech while
  the players listen), the single correct answer (only one phrase
  unlocks the NPC), the automatic failure (the party has no agency).

---

### Prompt 14 — `references/clocks-and-timers.md` [ ]

**Goal:** Countdown mechanics, villain timelines, and visible vs.
hidden pressure. How to build escalation into an adventure's structure
so that delay has consequences without forcing a fixed pace.

**File:** `skills/adventure-writing/references/clocks-and-timers.md`

**Content to include:**

- **What a clock is**: a named countdown attached to a faction,
  threat, or resource that advances when the party takes time, fails
  loudly, or makes specific choices. When the clock fills, the
  situation changes — not ends.
- **Three clock types**: (1) Villain timeline — the antagonist is
  doing something; each segment represents a completed step. (2)
  Resource clock — an NPC, location, or opportunity is deteriorating.
  (3) Discovery clock — the party's actions are leaving evidence; when
  the clock fills, the antagonist becomes aware of them.
- **Visible vs. hidden clocks**: visible clocks (the party knows the
  wagon train leaves in three days) create deliberate urgency. Hidden
  clocks (the antagonist is poisoning the water supply; the party
  doesn't know) create discovered urgency. Both are valid; mixing
  them produces the richest pacing.
- **Clock triggers**: when does a segment advance? Not randomly —
  on specific party choices or outcomes. "Every time the party rests
  for a full night, the villain's clock advances one segment." The
  trigger is stated in the clock's entry.
- **How many clocks**: one to three per adventure. More than three
  and the GM loses track. Less than one and the adventure has no
  structural urgency.
- **Clock cash-out**: when a clock fills, a specific consequence
  fires. The consequence is named in the clock's entry. It is not
  "game over" — it is a new situation that creates new pressure.
- **Clocks and consequence tracks**: clocks advance situations;
  tracks record relationships. They work at different registers. A
  clock can fire a track shift (the villain completing the route
  survey drops Army Respect by 1).
- **The open clock**: some clocks never fill within the adventure
  because players move fast. That's fine. An unfilled clock is a
  sandbox exit (see `references/endings-and-sandbox.md`): the
  antagonist's plan continues into the next chapter.
- **Anti-patterns**: the hidden clock that punishes without
  explanation, the clock that fills regardless of player agency, the
  single clock as the only pacing structure.

---

### Prompt 15 — `references/travel-and-wilderness.md` [ ]

**Goal:** Overland travel, hexcrawl and pointcrawl navigation,
landmark-based design, journey pacing, and the encounter table — how
travel becomes story rather than elapsed time.

**File:** `skills/adventure-writing/references/travel-and-wilderness.md`

**Content to include:**

- **Travel as story**: a journey is not dead time between scenes. The
  road has its own facts — weather, wildlife, infrastructure, the
  terrain's political meaning, the things that happen at the edges
  of civilization.
- **The journey beat**: a specific moment within a travel stretch
  that carries weight. Not every journey has a beat; not every beat
  is a combat. Journey beats include: a body on the road, an
  unexpected meeting, a terrain feature with tactical or political
  significance, a night of weather.
- **Three travel structures**:
  - **Linear travel** (the column marches from A to B): use journey
    beats to break the march. One beat per day of travel. Beats are
    drawn from a shelf (like camp scenes).
  - **Pointcrawl**: named locations connected by labeled paths.
    Each path has a distance (in days or encounters) and a travel
    hazard. Players navigate by choosing which path to take.
  - **Hexcrawl**: a spatial grid. Each hex contains terrain and
    optionally a keyed location or encounter. Players navigate by
    direction, not destination.
- **Landmark-based navigation**: for adventures without a hex map,
  use named landmarks as waypoints. The party moves from landmark to
  landmark. Each landmark has an entry (visible features, hidden
  features, threats, opportunities).
- **The encounter table**: system-agnostic encounter table design.
  Entries should be situations, not just creatures. Mix: hostile
  encounter / neutral NPC / environmental hazard / discovery / clue
  delivery / faction event. The table is a pacing tool, not a
  random damage generator.
- **Journey compression**: for long journeys that don't warrant beat-
  by-beat coverage, use the montage paragraph (two to four sentences
  of sensory travel prose followed by one consequence: "By the third
  day, the flour is damp."). See `references/pacing-and-arcs.md`.
- **Terrain as encounter design**: terrain shapes tactics, costs,
  and opportunities. List three to five terrain effects per major
  travel zone. See `references/combat-encounters.md` for terrain
  in combat; this file covers terrain in navigation and discovery.
- **Weather as pacing**: weather changes pace, cost, and mood. A
  storm slows the column, spoils supplies, creates cover for an
  ambush, and grounds aircraft. Build a simple weather system (1d6
  with named outcomes) for each chapter's travel season.
- **Navigation failure**: getting lost is a story generator, not a
  punishment. A party that misreads the trail and arrives at the
  wrong landmark has found an unscheduled node — give it content.

---

### Prompt 16 — `templates/investigation-skeleton.md` [ ]

**Goal:** A blank scaffold for investigation and mystery adventures.
Parallel in structure to `templates/chapter-skeleton.md` but
reorganized around the investigation arc: the crime, the investigation
nodes, the suspect web, and the resolution.

**File:** `skills/adventure-writing/templates/investigation-skeleton.md`

**Content to include:**

- Inline guidance for every section in `references/investigation-structure.md`.
- Sections: Cold open / Stakes / Historical frame / Shape of it /
  The crime (perpetrator timeline) / Suspects web / Clue distribution
  table (listing each critical fact and its three minimum carriers) /
  Investigation nodes (each with: entry condition / clues / suspect
  behavior / exits / what changes) / Timeline clock / NPC cast /
  Social encounter entries / Horror or tension arc (if applicable) /
  Verification scenes / Resolution conditions / Reckoning / Sandbox
  exits.
- Pre-publish audit checklist adapted for investigation adventures.

---

### Prompt 17 — `templates/one-shot-skeleton.md` [ ]

**Goal:** A blank scaffold for self-contained one-shot adventures.
Compressed version of `templates/chapter-skeleton.md` with tighter
scene density, single-session pacing, and a streamlined cast.

**File:** `skills/adventure-writing/templates/one-shot-skeleton.md`

**Content to include:**

- Scope block (session length target, word count target).
- Cold open / Stakes / Cast (4-6 NPCs max, each with the five-sentence
  template) / Single arc / Dilemma (one central dilemma, no arc
  subdivisions) / Reckoning (two to three end-states, simpler than
  the campaign chapter's four-axis reckoning) / Sandbox hooks (two
  to three potential follow-up seeds, not required for session).
- Note on compression: one-shots cannot carry all of architecture.md's
  sections. The note names which sections can be dropped and which
  are mandatory even in compressed form (non-negotiables: cold open,
  stakes, three clues per fact, dilemma, at least two endings).
- Pre-publish audit checklist adapted for one-shots.

---

## Completion Criteria

This TODO is complete when:

1. SKILL.md contains 17 workflow steps and library entries for all
   listed files (Prompt 1 ✓).
2. All Phase 0 reference files exist:
   `scope-and-format.md`, `research-pipeline.md` (Prompts 2-3 ✓).
3. All Phase 3 files exist: `playtesting.md`, `feedback-collection.md`,
   `feedback-form.md`, `learnings/README.md` (Prompts 4-7 ✓).
4. All new design domain references exist: `investigation-structure.md`,
   `node-based-design.md`, `horror-design.md`, `antagonist-design.md`,
   `location-design.md`, `social-encounters.md`, `clocks-and-timers.md`,
   `travel-and-wilderness.md` (Prompts 8-15 ✓).
5. New templates exist: `investigation-skeleton.md`,
   `one-shot-skeleton.md` (Prompts 16-17 ✓).
6. The `learnings/` folder exists with `README.md` and is empty of
   adventure-specific entries pending first playtest.

Total new files: 17 (1 SKILL.md edit + 16 new files).
