<!-- markdownlint-disable MD013 MD041 -->

## Chapter 2 - The Holdout (Homestead and Cabin Siege)

> _THE CABIN IS THE ONLY FORT THE FRONTIER HAD, AND THE NIGHT SOME MEN TRIED TO TAKE IT WAS THE NIGHT THE COUNTY LEARNED WHAT THE PEOPLE INSIDE WERE MADE OF. THE DOOR WAS OAK. THE WALLS WERE DIRT. THE MEN BEHIND THEM WERE WHATEVER THE NIGHT MADE OF THEM._
>
> — WEBB CALDER, TO A HAND WHO ASKED WHY THE LINE SHACK HAD LOOPS

### The Holdout and Its Work

The mass-combat chapter (Ch.23) gives you the unit-scale siege — the battalion on the ridge, the battery on the hill, the column breaching the stockade. The standoff chapter (Ch.1) gives you the scene-level tension before the guns. Neither gives you the scene the frontier made its own: a handful of named defenders barricaded in a cabin, a homestead, a line shack, or a ranch house, against a larger force, through a night — the classic "hold the cabin until dawn." It is a different mechanical shape from the skirmish line. It is a tension-and-attrition track, fought at PC scale, where the walls, the windows, the ammunition, and the dawn are the things the engine tracks.

This chapter gives the holdout its own operation frame, reusing the Progress-versus-Trouble engine with the polarity flipped: the defenders are not accumulating Progress toward a goal. They are holding a line while Trouble climbs, and the question is whether the line holds until the relief, the dawn, or the attackers' nerve breaks before the defenders' walls, ammunition, or resolve do.

> _Calder had barred the door and shut the shutters and set the two hands at the loops and the woman and the boy behind the stove with the rifle, and he had counted the shots outside and counted the men and counted the hours until dawn, which was the holdout's arithmetic, and the arithmetic was not in the defenders' favor. Eight men outside, by the sound. Four defenders, if you counted the boy, which Calder did not. Twelve rounds of the .50 between the loops, and the revolver cylinders, and the shotgun the woman held like she knew which end to point._
>
> _The first rush came at midnight and the .50 took the lead man in the door and the rest went back to the dark and the cabin held. The second rush came at two and the shutter splintered and the hand at the window went down with a ball in the shoulder and the cabin held, barely. The third rush had not come yet, and the sky was the color of iron, and Calder counted the .50 rounds again — eight now — and the hours — two more to dawn — and the hands — three now, if you counted the boy, which Calder was beginning to._
>
> _That was the holdout. The door, the loops, the ammunition, the dawn. Hold the one, watch the other, and pray the third outlasts the fourth._

### The Holdout as Operation

A holdout is an operation with its polarity flipped. The defenders do not accumulate Progress. The ** attackers** accumulate **Breach** (the holdout's Trouble track), and the defenders' job is to keep the Breach below the limit until the holdout's clock runs out — the relief, the dawn, or the attackers' collapse. The defenders' successes erase Breach (a repelled rush, a killed attacker, a patched wall); the defenders' failures and the attackers' successes add it.

| Holdout Scale | Breach Limit | The Holdout |
| --- | --- | --- |
| `The Stand at the Door` | `3` | A short holdout — a few hours, one or two rushes, a single night's trouble |
| `The Long Night` | `4` | A full night's siege — multiple rushes, the wounded, the ammunition running low |
| `The Siege` | `5` | A multi-day holdout — starvation, fire, the breach, the cellar, the last stand |

The holdout's clock is set when the operation begins. The most common clock is **dawn** (the attackers lose nerve in daylight, or the relief arrives), but the GM may set the clock to the relief column's arrival, the storm's break, the wire's restoration (the wire chapter), or the attackers' supply running out. Each Standoff Round of the holdout (see below) moves the clock forward; when the clock runs out, the holdout resolves.

### The Holdout Round

A holdout is resolved in **Holdout Rounds**, each representing a beat of the siege — a rush, an exchange of fire, an hour of tension, a lull. Each Holdout Round, the attackers choose an assault tactic (below), the defenders choose a response, and the exchange is resolved with a single opposed roll: the attackers' pool against the defenders' pool.

### The Cabin's Interior

The Breach track (below) is the siege's outer measure — how close the attackers are to breaking in. But the interior of the cabin is its own problem, and the defenders are managing three things while they hold the walls: the **ammunition**, the **wounded**, and the **fire**. These are not a second operation layered on the Breach track; they are the *contents* of the Breach track's Trouble, made concrete and playable, so the GM can make the inside of the cabin feel like a place under siege rather than an abstraction.

#### Ammunition as a Resource Die

The cabin's ammunition is tracked as a **resource die** — the same primitive the outlaw band's `Provisions` die uses, applied to the cabin's powder and lead. The die is set by what the defenders laid in before the siege began.

| The Cabin's Stores | Ammo Die |
| --- | --- |
| A few boxes, a handful of loose rounds | `D6` |
| A decent stock — a full box per defender | `D8` |
| A well-stocked cabin or a way-station's stores | `D10` |
| A fort or a prepared position | `D12` |

Each Holdout Round in which the defenders sustain fire (any Round that is not a pure lull or a parley), roll the ammo die. On a **1–2**, the die steps down one size. At **D4**, the cabin is down to the last rounds — sidearms, the shotgun's final shells, the few cartridges a defender kept in his pocket. At **D4 exhausted** (a 1–2 on the D4), the defenders are out of cartridges and down to edged weapons, revolvers held as clubs, and the ammunition's silent partner: the decision to shoot or not to shoot, which the ammo die forces on the defenders long before the Breach track would have.

The ammunition is the defenders' clock inside the siege. A cabin that holds the walls until dawn may still lose the fight if the ammo runs out at 4 a.m. and the last rush comes at 5, and the engine should let that tell — the ammo die is the resource that makes the holdout a *management* problem, not just a rolling problem.

#### The Wounded Gauge

The cabin's wounded are tracked on a **Wounded gauge** (1–5), the inverse of the outlaw chapter's `Cohesion`. Each defender who is taken down a condition-ladder rung by the siege — a hit through the loophole, a splinter-wound to the eye, a man thrown by the blast of a charge — steps the Wounded gauge up by one.

| Wounded | The Cabin's Medical State |
| --- | --- |
| `1-2` | A man hurt, still fighting. The `DOCTORIN'` roll patches him between Rounds; the defense holds. |
| `3` | A medical problem. The wounded cannot all be treated between Rounds; one is out of the fight, the others are hurting. The `DOCTORIN'` roll is under fire and at `-1 die` for the work's conditions. |
| `4` | The cabin is half a hospital. Two defenders are down; the remaining are splitting their time between the loops and the wounded. Defense rolls at `-1 die` while the work is split. |
| `5` | The cabin is a hospital with guns. The defense is barely holding; the wounded are dying if they are not already dead, and the `DOCTORIN'` roll is the only thing between the cabin and a surrender. |

The Wounded gauge is the holdout's human cost, and it gives the `DOCTORIN'` ability and the doctor-PC (or the hand with the bandages and the grit) a distinct role in the siege that the Breach track alone could not. A cabin that holds its walls but fills its Wounded gauge has won a siege it may not survive, and the engine should let that weight land on the defenders and the county.

#### The Fire as a Procedure

The Breach track is the slow clock. The fire, once it is lit, is the fast one. When the attackers choose the **Fire the roof** assault tactic (tactic 2, below), the fire is not a single Trouble step — it is a **second clock** that runs alongside the Breach track, and the defenders must answer it or lose the cabin to it.

Once the roof is alight, the fire is tracked by its **spread**: each Holdout Round the fire is unchecked, it advances one **room** closer to the cabin's last defensible space (the cellar, the back room, the stone chimney-corner the cabin was built around). The spread is the fire's Progress track, and the defenders may spend a Round's actions fighting it — a `LABOR` roll to beat out the spot-fires and tear away the burning shakes, or a `MAKIN'` roll to rig a bucket-line from the water barrel — which, on success, holds the fire's spread for a Round (buys time) and, on a critical, pushes it back a room (the fire is losing). A failed roll means the fire spreads and the action was wasted, which is the cost of dividing the defense between the loopholes and the roof.

A fire that reaches the last room is the fire that ends the holdout — the defenders must abandon the cabin (into the attackers' hands, or into the night) or burn. The fire is the holdout's most cinematic pressure and its most inexorable clock, and the engine should let it be what it was in the actual frontier: the thing that could end a siege in an hour that the Breach track would have taken all night to finish.

> _Calder counted the ammo die — D8, which was two more Boxes than a man ought to need for one night, which was one more than a man ought to count on — and he counted the wounded gauge, which was at two, which was the hand with the splinters in his eye and the boy who had taken the ricochet in the shoulder and was lying behind the stove with the rifle he could not lift. And he counted the roof, which was not yet alight but which the eight men outside had the means to light, and which the cabin had no answer for that Calder had not already thought of and found wanting._
>
> "How many rounds?"
>
> "Twelve in the .50. Six in the cylinders. The shotgun."
>
> "Then we don't shoot unless we shoot to hit." Calder did not take his eye from the loophole. "And we pray they don't fire the roof, because if they fire the roof we are fighting two sieges and we have the men for one."
>
> _That was the cabin's interior — the ammo die, the wounded gauge, and the fire that had not come yet but that Calder could smell in the kerosene the attackers had brought, which was the smell a man learned to read the way he read the weather, which was the smell of a holdout that might not end at dawn._

#### The Attackers' Pool

The attackers' pool is set by their number and quality (read off the mass-combat chapter's Quality tiers if they are a unit, or the outlaw chapter's band factors if they are a gang). A larger, better-led force rolls more dice; a smaller or demoralized force rolls fewer.

| Attacker Condition | Modifier |
| --- | --- |
| The attackers outnumber the defenders two-to-one or more | `+1 die` |
| The attackers are veterans or hard cases | `+1 die` |
| The attackers are a disciplined unit (the mass-combat chapter) | `+1 die` |
| The attackers are a mob, green, or drunk | `-1 die` to `-2 dice` |
| The attackers have a leader with `PRESENCE` or `AUTHORITY` present | `+1 die` |
| The attackers have already lost men or a rush this night | `-1 die` per failed rush (the nerve is going) |

#### The Defenders' Pool

The defenders' pool is set by the position and the defenders' quality. The cabin is the defenders' great advantage, and the walls, the loops, and the choke points are the dice the defenders roll.

| Defender Condition | Modifier |
| --- | --- |
| Defenders behind good cover (log walls, loopholes) | `+2 dice` |
| Defenders behind partial cover (sod, boards) | `+1 die` |
| A choke point (one door, a single approach) | `+1 die` |
| A defender with `SHOOTIN'` 4+ at a loop | `+1 die` |
| A defender with the `Defender` talent | `+1 die` |
| Defenders wounded, exhausted, or out of ammunition | `-1 die` to `-2 dice` |
| Non-combatants in the cabin (the woman, the boy, the cattle) | `-1 die` (the defenders' attention is split) |

Apply the modifiers that plainly matter, to the ±3 cap, on each side's pool.

### Reading the Holdout Round

Compare the attackers' and defenders' successes. The holdout's Breach track moves with the result.

| Result | Breach Movement |
| --- | --- |
| Defenders win by `2+` | **Breach erased by `1`** (a repelled rush, a killed attacker, the walls held and the attackers' nerve dropped). The attackers take a casualty; their next roll is at `-1 die`. |
| Defenders win by `1` | **Breach holds.** The rush was repelled, but barely. A defender is wounded or a wall is splintered; the GM may apply a small condition (a `Hurts`, a loop blocked). |
| A draw | **Breach holds, tense.** The exchange was even; ammunition was spent on both sides. If using the optional `Provisions` die for ammunition, step it down. |
| Attackers win by `1` | **Breach +1.** A wall breached, a defender wounded, a shutter down, the roof alight. The GM names the breach. |
| Attackers win by `2+` | **Breach +2**, and the attackers gain a foothold — a window forced, a wall down, a defender down. The next Holdout Round the attackers are at `+1 die` from the foothold. |

When the Breach reaches the limit, the holdout's outer defense fails and the fight moves indoors (below). When the clock runs out before the Breach reaches the limit, the holdout succeeds — the attackers break, the relief arrives, the dawn exposes the attackers to a county that can see them.

The Breach track is the siege's outer clock, but it is not the only clock running. The **Cabin's Interior** gauges (above) run alongside it. A Round of sustained fire from the defenders steps the **ammo die** down on a 1–2. A defender taken down a condition-ladder rung by a Breach result (a hit, a splinter, a blast) steps the **Wounded gauge** up by one. A fire that is lit and unchecked spreads a room each Round toward the cabin's last space. The GM should name which interior pressure each Breach result worsens — the wall that splintered also cost the defender at the loophole a `Hurts` (step the Wounded gauge), the rush that was repelled also spent the defenders' ammunition (roll the ammo die). The interior is the Breach track's human and material cost, and the holdout is won or lost on both.

### Assault Tactics Table

Each Holdout Round, the attackers choose or roll an assault tactic. The tactic sets the character of the round and may apply a modifier.

| D6 | The Assault Tactic |
| --- | --- |
| `1` | **Rush the door.** A direct attempt to force the entry. The choke point favors the defenders (`+1 die`); the attackers are betting on numbers. |
| `2` | **Fire the roof.** An attempt to burn the defenders out. `MAKIN'` or `LABOR` to set it; the defenders must spend the round fighting the fire or take a Breach step each Round it burns. Once the roof is alight, the fire becomes its own **spread clock** — see _The Fire as a Procedure_ (above), for the room-by-room spread and the defenders' options to hold or push it back. Hooks the corebook's fire rules. |
| `3` | **Starve them out.** The attackers settle in and wait. No Breach this Round, but the clock advances and the defenders' `Provisions` (if used) and `RESILIENCE` are tested by the wait. |
| `4` | **The parley.** The attackers offer terms — surrender, the thing they came for, a truce until dawn. A social conflict (the standoff chapter, the social-conflict rules); if the defenders refuse, the next rush is at `+1 die` (the attackers' blood is up). |
| `5` | **The feint.** A false rush at the door to draw the defenders' fire while the real approach comes from the side. `INSIGHT` vs the defenders' `HAWKEYE` to read it; a failed read applies the attackers' rush at `+1 die`. |
| `6` | **The breach.** A concentrated effort at the weakest wall — a drawn log, a dug-under, a powder charge. `LABOR` or `MAKIN'`; success is Breach `+2` and a foothold. |

### The Room-by-Room Breach

When the Breach reaches the limit, the outer defense fails. The door is down, the wall is breached, the roof is in. The fight moves indoors, and the holdout becomes a series of combat Rounds (the corebook's conflict rules) fought room by room — the door to the main room, the main room to the back, the back to the cellar or the roof. Each room is a choke point the defenders may hold for a Round or two, trading space for time, buying another tick of the clock. The defenders' ammunition, their wounded, and their position are the dice they roll, and the corebook's combat rules resolve each room's fight.

A breach that reaches the cellar or the roof is the last stand. The defenders fight until they break, surrender, or are rescued — the relief column's hoofbeats in the dawn, the attackers' nerve finally breaking, the sheriff's posse that was a day behind the wire. The engine does not soften a last stand. The holdout's payoff is the survivors and the story the county tells about the night the cabin held or the night it did not, and both stories are the kind the West was built on.

### The Dawn

The dawn is the holdout's natural resolution. When the clock runs out — when the sky goes from iron to grey to the color of a day — the attackers must decide whether to press a defended position in daylight, where the county can see them and the law can find them, or to break off and ride for the dark they came in. Most break off. A holdout that survives to the dawn is a holdout the defenders won, and the county's `Standing` shifts with the telling — the defenders' `Fame` rises, the attackers' is marked, and the feud (the families chapter) or the warrant (the justice chapter) picks up where the cabin's door left off.

A relief column that arrives at dawn is the engine's payoff for the wire that got out (the wire chapter), the rider who got away, the posse that was summoned. The GM should let the relief's arrival be the scene it is — the hoofbeats, the light, the defenders who did not know they were holding on for it until they heard it.

### The Holdout and the Other Rules

The holdout is the PC-scale siege the mass-combat chapter skips and the standoff chapter sets up.

- **The standoff chapter** is the holdout's door — a standoff that neither side breaks and neither side can leave becomes a holdout, the door barred, the night coming on.
- **The mass-combat chapter** is the holdout's unit-scale cousin — when the attackers are a unit, the holdout uses the mass-combat Quality tiers to set the attackers' pool.
- **The corebook's conflict rules** (Ch.5) resolve the room-by-room breach and any individual fight within the holdout. The holdout is the frame; the combat Round is the room.
- **The weather chapter** sets the night's conditions — a blizzard holdout, a rain holdout, a dust-storm holdout — which apply to both sides and to the clock.
- **The ammo die** (the Cabin's Interior, above) is the corebook's consumables-as-resource-dice rule and the outlaw chapter's `Provisions` die, applied to the cabin's powder and lead. Its exhaustion is the holdout's quiet killer.
- **The Wounded gauge** (above) hooks the sickness chapter (the infection risk in a cabin that cannot keep its wounded clean) and the corebook's `DOCTORIN'` ability (the under-fire surgery, the triage between Rounds).
- **The fire** (above) hooks the corebook's non-typical-harm fire rules and the weather chapter (a fire in a blizzard is a different crisis than a fire in a drought; the wind feeds it or the rain starves it).
- **The optional `Provisions` die** (food and water, distinct from the ammo die) applies to a long siege's starvation clock, stepped down if the holdout runs past the night the defenders prepared for.

The cabin was the only fort the frontier had, and the night some men tried to take it was the night the county learned what the people inside were made of. A chapter that gives the cabin a door, the walls a value, and the dawn a clock gives the campaign its most personal siege — not the column on the ridge, but the four people in the dark, with the door barred, counting the rounds and the hours, and praying the third outlasts the fourth.
