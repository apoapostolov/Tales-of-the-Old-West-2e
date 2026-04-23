# Village Statblock Helper for Montana Supplement

This document replaces the earlier inferred location-profile model.

The correct source for Montana village statblocks is:

- the settlement rules in [corebook/08-campaigns-in-the-old-west.md](/home/apoapostolov/git-public/Tales-of-the-Old-West-2e/corebook/08-campaigns-in-the-old-west.md)
- the presentation used for `Jornada Springs` in [corebook/09-the-new-mexico-campaign.md](/home/apoapostolov/git-public/Tales-of-the-Old-West-2e/corebook/09-the-new-mexico-campaign.md)

## Correction

The previous Montana helper was wrong because it treated the village statblock as a custom environment-and-pressure dashboard:

- water security
- timber access
- grazing access
- arable land
- freight access
- winter risk
- Army reach
- and similar tags

Those are useful design notes, but they are not the corebook's village statblock.

For a real settlement entry in this project, the statblock should use the settlement system:

1. `Settlement Points`
2. `Bonus SP per Season`
3. `Civic Offices`
4. six settlement aspects:
   - `FARMING`
   - `MERCANTILE`
   - `NATURAL RICHES`
   - `LAW`
   - `CIVIC`
   - `WELFARE`
5. `PROSPERITY`
6. amenity history

Montana-specific terrain, weather, Native-political pressure, Army reach, and freight logic belong in prose notes around the statblock, not inside it.

## What Jornada Springs Actually Shows

`Jornada Springs` uses five linked blocks:

1. summary table
2. civic-offices table
3. aspect-track grid with `X` marks and rank milestones
4. prosperity table
5. amenity ledger by year and season

That is the template to follow.

## Core Rule Frame

The six settlement aspects each run on tally points and ranks.

- Rank `I` begins at `1`
- Rank `II` begins at `3`
- Rank `III` begins at `7`
- Rank `IV` begins at `13`
- Rank `V` begins at `19`
- Rank `VI` begins at `26`

The GM-facing meaning of the aspects comes from the rulebook:

- `FARMING`: the settlement's food production and agricultural base
- `MERCANTILE`: trade, stores, services, and general business life
- `NATURAL RICHES`: extractive wealth and useful raw resources
- `LAW`: formal and informal justice, enforcement, and the grip of order
- `CIVIC`: public life, institutions, meetings, schools, and municipal confidence
- `WELFARE`: sanitation, danger mitigation, medicine, and how survivable the place is

`PROSPERITY` is the sum of the six aspect totals. Its band sets the settlement class and Turn of the Season modifier:

| Prosperity total | Description | Turn of the season modifier | Population guidance |
| --- | --- | --- | --- |
| 6-10 | Trading Post | `-2` to the Tens die | a couple hundred at most |
| 11-14 | Camp | `-1` to the Tens die | up to about `500` |
| 15-18 | Shanty | `-3` to the Units die | over `500`, under `1,000` |
| 19-23 | Village | no modifier | around `1,000` |
| 24-27 | Town | `+3` to the Units die | about `1,500-2,000` |
| 28-31 | Large town | `+1` to the Tens die | more than `2,500` |
| 32-36 | City | `+2` to the Tens die | `5,000+` |

## Required Block Format

Every full Montana settlement statblock should be built in this order.

### 1. Summary table

```md
| Bozeman Summary | Value |
| --------------- | ----- |
| Settlement Points | 0 |
| Bonus SP per Season | 1 |
```

### 2. Civic offices table

This mirrors `Jornada Springs`.

```md
| Civic Offices | Holder | Notable Citizens | Role |
| --- | --- | --- | --- |
| Mayor | None | [Name] | [power base] |
| Judge | None | [Name] | [power base] |
| Sheriff | None | [Name] | [power base] |
| Deputy | None | [Name] | [power base] |
```

Use `None` when the office does not formally exist or is not yet filled.

### 3. Aspect-track grid

This is the heart of the statblock. Copy the aspect table structure from the village template exactly, including every helper row you have added there.

At minimum, the grid must preserve:

- the `Aspect` header row with columns `1` through `30`
- the alignment row
- the `Rank Milestones` row
- each aspect row in order:
  - `FARMING`
  - `MERCANTILE`
  - `NATURAL RICHES`
  - `LAW`
  - `CIVIC`
  - `WELFARE`

The values are shown with `X` marks, not with a single numeric score.

Use this exact working pattern from the template:

```md
| Aspect          | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  | 13  | 14  | 15  | 16  | 17  | 18  | 19  | 20  | 21  | 22  | 23  | 24  | 25  | 26  | 27  | 28  | 29  | 30  |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Rank Milestones | I   |     | II  |     |     |     | III |     |     |     |     |     | IV  |     |     |     |     |     | V   |     |     |     |     |     |     | VI  |     |     |     |     |
| FARMING         | [X] |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| MERCANTILE      | [X] |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| NATURAL RICHES  | [X] |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| LAW             | [X] |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| CIVIC           | [X] |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| WELFARE         | [X] |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
```

If you add another structural row to the template later, update this helper and copy that row into the example block instead of describing it loosely.

### 4. Prosperity table

Repeat the full prosperity-band table and mark the active band with `X`, as `Jornada Springs` does.

### 5. Amenity ledger

Track how the settlement became what it is.

```md
| Year | Season | Amenity | Notes |
| ---- | ------ | ------- | ----- |
| 1871 | Spring | Wells | foundation amenity |
| 1871 | Summer | Sheriff's Office | law takes shape |
```

Include `+1 SP per Season` notes for `Church` or `Newspaper` where relevant.

## Montana-Specific Additions

These are allowed, but they must sit outside the statblock proper.

Add a short prose or bullet section after the amenity ledger for:

- county or district
- road, river, pass, or freight position
- winter pressure
- Army or federal reach
- Native political-military context in `1873`
- what the settlement exports
- what it must import

That gives Montana its territorial specificity without breaking the corebook rules format.

## How to Derive a Montana Settlement

Start with the actual life of the place, then map that into the six-aspect system.

### Farming

Ask:

- does the place feed itself well
- is it a ranching place, farming place, or both
- does it have hay, corrals, barns, markets, or stock trade

### Mercantile

Ask:

- does it have stores, hotels, saloons, traders, blacksmiths, attorneys, doctors
- is it on a route people rely on
- can people buy specialist services there

### Natural Riches

Ask:

- does it rest on mining, timber, trapping, fishing, clay, quarrying, or other extractive base
- how much of its confidence comes from raw material wealth

### Law

Ask:

- is there a sheriff
- is there a judge or courthouse
- do outlaws avoid the place or work it openly

### Civic

Ask:

- does the settlement have meetings, schools, churches, fairs, a paper, a council
- does it behave like a community or just a camp of interests

### Welfare

Ask:

- does it have wells, latrines, stables, cemetery, doctor, apothecary, fire response
- how badly do weather, disease, industrial accidents, or remoteness hurt it

## What Not to Do

- Do not replace the six aspects with environmental tags.
- Do not collapse the aspect grid into one summary number.
- Do not use `Tier`, `Water Security`, `Freight Access`, `Army Reach`, or `Strategic Value` as the main village statblock fields.
- Do not treat the prosperity label like flavor text; it is mechanically tied to Turn of the Season.

## Practical Montana Rule

For this supplement, use two layers:

1. the corebook settlement statblock for rules-facing village format
2. Montana prose notes for terrain, winter, Native politics, Army presence, freight, and outlaw pressure

That preserves compatibility with the game while still making Montana feel like Montana.
