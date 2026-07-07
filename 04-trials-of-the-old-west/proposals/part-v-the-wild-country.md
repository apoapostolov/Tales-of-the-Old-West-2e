<!-- markdownlint-disable MD013 MD041 -->

# Part V — The Wild Country (Procedural Proposals)

> Ch.20 Weather · Ch.21 Deep Wild Land · Ch.22 Regional Encounters ·
> Ch.23 Winter
>
> The wild-country chapters are the ones where the Operation frame is
> most *defensible* (a disaster and an expedition are genuinely linked
> sequences) and where the critique is mildest. The proposals here add
> **environmental texture** — resource dice for the supplies the wild
> land consumes, a travel-activity menu, and a cumulative depletion
> model for winter — rather than replacing the Operation wholesale.

---

## Ch.20 — Weather and the Trail's Teeth

### Current weakness

The regional weather table and the three disaster Operations (blizzard, fire, flood) are good and distinctive. The weakness is that weather is **episodic** — each day rolls independently on the table, and a season of travel is a series of disconnected rolls rather than a *pattern* the party can read. A real frontier traveler watched the sky for *trends* (a dry stretch building to fire risk; a cold front dropping over days toward a blizzard), and the engine should model the trend, not just the day.

### Proposed system — the Weather Pattern + the Exposure Gauge (light–medium)

- **The Weather Pattern** — replace the independent daily roll with a **pattern die**: a D6 that represents the current weather *trend*, stepped up or down by the day's roll. A pattern of "clear and warm" (die at 1–2) is stable; a pattern of "building heat" (die climbing toward 6) raises the fire risk each day it holds; a pattern of "front dropping" (die falling toward 1) raises the blizzard risk. The GM rolls the day's weather *onto* the pattern die, not instead of it — the table still produces the day's weather, but the pattern die tracks whether the weather is *building toward* something. This is the **encounter-with-memory primitive** applied to weather: the country remembers what it has been doing, and the trend is the early warning the watchful traveler reads.

- **The Exposure Gauge** — track the party's cumulative **Exposure** (0–5) during sustained bad weather. Each Shift in a storm or extreme conditions steps Exposure up by 1; each Shift in shelter or good weather steps it down. At 3+, the party rolls the conditions (Freezing, Heatstroke, Exhausted) at `-1 die`; at 5, at `-2 dice`, and a `RESILIENCE` test is forced regardless of shelter. The Exposure gauge is the weather's *attritional* dimension — a single blizzard is a disaster Operation, but a week of cold rain is a slow erosion the gauge models, and the flat daily condition rolls did not.

### Why it fits

Weather is a trend, not a series of independent days, and the pattern die models the trend. Exposure is the weather's cumulative cost, and the gauge models the slow erosion a single disaster roll couldn't. Both are light additions that give the weather chapter a texture the daily-roll lacked.

### Complexity: **light–medium.** One pattern die (rolled onto, not instead of, the daily table); one Exposure gauge (0–5, stepped by Shift). The disaster Operations remain the frame for the acute events.

---

## Ch.21 — Deep Wild Land Exploration

### Current weakness

The three modes (river, forest, mountain) with their travel rows and expedition Operations are good and distinctive. The weakness is that the **expedition as Operation** treats the journey as a sequence of obstacles, when a real expedition is also a **resource-management problem** — the party is carrying finite supplies (food, feed, gear) into a country that does not resupply them, and the engine should model the depletion, not just the obstacles.

### Proposed system — the Expedition Supplies as Resource Dice + the Travel-Activity Menu (medium)

- **The Expedition Supplies as Resource Dice** — the party tracks its wilderness supplies as **resource dice** (the corebook's consumables rule, extended): a **Provisions die** (food), a **Feed die** (for the pack animals), and a **Gear die** (ammunition, tack, tools — the stuff that breaks and is consumed). Each die steps down on a 1–2 rolled at intervals set by the expedition's strain (daily in hard country, every few days in easy). At D4 exhausted, the party is in trouble — Starving (the sickness chapter), afoot (the animals unfed), or improvising (the gear broken). This is the **resource-die primitive** (`yze-design/references/16` P5), already in the corebook for consumables, extended to the expedition's full supply load. The expedition Operation's Trouble now has a *source* — the supplies are depleting — and the party's decisions (push on or turn back; ration or feast; repair or abandon) have mechanical weight.

- **The Travel-Activity Menu** — each Shift of overland travel, the party chooses its **travel activity** (an activity menu, the travel-and-downtime primitive from `yze-design/references/06`):
  - **Push** (cover the miles; full distance; no forage; supplies step down)
  - **Careful** (reduced distance; forage/hunt roll to offset Provisions; `HAWKEYE`/`NATURE` to read the country)
  - **Rest and repair** (no distance; recover conditions; repair gear; the `MAKIN'`/`DOCTORIN'` work)
  - **Scout** (reduced distance for the party; the scout pushes ahead; `HAWKEYE` to find the route, the water, the sign — the encounter chapter's hook)

  The menu gives the party a *choice* each Shift that the flat Operation Progress did not — the trade-off between speed, supply-conservation, recovery, and information, which is the wilderness-travel loop's core decision.

### Why it fits

An expedition is a resource-management problem as much as an obstacle-course, and the resource dice model the supplies' depletion. The travel-activity menu gives the party the daily decision the flat Progress track abstracted away — push or conserve, rest or scout — which is the wilderness loop's texture.

### Complexity: **medium.** Three resource dice (Provisions, Feed, Gear); a four-option activity menu per Shift. The expedition Operation remains the frame for the journey's arc; the resource dice and the menu are its *contents*.

---

## Ch.22 — Regional Encounter Tables

### Current weakness

The regional tables are good and the right weight. The only weakness is that the encounters are **stateless** — the table does not remember what the party has met, so a region never *changes* in response to the party's actions (clearing the bandits, hunting out the game, befriending the nation).

### Proposed system — the Region as a Stateful Layer (light)

- Adopt the **encounter-with-memory primitive** (`yze-design/references/16` P14): each region the party travels in has a small **state** — a **Tension rating** (how hostile the region is to the party, raised by clashes, lowered by good deeds), a **Game rating** (how much wildlife is left, lowered by market hunting — the logging/fur/hunt chapter's Decline track), and a **Sign rating** (how much traffic is in the country, raised by a boom, lowered by a bust). These shift the encounter table's rolls: a high-Tension region pushes the table toward the war party and the ambush; a low-Game region pushes it away from the grazing herd; a high-Sign region pushes it toward the freight outfit and the patrol. This is a light layer — three ratings per region, shifted by the party's actions and the season — that makes the country *respond* to the party's presence, which the flat table did not.

### Why it fits

The country is not a static encounter deck; it is a place the party changes by being in. The three ratings make the change mechanical, and they tie the encounter chapter to the trade, the hunt, and the factions chapters (whose actions shift the ratings).

### Complexity: **light.** Three ratings per region; the table's modifiers shift by them. No new subsystem, just a stateful layer on the existing tables.

---

## Ch.23 — Winter and Wintering

### Current weakness

The Winter Quarter (the Count, the "What Winter Brought" table, the monthly attrition, the spring thaw) is good and distinctive — it is already a procedural subsystem, not an Operation. Its weakness is that the **monthly attrition** is a flat application of the gauges (Provisions, Horsestock, Cohesion all step down), which makes the winter a *grind* rather than a *decision*. A real wintering is a series of choices — ration or feast, cut wood or freeze, hold the cabin or risk the ride — and the engine should model the choices, not just the attrition.

### Proposed system — the Wintering Activity Menu + the Cabin Fever Track (medium)

- **The Wintering Activity Menu** — each month of the winter, the household (the party, the ranch, the gang) chooses one **wintering activity** per able body:
  - **Ration and conserve** (step the Provisions die down slowly; everyone tests `RESILIENCE` at `-1` for the hunger)
  - **Cut wood and fuel** (a `LABOR` operation in the cold; steps the Fuel die up; risk of Freezing exposure)
  - **Tend the stock** (the `ANIMAL HANDLIN'` work; hold the Horsestock gauge; risk of the weather chapter's conditions)
  - **Hold the cabin** (the `Cohesion` test; the cabin-fever track, below)
  - **Risk the ride** (the hard ride in the snow — the doctor, the law, the errand; a `Hard Ride and Flight` roll in the weather chapter's blizzard; risk of horse and rider)

  The menu replaces the flat monthly attrition with *choices* — the household decides where to spend its labor, and each choice trades one risk for another. This is the **activity-menu primitive**, applied to the winter's monthly cycle.

- **The Cabin Fever Track** (the winter's distinct social cost) — a gauge (0–5, the inverse of Cohesion, specific to the wintering) that steps up each month the household is confined. At 3+, the household tests `Cohesion` at `-1` (the quarrel, the feud, the split); at 5, a named member leaves or a violence occurs (the GM's call, or a roll on a small "cabin fever" table). The track is the winter's *social* dimension — the cold and the close air break people, not just supplies — and it gives the winter a human cost the attrition-of-gauges did not model.

### Why it fits

Winter is a decision-making season, not just an attrition season, and the activity menu models the decisions. The cabin-fever track gives the winter its distinct human cost — the close air's erosion of the household's peace — which no other chapter's gauge models. Together they make the winter a *strategic and social* subsystem, not a grind.

### Complexity: **medium.** A five-option activity menu per month; a cabin-fever gauge (0–5). The Count and the spring thaw remain the frame; the menu and the track are the winter's monthly contents.
