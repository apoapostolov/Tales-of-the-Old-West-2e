# Location Design

A location is a place the adventure inhabits, not a
backdrop it moves through. The difference is in how
it is written: a backdrop has mood. A location has
history, architecture, specific NPCs in specific
places, and things that are wrong.

Keyed location design names and numbers each area,
then writes an entry for each. The result is a GM
who can navigate the location spatially, answer player
questions about what is where, and reveal the location's
secrets in response to player action rather than at
scripted moments.

## The location entry format

Five components, in this order:

1. **What is immediately visible**: one line. The GM
   reads this as the players enter. It establishes
   orientation and the dominant sensory impression.
   No secrets here.

2. **What requires investigation**: one to two lines.
   What the players find if they look closely, search,
   or ask. Clues, hidden objects, evidence of recent
   use or misuse.

3. **Who or what is present**: who occupies this space
   at the location's default state (before player
   action changes it) and how they are behaving. Not
   a full NPC entry — a posture and a one-line motive.

4. **What exits exist**: all doors, passages, windows,
   hidden exits. Each exit names its destination entry
   number and a one-word descriptor.

5. **One threat or opportunity**: the thing in this
   space that can harm or benefit the players. Not both.
   Choose the more dramatically useful.

Example entry:

```
ENTRY 6 — THE SCULLERY

Immediately visible: A long stone room with a low
ceiling. Smell of lard and old smoke. A rack of
hanging game birds, three already spoiling. Dishes
stacked unwashed.

Investigation: A message scratched into the underside
of the chopping block in Spanish: "Tell no one I was
here." A lock of dark hair in the lard tin.

Present: Dorie (the cook's assistant) is scrubbing a
pot with deliberate focus. She knows something she is
afraid to say. She will not make eye contact.

Exits: Door north to the kitchen (Entry 4). Stair
west to the cellar (Entry 11). Window east, unlatched —
leads to the yard.

Threat / opportunity: The game birds are diseased.
A character who eats from this kitchen tonight will
be sick by morning. Opportunity: the unlatched window
allows quiet exit without passing through the kitchen.
```

## Environmental storytelling

The location tells its own history through what is
present, damaged, missing, or wrong.

Damaged: a lock broken from the inside, not the
outside. A portrait with the face scored out. A
wall with scorch marks that someone tried to clean.

Missing: a space on the gun rack where a rifle should
be. An empty picture frame. A cold hearth in a room
where a fire should always be burning.

Wrong: a child's toy in a room with no children.
Books with all the names cut from the spines. A
clock stopped at the same time in three different
rooms.

These details are not puzzles with correct solutions.
They are texture that signals: this place has history.
Something happened here. The players will theorize.
Some theories will be confirmed; others won't.

Write two to three environmental storytelling details
per major location entry. They cost nothing in text
length and produce enormous table engagement.

## Density calibration

How many entries to write per location type:

| Location type                      | Minimum entries | Maximum entries |
| ---------------------------------- | --------------- | --------------- |
| A manor house or estate            | 8               | 15              |
| A ship                             | 6               | 10              |
| A mining camp                      | 5               | 8               |
| A cave system                      | 4               | 8               |
| A single building (saloon, church) | 4               | 7               |
| A town quarter or block            | 6               | 12              |

The minimum is enough to run the location. The maximum
is enough to survive a group that examines everything.

Err toward the minimum. Dense location entries produce
over-preparation; thin entries are patched on the fly.

## The three-zone rule

Every interesting location has three concentric zones:

**Public zone**: open, accessible, and visible to
any visitor. The saloon floor. The sheriff's lobby.
The camp's main avenue. What the antagonist wants
the world to see. The public zone confirms the lie
the antagonist is telling.

**Private zone**: restricted, watched, or guarded.
Requires permission, authority, or force to access.
The back office. The locked storeroom. The foreman's
quarters. The private zone contains partial truths —
information that is real but filtered.

**Hidden zone**: secret or actively concealed.
Requires significant effort, investigation, or
accident to reach. The false-floor compartment.
The collapsed section of the mine that someone
recently reopened. The locked trunk behind the
locked door. Secrets concentrate here.

Apply the three zones when building the location map.
Mark each entry as public, private, or hidden. If
all entries are public, the location has no depth.
If the hidden zone is empty, the location has no
secrets worth finding.

## Secret placement

**Public zone**: no secrets. The lie, the facade,
the official story.
**Private zone**: one partial truth per major private
area. The ledger that implies but doesn't prove the
fraud. The letter that names an accomplice but not
the act.
**Hidden zone**: the full truth or the most dangerous
object. The complete ledger. The weapon. The deed.

This structure rewards players who push into
restricted spaces. It punishes only those who stop
at the public zone.

## NPC placement in locations

Every NPC in a location has a default position —
where they physically are before player action
changes anything.

List each NPC's default position in the location
overview, before the individual entries begin:

```
NPC POSITIONS (default state):
- Aldermoor: Entry 2 (his office), reviewing papers.
- Dorie: Entry 6 (the scullery), working.
- The two guards: Entry 1 (front door), one awake
  and one asleep.
- Vane: Entry 11 (the cellar), waiting.
```

NPC movement is driven by player interaction and
NPC motivation — not by scene triggers. If the
players make noise in Entry 5, the guard at Entry 1
may move to Entry 5. The GM uses the NPC's motivation
and alertness to determine this, not a scripted event.

## The living location

A location visited twice is never the same.

When the party returns to a location after a
significant interval (a night, a session, a major
event), update it:

- Who moved?
- What was removed, added, or changed?
- What evidence of time passing is visible?
- Has the antagonist responded to the party's
  previous actions here?

Write the "second visit" state in the location's
GM notes, not as a separate entry. The GM uses it
when the party returns.

## Mapless design

When a visual map is not available or not provided,
the location is navigated entirely through exit
descriptions in each entry.

Every exit in an entry must:

- Name the destination entry (by number or label).
- Give a one-word descriptor of the path (stair,
  corridor, door, window, passage).
- Note any barrier (locked, guarded, concealed).

Players who want to map the location can do so
from the exits alone. The GM can orient themselves
without a diagram.

"The east door leads to Entry 4 (the scullery).
The back stairs lead to Entry 7 (the locked study),
but the stairs creak." — this is sufficient.

## Dungeon vs. social vs. wilderness locations

**Combat-focused locations (dungeon, battlefield,
stronghold)**: each entry emphasizes the threat or
opportunity component most strongly. Tactical
information (cover positions, choke points, elevation)
is in the entry. Environmental storytelling can be
brief.

**Investigation-focused locations (manor, office,
ship cabin)**: each entry emphasizes the investigation
component. What requires investigation is the longest
component. Environmental storytelling is dense.

**Travel-focused locations (wilderness stretch,
landmark, ford)**: entries are shorter and landmark-
based. Not every physical space has an entry — only
named features that carry story weight. See
`references/travel-and-wilderness.md`.
