# Combat Encounters — The Block, the Texture, the Function

Combat in an adventure is not a fight scene. It is a
consequence-amplifier. Every combat in a published chapter
must answer three questions:

1. **What does the fight reveal?** (information)
2. **What does the fight cost?** (resources, NPCs, time)
3. **What does the fight change?** (faction stances, tracks,
   environment)

A fight that answers none of these is a tactical exercise
detached from the chapter. Cut it.

This file defines the system-agnostic combat block, the
texture rules that prevent every fight from feeling the same,
and the placement rules that put combat where it belongs in
the arc.

## The combat block (system-agnostic template)

Every set-piece combat in the chapter uses this block, placed
at the end of the scene grammar.

```
**Combat Encounter: [Title]**
- **Enemies:** [list of opposed forces, named tags only — no
  stats]
- **Area:** [the physical space, in evocative one-line prose]
- **Terrain and Effects:** [what the environment does to the
  fight; one to four short sentences]
```

### Worked example

```
**Combat Encounter: Raid on the Remuda**
- **Enemies:** `1 REMUDA CUTTER` inside the line, `4-6 HIRED
  RIDERS`, and `1-2 HIRED WHITE SABOTEURS`.
- **Area:** The Fort Ellis horse yard: picket ropes, hitch
  rails, feed crates, wagons, and packed animals.
- **Terrain and Effects:** Darkness blurs sightlines. Loose
  horses knock men down, foul firing lines, and force `MOVE`
  and `ANIMAL HANDLIN'` tests. Stakes and dragged ropes foul
  footing. Lit yards make targets visible to everyone.
```

### Why this format

- **Enemies as tags, not stats.** The block tells the GM
  _who_ the enemies are. The actual statblocks live in an
  appendix or stat-block file. This keeps the chapter
  readable and lets one set of stats serve many encounters.
- **Area as evocative prose.** One line. Names the space and
  three or four objects in it. The objects are the fight's
  raw material.
- **Terrain and effects as gameplay.** Three or four
  sentences telling the GM how the environment pushes back.
  Always concrete. Always actionable.

## The four mandatory texture rules

If you write more than one combat in a chapter, no two may
share the same texture. Variety is the rule.

### Rule 1: rotate the dominant element

Each fight has a dominant elemental texture. Across the
chapter, rotate them.

The standard elements:

- **Darkness** (night raids, broken visibility)
- **Fire** (burning hay, lit yards, smoke)
- **Mud or water** (fords, bogs, rain, snow)
- **Open exposure** (no cover, range fight, prairie)
- **Tight space** (alleys, stairwells, boarding houses)
- **Panic** (broken stock, civilians, fleeing crowds)
- **Wreckage** (splintered wagons, debris, recent damage)
- **Cold or heat** (weather as enemy)

A six-fight chapter might run: darkness → fire → exposure →
mud → tight → wreckage. Never repeat the same element back-
to-back.

### Rule 2: rotate the dominant pressure

Each fight has a dominant pressure beyond "kill the enemy."
Across the chapter, rotate them.

The standard pressures:

- **Save the goods** (protect the survey wagon, the records,
  the package)
- **Save the people** (protect a wounded NPC, a civilian, an
  ally)
- **Capture, not kill** (a witness must survive)
- **Escape** (extraction is the win, not victory)
- **Hold position** (rear guard, last stand)
- **Pursue** (chase the runner, prevent escape)
- **Identify** (find which one of several is the target)

The Yellowstone Line uses: save-the-line → defend-the-ranch →
protect-the-records → ford-survival → night-camp-chaos →
rearguard → law-restricted-final. Seven combats, seven
distinct pressures.

### Rule 3: rotate the consequences

Each fight changes the chapter's state in a different way.

- A fight that kills a key NPC.
- A fight that captures a key NPC.
- A fight that destroys a key resource.
- A fight that exposes a faction.
- A fight that escalates a track.
- A fight that demands a moral choice during the fight (a
  prisoner, a coup de grace, a wounded enemy begging).

If two of your fights resolve in the same way, redesign one.

### Rule 4: rotate the time of day

Sounds trivial; it is not. Players' tactical instincts
change with light. A morning fight in clear weather plays
nothing like a night fight in rain.

A six-fight chapter rotation: dusk → night → midday →
dawn → night → late afternoon. Use weather and light to
make every fight feel new.

## Where combat lives in the arc

### Arc I: one combat

Usually the inciting violence — small, sudden, intimate. A
killing or a raid. Establishes the threat is real. Often
fought against numerically inferior enemies; the difficulty
is the _texture_ (darkness, panic, broken stock), not the
opposition.

### Arc II: two or three combats

The pressure phase. At least one major engagement against
the chapter's primary external threat. At least one
"in-camp" or "in-quarters" fight where the threat is
internal — a betrayal, a saboteur, a midnight raid.

The Arc II combats should escalate: each one larger, more
costly, or more compromising than the last. The escalation
is felt in resources spent, not in stat-block size.

### Arc III: one or two combats

The reckoning phase. Often a _constrained_ combat: in a
town, a building, an office. Witnesses present. Law
present. The fight is not just tactical — it is political.
Killing the antagonist may solve the immediate problem and
ruin the long-term one.

The final combat is rarely the largest. It is the most
_loaded_ — every shot has consequences in the next chapter.

## Combat as consequence-amplifier

Combat amplifies whatever the chapter has already set up.
It does not introduce new factions or new pressures during
the fight itself.

Diagnostic: if the chapter introduces a new enemy _during_
a combat that the players have never heard of and never
will hear of again, that combat is filler. Cut.

Every combat's enemy list should be drawn from threats the
chapter has previously named. The Raid on the Remuda uses
hired riders the rumor table mentioned. The Hay-Yard Fight
uses either Vane's network or Iron Hail's riders, both
established. The Final Standoff uses Pike or Vane with their
named muscle. No surprises in the cast list.

## How combat ends in fiction

Every combat block must answer _what changes when the fight
ends_. This usually goes in the surrounding scene grammar
(the "what this scene leaves behind" line), not in the block
itself, but the writer must know it.

Standard end-states:

- **Pyrrhic victory.** The party wins but loses something
  named — an NPC, a resource, a track point.
- **Tactical loss, strategic win.** The party loses the
  immediate engagement but gains intelligence, a captive,
  or a moral high ground.
- **Tactical win, strategic loss.** The party wins the
  fight but the _context_ of the win damages them — they
  killed the wrong person, or the witnesses saw too much.
- **Mutual exhaustion.** Both sides withdraw bloodied. The
  consequence is in the medical and supply costs, not the
  tactical outcome.

A chapter that resolves every combat with "the party
wins, the threat is gone" reads as a power-fantasy. Mix
the end-states.

## Combat density

A chapter sustainably holds:

- **Short chapter (1 session):** 1–2 combats
- **Standard chapter (3–4 sessions):** 4–6 combats
- **Long chapter (6+ sessions):** 6–8 combats

More than 8 combats and the chapter is a dungeon crawl.
That is a different design discipline; this skill does not
cover it.

Counter-rule: at least one arc must contain a non-combat
hammer beat. If every hammer is a fight, the chapter is a
sequence of fights. The dilemmas, the betrayals, the
revelations are also hammers.

## Mixed-faction combats

The most memorable fights involve more than two sides. The
Hay-Yard Fight could be hit by white riders _or_ Lakota
raiders — and a really memorable variant has both arrive
in succession or simultaneously, fighting each other as
much as the party.

Use mixed-faction combats sparingly (one per chapter) but
deliberately. They:

- Reveal the chaos of the situation
- Force the players to choose targets in the moment
- Create complex track shifts (defending against Lakota
  raiders while accepting their indirect aid against the
  white riders)
- Generate stories the players retell

## Combat as moral test

The strongest combats include a moral micro-decision _in_
the fight, not just before or after.

- A wounded raider asks for mercy. Does the party give it
  mid-fight, knowing they may rejoin?
- A captured saboteur tries to flee. Shoot in the back, or
  pursue at risk?
- A civilian appears in the field of fire. Hold the shot,
  or take it?
- An ally NPC takes a wound. Protect them, or push the
  attack?

Plant one of these in at least one combat per chapter. The
moral micro-decision is what separates a remembered fight
from a forgotten one.

## Anti-patterns

### The cinematic ambush

Avoid combats where the chapter assumes the party is
ambushed and _cannot_ react meaningfully. Ambushes happen,
but the chapter must let the party's preparation, watch
discipline, and prior choices matter. A pure-cinematic
ambush is a railroad in fight clothes.

### The mandatory boss

Avoid combats with named NPCs whose deaths break the
chapter. If the chapter requires Iron Hail to live for the
sandbox, do not put him in a combat where the players might
plausibly kill him.

If a named NPC must appear in combat, write the combat so
that the NPC's death is _one of the consequences_, not an
unintended catastrophe. Plan for both their death and their
survival.

### The HP wall

Avoid scaling enemies' hit points to artificially extend
fights. A combat that drags because the enemies refuse to
die feels punitive, not climactic. Extend tension through
texture and stakes, not through stat inflation.

### The reset combat

Avoid combats that "test" the party but leave no residue. If
a fight ends with everyone healed, all resources restored,
and no NPC changed, the fight should not have happened.

Every fight costs something visible: ammunition, hit points,
sleep, an NPC's trust, a wounded mule, a burned sack of
flour. The cost is the proof the fight mattered.
