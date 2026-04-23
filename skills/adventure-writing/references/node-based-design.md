# Node-Based Design

A node is a unit of adventure: a location, a scene, a
named encounter — any discrete thing the players can
interact with. Node-based design treats the adventure
as a map of connected units rather than a linear
sequence of events.

The three-act arc from `references/pacing-and-arcs.md`
describes _rhythm_ — the rise and fall of pressure.
Node design describes _structure_ — the shape of what
the players can reach and in what order.

They are compatible. Use the three-act arc for pacing
rhythm; use node design for scene structure within
each act.

## What a node contains

Every node has five components:

1. **Entry condition**: how do the players reach this
   node? Via a specific location, a specific NPC contact,
   the results of a previous scene, or freely (the node
   is always accessible)?
2. **Information**: what facts, clues, or world-state
   does this node contain? Which are freely visible?
   Which require investigation, persuasion, or force?
3. **Choices**: what can the players decide or do here?
   What are the decision surfaces?
4. **Exit paths**: where can the players go from here,
   and what does each exit require or reveal?
5. **What changes on a return visit**: if the players
   come back to this node, what is different?

A node with no exit paths is a dead end. Every non-final
node must have at least two exits.

## Node types

**Information nodes**: deliver a fact, a clue, or
context. The player action that unlocks the information
can be observation (free), conversation (social roll
or approach), or investigation (skill check or
physical search). Information nodes are the backbone
of investigation adventures.

**Decision nodes**: present a moral or practical
choice with no clean option. Both paths have costs.
See `references/dilemmas.md` for the no-clean-option
principle. Decision nodes are the emotional heart of
the adventure.

**Encounter nodes**: a conflict, confrontation, or
challenge. Not necessarily combat — a hostile negotiation
is an encounter node. What distinguishes it: the players
face active resistance, not passive information.

**Hub nodes**: a location or scene from which the
players can reach multiple other nodes. The town
square, the saloon, the sheriff's office. Hub nodes
provide orientation and player agency. An adventure
with no hub nodes is hard to navigate.

Every adventure should have at least one hub node per
act. The hub node is where the party reassembles, plans,
and chooses their next direction.

## Designing backward

Start with the final node — the reckoning, the
confrontation, the revelation — and work backward.

Ask: what must the players know to arrive at this
final node with agency? What information, decisions,
and encounters are prerequisites?

For each prerequisite, build a node. For each of those
nodes, ask the same question. Stop when you reach nodes
that have no prerequisites — these are your entry nodes,
the scenes where the adventure begins.

Designing backward prevents a common error: building
the early scenes first without knowing what they must
deliver. Early scenes built without knowing the final
node often deliver nothing useful.

## Floating clues

A floating clue is a critical piece of information that
is not locked to a single node. It can appear at any
node where its presence is plausible.

Why floating clues exist: in a branching adventure,
players will miss nodes. A player group that bypasses
the mill and never recovers a fact locked there has
hit a single-point failure — the adventure is blocked.

A floating clue eliminates single-point failures for
critical information. If the players miss the mill
(the first carrier), the clue surfaces at the next
relevant node they visit.

**Rules for floating clues:**

- Float only critical facts (facts the adventure
  cannot function without). Non-critical clues can be
  locked to specific nodes.
- The clue's appearance at a secondary node must be
  plausible — it doesn't materialize from nowhere.
  The GM uses the environment to surface it. (The
  storekeeper who trades with the mill mentions it
  in passing; the clue arrives through a different
  carrier.)
- The adventure never retcons what the players have
  already seen. Floating applies to what hasn't been
  reached, not to what has.

See `references/clue-discipline.md` for the three-clue
rule and carrier-redundancy mechanics. Floating clues
are the runtime implementation of that rule.

## Chokepoints

A chokepoint is a node that every branch must pass
through. Use chokepoints sparingly — only when an
information node is so foundational that the adventure
cannot function without it.

When to accept a chokepoint:

- A revelation the adventure structurally requires.
- A location that is the only access point to the
  adventure's main action.
- A character confrontation that cannot be bypassed
  without ending the adventure prematurely.

When to reject a chokepoint:

- When you are forcing a chokepoint for narrative
  reasons ("I want them to meet Aldermoor before the
  valley"). Narrative reasons are the author's
  preferences, not structural requirements.
- When the chokepoint is solvable by other means —
  the information could surface at a different node.

A chokepoint should never be an information node
for a non-critical fact.

## Exit design

Every node that is not the final node must have at
least two exit paths. An exit path names:

- The destination node.
- The condition for traveling that path (free,
  requires a result from this node, requires a
  decision here).

Example exit design for a conversation node:

```
EXITS:
- If the party asks Aldermoor about the northern
  route: he sends them to the surveyor's camp
  (Node 7).
- If the party confronts Aldermoor about the land
  deed: he closes the conversation and they need
  another approach — but Carver outside has been
  listening (Node 9: Carver's offer).
- If the party leaves without pressing: the alley
  behind the office (Node 5: someone followed them).
```

Three exits is a well-designed conversation node.
Two exits is the minimum. One exit is a railroad.

## The relationship map

Draw the relationship map before drafting. Every node
is a circle. Every exit path is an arrow connecting
two circles. Label the exit condition on the arrow.

What the map reveals:

- Nodes with only one outgoing arrow are bottlenecks —
  review them.
- Nodes with no incoming arrows are unreachable —
  verify they have a clear entry condition.
- The hub nodes are visible as the circles with the
  most incoming arrows.
- The shape of the adventure is visible — whether it
  is genuinely branching or secretly linear.

A secretly linear adventure's map looks like a chain:
A → B → C → D. If your map looks like this, revise
until it branches.

## Linear chain as railroad detection

If your node map is: A → B → C → D with no
alternatives at each step, you have designed a
railroad regardless of what the prose says.

Minimum viable branching: each major node offers
at least two exit paths that lead to meaningfully
different next nodes.

A node map with genuine player agency looks like
a web: multiple paths from early nodes, convergence
at hub nodes, multiple paths out again.

## Node density per session

Planning guidance:

| Session type     | Reachable nodes | Design total |
| ---------------- | --------------- | ------------ |
| 3-hour session   | 4-6             | 8-12         |
| 4-hour session   | 5-7             | 10-14        |
| Full-day session | 10-14           | 18-24        |

"Reachable" is how many nodes a group will typically
reach. "Design total" is how many you build. The
gap is player agency: a group that moves fast will
reach more; a group that lingers will reach fewer.
Design the gap so both groups feel full.

## When to use node design versus three-act arc

Use **node design** for:

- Investigation adventures.
- Dungeon or location exploration.
- Adventures where the players' choices about _which_
  path to take is the primary engagement.

Use **three-act arc** for:

- Journey and pressure narratives.
- Adventures where the primary engagement is _how_
  the players respond to escalating stakes.
- One-shots where pacing cohesion is more critical
  than branching.

**Combine them**: use the three-act arc to set the
rhythm of the adventure's pressure (breath / hammer /
reckoning) and use node design to structure the scenes
within each act.

An act-based node design: Act I nodes (breath/setup)
form a loose web leading to a mid-act hub. Act II nodes
(hammer/escalation) escalate from there, converging
on the Act III chokepoint. Act III nodes (reckoning)
branch into the four end-states.
