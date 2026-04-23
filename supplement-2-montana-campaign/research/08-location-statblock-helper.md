# Village Statblock Helper for Montana Supplement

This document defines how to turn a real 1870s settlement into the village statblock used by the Montana supplement.

The correct source for the rules is:

- the settlement rules in [corebook/08-campaigns-in-the-old-west.md](/home/apoapostolov/git-public/Tales-of-the-Old-West-2e/corebook/08-campaigns-in-the-old-west.md)
- the settlement presentation used for `Jornada Springs` in [corebook/09-the-new-mexico-campaign.md](/home/apoapostolov/git-public/Tales-of-the-Old-West-2e/corebook/09-the-new-mexico-campaign.md)
- the Montana template in [villages/00-village-template.md](/home/apoapostolov/git-public/Tales-of-the-Old-West-2e/supplement-2-montana-campaign/villages/00-village-template.md)

Montana material may add terrain, freight, winter, Native-political, Army, and outlander notes in prose, but the village statblock itself should stay in the corebook format.

## What the Statblock Is Doing

The village statblock is not a demographic spreadsheet. It is a game-facing profile of how a real settlement behaves under frontier pressure.

The six aspects measure:

- `FARMING`
- `MERCANTILE`
- `NATURAL RICHES`
- `LAW`
- `CIVIC`
- `WELFARE`

The statblock also tracks:

- `Settlement Points`
- `Bonus SP per Season`
- civic offices
- aspect ranks
- `PROSPERITY`
- amenity history

The job of this helper is to turn real settlement facts into those numbers in a consistent way.

## The Data You Should Collect

When researching a real village, gather these facts first.

- Population for the target year.
- Household count if available.
- Population density in the built-up district.
- Settled footprint, if the map or source gives one.
- Number and type of permanent buildings.
- Number of stores, saloons, hotels, stables, blacksmiths, banks, churches, schools, mills, and offices.
- Transport access: rail, river landing, ferry, wagon road, trail junction, stage stop, freight depot, or pass.
- Main economic base: farming, ranching, mining, timber, trade, government, military, or mixed.
- Output or throughput if the source gives it: bushels, cattle, tons, carloads, freight wagons, payrolls, claims, assay values, or tax receipts.
- Signs of state power: sheriff, judge, marshal, jail, county seat, court, ordinance, militia, Army presence.
- Signs of civic life: church, school, newspaper, hall, lodge, fair, mutual aid, elections, councils, festivals.
- Signs of welfare pressure: water, drainage, wells, fire risk, disease, winter exposure, flood risk, industrial injury, and road isolation.

If the data is sparse, use the best contemporary estimate and classify the settlement by its actual lived role rather than by modern municipal boundaries.

## Mandatory People Rule

If a settlement has meaningful `LAW` in its statblock, do not leave the civic offices blank.

- A lawful settlement must have named people for `Mayor`, `Judge`, `Sheriff`, and `Deputy` or the closest historically accurate equivalents.
- Search the settlement year first, then widen the search across the full `1870s` if the exact year is thin.
- Search settlement histories, county histories, newspapers, court records, city directories, and territorial references before giving up.
- If no documented officeholder can be verified after that search, invent a plausible officeholder and record the inference only in private research notes, not in the public chapter text.
- Do not use `None` for all authority figures in a place that is already described as having law or formal order.
- If the settlement lacks a formal municipal office in the period, use the nearest actual authority figure: justice of the peace, county sheriff, county judge, marshal, town trustee, or acting mayor.

## How To Measure Density

Population density matters because a compact village behaves differently from a spread-out ranching district.

Use one of these methods:

- If you know the built-up area in acres, divide population by built-up acres.
- If you know the number of town blocks, estimate one developed block as about 2 to 3 acres of effective settlement land.
- If the town is linear, such as a river landing, road village, or rail stringtown, measure the inhabited strip rather than the whole township grant.
- If the settlement is dispersed, measure the inhabited core separately from the surrounding farms or ranches.

Use the built-up density, not the county average.

### Density Bands

Use the bands below as a guide.

| Density | Settlement shape | Typical effect |
| --- | --- | --- |
| Under 5 people per developed acre | scattered hamlet, ranch district, mission outbuildings, loose farm cluster | strong `FARMING`, weak `MERCANTILE`, limited civic life |
| 5-15 people per developed acre | ordinary village, small plaza town, thin mining camp | balanced village with one or two clear strengths |
| 16-40 people per developed acre | compact village core, district center, railroad stop with a real street front | stronger `MERCANTILE`, `CIVIC`, and usually `LAW` |
| 41-80 people per developed acre | crowded village core or busy camp town | high trade, visible public life, rising health pressure |
| 81+ people per developed acre | tight town center, mining rush core, railroad bottleneck | strong `MERCANTILE` and `LAW`, but welfare stress is common |

## The Conversion Method

Start all six aspects at rank 1. That gives the village the minimum baseline the corebook expects.

Then add tally points using the rules below.

### 1. Farming

Add tally points for evidence of food production and land use.

- +1 if the village depends on farming or ranching in its immediate district.
- +1 if there are fields, orchards, irrigation works, fences, corrals, barns, or feed lots.
- +1 if the settlement exports food, stock, hay, butter, eggs, or grain rather than only feeding itself.
- +1 if most household life depends on local agricultural production.
- +1 if there is a gristmill, creamery, stockyard, or regular produce exchange.
- -1 if the area is arid, rocky, steep, flood-prone, frost-prone, or otherwise unreliable for agriculture.
- -1 if the village imports most of its food and survives on freight rather than local production.

### 2. Mercantile

Add tally points for trade, services, and cash circulation.

- +1 if there are 3 or more permanent stores, saloons, hotels, or service businesses.
- +1 if there is a bank, freight office, post office, livery, newspaper, or regular market.
- +1 if the village is on a rail line, river landing, ferry, major wagon road, or trail junction.
- +1 if it serves as the trade center for farms, mines, ranches, or surrounding hamlets.
- +1 if the place supports specialist services like a doctor, lawyer, blacksmith, milliner, or undertaker.
- +1 if weekly or seasonal freight traffic is a visible part of life.
- -1 if freight is unreliable, the place is isolated, or trade mostly leaks to a larger nearby town.
- -1 if the population exists but cash trade barely does.

### 3. Natural Riches

Add tally points for extractive wealth and raw resources.

- +2 if the village exists mainly because of mining, timber, trapping, fishing, quarrying, or a similar extractive base.
- +1 if there is a working mine, sawmill, panning district, timber stand, trap line, quarry, salt lick, or other usable resource.
- +1 if the town draws outside labor or outside capital because of the resource.
- +1 if the resource is still expanding rather than already exhausted.
- +1 if the settlement controls a useful waterpower, stone source, clay bed, or rich floodplain.
- -1 if the resource is seasonal, speculative, or already nearly worked out.
- -1 if the town exists only as a transport stop for resource extraction elsewhere.

### 4. Law

Add tally points for the degree to which order is formalized and enforced.

- +1 if there is a sheriff, marshal, constable, justice of the peace, or regularly active peace officer.
- +1 if there is a jail, courthouse, police room, or regular hearing space.
- +1 if the village is a county seat, district seat, military post, railroad division point, or company town with formal authority.
- +1 if ordinances are enforced, firearms are restricted, vice is licensed, or fines are collected.
- +1 if the law can actually be brought to bear beyond a single family or faction.
- -1 if vigilantes, range war, strike violence, or open intimidation are normal.
- -1 if the place is a legal vacuum and the only rule is who is armed.

### 5. Civic

Add tally points for the social and institutional life of the settlement.

- +1 if there is a school, church, mission, meetinghouse, lodge, town hall, newspaper, or public hall.
- +1 if elections, councils, festivals, fairs, mutual aid, or civic committees actually happen.
- +1 if the village has a recognized center of communal identity rather than only workspaces and sleeping quarters.
- +1 if there are 2 or more enduring civic institutions.
- +1 if the place is a county seat, church center, Mormon ward, mission village, or ethnic district with a shared social structure.
- -1 if the settlement is only a work camp, a freight stop, or a collection of business interests with no public life.

### 6. Welfare

Add tally points for survivability, infrastructure, and hazard control.

- +1 if there is reliable clean water, wells, drainage, or a decent natural supply.
- +1 if housing is sturdy enough for the climate rather than temporary canvas or shacks.
- +1 if there is a doctor, apothecary, midwife, hospital, or other practical medical support.
- +1 if there is sanitation, latrines, waste removal, fire response, or some effort at public health.
- +1 if the settlement is buffered from common frontier dangers like raids, wildfire, flood, winter blowups, or industrial accidents.
- +1 if mutual aid, family networks, or a religious community absorb hardship.
- -1 if disease, bad water, exposed housing, winter exposure, fire, or industrial injury is part of daily life.
- -1 if the settlement is on a floodplain, in a tight canyon, on a burnable timber edge, or in other hazardous ground.

## How To Use Population In The Score

Population does not directly create an aspect rank. It acts as evidence.

Use these population rules as a shortcut.

| Population | Common read | Likely aspect pressure |
| --- | --- | --- |
| Under 100 | hamlet, ranch cluster, mission satellite, line camp | weak `MERCANTILE`, weak `LAW`, low civic load |
| 100-299 | small village | one local trade center, one church or school, modest welfare pressure |
| 300-699 | established village | clear trade life, some civic structure, first formal law signs |
| 700-1,499 | district village | market gravity, public institutions, stronger law and services |
| 1,500-2,999 | large village or small town | dense trade, formal order, visible welfare strain |
| 3,000+ | town-scale settlement | usually not a village any more unless it is highly specialized |

Population matters most when it is paired with density and institutions.

## Quick Settlement-Type Rules

Use the real-world settlement type to decide where to push the score.

### Agricultural village

- `FARMING` usually ends up highest.
- `CIVIC` can be surprisingly strong if the church or school is central.
- `MERCANTILE` is usually moderate.
- `LAW` is usually light unless it is a county seat or railroad node.

### Hispano plaza village

- `CIVIC` and `FARMING` often carry the place.
- `WELFARE` can be stronger than outsiders expect because of family networks and older settlement patterns.
- `MERCANTILE` is usually tied to local exchange rather than cash volume.

### Mormon ward village

- `CIVIC` is often the strongest aspect because of meetinghouse, ward, and cooperative labor.
- `FARMING` is usually very strong.
- `WELFARE` is often better than the average frontier village because of mutual aid and planned settlement.

### County seat

- `LAW` and `CIVIC` should be the standout aspects.
- `MERCANTILE` follows the courthouse and service economy.
- `FARMING` may be modest if the seat is a service town rather than an agricultural center.

### Rail village

- `MERCANTILE` is the main driver.
- `LAW` often rises because rail traffic attracts disorder and formal presence.
- `CIVIC` follows if the town becomes a permanent community instead of a stop.

### Mining camp

- `NATURAL RICHES` should usually be highest.
- `MERCANTILE` is the second engine.
- `WELFARE` often suffers because crowding, injury, and bad water are normal.

## Converting Points To Ranks

Once tally points are assigned, use the corebook rank bands.

| Tally points | Rank |
| --- | --- |
| 1-2 | 1 |
| 3-6 | 2 |
| 7-12 | 3 |
| 13-18 | 4 |
| 19-26 | 5 |
| 27+ | 6 |

Do not flatten the village into one average number. Let a place be lopsided if the evidence says it is lopsided.

## Converting Ranks To Prosperity

Add the six ranks together to get `PROSPERITY`.

| Prosperity total | Description | Turn of the season modifier | Population guidance |
| --- | --- | --- | --- |
| 6-10 | Trading Post | -2 to the Tens die | a couple hundred at most |
| 11-14 | Camp | -1 to the Tens die | up to about 500 |
| 15-18 | Shanty | -3 to the Units die | over 500, under 1,000 |
| 19-23 | Village | no modifier | around 1,000 |
| 24-27 | Town | +3 to the Units die | about 1,500-2,000 |
| 28-31 | Large town | +1 to the Tens die | more than 2,500 |
| 32-36 | City | +2 to the Tens die | 5,000+ |

Use the lived role of the settlement to choose the band. A small but institution-heavy village can feel larger than a larger but hollow one.

## Filling The Montana Village Template

Use this order when writing the file.

1. Summary table.
2. Civic offices table.
3. Aspect track grid with `X` marks.
4. Prosperity table.
5. Amenity history ledger.
6. Montana notes prose.

### Summary Table

Set `Settlement Points` to the total tally earned across the six aspects.

Set `Bonus SP per Season` from the village's civic and economic base.

- `0` for a bare camp or dependent stop.
- `1` for an ordinary village with a functioning trade base.
- `2` if the settlement has clear market pull, strong institutions, or durable county-level importance.
- `3` if it is a district center, railroad hub, or unusually strong regional node.

### Civic Offices

Use actual offices if they exist.

- `Mayor` for incorporated or self-governing towns.
- `Judge` if there is a local justice or district court.
- `Sheriff` if the county or district seat supports one.
- `Deputy` or `Marshal` if the place is policed that way.

If the office is missing in the historical record, do not default to `None` for a lawful settlement. Use the closest documented authority figure or, if needed, an invented name that appears cleanly in the final text.

### Amenity History

Track only amenities that materially changed the village.

- `Church`
- `School`
- `Wells`
- `Sheriff's Office`
- `Newspaper`
- `Boardwalks`
- `Hotel`
- `Livery`
- `Bank`
- `Gallows`
- `Town Hall`

The point is to show how the place became what it is.

When the record is incomplete, reconstruct the amenity history from the settlement's economic level and institutional shape.

- Start from the earliest period the settlement could realistically support the amenity, not from the date of the finished building if a simpler form existed earlier.
- Use the town's role to decide the expected order: food and labor services first, then communication and credit, then formal institutions, then public improvements.
- For a market town or county seat, expect `Newspaper`, `Telegraph`, `Bank`, `School`, `Church`, and `Sheriff's Office` to appear early in the 1870s or before if the record supports it.
- For a farming village, backdate `Church`, `School`, `Blacksmith`, `Livery`, and `Cemetery` before luxuries.
- For a mining settlement, backdate `Mines`, `Assay`, `Saloons`, `Jail`, and `Doctors` before civic polish.
- If a source gives only an approximate decade, use the earliest defensible year inside that decade and note the uncertainty in your research ledger, not in the public statblock.
- If a settlement is prosperous enough to support a stronger amenity than the record explicitly names, infer the amenity from the town's services and transport role, then verify it against nearby contemporary towns of the same type.

Use the `Notes` column in the amenity history table only for the corebook rule text that grants `+1 SP per Season`.

- `Church` should carry `+1 SP per Season`.
- `Newspaper` should carry `+1 SP per Season`.
- Leave `Notes` blank for every other amenity unless the corebook explicitly grants seasonal SP.

## Farm And Holding Statblock

Use the compact farm template for any site that is not really a village, town, or camp with civic life of its own.

- farms
- ranches
- homesteads
- line camps
- small holdings
- isolated supply places

The compact sheet should record:

- owner or operator
- working hands
- main resources
- market outlet
- amenity history

Treat amenities on a farm as practical site improvements, not town growth markers. Put the remaining detail in the description paragraphs, not in a separate holding sheet.

- `Barns`
- `Corrals`
- `Blacksmith`
- `Livery`
- `Wells`
- `Ditch Work`
- `Cemetery`
- `Schoolhouse`
- `Chapel`
- `Milkhouse`
- `Granary`

Only use `+1 SP per Season` in the notes field if the amenity itself grants seasonal SP in the corebook. Most farm amenities do not.

## A Practical Scoring Pattern

If you need a repeatable method, use this:

1. Start every aspect at rank 1.
2. Add 1 point for each major confirming fact.
3. Add 2 points for the settlement's defining economic engine.
4. Add 1 point for strong density or institutional concentration.
5. Subtract 1 point for each major pressure that makes the place worse.
6. Cap the result at 6 unless the place is extraordinary.

That gives you a settlement that feels grounded in real history but still plays cleanly at the table.

## What Not To Do

- Do not replace the six aspects with environmental tags.
- Do not collapse the aspect grid into a single narrative field.
- Do not use `Tier`, `Water Security`, `Freight Access`, `Army Reach`, or `Strategic Value` as the main statblock fields.
- Do not turn the helper into a census worksheet.
- Do not hide the place's weaknesses just because the population number is high.
- Do not ignore density, because dense settlements create different problems from loose ones.

## Montana Rule Of Thumb

For Montana settlements in `1873`, use two layers:

1. the corebook settlement statblock for rules-facing village format
2. Montana prose notes for terrain, winter, freight, Army presence, Native politics, and remoteness

That keeps the rules compatible with the main game while still making each place feel like a real territorial settlement.
