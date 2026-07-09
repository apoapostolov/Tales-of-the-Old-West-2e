<!-- markdownlint-disable MD013 MD041 -->

## Chapter 23 - Mass Combat and the Skirmish Line

> _THE SKIRMISH LINE IS NOT THE LINE OF MEN. IT IS THE LINE THE MEN ARE WILLING TO DIE ON. FINDING OUT WHERE THAT LINE IS, AND WHO IS ON WHICH SIDE OF IT, IS THE SERGEANT'S WORK AND THE OFFICER'S FEAR._
>
> — SERGEANT MOSES CARVER, TO A LIEUTENANT WHO HAD DRAWN THE LINE IN THE WRONG PLACE

### Mass Combat and Its Trade

There are fights in the West that are too large for the player characters' pistols. The Indian Wars are the setting's central fact, and the army's campaign against the horse nations cannot be run as a saloon brawl. The Lincoln County War, the fence wars, the railroad's strike-breaking, the Committee's raid on a camp, the gang war that spills past the posse and into the column — all of these are fights of dozens and hundreds, and the corebook's conflict rules, which are built for the handful, do not reach them.

This chapter is an optional framework for groups who want those fights on the table. It builds a **unit abstraction** — a body of fighters treated as a single entity with a Quality rating, a Strength die, and a Cohesion gauge — and resolves the skirmish between units with the same dice the engine uses for everything else. It lets **player characters attach** to a unit as leaders, in which case their own abilities carry the day. It wraps the whole in the **operation framework**, so a battle that matters is run as a battle and not as a single mass roll.

It is written to sit alongside the corebook's `Morale & Rout` rule, which is the engine's native mass-morale mechanic, and to reuse the outlaw chapter's `Cohesion` gauge rather than invent a new one. The point is to make a skirmish feel like a fight the engine understands, not a different game bolted on.

You do not need these rules for a barroom brawl or a posse's running fight. Use them when the fight is thirty or more a side, when the player characters are officers or war leaders rather than just shooters, and when the outcome of the battle changes the campaign — who holds the ground, who keeps the herd, who survives the column.

> _Carver dismounted the troop on the ridgeline and read the ground below him and the enemy on the next ridge and the order in his lieutenant's hand that had put them there, and he did not like any of the three. The ground said the troop was sky-lined against the morning. The enemy said it knew the troop was there and had not moved, which meant it was where it wanted to be. The order said hold the ridgeline until relieved, which was the kind of order a man wrote when he did not intend to be the one holding it._
>
> _He did not say any of this to the lieutenant. The lieutenant was twenty-two and had the order in his hand and the order's confidence in his voice._
>
> "Sergeant. We hold here until the column comes up."
>
> "Yessir. The men will hold."
>
> "We're sky-lined," the lieutenant said. He had seen it too, which gave Carver one small hope for the boy.
>
> "We are, sir. I'd pull the line back thirty yards to the draw, if it's all the same to you. Break the silhouette and give the carbines a rest."
>
> "The order says hold the ridgeline, Sergeant."
>
> "Yessir." _Carver said it flat, the way he said everything to the officers, aimed at the truth of the moment and not the truth of the day. The truth of the day was that Calder's herd was the reason the enemy was on the next ridge, and Riddle was in the wrong corner of the wrong coulee, and the column the lieutenant was waiting for was two hours behind its wire. Carver put the men on the sky line and loaded the carbines and waited to see whether the morning was going to be the kind that ended in a report or the kind that ended in a letter to Leavenworth._

### The Unit

A unit is a body of fighters treated as one. It is the abstraction that lets a battle of sixty run as a fight between four pieces on the GM's map. A unit is defined by four things.

- **Quality.** The fighters' training and nerve, rated `1` to `3`, which is also the number of base dice the unit rolls.
- **Strength.** The unit's numbers and condition, a stepped die (`D6` at full strength, stepping down with casualties like the optional `Provisions` die). When the Strength die is exhausted, the unit breaks.
- **Cohesion.** The unit's willingness to hold the line, on the outlaw chapter's `1-5` scale (start at `3`), with all of its effects.
- **A name.** What the unit is — the Tenth's Company D, the Committee's mob, the war party under Iron Hail, Calder's trail crew. A unit is not a statblock; it is a body of people the campaign has a stake in.

#### Quality

| Quality | Rating | Who |
| --- | --- | --- |
| `Green` | `1` | Raw militia, an armed mob, a posse of shopkeepers, a gang's hired extras |
| `Regular` | `2` | Trained troopers, hardened cowhands, a veteran war party, an experienced gang |
| `Veteran` | `3` | Disciplined regulars, seasoned fighters, the regiment's best company |

Quality sets the unit's base dice. A `Green` unit rolls `1` die on its checks; a `Regular` unit rolls `2`; a `Veteran` unit rolls `3`. These map directly to the corebook's `Morale & Rout` tiers — `2` dice for frightened rabble, `4` for ordinary fighters, `6` for hard cases — by doubling, which keeps the two systems on the same scale.

#### Strength

| Strength Die | The Unit's Condition |
| --- | --- |
| `D8` | Reinforced or oversized; a unit at the top of its scale |
| `D6` | Full strength, the baseline |
| `D4` | Bloodied, thinned, or tired; one bad exchange from breaking |
| `exhausted` | The unit is broken. It routs, surrenders, or stands and dies where it stands |

A unit begins at `D6` (or `D8` if it is reinforced or oversized for its scale, such as a fifty-man militia or a hundred-strong war party). Each lost exchange steps the Strength die down. When the `D4` Strength die steps down, the unit is broken and the Morale check (below) decides its fate.

#### Cohesion

A unit's `Cohesion` works exactly as the outlaw chapter's gang Cohesion works, on the same `1-5` scale with the same states (`Keen`, `Solid`, `Uneasy`, `Fraying`, `Broken`) and the same effects. A unit at `Fraying` is a unit one bad moment from a rout; a unit at `Broken` is a unit that must be held together by its leader on every round or it comes apart. Reuse the outlaw chapter's table verbatim. This is the engine's discipline: a body of people holds together by the same pressure whether they are a gang in a hideout or a troop on a ridgeline.

### The Skirmish Turn

A skirmish is resolved in Rounds, like the corebook's conflict. Each Round, every unit on the line takes a turn, in an order set by a single initiative draw (one card for the whole side, or one `Quick` roll per side, as the corebook's Fast Initiative option allows). On its turn, a unit acts: it moves, it fires, it charges, it holds, it rallies. The skirmish is the linked sequence of these turns.

#### The Volley and the Melee

When a unit attacks another unit, resolve it as an **opposed unit roll**. Each side rolls its Quality dice (the base `1`/`2`/`3`) plus its current Strength die, plus any help or penalty dice for terrain, cover, range, weather, and the presence of attached player characters (below).

| Situation | Modifier |
| --- | --- |
| Defender in good cover (a ridge, a wall, timber) | `+1 die` to the defender |
| Defender in heavy cover (a breastwork, a building) | `+2 dice` to the defender |
| Attacker charging across open ground | `+1 die` to the defender |
| Volley at Long or Distant range (rifle fire) | `-1 die` to the attacker |
| Volley in a dust storm or high wind | `-1 die` to both |
| Attached player character leading the unit (below) | the PC's relevant ability as help dice, max `+3` |
| Unit at `Cohesion 2` (Fraying) | `-1 die` |
| Unit at `Cohesion 1` (Broken) | `-2 dice` |
| Unit at `Cohesion 5` (Keen) | `+1 die` |

Read the opposed roll by successes. The side with more successes wins the exchange. The loser steps its Strength die down by the margin (each extra success the winner rolled is one step of loss). A draw means both sides hold and neither loses Strength this exchange, though the GM may apply `Trouble` (a casualty among named figures, ammunition spent, a flank turned) at her judgment.

A melee is resolved the same way, with the same opposed roll, the difference being that the loser of a melee is more likely to break (the Morale check after a lost melee is at `-1 die`).

#### Attached Player Characters

A player character attached to a unit is its leader, and the unit fights with the PC's ability on the line. Choose the ability that fits the unit's action: `SHOOTIN'` for a volley, `FIGHTIN'` for a melee, `PRESENCE` for a rally or a charge, `ANIMAL HANDLIN'` for a mounted unit, `INSIGHT` to read the enemy's move. The PC's ability rating is added as help dice to the unit's opposed roll, to the `+3` cap — the same help-dice discipline the engine uses everywhere.

An attached PC can also **peel off** to resolve a personal fight using the corebook's Chapter 5 conflict rules — the PC's duel with the enemy captain, the sergeant's charge into the breach, the player character's attempt to reach the wounded man under fire. These scenes run in the corebook's Rounds, nested inside the skirmish's Round, and their outcome can swing the unit's next roll (a captain killed is a unit at `-1 die`; a breach forced is a defender's lost exchange).

An attached PC is also a target. A unit that loses an exchange with a PC attached may, at the GM's judgment, have put the PC in harm's way: the PC takes `1` point of `Hurts` from the firefight, or rolls on the Critical Injury table if the exchange was a melee or a close-range volley. The player character who attaches to a unit is not insulated by the abstraction; the PC bleeds.

#### Morale and Rout

When a unit's Strength die is exhausted, or when the conditions of the corebook's `Morale & Rout` rule are met (the leader down, half the unit fallen, plainly outmatched, a terrifying display), the unit tests Morale. Roll the unit's Quality dice, doubled for the Morale check (so `Green` rolls `2`, `Regular` rolls `4`, `Veteran` rolls `6`, exactly as the corebook's table). On a success, the unit holds for now. On a failure, read the result on the corebook's `Morale & Rout` outcomes: flee, surrender, scatter for cover, or freeze and fight at `-2`.

A unit that flees or scatters may be rallied by an attached PC's `PRESENCE` roll, on the standard ladder. A unit that surrenders is out of the fight, and its surrender is a fact the campaign's faction system will remember — a war party that surrenders to the troop is a war party with a grievance, and a mob that surrenders to the Committee is a mob that will not surrender twice.

### The Battle as Operation

A skirmish that matters — one whose outcome changes the campaign — is run as an **operation**, with the Progress-versus-Trouble track wrapped around the exchange-resolution above. This is the engine's way of making a battle more than a series of dice rolls, by giving it a destination.

| Battle Scale | Progress Needed | Trouble Limit | The Fight |
| --- | --- | --- | --- |
| `Skirmish` | `4` | `3` | A sharp fight; a column's morning, a raid repulsed |
| `Battle` | `6` | `4` | A set engagement; the holding of the ridge, the taking of the camp |
| `Major Action` | `8` | `5` | A column's full fight; the day that decides a campaign |

**Progress** is the battle's objective: break the enemy, hold the ground, take the camp, drive the raiders off the herd. Each exchange the player characters' side wins adds its margin to Progress. **Trouble** is the battle's cost: a unit's Strength lost, a leader down, ammunition running low (the `Provisions` die, if used), a flank turned, the weather closing in, a faction's intervention or betrayal. Read Trouble on the standard ladder — at `3+`, the battle is turning into the kind of fight that breaks the side that began it.

Each exchange in a battle operation is tagged Safe / Risky / Desperate, the way a score's checks are. A volley from good cover against an enemy at Long range is `Safe`. A charge across open ground against a defended ridge is `Desperate`. The GM's tagging is the pressure that makes the player characters' choices about when to push and when to hold feel like the choices a war leader actually makes.

When the Progress fills, the battle is won — the objective taken, the enemy broken, the ground held. When the Trouble hits its limit, the plan is dead: the line is broken, the unit is routing, the player characters must decide whether to rally, retreat, or go down with the fight. The engine does not soften the latter. A battle lost is a battle lost, and its consequences run through the faction system, the season, and the campaign.

### Artillery, the Gatling, and the Charge

Some fights have weapons that change the skirmish line. These are modifiers and special resolutions, not a separate engine.

- **Artillery** (a mountain howitzer, a field gun) is a unit of its own, with `Quality 2`, no Strength die but a fixed effect, and the ability to fire at any range. An artillery exchange is `+2 dice` to the firing side and forces a Morale check on the target unit regardless of casualties, which is what artillery actually did to men who had never been under it.
- **The Gatling gun** is an infantry-broken. Treat it as `+3 dice` to the unit it supports in a volley, with the caveat that it jams on a roll of all `1`s (the GM applies a Trouble step and the gun is silent until cleared). A unit facing a Gatling tests Morale at `-1 die` the first time it fires.
- **The charge** is the melee's desperate cousin. A charging unit adds `+1 die` to its melee roll but steps its Strength down by one on a loss, regardless of margin — a failed charge is a broken charge, and the men who made it are the men who pay for it.
- **Fortifications** (a stockade, a blockhouse, a breastwork) add their cover modifier to the defender's volley and melee rolls, and force the attacker to win two exchanges to step the defender's Strength down once, which is what makes a siege a siege.

### The Siege and the Running Fight

Two special cases deserve a word.

A **siege** is an operation whose Progress is the breach (for the attacker) or the holding out (for the defender), and whose Trouble is starvation, disease, the ammunition, the relief column, the weather. A siege runs across days and Turn-of-the-Season increments, not Rounds, and it uses the town's `Welfare` and `Natural Riches` aspects and the optional `Provisions` die to model the slow pressure of a place cut off. A siege is the engine's way of making the campaign's long arc do the work of a siege, which is patience and attrition.

A **running fight** — a retreat, a pursuit, a column's withdrawal — is a series of skirmishes linked by the corebook's `Chases` and the outlaw chapter's `Hard Ride and Flight`. Each skirmish is a `Skirmish`-scale operation, and the column's Cohesion and Horsestock (the outlaw gauge, applied to a troop as readily as a gang) erode across the run. A running fight that ends in the column's breaking is the campaign's disaster, and the engine should let it be.

### The Cast on the Line

This book's cast is built for this chapter. Carver is the sergeant whose `PRESENCE` and `SHOOTIN'` carry the troop's line; Calder's herd is the stake the war party has come for; Riddle is the man in the wrong place whose `SHOOTIN'` may save him or expose him; Sandoval's way-station is the ground the column falls back to. The GM should let the battle be a place the cast's histories surface, the way the drive and the trial are. A war party under a leader the troop has wronged fights differently from one driven by hunger; a lieutenant the sergeant has saved twice is a lieutenant who will listen on the third.

The mass combat chapter is also the chapter where this book's honest rendering of the Indian Wars must do its work. The nations the troop campaigns against are not statblocks; they are peoples with their own causes, their own factions, and their own claims on the country, and the writing skill's `native-material-culture.md` governs every scene in which they appear. A campaign that runs mass combat with only one side humanized is lying about the war, the way a campaign that runs justice with only one side of the law is lying about the bench.

### Sample Units

Four units, in the statblock voice the rest of the book uses, so a GM can see how a unit looks on the page. The named figures are drawn from the cast.

#### The Tenth, Company D (Dismounted)

| Quality | Strength | Cohesion | The Unit |
| --- | --- | --- | --- |
| `3` Veteran | `D6` | `3` Solid | Twenty-two carbines, a sergeant who reads, a lieutenant who does not |

**Talents:** Attached leader `— Sergeant Moses Carver` `SHOOTIN' 4`, `PRESENCE 4`, `ANIMAL HANDLIN' 3`. Adds `+4` dice (capped to `+3`) when Carver leads the unit's fire or rally.

**Notes:** The troop fights dismounted in four-to-one doctrine — one man in four holds the horses. A dismounted troop at full Strength fields about sixteen carbines. The horse-holder is the unit's soft flank; if the horses are stampeded or taken, the troopers are afoot and the unit's effective Quality drops to `2` for pursuit and flight.

#### The War Party, Under Iron Hail

| Quality | Strength | Cohesion | The Unit |
| --- | --- | --- | --- |
| `3` Veteran | `D8` (oversized) | `4` Solid | Forty mounted Lakota, repeaters and bows, a chief with a grievance |

**Talents:** Attached leader `— Iron Hail` `SHOOTIN' 4`, `ANIMAL HANDLIN' 5`, `HAWKEYE 4`. Adds `+3` dice (capped) to the unit's mounted moves, volleys, and reads.

**Notes:** The war party fights as it campaigns — fast, mounted, refusing the set engagement unless the ground favors it. A war party that takes a defended ridge is a war party that means to; a war party that breaks off is not beaten, it is elsewhere. The troop's mistake is reading a withdrawal as a rout.

#### The Committee's Mob

| Quality | Strength | Cohesion | The Unit |
| --- | --- | --- | --- |
| `1` Green | `D6` | `2` Fraying | Thirty armed townsmen, two ranchers with rifles, a storekeeper in command |

**Talents:** No attached leader of quality. The mob fights with the courage of the drunk and the reserve of the man with something to lose.

**Notes:** The mob is dangerous in the way all armed mobs are — to itself and to anyone caught — and it breaks the moment the exchange goes against it. A mob that takes even one step of Strength loss tests Morale immediately, which is the difference between a posse and a lynching party.

#### Calder's Trail Crew, on the Defensive

| Quality | Strength | Cohesion | The Unit |
| --- | --- | --- | --- |
| `2` Regular | `D6` | `3` Solid | Twelve cowhands, revolvers and a rifle or two, a trail boss who has seen this before |

**Talents:** Attached leader `— Webb Calder` `SHOOTIN' 3`, `ANIMAL HANDLIN' 4`, `PRESENCE 3`. Adds `+3` dice (capped) when Calder holds the crew on the line.

**Notes:** The crew is not a military unit, and it should not be played as one. It fights to hold what it has — the herd, the chuck, the horses — and it breaks the moment the herd stamps or the horses are taken. A trail crew that holds a war party for two exchanges has done a remarkable thing, and the GM should let the engine say so.

A campaign that uses these rules will find that the skirmish line is where the book's pressures meet. The battle is the engine's largest scale, and it is built to make the fight feel like the work it was — loud, confused, costly, and decided as often by the cohort and the country as by the player characters' courage. The war is the setting's central fact, and the rules here are the engine's honest accounting of it, run on the same dice and the same gauges as the saloon brawl and the jailbreak, because the country is one country and the rules that govern it should be one engine.
