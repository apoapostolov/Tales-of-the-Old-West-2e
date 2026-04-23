# NPC Creation Helper for Montana Supplement

This document is a working crib for building NPCs for `supplement-2-montana-campaign/` without reopening half the corebook every time.

It is based on:

- [corebook/02-your-player-character.md](/mnt/c/git-public/tales-of-the-old-west-2e/corebook/02-your-player-character.md)
- [corebook/04-talents.md](/mnt/c/git-public/tales-of-the-old-west-2e/corebook/04-talents.md)
- [corebook/09-the-new-mexico-campaign.md](/mnt/c/git-public/tales-of-the-old-west-2e/corebook/09-the-new-mexico-campaign.md)
- [corebook/10-patience-is-a-virtue.md](/mnt/c/git-public/tales-of-the-old-west-2e/corebook/10-patience-is-a-virtue.md)

Use this helper for fast draft work. If a later rules pass shows a mismatch, fix the helper and then fix the NPCs derived from it.

## First Rule: NPCs Are Not Bound by Player Creation Limits

The character-creation rules in the corebook are advisory for starting player characters. They are a useful baseline for what an ordinary capable person looks like at the beginning of play.

They are not a ceiling for NPC design.

For Montana supplement work, the AI may and should build NPCs above player-character starting limits when the fiction calls for it.

That means:

- an important officer can have higher attributes than a starting player character
- a veteran scout can have more abilities at useful ratings than a starting player character
- a wealthy mine owner, railroad fixer, or territorial judge can have more talents, better gear, and broader social reach
- a feared killer, famous lawman, or chapter boss can be plainly stronger than the party at the start of a campaign

Do not weaken an NPC just to make them look fair under player creation rules. Build the block that the fiction demands.

## How to Use Player Rules Properly

Use player-character creation rules as:

- a language for judging what is ordinary
- a baseline for what a new but competent frontier adult may look like
- a source for ability, attribute, gear, and talent names

Do not use them as:

- a cap on NPC power
- a limit on number of talents
- a limit on useful gear
- a ban on wide skill spread for older, richer, harder, or more established NPCs

If a man has spent twenty years riding, killing, bribing, studying, commanding, or surviving, his block should show it.

## Core Rule Reminders

### Attributes

Every person has four attributes:

- `GRIT`
- `QUICK`
- `CUNNING`
- `DOCITY`

Player-character guidance says healthy people do not usually go below `2`. Keep that as the default for ordinary human NPCs unless sickness, age, injury, or unusual weakness matters to play.

### Abilities

Abilities run from `0` to `5`. For ordinary published NPC work, staying inside `0-3` keeps the numbers readable and close to many existing statblocks.

That said, powerful NPCs may exceed that comfort band.

Use `4` or even `5` when needed for:

- legendary specialists
- feared killers
- brilliant professionals
- long-serving guides or scouts
- major political, legal, or economic powers whose competence is part of the threat

Attribute pairings:

- `GRIT`: `FIGHTIN'`, `LABOR`, `PRESENCE`, `RESILIENCE`
- `QUICK`: `LIGHT-FINGERED`, `MOVE`, `OPERATE`, `SHOOTIN'`
- `CUNNING`: `ANIMAL HANDLIN'`, `HAWKEYE`, `INSIGHT`, `NATURE`
- `DOCITY`: `BOOKLEARNIN'`, `DOCTORIN'`, `MAKIN'`, `PERFORMIN'`

### Talents

Talents come in `Basic` and `Advanced`.

For fast NPC design:

- ordinary folk usually have `0-1` talents
- seasoned field hands usually have `1-2`
- named professionals usually have `2-4`
- major movers can carry `4-5` if the fiction supports it
- top-tier NPCs may carry `6+` talents if age, reputation, and role justify it

More talents are especially appropriate for:

- old campaign antagonists
- famous lawmen
- chapter bosses
- wealthy operators with education, influence, and hired help
- elite scouts, hunters, and warriors

### Publication Pattern

The published campaign chapters do not write full player-character sheets. They write lean NPC blocks:

1. attributes
2. only the abilities that matter at the table
3. talents
4. one or two weapons

Follow that pattern unless the NPC is unusually complicated.

## Statblock Format

Mirror the existing campaign format:

```md
**NAME**

| GRIT | 4 | QUICK | 3 | CUNNING | 4 | DOCITY | 3 |
| ---- | - | ----- | - | ------- | - | ------ | - |
| SHOOTIN' | 2 |     |   | INSIGHT | 2 |        |   |
| PRESENCE | 2 |     |   | NATURE  | 1 |        |   |

**Talents:** AUTHORITY (Basic), QUICK DRAW (Basic).

| Weapon             | Action | Draw Mod | Attack Mod | Damage | Critical | Range  | Ammo |
| ------------------ | ------ | -------- | ---------- | ------ | -------- | ------ | ---- |
| Colt 45 Peacemaker | Single | -1       | +1         | 3      | 1        | Medium | 6    |
```

Rules:

- list only relevant abilities
- leave blank cells blank
- do not pad the table with zeros
- use all-caps for the NPC name
- keep weapon lists short

## Fast Build Method

### Step 1. Pick the job

Ask what the NPC actually does in play:

- talker
- gun hand
- officer
- scout
- clerk
- doctor
- rancher
- miner
- outlaw
- labor boss
- preacher

Do not start with numbers. Start with function.

### Step 2. Pick one strong attribute

Most NPCs should have one clear edge.

Examples:

- officer: `CUNNING` or `DOCITY`
- cavalry trooper: `GRIT` or `QUICK`
- scout: `CUNNING`
- surveyor: `DOCITY`
- freight boss: `GRIT`
- confidence man: `DOCITY`

### Step 3. Pick three useful abilities

Most scenes only test a few things. Give the NPC the abilities those scenes need.

Examples:

- Army officer: `PRESENCE`, `INSIGHT`, `SHOOTIN'`
- surveyor: `BOOKLEARNIN'`, `OPERATE`, `NATURE`
- scout: `HAWKEYE`, `NATURE`, `MOVE`
- freight boss: `LABOR`, `ANIMAL HANDLIN'`, `PRESENCE`
- outlaw leader: `SHOOTIN'`, `MOVE`, `INSIGHT`

### Step 4. Add talents that explain reputation

Talents should answer: why is this person worth naming?

Examples:

- respected officer: `AUTHORITY`
- smooth operator: `CHARMING`
- trail man: `TRACKER`, `LIGHT-FOOTED`, `MOUNTAIN FOLK`
- hard killer: `COLD BLOODED`, `DEAD EYE`, `FAST SHOOTER`
- railroad or survey specialist: `ENGINEER`, `EDUCATED`

### Step 5. Give them one weapon they would actually carry

Do not over-arm everyone. A clerk with a pistol and a knife is enough. A surveyor may be worse with a gun than the cook.

### Step 6. Decide whether this person exceeds player scale

Ask plainly:

- Is this person older, richer, harder, more feared, more educated, or more influential than a starting player character?
- Has this person had years or decades to accumulate expertise, scars, and equipment?
- Is the point of the scene partly that the players are dealing with someone out of their weight class?

If yes, raise the block without apology.

## Rating Bands

Use these as rough production tiers.

### Tier 1. Background civilian

For clerks, cooks, camp followers, laborers, drunks, witnesses.

- attributes: mostly `2`
- one attribute may be `3`
- abilities: `1-2` relevant ratings
- talents: `0-1`

### Tier 2. Working frontier hand

For teamsters, ranch hands, ordinary troopers, mule skinners, miners, packers.

- attributes: one `4`, one or two `3`, none below `2`
- abilities: `2-4` relevant ratings, mostly `1-2`
- talents: `1-2`

### Tier 3. Proven professional

For officers, scouts, lawmen, veteran outlaws, business operators, good doctors.

- attributes: usually `4/4/3/3` or `4/3/3/3`
- abilities: `3-5` relevant ratings, often one or two at `3`
- talents: `2-4`

### Tier 4. Chapter mover

For adventure bosses, key patrons, feared killers, major political operators.

- attributes: one `5` is fine if it matters
- abilities: wide spread, but still keep the block readable
- talents: `4-5`

Do not hand out `5`s casually. If someone has a `5`, the table should feel it.

### Tier 5. Territory mover

For people who should feel larger than most starting player characters in every room they enter.

Examples:

- territorial governors and chief political fixers
- famous vigilante veterans
- feared outlaw chiefs
- legendary scouts
- dominant merchants, syndicate men, judges, and cattle barons

Guidelines:

- attributes: one or two `5`s is acceptable
- abilities: several at `3-4`, with one signature rating at `4-5`
- talents: `5-7`
- gear: high-quality, rare, or unusually well-maintained

This tier exists for NPCs who should feel dangerous before they ever draw.

## Advanced NPC Design Rules

### More skills than a player character

NPCs may have a broader spread of useful abilities than a new player character because they are older, more specialized, or simply more established in the world.

Examples:

- a veteran officer may have `PRESENCE`, `INSIGHT`, `SHOOTIN'`, `ANIMAL HANDLIN'`, and `BOOKLEARNIN'`
- a famous scout may have `HAWKEYE`, `NATURE`, `MOVE`, `ANIMAL HANDLIN'`, `SHOOTIN'`, and `INSIGHT`
- a merchant prince may have `PRESENCE`, `BOOKLEARNIN'`, `PERFORMIN'`, `INSIGHT`, and `LIGHT-FINGERED`

### More talents than a player character

If a character's reputation comes from long practice, wealth, schooling, or violence, stack the talents needed to show that.

The only real check is readability. If the block stops being useful at the table, cut back to the talents that matter in play.

### More and better gear

NPCs may own:

- multiple firearms
- rare or expensive guns
- quality tack and horses
- papers of office
- ledgers, deeds, instruments, watches, and valuable personal equipment
- hired guards, assistants, or servants beyond what a player character starts with

Wealth and influence should show in gear, not just in biography.

### Social power is real power

Do not measure strength only by combat.

A judge with `LAWYER`, `HIGH SOCIETY`, `AUTHORITY`, and a bought sheriff may be more dangerous than a fine gunman. A railroad fixer with ledgers, telegraph access, and hired riders may be stronger than the strongest duelist in town.

Build that power into the block, the writeup, and the scene.

## Quick Packages

### Army officer

- attributes: `GRIT 3`, `QUICK 3`, `CUNNING 4`, `DOCITY 3`
- abilities: `PRESENCE 2-3`, `INSIGHT 2`, `SHOOTIN' 1-2`, `RIDE` is folded into `ANIMAL HANDLIN' 1-2`
- talents: `AUTHORITY`, `JUDGE OF CHARACTER`, `QUICK DRAW`

### Trooper or cavalry corporal

- attributes: `GRIT 4`, `QUICK 3`, `CUNNING 3`, `DOCITY 2`
- abilities: `SHOOTIN' 2`, `FIGHTIN' 1-2`, `ANIMAL HANDLIN' 1`, `RESILIENCE 1-2`
- talents: `BORN IN THE SADDLE`, `FAST SHOOTER`, `HARD TO HIT`

### Frontier scout

- attributes: `GRIT 3`, `QUICK 3`, `CUNNING 5`, `DOCITY 2`
- abilities: `HAWKEYE 3`, `NATURE 3`, `MOVE 2`, `INSIGHT 2`
- talents: `TRACKER`, `LIGHT-FOOTED`, `MOUNTAIN FOLK`, `ANIMAL HUNTER`

### Surveyor or engineer

- attributes: `GRIT 2`, `QUICK 2`, `CUNNING 4`, `DOCITY 4`
- abilities: `BOOKLEARNIN' 3`, `OPERATE 2`, `NATURE 2`, `MAKIN' 1`
- talents: `EDUCATED`, `ENGINEER`

### Freight boss

- attributes: `GRIT 4`, `QUICK 2`, `CUNNING 4`, `DOCITY 2`
- abilities: `LABOR 2`, `ANIMAL HANDLIN' 2`, `PRESENCE 2`, `INSIGHT 1`
- talents: `BUSINESS MINDED`, `AUTHORITY`, `BRONC BUSTER`

### Merchant or town booster

- attributes: `GRIT 2`, `QUICK 2`, `CUNNING 4`, `DOCITY 4`
- abilities: `PRESENCE 2`, `BOOKLEARNIN' 2`, `PERFORMIN' 2`, `INSIGHT 2`
- talents: `BUSINESS MINDED`, `CHARMING`, `HIGH SOCIETY`

### Outlaw rider

- attributes: `GRIT 3`, `QUICK 4`, `CUNNING 3`, `DOCITY 2`
- abilities: `SHOOTIN' 2-3`, `MOVE 2`, `HAWKEYE 1-2`, `LIGHT-FINGERED 1`
- talents: `FAST SHOOTER`, `QUICK DRAW`, `COLD BLOODED`, `DEAD EYE`

### Camp clerk or paper man

- attributes: `GRIT 2`, `QUICK 2`, `CUNNING 3`, `DOCITY 4`
- abilities: `BOOKLEARNIN' 2-3`, `INSIGHT 1`, `PERFORMIN' 1`, `LIGHT-FINGERED 1`
- talents: `EDUCATED`, `FORGER`, `SHILL`

## Ability Benchmarks

These are not formal rules. They are production shortcuts.

- `0`: can try it if the fiction allows, but has no special competence
- `1`: knows the work
- `2`: dependable professional
- `3`: locally respected, dangerous, or unusually good
- `4+`: reserve for exceptional cases

For Montana campaign work, read them this way:

- `4`: district-level threat or talent
- `5`: rare enough that people tell stories about it

## Talent Shortlist for This Supplement

The Montana book will keep reusing these.

### Field and travel

- `ANIMAL HUNTER`
- `BORN IN THE SADDLE`
- `BRONC BUSTER`
- `GUARD DOG`
- `LIGHT-FOOTED`
- `MOUNTAIN FOLK`
- `SURVIVOR`
- `TRACKER`

### Violence

- `AUTHORITY`
- `BRAWLER`
- `COLD BLOODED`
- `DEAD EYE`
- `DEFENDER`
- `FAST SHOOTER`
- `HARD TO HIT`
- `KNIFE FIGHTER`
- `LIGHTNING FAST`
- `QUICK DRAW`
- `SHARPSHOOTER`
- `SHOTGUN MASTER`

### Social and institutional

- `BUSINESS MINDED`
- `CALMING MANNER`
- `CHARMING`
- `EDUCATED`
- `ENGINEER`
- `HIGH SOCIETY`
- `JUDGE OF CHARACTER`
- `LAWYER`
- `RABBLE ROUSER`
- `THE VOICE`

### Dirty work

- `FORGER`
- `LOCKPICKER`
- `MANHUNTER`
- `SHILL`
- `SWINDLER`

## Working Weapon Palette

Use the values already seen in published campaign statblocks so the appendix matches the existing books.

| Weapon             | Action | Draw Mod | Attack Mod | Damage | Critical | Range  | Ammo |
| ------------------ | ------ | -------- | ---------- | ------ | -------- | ------ | ---- |
| Colt 45 Peacemaker | Single | -1       | +1         | 3      | 1        | Medium | 6    |
| Metropolitan Navy  | Single | 0        | +1         | 2      | 1        | Medium | 6    |
| Derringer          | Single | +2       | 0          | 1      | 2        | Short  | 1    |
| Winchester 1873    | Lever  | N/A      | +2         | 2      | 1        | Long   | 15   |
| Spencer Carbine    | Lever  | N/A      | +2         | 2      | 1        | Long   | 7    |
| Standard Shotgun   | Breech | N/A      | +1         | 3      | 3        | Medium | 2    |
| Hunting Blade      | N/A    | N/A      | +2         | 2      | 1        | Arms   | -    |
| Standard Bow       | Special| 0        | +1         | 1      | 1        | Medium | N/A  |

If later manuscript work needs buffalo guns, repeaters, or special weapons, add them here first.

## When to Push Above Starting Power

Raise an NPC above starting-player scale when they are any of the following:

- older than the party by a generation
- well trained by Army, law, Church, mission, or trade institutions
- rich enough to buy leverage and education
- violent enough to have survived long by being better than most men around them
- famous enough that their name should already alter a room

Questions to ask:

- Should the players feel outclassed, impressed, or wary on sight?
- Would a weaker block make this NPC's reputation unbelievable?
- Is this person an anchor for a whole settlement, faction, or chapter?

If yes, build upward.

## Final Sanity Check

Before locking an NPC:

- Does the statblock match the life story?
- Does the gear match the money and influence?
- Do the talents explain the reputation?
- If the NPC is powerful, does the block actually show that power?

If not, the block is still too timid.

## Native and Military NPC Notes

- Do not make Native scouts or war leaders generic copies of white frontier archetypes with different names.
- Give Army officers `PRESENCE`, paper men `BOOKLEARNIN'`, scouts `HAWKEYE` and `NATURE`, freight men `LABOR` and `ANIMAL HANDLIN'`.
- Distinguish people by work, rank, and lived pressure, not just by faction label.

## Appendix Discipline for Chapter 02

For the starter adventure:

- every named NPC in `book-content/02-the-yellowstone-line.md` must appear in `book-content/02A-dramatis-personae-and-statblocks.md`
- unnamed extras can use generic profiles
- if a new named NPC is added during revision, add the statblock the same day

Use this checklist when writing:

- Is the NPC named on the page?
- Will the players likely talk to, fight, follow, or remember them?
- Does that NPC need a block in chapter `02A`?

If the answer is yes, add the block.
