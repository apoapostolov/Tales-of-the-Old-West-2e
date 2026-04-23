# Factions and Tracks — The Consequence Ledger

This file defines the system-agnostic mechanism that makes
player choices durable. The mechanism is simple: three or four
named counters, each shifting `+1` or `-1` per significant
choice, cashed out at the reckoning.

The mechanism is small on purpose. Players should not be
managing a dashboard. The GM tracks the ledger; the players
feel the weight in NPC behavior.

## Why a ledger at all

Without tracks, the GM has two bad options:

1. **Score every choice mentally** — fragile, inconsistent
   between sessions, prone to the GM's mood.
2. **Pre-script the ending** — players' choices retroactively
   meaningless.

A ledger of three or four named tracks gives the GM a
defensible record. The reckoning falls out of the totals; the
GM does not have to "decide" who wins.

## Designing the tracks

### How many

**Three or four. Never two. Never five or more.**

- Two tracks force a binary morality. The chapter feels like
  a dial between "good" and "evil."
- Five or more overload the GM. They become bookkeeping
  instead of texture.
- Three tracks fit on a sticky note. Four is the upper limit
  for any working memory.

### What each track names

A track names a **relationship** or a **resource**, not a
virtue.

Good tracks:

- `Army Respect`
- `Survey Leverage`
- `Crow Trust`
- `Local Goodwill`
- `Court Favor`
- `Cartel Standing`
- `Guild Influence`
- `Black Market Credit`
- `Witness Network`

Bad tracks (avoid):

- `Honor` — abstract virtue. What does +1 honor mean?
- `Reputation` — too broad. Reputation with whom?
- `Karma` — unfalsifiable.
- `Heroism Points` — names the player, not the world.

The right track lets the GM say: _"Captain Rowe heard about
Hannah's ranch. Your `Army Respect` is high enough that he
listens. He would not listen if it were lower."_ The wrong
track requires the GM to invent that connection on the fly.

### Coverage rule

Together, the tracks must cover all the major factions in the
chapter. If one of your factions is not represented by a track,
players who interact with it have no measurable consequence.

A typical four-track set:

- One for the **legitimate authority** in the situation.
- One for the **opposed agenda** (private interest, criminal
  network, political faction).
- One for the **outsider faction** (Native nation, foreign
  power, supernatural court).
- One for the **grounders** (locals, victims, witnesses, the
  people who live there).

Adjust for genre. A heist chapter might use:

- `Crew Trust`, `Mark's Suspicion`, `Fence Standing`,
  `Patron Favor`.

A horror chapter might use:

- `Town Trust`, `Cult Awareness`, `Survivor Bond`,
  `Reality Erosion`.

## Writing the ledger section

In the chapter's "Consequence Ledger" section
(see `references/architecture.md`), include three things:

### 1. The principle paragraph

One paragraph stating the system. Names the tracks. Names that
they start at zero. Names that the reckoning cashes them out.

> Track party standing with four groups: `Army Respect`,
> `Survey Leverage`, `Crow Trust`, and `Local Goodwill`.
> Start each at `0`. When players make a hard choice, shift
> the tracks `+1` or `-1`. The ride back into settlement
> cashes the totals.

### 2. The high/low effects

For each track, one short sentence on what high standing
means and one on what low standing means. Be concrete:
specific NPCs, specific access, specific opportunities.

> High `Army Respect` opens Fort Ellis work and legal shelter.
> Low scores build walls, ruin credit, and run bad stories
> ahead of them.

### 3. The faction-action bullets

A bulleted list naming how each faction's agents _behave_
based on the track. This is the GM's reference card.

> - High `Army Respect` pushes Rowe to grant freedom, ask
>   judgment, and offer escort work.
> - Low `Army Respect` draws Harlan's watch, hardens orders,
>   and strips lawful shelter.

The bullets must reference specific NPCs by name. Generic
"the Army respects you more" is useless. "Rowe asks your
judgment" is actionable.

## Shifting tracks at the table

### When to shift

Shift on **decision**, not on **outcome**.

A player who decides to betray Hannah Calder loses
`Local Goodwill` whether or not the betrayal succeeds, whether
or not Hannah survives, whether or not she finds out. The
character has revealed something.

A player who _fails_ to protect Hannah from a Lakota raid
because they were outnumbered does not lose `Local Goodwill`.
The intent was honorable; the dice were bad. The chapter does
not punish bad rolls with track shifts.

### How much to shift

`+1` or `-1`. That is the standard.

`+2` or `-2` only for choices that are _flagged in the
chapter text_ as catastrophic or transformative. For example:
"If they sell Keene to Vane, `Local Goodwill -2`."

Never shift `+3` or higher. If a choice feels that big,
break it into multiple choices each shifting `+1`.

### When to tell the players

Players should _feel_ their standing through fiction, not see
the numbers.

- NPCs from a high-standing faction become more open, offer
  more help, share rumors more willingly.
- NPCs from a low-standing faction become curt, charge more,
  refuse favors, send watchers.

If a player asks "what's our standing with the Army?" the
answer is a fictional vignette: _"Sergeant Duffy nods to you
across the parade ground. Last week he didn't."_ Not a number.

Some tables prefer the numbers visible. That is a table
choice, not a chapter choice. Write the chapter for invisible
tracks; let the GM choose to expose them.

## Cashing the ledger

At the reckoning, the totals determine which end-state plays.
See `references/endings-and-sandbox.md` for the full
treatment.

The cash-out rule of thumb:

- **Highest track** determines the dominant end-state.
- **Lowest track** determines the dominant cost.
- **Combined positive** opens a coalition ending.
- **Combined negative** opens a fugitive ending.

Example:

- Highest: `Crow Trust +3` → Crow Understanding ending plays.
- Lowest: `Army Respect -2` → cost: military hostility,
  legal exposure.
- Combined positive: `Local Goodwill +2`, `Survey Leverage
+2` → coalition: ranchers and surveyors back the party in
  Bozeman.

Write the end-states to support these readings.

## Faction Want / Method / View

For each faction, the chapter must state three things in plain
language. The cleanest place is the "What the Main Factions
Want" section.

### Want

What does this faction want by the end of the chapter? One
sentence.

> _Rowe and the Army:_ Rowe wants the column out and back
> cleanly.

### Method

How will they pursue it? What pressure will they bring? One
sentence.

> _He refuses fraud or pointless death._

### View / Offer / Cost

What does the faction offer the PCs, and what does it cost
them?

> _Helping him earns trust. Tainting the expedition forces
> him between truth and career._

The triplet (Want / Method / View) governs every NPC who
serves that faction. When the GM forgets why an NPC is doing
something, they reread the triplet.

## Conflicting wants

The chapter is interesting because the wants conflict. A
useful diagnostic: write the wants of all factions on one
page. Draw a line between any two wants that are mutually
exclusive.

If the page has fewer than three lines, your factions are not
in enough tension. Add pressure points until the page is
crisscrossed.

## Wants must be visible to players

A faction whose want is hidden until the reckoning is a
twist, not a faction. Players cannot make informed choices
about wants they cannot see.

By the end of the second arc, every faction's want should be
visible to a careful party. Hidden wants belong to individual
NPCs (Mercer's panic, Vane's specific buyer), not to factions.

## The ledger as memory

A side benefit of the ledger: it is the chapter's institutional
memory. When the party returns to this territory in three
sessions, the GM reads the final track totals and knows
exactly how the world greets them.

Save the totals in your campaign notes. The ledger is the
bridge to every future chapter set in the same territory.
