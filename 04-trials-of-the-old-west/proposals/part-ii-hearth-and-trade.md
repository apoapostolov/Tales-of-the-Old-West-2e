<!-- markdownlint-disable MD013 MD041 -->

# Part II — Hearth and Trade (Procedural Proposals)

> Ch.3 Sickness · Ch.4 Weddings/Funerals/Church · Ch.5 Saloons ·
> Ch.6 Trade · Ch.7 Cattle · Ch.8 Mining · Ch.9 Logging/Fur/Hunting ·
> Ch.10 Banking
>
> This is the heaviest redesign. The core critique lands here: every
> business is currently a "season roll + Bonus/Penalty D66," which means
> running a saloon, a mine, and a cattle outfit feel mechanically
> identical. The proposals give each enterprise a **distinct procedural
> flow** built on the org-lifecycle pattern, with a **trade-specific
> resource** and an **investment-cycle** that replaces the flat roll.

## The shared frame — the Investment Cycle (applies to Ch.5–10)

Every business in the book should run on the same five-beat seasonal cycle, which is the org lifecycle (`yze-design/references/07`) calibrated to the season. This replaces "roll the key ability, read 0/1/2+ on the ladder, roll the Bonus/Penalty table."

```
1. ASSESS  — read the market, the season, the gauges; decide the season's strategy
2. INVEST  — spend Capital/cash/resources to set the season's dials
3. OPERATE — the working phase (events, trouble, the season's play)
4. RECKON  — the season roll, read against the dials you set in step 2
5. REINVEST— pay out, recover, or reinvest into functions/growth
```

The beats are shared; the **dials** and the **currency** differ by trade. A ranch invests in stock and grass; a mine invests in timber and powder; a saloon invests in stock and reputation. The Reckon step is where the die rolls, but the die rolls *against the dials the player set* — not a flat ability check. This gives the player agency over the season's outcome that the flat roll never did.

> **NOTE (implementation reference).** This Investment Cycle is the
> shared frame the business chapters (Ch.5–10) adopt. Each business
> chapter that is implemented against this proposal should include a
> one-line pointer to this frame (e.g. "the saloon runs on the
> Investment Cycle — see the proposal's shared frame") rather than
> restating the five beats, and then define its **distinct dials and
> currency** in its own section. The chapters that are *not* businesses
> (Ch.3 Sickness, Ch.4 Rites) do not use this cycle — they have their
> own procedural flows (the Contagion Loop, the Social Combat
> scene-types) defined in their own proposals below.

---

## Ch.3 — Sickness and the Fever

### Current weakness

The Spread/Severity gauges are good, but the **outbreak as Operation** flattens the disease into another Progress/Trouble track. A cholera outbreak in a wagon train should feel different from a mine cave-in, and the medical response should be a *system* (triage, quarantine, treatment, the limits of period medicine), not a single Operation stage.

### Proposed system — the Contagion Loop + the Triage Menu (medium)

- **The Contagion Loop** replaces the outbreak Operation with a per-Shift cycle during an active outbreak:
  1. **Spread check** — roll the disease's Spread die (set by vector and crowding). On a 4+, the Spread gauge climbs. Quarantine, clean water, and the doctor's work subtract dice from this roll.
  2. **Triage** — each stricken person tests Severity. This is where the doctor's player makes **triage choices**: who gets the limited medicine, the doctor's attention, the clean bed. The triage is an **activity menu** (the doctor picks N patients to treat per Shift; the rest test Severity unaided).
  3. **The Mortality** — those who fail the Severity test by margin die, recover, or take the permanent condition. The doctor's `DOCTORIN'` roll is the modifier, and the period's limits (calomel, miasma, the odds) set the floor.
  4. **The Burn-out** — the outbreak ends when the Spread stops climbing for `1D6` Shifts (the disease runs out of susceptibles, the quarantine holds, or the season turns). This is the disease's clock, not the Operation's Progress track.

- **The Triage Menu** (the doctor's subsystem): each Shift, a doctor with `DOCTORIN'` ≥ 2 may treat a number of patients equal to their rank. Each treatment is a roll modified by supplies (medicine as a resource die — the same primitive), conditions (clean water, rest), and the disease's Severity. A doctor who treats fewer patients than are sick must **choose who goes untreated**, which is the subsystem's moral weight — the engine should let that choice sit on the player, the way the vignette's Sandoval sat with the boy on the porch.

### Why it fits

The Contagion Loop makes the outbreak a *medical* scene, not a generic Operation. The Spread die is a mechanic only disease has (a self-reproducing threat). The triage menu gives the doctor a unique role no other subsystem offers. The period's medical limits are in the floor of the Severity test, not a flavor note.

### Complexity: **medium.** A per-Shift cycle during outbreaks (4 steps), a triage menu, and a medicine resource die. Outside an outbreak, none of this is tracked.

---

## Ch.4 — Weddings, Funerals, and the Church Service

### Current weakness

These are framed as social-conflict scenes (match/objection/merger), which is fine but thin — a wedding and a trial resolve on the same opposed `PRESENCE` roll, which makes them feel the same.

### Proposed system — Social Combat calibration + the Rite as Scene-Type (medium)

- **Adopt Social Combat** (the `yze-design` workshop module) for the high-stakes rite: the wedding's objection, the funeral's will-contest, the revival's conversion attempt. This gives each a **Composure pool**, **leverage as consumable dice** (the dowry deed, the codicil, the family secret), **social-distance bands** (the whisper at the altar vs the public objection from the back pew), and an **audience track** (the congregation's opinion, which is the rite's real prize).
- **The Rite as Scene-Type** — distinguish the three rites by their *shape*, not just their content:
  - **The Wedding** is a **fusion scene** — the merger is the goal, the objection is the opposition, and the audience (the gathered families) is whose opinion shifts the `Standing`. The social-distance band that matters is **Public** (the objection must be public to count).
  - **The Funeral** is a **revelation scene** — the will, the secret, the grudge surface; it uses the **Investigation** primitive (clues as currency, per `yze-design/workshop/05`) more than combat. The funeral's tension is *what comes out*, not who wins an exchange.
  - **The Revival** is an **audience-as-combatant scene** — the preacher works the crowd; the crowd's opinion is a track both the preacher and the opposition compete to shift. This is the Social Combat "audience dial" turned up to its fullest.

### Why it fits

Social Combat gives the rites tactical depth the single roll lacked, and the three scene-types give each rite a distinct *shape* so they don't collapse into "social conflict with different nouns." The funeral-as-investigation is the key differentiation — it makes the funeral about *information*, not persuasion.

### Complexity: **medium.** Social Combat is a full subsystem but only deployed for high-stakes rites; incidental persuasion stays a single roll. The scene-type distinctions are framing, not extra mechanics.

---

## Ch.5 — Saloons and the Trade

### Current weakness

The saloon is a business (season roll + Bonus/Penalty) plus a `Refuge`-style house gauge. But the saloon's distinct character — the **crossroads** where every faction drinks and every drink is a `Standing` move — is not mechanically modeled. The keeper is running a business *and* an intelligence operation simultaneously, and the engine should let both run.

### Proposed system — the House as Crossroads Org + the Trade-Night Procedure (medium–heavy)

- **The House as Org** (full lifecycle): founding (the deed, the license, the stock), functions (the bar, the faro layout, the rooms, the back room — each a discrete improvement with a mechanical effect), upkeep (the wages, the restocking, the bribes), events (the fight, the raid, the girl in trouble), scale (the way-station → the saloon → the saloon-and-hotel). This replaces the flat season roll with the Investment Cycle.
- **The Trade-Night Procedure** — a light scene-level frame for a night behind the bar, distinct from both combat and social conflict. Each Shift of a trade night, the keeper makes **one read** (`INSIGHT`) of the room — who's drinking, who's talking to whom, who's holding a grudge — and **one move** (serve, warn, refuse, listen, rent the back room). Each move is a `Standing` shift with the faction whose man is in the room. This is the saloon's unique gameplay loop: the keeper is a faction-manager by the drink, not by the season.
- **The House Gauge as the Crossroads dial** — the existing `Refuge`-style gauge becomes the **Crossroads rating**: how much the county's traffic comes through. A high Crossroads rating means more custom, more information, more trouble. The keeper manages it the way a rancher manages grass — invest (the good whiskey, the faro bank, the reputation), upkeep (the mirror, the bouncer, the bribe), events (the boom, the bust, the fire).

### Why it fits

The saloon is the book's most social business, and the Trade-Night Procedure gives it a loop no other business has — the keeper is playing the faction game *while* running the business, every night. The org lifecycle gives the business depth; the Trade-Night gives the crossroads depth; the two interlock at the Crossroads rating.

### Complexity: **medium–heavy.** The org lifecycle is shared with the other businesses; the Trade-Night Procedure is saloon-specific. A keeper-PC gets the richest subsystem in the book, which fits the saloon's role as the engine's densest crossroads.

---

## Ch.6 — Running Trade and Resources

### Current weakness

The spatial economy table is good, but the **freighting outfit** is just another business (season roll + Bonus/Penalty) and the **supply run** is just another Operation. The distinct character of trade — the **route as a managed asset**, the **cargo as a risk-weighted bet**, the **schedule as the rhythm everything sets its clock by** — is not mechanically modeled.

### Proposed system — the Route Ledger + the Cargo Bet (medium)

- **The Route Ledger** — the freighter's distinct "functions" are their **routes**: tracked lines between markets, each with a distance, a terrain, a demand, and a **competition** rating. The freighter invests in routes (the way a rancher invests in stock): scouting a new route, building a way-station relationship, buying out a rival's contract. Routes are the org's "functions" list, acquired and improved over time. This is the **encounter-with-memory primitive** (`yze-design/references/16` P14) — a route the freighter has run before is safer and better-read than one they haven't.
- **The Cargo Bet** — each run, the freighter chooses a cargo (the trade chapter's spatial economy sets the buy and the sell), and the cargo is a **risk-weighted bet**: the higher the margin (the dearer the destination), the higher the Trouble. The run's Operation is the execution, but the *bet* is the strategic decision the freighter makes at the Investment step — "do I run the safe flour to the county seat at 5%, or the powder to the snowbound mine at 200%?" The cargo choice sets the Operation's stakes before the dice roll.
- **The Schedule as a Metronome** — the rail and the stage run on schedules the county lives by. The freighter who knows the schedule knows when the railhead's prices drop (the day the train arrives) and when the mine's powder runs out (the day before the next scheduled run). This is **information as advantage** — the `INSIGHT`-based read of the market that the flat season roll never rewarded.

### Why it fits

The Route Ledger gives the freighter a *growing asset* (routes, like functions) that a generic business doesn't have. The Cargo Bet makes each run a strategic decision, not just a die roll. The Schedule metronome ties the trade chapter to the wire and rail chapters in a way the flat roll didn't.

### Complexity: **medium.** The Route Ledger is light bookkeeping (3–5 routes); the Cargo Bet is a decision at the Investment step; the Schedule is an `INSIGHT` read. The Operation engine still handles the run itself.

---

## Ch.7 — Cattle Drives and the Open Range

### Current weakness

The drive is an Operation (Progress = miles, Trouble = trail's teeth) and the ranch is a business (season roll + Bonus/Penalty). Both are fine, but the **herd as a living asset** — nervous, valuable, capable of gaining or losing weight, of stampeding, of being improved by breeding — is not mechanically modeled. The herd is just "the Progress track's stake."

### Proposed system — the Herd Ledger + the Breeding Dial (medium–heavy)

- **The Herd Ledger** — the ranch's distinct "resource" is its **herd**, tracked not as a cash value but as a **herd die** (the stepped die, D6→D12, representing headcount and condition) plus a **Quality rating** (1–3, representing breeding). The herd die is the ranch's main asset and its main risk: it steps *down* on a bad season (drought, stampede, winter kill, rustling) and steps *up* on a good one (calf crop, good grass, a clean drive). The herd die is the rancher's version of the outlaw's `Horsestock` — a managed, depletable, growable resource.
- **The Drive as the Herd's Test** — the drive is the Operation, but its *stakes* are the herd die: a drive that arrives light steps the herd die down; a drive that arrives heavy (good grass, no losses, a premium market) steps it up or pays out in cash. The drive is the season's climax because it is where the herd die is cashed in or eroded.
- **The Breeding Dial** — the rancher's long-term investment is **breeding**: spending Capital to raise the herd's Quality rating, which improves the calf crop (the chance the herd die steps up in a good season) and the sale price (the per-head multiplier at the railhead). Breeding is the rancher's "functions" track — slow, expensive, and the difference between a range operation and a ranch that lasts.
- **The Open Range as a Common-Pool Resource** — model the open range's grass as a **shared resource die** (the way the outlaw band shares a Provisions die): all the ranchers drawing on the same range draw down the same grass die. Overstock and the grass die steps down for everyone; a drought (the weather chapter) drops it sharply; a faction's range war is a fight over who gets to draw on it. This is the **common-pool-resource primitive**, and it makes the open range's tragedy mechanical, not just narrative.

### Why it fits

The herd-as-asset gives the rancher a managed resource no other business has — a living thing that grows, shrinks, panics, and can be improved. The breeding dial gives the ranch a multi-season strategic arc. The common-pool range makes the factional politics of the open range mechanical: the grass is finite, and the ranchers are drawing from the same well.

### Complexity: **medium–heavy.** The Herd Ledger is one die + one rating; the Breeding Dial is a Capital spend over seasons; the common-pool range is a shared die per region. The drive Operation remains the frame; the herd die is its stake.

---

## Ch.8 — Mining Claims and the Ground's Promise

### Current weakness

The mine is a business (season roll + Bonus/Penalty) and the prospecting is an Operation. But the mine's distinct character — the **vein as a depletable mystery**, the **shaft as a dungeon**, the **dust as an accumulating doom**, the **company-vs-union politics** — is not mechanically modeled beyond flavor.

### Proposed system — the Vein Ledger + the Dust Track + the Shift Menu (heavy)

- **The Vein Ledger** — the mine's distinct "resource" is its **vein**: tracked as a **vein die** (the stepped die, representing the ore's richness) and a **Depth rating** (how deep the shaft goes). The vein die is mined down each season (the ore is taken out); when it steps to exhausted, the miner must **sink the shaft deeper** (a `LABOR`/`MAKIN'` operation that risks the cave-in and the water) to find the vein's continuation, or the mine plays out. This is the **depletable-resource primitive** with a *discovery* twist — you don't know if the vein continues until you sink the shaft.
- **The Dust Track** (silicosis as an accumulating doom) — a miner who works the drift tracks a **Dust gauge** (0–5, the inverse of Cohesion). Each season underground steps it up by 1 (more with dry drilling, less with wet). At 3+, the miner takes the chronic cough (a permanent `-1` to `RESILIENCE` and `LABOR`); at 5, the miner is dying of the dust, and the engine should let that be a slow death the mine's seasons track. This is the **corruption/taint primitive** (`yze-design/workshop/07`) calibrated to industrial disease, and it gives the mine a personal cost no other trade has.
- **The Shift Menu** — the mine's "working phase" is the **shift**: a choice menu (each miner picks one action per Shift underground) — drill-and-blast (the vein die, fast and dusty), muck-and-timber (the shaft's safety, slow and clean), prospect-the-drift (the `HAWKEYE` read for the vein's continuation), or shore-up (the `MAKIN'` that prevents the cave-in). The shift menu is the mine's distinct loop — it is the only business where the "operate" phase is a series of *underground tactical choices* about speed vs. safety vs. discovery.
- **The Company-vs-Union as a Faction Web** — the mine's politics are a two-faction relationship web (the company and the union), with the party's `Standing` with each propagating between them (helping the union chills the company; helping the company chills the union). This is the **faction web primitive**, scoped to one mine, and it gives the mine's labor politics the relational depth the flat season roll lacked.

### Why it fits

The mine is the book's most spatially and physically intense business, and the Vein Ledger + Dust Track + Shift Menu give it three subsystems no other trade has: a depletable mystery (the vein), an accumulating personal doom (the dust), and a tactical work loop (the shift). The company-vs-union web gives the politics mechanical weight.

### Complexity: **heavy.** Three subsystems (vein, dust, shift menu) plus the faction web. This is the right weight for the mine — it is the book's deepest trade, and a miner-PC should feel that depth.

---

## Ch.9 — Logging, Fur Trade, and Hunting

### Current weakness

Three trades in one chapter, each a take-based operation with no distinct resource. The river drive, the trapline, and the market hunt all resolve the same way.

### Proposed system — three distinct take-economies (medium)

Give each trade a **distinct resource and a distinct clock**, so the three feel different:

- **Logging — the Stand Ledger + the River Drive as a timed Operation.** The logger's "resource" is the **stand** (a tract of timber, tracked as a stand die that depletes as it's cut). The river drive is the Operation, but it is **timed by the spring thaw** — a clock that runs regardless of the drive's Progress, and when the water drops, the drive is over whether the logs made the boom or not. This is the **protected-dial primitive** (`yze-design/references/16` P10) — the season's window is the dial the logger cannot extend.
- **Fur Trade — the Trapline as an Activity Menu + the Rendezvous as a Market Scene.** The trapper's "working phase" is the **trapline menu**: each Shift on the line, choose — run the line (collect the catch, risk the spoilage), move camp (find new ground, risk the nation's territory), or rest and repair (maintain the gear, lose the day's catch). The **rendezvous** is the trade's distinct scene: a market where the winter's take is sold, the next season's supplies bought, and the faction's `Standing` shifted — a crossroads scene like the saloon's trade-night, but annual and in the wild land.
- **Market Hunting — the Take as a Resource Die + the Decline Track.** The market hunter's "resource" is the **take die** (the stepped die, representing the season's kill). But the market hunt's distinct mechanic is the **Decline track**: each season of heavy market hunting in a region steps the region's game entries on the encounter table (Ch.22) down a die, and steps the plains nations' `Standing` toward hostility. This is the **encounter-with-memory primitive** — the hunter's success is the country's loss, mechanically tracked across seasons.

### Why it fits

The three trades share a shape (take-based) but differ in their resource and clock: logging is a timed drive, trapping is an activity menu with an annual market, market hunting is a take die with a cumulative cost to the country. The Decline track especially is the book's strongest mechanic for the buffalo's end — it makes the hunter's prosperity the country's impoverishment, mechanically, over seasons.

### Complexity: **medium.** Each trade gets one distinct subsystem; they share the take-based frame. The Decline track is the most ambitious (it crosses into the encounter chapter), and it is the one that makes the chapter more than three copies of the same Operation.

---

## Ch.10 — Banking and the Vault

### Current weakness

The bank robbery is an Operation (parallel to train robbery) and the deposit/bank-run is a rule. But the **bank as an institution** — a fractional-reserve lender whose solvency is a bet on the county's future — is not mechanically modeled. The bank is either a target or a safe, not a living financial organism.

### Proposed system — the Reserve Track + the Banker's Dial (medium)

- **The Reserve Track** — the bank's distinct "resource" is its **reserve**: the ratio of its deposits to its loans, tracked as a gauge (1–5, where 3 is sound, 1 is overextended, 5 is hoarding). The reserve is the bank's solvency, and it is the dial the banker (or the faction that owns the bank) sets: a low reserve means more loans, more profit, more risk; a high reserve means safety, lower profit, and the county's grumbling about tight money. A bank run (the event) tests the reserve directly — if the reserve is below 3, the run can break the bank; if it is at 5, the run is weathered. This is the **protected-dial primitive** applied to fractional-reserve banking, and it makes the bank's solvency a *managed* thing, not a GM-fiat event.
- **The Banker's Dial** — for a PC banker, the Investment step of the season cycle is the **reserve decision**: how much to lend (profit, risk) vs how much to hold (safety, opportunity cost). This is the bank's distinct strategic loop — no other business runs on a reserve ratio — and it gives the banker-PC a financial lever the other businesses don't have.
- **The Robbery as a Reserve Shock** — the bank robbery Operation's consequence is not just "the take is gone" but "the reserve is hit." A robbery that takes the vault's cash drops the reserve gauge, which can trigger a run, which can break the bank, which can take the county's deposits with it. The robbery's weight is the *institutional* weight, not just the cash.

### Why it fits

The bank is the book's only financial institution, and the Reserve Track gives it a distinct management loop (the reserve ratio) that no other business has. The robbery-as-reserve-shock ties the crime chapter to the institution chapter, so a gang that robs a bank is not just taking cash — they are (possibly) breaking the county's credit, which is the kind of consequence the engine should make stick.

### Complexity: **medium.** One gauge (the reserve) and one decision (the reserve ratio at the Investment step). The robbery Operation remains the frame for the crime side; the reserve is the institution's frame.

---

## Summary — what makes each business feel different

| Chapter | Distinct resource/currency | Distinct loop |
| --- | --- | --- |
| Ch.5 Saloons | the Crossroads rating (traffic + information) | the Trade-Night Procedure (read the room, make a move, shift Standing) |
| Ch.6 Trade | the Route Ledger (routes as acquired functions) | the Cargo Bet (risk-weighted margin) + the Schedule metronome |
| Ch.7 Cattle | the Herd die + Quality rating | the Breeding Dial + the common-pool Range grass die |
| Ch.8 Mining | the Vein die + Depth rating; the Dust gauge | the Shift Menu (drill/muck/prospect/shore) + the company-vs-union web |
| Ch.9 Logging/Fur/Hunt | the Stand die / the Take die / the Trapline menu | the timed River Drive / the annual Rendezvous / the Decline track |
| Ch.10 Banking | the Reserve gauge (solvency ratio) | the reserve decision (lend vs hold) + the robbery as reserve shock |

All share the **Investment Cycle** (assess, invest, operate, reckon, reinvest) as the seasonal frame; each has a **distinct resource and loop** that makes running it feel different from running the others. The GM and the player feel the trade in the mechanic, not just in the nouns.
