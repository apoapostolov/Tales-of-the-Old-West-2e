<!-- markdownlint-disable MD013 MD041 -->

# Part III — Crime and the Law (Procedural Proposals)

> Ch.11 Train Robbery · Ch.12 Justice · Ch.13 Atrocities
>
> The crime chapters are where the Operation frame is most defensible —
> a robbery *is* a linked sequence of situations, and the outlaw chapter's
> Progress-vs-Trouble engine is a proven fit. So the proposals here do
> not replace the Operation; they add a **distinct pre-Operation planning
> layer** and a **distinct post-Operation consequence layer** to each,
> so the three crimes feel different in their *shape*, not just their
> nouns. Justice gets the heaviest redesign: the trial becomes a full
> Social Combat, not an Operation.

---

## Ch.11 — Train Robbery and the Iron Horse

### Current weakness

The robbery is a clean Operation (stop, take, run) with good anatomy and a derailment table. Its weakness is that the **planning/casing phase** — the gang's intelligence-gathering, the inside man, the wire cut, the schedule read — is folded into the Operation's first stage rather than being its own distinct layer. A heist's pleasure is half in the plan; the engine should reward the plan mechanically, not just narratively.

### Proposed system — the Casing Layer + the Heat Track (medium)

- **The Casing Layer** (pre-Operation, distinct from the Operation itself): a short **intelligence-gathering phase** where each gang member takes one **casing action** per Shift of preparation — `HAWKEYE` the run (learn the schedule, the crew, the habitual stops), `INSIGHT` the railroad (read the wire traffic, the detective's pattern, the mail car's contents), `LIGHT-FINGERED` the inside man (turn the clerk, seduce the fireman, buy the agent), `OPERATE` the wire (the wire chapter's cut/dummy, ahead of the job). Each successful casing action grants the gang a **casing die** — a bonus die banked for a specific stage of the Operation (the signal, the express car, the wire, the get clear). The gang enters the Operation with a pool of banked dice that reward the plan, and the Operation's Trouble is steeper for a gang that didn't case. This is the **investigation primitive** (`yze-design/workshop/05`) inverted — the gang is *gathering clues about the job*, and the clues become dice.

- **The Heat Track** (post-Operation consequence layer): the railroad's memory, tracked as a **Heat gauge** (0–5) that rises with each train job in the railroad's territory and decays slowly (one step per season the gang lies low in that territory). At 3+, the railroad assigns a dedicated detective (a recurring NPC with a name and a file); at 5, the railroad hires the Pinkertons or petitions for federal troops. The Heat track is the railroad-faction's distinct expression — it is the **faction-web primitive** scoped to one adversary, and it makes the railroad's pursuit escalate across jobs, not reset each score.

### Why it fits

The Casing Layer makes the plan mechanically rewarding — a gang that cases well enters the Operation with advantages a gang that improvises lacks, which is the heist genre's core pleasure. The Heat Track makes the railroad a *persistent adversary* whose response escalates, which the flat `Wanted` tier never modeled (Wanted resets; Heat accumulates in a territory).

### Complexity: **medium.** The Casing Layer is a pre-Operation activity menu (one action per Shift); the Heat Track is one gauge per railroad territory. The Operation itself is unchanged.

---

## Ch.12 — Justice, Trial, and Incarceration

### Current weakness

The trial is a social-conflict Operation — Progress toward acquittal, Trouble as the stain. This is the flattest of the three: a trial is *not* a heist, and resolving it as Progress-vs-Trouble loses the courtroom's tactical shape. A trial has opening statements, witnesses, cross-examination, the jury's temper, the judge's lean, the closing — it is a structured contest with distinct phases, not a generic accumulation of successes.

### Proposed system — the Trial as Social Combat + the Docket (heavy)

- **The Trial as Social Combat** (full adoption of the `yze-design` workshop module): the courtroom is a Social Combat scene with the action economy, Composure pools (the defendant's, the key witness's, the prosecutor's), leverage as consumable weapon-dice (the evidence, the deposition, the surprise witness, the damning letter), social-distance bands (the sidebar at the bench = Intimate; the cross-examination = Personal; the closing argument = Public), and the **jury as the audience track** — the prize both sides compete to shift. The trial's phases map to Social Combat's structure:
  - **The opening** — each side's thesis (a `PERFORMIN'` or `PRESENCE` attack, read against the jury's starting temper).
  - **The prosecution's case** — each witness is a Social Combat exchange; the defense may cross-examine (deflect), object (a `BOOKLEARNIN'` reaction), or let the witness's testimony land (absorb).
  - **The defense's case** — the same, inverted; the defense calls its witnesses and the prosecutor cross-examines.
  - **The summation** — each side's closing is a Public-band attack, the most damaging move in the scene, with all accumulated leverage spent.
  - **The verdict** — the jury's final opinion (the audience track's endpoint) reads as acquittal, conviction on a lesser charge, or conviction as charged, with the Trouble-as-stain folded into the leverage the prosecution spent (the testimony that sticks even if the defendant walks).

- **The Docket** — the court's schedule, distinct from any one trial. A circuit judge arrives on a schedule (the docket), and the docket is the court's **activity menu**: the judge hears the criminal cases, the civil suits (the inheritance chapter's paper wars), the probates, and the bench's administrative business in a known order, and the party that wants its case heard (or wants to delay a rival's) must work the docket. The docket is the trial chapter's *strategic* layer — the timing of the trial is a lever, and a faction that can move a case up or down the docket has an advantage no amount of courtroom skill can overcome. This is the **schedule-as-metronome** primitive (the trade chapter's rhythm), applied to the law.

- **The Jail as a Pressure Loop** (incarceration as a distinct subsystem): the held character's time in jail is not a single downtime entry — it is a **pressure loop** with a daily/seasonal cycle: test `RESILIENCE` or `DOCITY` (the cell), the disease risk (the sickness chapter, applied to the county jail's bad air), the gang's `Cohesion` test (the member left behind), and the **jailbreak planning track** — a slow, multi-stage Operation run from the inside (casing the lock, the schedule, the walls, the bribable guard) that rewards patience the way the train robbery's Casing Layer rewards planning. The jailbreak is the incarceration chapter's heist, and it should be cased as carefully.

### Why it fits

The trial is the book's most structured social scene, and Social Combat gives it tactical depth the Operation never could — the phases, the leverage, the jury-as-audience, the judge's lean as a modifier. The Docket gives the court a strategic layer (timing) that no amount of courtroom skill provides. The Jail loop gives the incarceration a distinct shape (a pressure cycle) that the trial and the jailbreak bookend.

### Complexity: **heavy.** This is the right weight for the justice chapter — it is the book's civil spine, and a trial-PC or a lawyer-PC should feel that the courtroom is as tactically rich as the gunfight. The Docket and the Jail loop are medium-weight add-ons that give the chapter strategic and attritional depth.

---

## Ch.13 — Atrocities and Human Trade

### Current weakness

The atrocity is an Operation with moral weight (the `Doubts`/`Vexes` by Trouble step). The moral-weight mechanic is good — it is the chapter's reason for being. Its weakness is that the **trade in people** is modeled as "an economy with a buyer, a seller, a price, and a faction," which is accurate but abstract. The trade should feel *physically* different from a cattle drive or a bank robbery, because the cargo is people, and the engine's harm and condition rules should make that weight land.

### Proposed system — the Captive as a Tracked Person + the Moral Corrosion Track (medium–heavy)

- **The Captive as a Tracked Person** — a captive is not cargo. The engine tracks the captive as a **named NPC** with attributes, conditions, and a `Standing` with the captor (a small gauge, −3 to +3, that shifts with treatment). The captive's condition ladders (Starving, Dehydrated, the harm tracks) are live — a captive mistreated takes real condition damage the engine does not abstract away. A captive who is `Broken` on an attribute is a captive the captor has harmed in a way the engine makes the player *see*, not a Trouble step. This is the most important differentiation: the trade's cargo is a person, and the engine treats the person as a person.

- **The Moral Corrosion Track** — the `Doubts`/`Vexes` the current chapter assigns by Trouble step are good, but they should be a **tracked gauge** (0–5, the corruption/taint primitive from `yze-design/workshop/07`) that *accumulates across atrocities*, not resets per Operation. At 3+, the character takes a permanent `Reputation` shift toward the violent and the feared, and the county's decent factions' `Standing` drops. At 5, the character is corroded — the engine should let that be a slow moral death the campaign tracks, with the atonement dial (step the track down through costly, risky acts of repair or refusal) as the only way back. This is the **corruption spiral** primitive, calibrated to the moral weight of the atrocity rather than the supernatural.

- **The Refusal as a Protected Dial** — the character who refuses the order (the chapter's current "refusal" entry) should be mechanically rewarded *and* punished, the way a protected dial works: the refusal steps the Corrosion track *down*, but it shifts the `Standing` with the ordering faction to hunted and risks the court-martial or the rope. The refusal is the chapter's central moral choice, and the engine should make it a real one — costly on both sides, which is what makes it a choice.

### Why it fits

The atrocity chapter's subject demands that the cargo be a person, not a commodity, and that the moral cost accumulate rather than reset. The Captive-as-person and the Corrosion track give the chapter the weight the subject requires, mechanically — not as flavor, but as tracked state the player cannot look away from. The refusal-as-protected-dial makes the moral choice a real choice, which is the chapter's whole purpose.

### Complexity: **medium–heavy.** The Captive-as-person is a named NPC (the engine already supports this); the Corrosion track is one gauge per character; the refusal is a `Standing` shift plus a track step. The heaviest part is the moral weight, which is the point — the chapter's complexity should be the weight, not the bookkeeping.
