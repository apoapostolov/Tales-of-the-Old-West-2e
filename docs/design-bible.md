<!-- markdownlint-disable MD013 MD041 -->

# Design Bible — Tales of the Old West 2E

A living, agnostic reference for the engine. Written so that any future
work — a new chapter, an audit, a conversion, a fresh agent in a fresh
session — can read this and produce rules that belong in the same book.

This is not a chapter of the game. It is the engineering spec under the
prose. Where this document and the corebook disagree, the corebook wins;
update this document.

---

## 1. What the game is, and what it wants

**Engine:** Year Zero (Free League) D6 dice pool. Roll attribute +
ability + modifiers in D6s. Every 6 is one success.

**Attributes (1–5, healthy minimum 2):** each is also a damage track that
counts down to **Broken**.

| Attribute | Means | Damage type | Broken by |
| --- | --- | --- | --- |
| GRIT | resilience, strength, presence of body | Hurts | Hurts |
| QUICK | dexterity, hand-eye, coordination | Shakes | Shakes |
| CUNNING | instinct, common sense, woodcraft | Vexes | Vexes |
| DOCITY | learning, recall, applied knowledge | Doubts | Doubts |

**Abilities (0–5):** sixteen, four per attribute.

| GRIT | QUICK | CUNNING | DOCITY |
| --- | --- | --- | --- |
| FIGHTIN' | LIGHT-FINGERED | ANIMAL HANDLIN' | BOOKLEARNIN' |
| LABOR | MOVE | HAWKEYE | DOCTORIN' |
| PRESENCE | OPERATE | INSIGHT | MAKIN' |
| RESILIENCE | SHOOTIN' | NATURE | PERFORMIN' |

**Talents:** specialized edges, ranked **Basic** and **Advanced**. ~50 in
the corebook (`01-corebook/04-talents.md`). Names referenced by new
subsystems must already exist unless a new talent is explicitly being
proposed.

**Faith / Big Dream / Relationships / Pardner:** the narrative layer that
feeds the engine. Faith is a spendable point resource; the others are XP
and scene-fuel.

### What the game wants

The game wants scarcity, distance, and the cost of violence on the table.
It does not want heroism as a default. It wants a man who draws his gun to
be calculating the price of it, a rider who pushes his horse to know the
horse may not make the next water, a town that grows because people paid
for it in tally points and seasonal labor. The engine rewards the
*decision that cannot be taken back* and charges interest on every
shortcut. New rules should make the country harder and the choices
sharper, never safer.

---

## 2. The resolution vocabulary

### The success ladder

| Successes | Result |
| --- | --- |
| 0 | failure; pay for it |
| 1 | **limited** — get the goal, but not cleanly; pay in time/money/goodwill/safety |
| 2 | **full** — get the goal at no further cost |
| 3+ | full, plus something extra (better terms, a contact, pressure shifted) |

This is the **default** reading for a single acting-hand roll. It is
applied so consistently that a new subsystem should reach for it before
inventing any other outcome scheme.

### Pushing

Reroll non-6s once. Costs **1 Faith point**. Can generate Trouble.

### Trouble — the signature pressure

The GM tags a roll **Safe / Risky / Desperate**. The player rolls the
normal pool; Trouble is then computed from the failures:

| Tag | On 0 successes | Each rolled `1` | Note |
| --- | --- | --- | --- |
| Safe | none | none | unless the fiction is plainly loud |
| Risky | +1 Trouble | every two `1`s → +1 Trouble | successful rolls usually ignore `1`s |
| Desperate | +1 Trouble | each `1` → +1 Trouble | |
| Pushed & failed | +1 additional Trouble | | stacks on the above |

A pushed check that still fails adds one more Trouble. Successful Risky
and Desperate rolls *usually* ignore the `1`s unless the fiction says the
win was loud, bloody, or compromising. The pressure is the rule: Trouble
is the GM saying "this is getting away from you."

### Hidden Bad Luck

A GM-side secret pool, built from compounded bad player decisions (at
least two, usually), spendable later as penalty dice, Trouble, or a bad
situational turn. Use it where player recklessness should pay out as
consequences rather than be retconned.

### Modifier discipline

| Rule | Value |
| --- | --- |
| Bonus dice cap | +3 |
| Penalty dice cap | −3 |
| Help another | +1, costs an action, requires ≥1 ability |
| Group roll | lead/highest/lowest ability per the case |

**Do not stack every possible factor.** Apply the one or two that make
the moment dangerous and real. The outlaw chapter says it plainly: pick
the ones that matter.

### Difficulty ladder

Bonus/penalty dice, capped ±3. The difficulty is a number of dice added
or removed, not a target number. There is no target-number system.

---

## 3. The two resolution modes

### Mode A — the single check

One acting hand rolls. Read on the 0/1/2/3 ladder. Use for any
discrete action whose outcome is genuinely uncertain and whose
consequences can be named in one breath.

### Mode B — the Progress-vs-Trouble operation

Use when a scene is a linked sequence of situations and one roll is a
shrug. The spine of the outlaw chapter's scores, and the spine of most
new subsystems in this supplement.

Two parallel tracks:

- **Progress** — accumulate successes toward a target.
- **Trouble** — a pressure track; failures and rolled `1`s push it
  toward a limit. When Trouble hits the limit, the plan as intended is
  dead even if escape or partial gain is still possible.

| Operation scale | Progress needed | Trouble limit |
| --- | --- | --- |
| Small | 4 | 3 |
| Medium | 6 | 4 |
| Big | 8 | 5 |

Calibrated so a normal operation takes **about 3 to 6 checks**. If a plan
needs more, split it into phases or two linked operations.

Per-check flow:

1. GM names the immediate problem.
2. Players say how they mean to handle it.
3. GM tags the attempt **Safe / Risky / Desperate** (see §2).
4. One acting hand rolls the most relevant ability.
5. Add successes to Progress. Compute Trouble from the tag and the `1`s.
6. Read Trouble on the pressure ladder when it climbs.

The Trouble pressure ladder (the canonical wording):

| Trouble | Effect |
| --- | --- |
| 1 | minor alarm, delay, a wounded hand, a lost opportunity |
| 2 | somebody notices, a witness survives, the path narrows |
| 3 | heat rises, stock suffers, the law closes a road or town |
| 4+ | the job turns into a chase, fight, split, or disaster |

### When to use which

- One action, one consequence → **Mode A.**
- A heist, a drive, a trial, a siege, a flight → **Mode B.**
- Don't reduce a rich scene to one roll, and don't bloat a simple one
  into an operation.

---

## 4. The gauge catalog

The engine runs on small integer gauges and one stepped die. **Invent no
new gauge size.** If you need a tracker, it should fit one of these
shapes.

| Gauge | Range | Baseline | What it is |
| --- | --- | --- | --- |
| Cohesion (gang, unit) | 1–5 | 3 | how close a body holds together |
| Refuge (a settlement) | −2 to +2 | 0 | how one place stands with you |
| Fence Access | 0–2 | 0 | can you move hot goods |
| Horsestock | 0–4 | — | the band's mounts as a resource |
| Hideout Rating | 1–5 | — | enemies need N successes to find it |
| Loyalty (notable member) | 0–3 | — | a follower's bond |
| Standing (faction) | −3 to +3 | 0 | how a faction regards the party |
| Town Aspect rank | 1–6 | — | Farming/Mercantile/Natural Riches/Law/Civic/Welfare |
| Prosperity | 6–36 | — | sum of the six aspect ranks |
| Tally Points (per aspect) | 1–30+ | — | amenities grant them; rank is derived |
| Provisions (optional) | D4→D6→D8→D10→D12 | D10 | resource die; 1–2 steps down; D4 rolling 1–2 = exhausted |

**The gauge discipline:**

- A new subsystem that tracks a relationship uses a ±2 or ±3 band.
- A new subsystem that tracks a body of people uses a 1–5 Cohesion.
- A new subsystem that tracks consumables uses the stepped die.
- A new subsystem that tracks a town-scale quality uses rank 1–6 and
  feeds Prosperity.

### The aspect-rank → modifier ladder

| Aspect rank | Modifier |
| --- | --- |
| 1 | −2 |
| 2 | −1 |
| 3 | 0 |
| 4 | +1 |
| 5 | +2 |
| 6 | +3 |

Rank 3 is the baseline. This ladder is applied wherever a town aspect
bears on a roll. Reuse it; do not invent a parallel one.

---

## 5. The table formats (clone these)

### Critical Injury Table — 7 columns

```
| Roll | Location | Injury | Fatal | Healing Time | Immediate Effect | Long-term Effect |
```

- **Roll** — D66, grouped by body region (11–16 leg, 21–26 upper leg,
  31–36 arm, 41–46 gut, 51–56 chest, 61–66 head).
- **Fatal** — `No`, or `Yes` + interval (`Yes -1/D6 Rounds`, `Yes / D6
  days`, `Yes / Instant`).
- **Healing Time** — die + unit (`D6 days`, `3D6 days`, `D6 weeks`).
- **Immediate Effect** — penalty text.
- **Long-term Effect** — `None`, or a permanent consequence.

A Called Shot crit rolls only the Units die (location is set).

### Fortune tables — D66 + prose

```
| D66 | <Fortunes> |
```

- Single prose column.
- Bands: a leading **01–06** bad band, then **11–66** standard, then
  **71–76** premium.
- **11 = Calamity!** — "Roll D66 again, the Tens die is automatically 0."
- **66 = Jackpot!** — "Roll D66 again, the Tens die is automatically 7."
- A natural 11 or 66 always counts as that result regardless of
  modifications.
- Self-modifies via an aspect: e.g. Welfare 1–2 → −1 Tens, Welfare 5–6
  → +1 Tens.

### Business Bonus / Penalty — 3-column D66

```
| D66 | Business Bonus | Business Penalty |
```

- D66 keyed in bands (11–16, 21–23, 24–26, … 64–66, 71+).
- Penalty column has no 71+ entry.
- Built so a good season rolls the Bonus column and a bad one rolls
  Penalty.

### Wildlife stat table — 8 columns

```
| Animal | Grit | Quick | Cunning | FIGHTIN' (Grit) | MOVE (Quick) | HAWKEYE (Cunning) | Attacks |
```

- The attribute columns pair with a parenthesized base ability.
- **Attacks** is free text, embedding **Toughness** where it applies:
  "Bite: Damage 2, Crit 1; Toughness: 1."
- Toughness = dice rolled; each success reduces incoming damage by one.

### Animal Critical Effect — D66 bands

```
| D66 | Critical effect |
```

- Bands split each tens-group low-three / high-three: 11–13, 14–16,
  21–23, 24–26, … 64–66.

### NPC statblock — the 8-column grid

Fixed structure. Never list attributes as flat columns.

```
| GRIT | <v> | QUICK | <v> | CUNNING | <v> | DOCITY | <v> |
| ---- | --- | ----- | --- | ------- | --- | ------ | --- |
| PRESENCE   | <v> |           |     | HAWKEYE    | <v> |            |     |
| RESILIENCE | <v> |           |     | INSIGHT    | <v> |            |     |

**Talents:** NAME (rank), NAME (rank).
```

Abilities sit under their attribute's column:

- GRIT: FIGHTIN', LABOR, PRESENCE, RESILIENCE
- QUICK: LIGHT-FINGERED, MOVE, OPERATE, SHOOTIN'
- CUNNING: ANIMAL HANDLIN', HAWKEYE, INSIGHT, NATURE
- DOCITY: BOOKLEARNIN', DOCTORIN', MAKIN', PERFORMIN'

Talents go in a standalone bold line *after* the table (markdown tables
cannot colspan). A weapon line may follow, columns:
`Action | Draw Mod | Attack Mod | Damage | Critical | Range | Ammo`.

Simple animals (wolves, dogs) use a simpler inline table, not this grid.

### Pursuit / Escalation / Gang Trouble — small D6/D66 tables

Two-column `| D6 or D66 | result |`, grouped 3-wide per tens digit when
D66. One-sentence results that name a concrete consequence.

---

## 6. The downtime spine — Turn of the Season

The season (3 months; four per year) is where the long arc lives. Resolve
in this order:

**Looking Back**

1. Apply Amenity Modifiers.
2. Season Business Rolls (outfits).
3. Season Congregation Rolls (preachers).

**Looking Forward**

4. Choose New Town Amenities.
5. Lifestyle (pay up-front).
6. Personal Fortune Rolls (each player, D66, modified by Welfare).
7. Town Fortune Rolls (D66, modified by Prosperity).

### The Season Business Roll

- Proprietor rolls the business's **key ability**.
- Pool: key ability + help dice (max +3) from owners/employees/compadres
  + Competition modifier (−2 to +2) + town Law modifier + relevant
  aspect modifier.
- **Cannot be pushed. No Trouble.**
- 0 successes → roll the Penalty column.
- 1 success → steady; wages paid.
- 2+ successes → roll the Bonus column, +1 to the Tens die per success
  beyond the first.

This is the template for any **seasonal enterprise roll** in a new
subsystem (a ranch, a mine): key ability, help dice, town-aspect
modifiers, the 0/1/2+ ladder, a Bonus/Penalty D66.

### The Investment Cycle

The Season Business Roll above is the **reckon** beat of a larger
five-beat cycle every business in Book 4 runs on. The cycle is the
org-lifecycle pattern (`yze-design/references/07`) calibrated to the
season; it wraps the existing roll rather than replacing it, and it
gives the proprietor agency over the dials the roll reads against.

```
1. ASSESS   — read the market, the season, the gauges; decide the season's strategy
2. INVEST   — spend Capital/cash/resources to set the season's dials
3. OPERATE  — the working phase (events, trouble, the season's play)
4. RECKON   — the Season Business Roll, read against the dials set in step 2
5. REINVEST — pay out, recover, or reinvest into functions/growth
```

The beats are shared. The **dials** and the **currency** differ by trade.
A ranch invests in stock and grass; a mine invests in timber and powder;
a saloon invests in stock and reputation. The Reckon beat is where the
die rolls, but the die rolls *against the dials the proprietor set* —
not a flat ability check. Each business chapter (Ch.4–9) restates and
skins these beats in its own trade's vocabulary, names its distinct
resource as the cycle's dial, and defines its distinct loop at the
Operate beat. A chapter that only points the reader here has missed the
point: the cycle lives in the chapter, flavored to the trade.

### How Fortune rolls self-modify

Personal Fortune → Welfare. Town Fortune → Prosperity. The modifier
table is asymmetric and worth re-reading each time:

| Prosperity | Modification |
| --- | --- |
| 10 or less | −2 to Tens die |
| 11–14 | −1 to Tens die |
| 15–18 | −3 to Unit die (min 1) |
| 19–23 | none |
| 24–27 | +3 to Unit die (max 6) |
| 28–31 | +1 to Tens die |
| 32+ | +2 to Tens die |

Low and high Prosperity hit the Tens die; the middle bands hit the Units
die with a clamp. Personal Fortune (Welfare) is simpler: 1–2 → −1 Tens,
5–6 → +1 Tens.

---

## 7. The integration map

Nothing in this engine stands alone. A new rule plugs into this map at a
known node; it does not build a new one.

```
outlaw gang ──► town aspects (Law, Mercantile, Civic, Welfare)
      │              │
      │              ▼
      │        Turn of the Season ──► Fortune rolls ──► Fame & Reputation
      │              │
      ▼              ▼
   Wanted ──► pursuit (Hard Ride) ──► Refuge / Horsestock / Cohesion
      │
      ▼
   capture ──► (JUSTICE fills this gap) ──► sentence / jailbreak / pardon
```

- **Town aspects** (Ch.8) gate availability, fence access, and season
  rolls. A new subsystem that touches a settlement reads its aspects.
- **The season** (Ch.8) is the heartbeat. A new enterprise, pressure, or
  recurring event should resolve in the season where possible.
- **Fame & Reputation** (Ch.6) are the long-term face a character wears.
  Dangerous Fame can sour "decent" factions and warm outlaw ones.
- **Wanted** (Ch.11 outlaw) is a three-tier pursuit ladder that currently
  ends at capture. Justice extends it.
- **Cohesion / Refuge / Horsestock** (Ch.11) are the outlaw's gauges. A
  new subsystem that tracks a body, a place, or mounts should reuse these
  shapes.

### What the supplement plugs in

- **Factions & Standing** — a new node, but it reads town aspects and
  Fame, and it is consumed by Justice, Mining, Cattle, and Mass Combat.
- **Weather** — feeds the existing conditions (Freezing, Heatstroke,
  Exhausted) and the Traveling table; does not add new conditions.
- **Justice** — extends Wanted past capture; reads town Law/Civic; uses
  social-conflict resolution.
- **Train Robbery** — a new operation type; feeds Wanted; reads the
  railroad as a faction.
- **Cattle Drives** — a new operation type + a seasonal enterprise roll;
  reads town Natural Riches/Farming.
- **Mining Claims** — a new seasonal enterprise roll + a prospecting
  procedure; reads town Natural Riches/Civic.
- **Mass Combat** — reuses Cohesion and the Morale & Rout tiers;
  attaches PCs as help dice.

---

## 8. Design standards

From `skills/western-rpg-design/SKILL.md`. A rule is good when:

- it produces a clear table behavior, not just evocative text;
- it uses existing terms unless there is a strong reason to add one;
- it creates a meaningful decision or pressure point;
- it does not silently break an adjacent system;
- it fits the harsh, practical frontier-survival logic;
- if it increases realism, it still preserves playability and campaign
  function.

### The design method (per mechanic)

1. **Rule loop** — trigger → player decision → roll → consequence →
   downstream state change.
2. **Design purpose** — what behavior it encourages, what pressure it
   creates, what table feeling it supports.
3. **Integration map** — linked chapters, linked subsystems, terms that
   must stay consistent.
4. **Table behavior** — player-facing complexity, GM burden, speed in
   live play, ambiguity risk.

### Proposal review checklist

- rules completeness
- cross-chapter integration
- recoverability and permanence logic
- player agency after the rule lands
- whether catastrophic outcomes are playable, retirement-default, or dead
  ends
- whether the text belongs in proposal space or final manuscript space

---

## 9. The feel — prose register and what the engine rewards

### What the engine rewards

- The **cost of safety.** A night in town costs money (Lifestyle). A
  strongbox costs Capital. A good horse costs Horsestock. Nothing is
  free; the cheap path is the dangerous one.
- The **decision that cannot be taken back.** A drawn gun, a cheated
  split, a man left behind, a town crossed. The engine makes these hurt
  via Reputation, Wanted, Cohesion, Standing.
- **Attrition over climax.** Conditions, Provisions, Horsestock, and
  Trouble erode a character and a gang long before the gunfight. The
  wise table sees the erosion coming.
- **The world acting back.** Fortune rolls, Faction clocks, Wanted
  escalation — the country does not wait for the player characters.

### The prose register (summary; full rules in the western-writing skill)

- **No mood without object.** Every atmospheric line carries a physical
  noun.
- **No paragraph without a job.** Name the job before writing the
  paragraph.
- **No synonym cycling.** A revolver is a revolver. Game terms never
  vary.
- **End on weight** — concrete nouns, bodily consequence, hard verbs,
  material fact.
- **No anachronism of mind.** Characters feel shame, anger, grief, lust,
  fear, hunger, thirst, the cold. They do not "process" or "set
  boundaries."
- **No clean violence.** The body is meat.
- **No designer jargon, no safety scaffolding, no AI tells.**
- **No therapy, no corporate, no blog diction.** The kill list:
  meaningful, impactful, engage with, it's worth noting, basically, in
  other words, the key takeaway, journey, navigate, unpack, dive into,
  reach out, leverage, holistic, wellness, resonate.

### The manuscript chapter architecture (clone it)

1. Epigraph (an in-world quote, italic blockquote).
2. "X and Their Trade" — the lead paragraph(s) that frame what the
   chapter is and when to use it.
3. Optional / when-to-use callout.
4. Gauges, defined one at a time with a ladder table.
5. Core procedures, each as: trigger → roll → ladder.
6. Worked-fiction blockquote showing the rule in the flesh.
7. GM advice — short, at the place the concern arises, never a
   "Guardrails" section.
8. Tables and seeds last, where a table is the cleanest expression.

### Vignette and dialogue rendering

- The blockquote (`>`) renders italic by default. **Do not wrap the
  whole vignette in `_underscore_` italics** — it is redundant and
  flattens the prose into an undifferentiated slab.
- Wrap only **pure narration** in `_..._` when you want it set apart
  from dialogue within the same blockquote. Narration without
  underscores is also fine; the blockquote's italic carries it.
- **All speech uses proper English quotation marks** (`"..."`) with
  standard dialogue tags (`he said`, `she said`), never bare clauses
  buried in italic. Inside an italic blockquote, the quoted lines
  render upright against the italic narration, which is the point —
  the reader can tell a spoken line from a narrated one at a glance.
- Inline game terms (`Standing`, `Pressure`) inside a narration line
  use `_..._` to **de-italicize** them (italic-within-italic cancels
  to upright), which makes the term stand out from the surrounding
  italic prose. This is the intended emphasis and should be kept.
- No integration/technical suffix section at the chapter's end. The
  chapter closes on a short narrative paragraph that lands on weight,
  not on a list of what it reads and feeds.

---

## 10. A note on tone for new work

The country is dry, hard, and indifferent. The rules should feel that
way too: short sentences, concrete nouns, the verb doing the work. A new
chapter is not a place to show range. It is a place to make the next
scene at the table run without interpretation drift, and to make the
weight of the choice land on the player, not the page.
