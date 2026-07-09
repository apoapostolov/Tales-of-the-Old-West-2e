<!-- markdownlint-disable MD013 MD041 -->

# Part VI — The Nation and the Decade (Procedural Proposals)

> Ch.24 Mass Combat · Ch.25 Robber Barons · Ch.26 Political Scene
>
> The nation-scale chapters are where the subsystems should be the
> *heaviest* — these are the largest scales the engine reaches, and the
> player should feel the weight. Mass Combat gets a refined unit model;
> the Robber Barons get the Influence/Faction-Web at territorial scale;
> the Political Scene gets a **party-layer strategic system** with the
> national metaplot as a live modifier engine, not just a timeline to
> read.

---

## Ch.24 — Mass Combat and the Skirmish Line

### Current weakness

The unit model (Quality 1–3, Strength die, Cohesion) and the opposed skirmish roll are clean and playable. The weakness is that the **battle as Operation** (Progress = break the enemy) flattens the battle's *phases* — a real battle has a recon, a deployment, an engagement, a crisis, and a pursuit, and resolving it as a single Progress track loses the shape. The attached-PC mechanic is also thin — a PC leading a unit gets help dice, but the PC's *decisions* (commit the reserve, hold the flank, order the retreat) are not mechanically modeled.

### Proposed system — the Battle as a Phased Operation + the Command Menu (medium–heavy)

- **The Battle as a Phased Operation** — replace the single Progress track with **three sequential mini-Operations**, each with its own Progress and Trouble, modeling the battle's phases:
  1. **The Recon and Deployment** (Progress 3, Trouble 2) — `HAWKEYE`/`INSIGHT` to read the ground and the enemy; deployment choices (where to put the units) set the modifiers for phase 2. A failed recon means the enemy has the ground; a successful recon means the party does.
  2. **The Engagement** (Progress 6, Trouble 4) — the main fight; the opposed unit rolls; the attached PCs lead; the Trouble is the casualties and the flank collapses. This is the existing skirmish-turn engine, run as the battle's center of gravity.
  3. **The Crisis and Pursuit** (Progress 4, Trouble 3) — the breaking point; one side breaks (the Morale test); the pursuit is the pursuit or the rout. The phase's Trouble is the cost of victory or the cost of defeat — the casualties taken in the rout, the prisoners, the captured guns.

  The phased structure makes the battle a *shape* — it has a beginning, a middle, and an end, and each phase's outcome sets the next's modifiers. This is the **scale-escalation ladder** (`yze-design/references/07` §9) applied to the battle's internal structure.

- **The Command Menu** (the attached PC's distinct loop): a PC commanding a unit or a force has a **command action** each battle Round (a slow action, distinct from the unit's exchange):
  - **Commit the reserve** (add a unit to the line; risk it)
  - **Rally** (a `PRESENCE` roll; step a breaking unit's Cohesion up; risk the commander's person)
  - **Lead from the front** (add the PC's combat ability to a unit's roll this Round; risk the PC taking attrition)
  - **Order the retreat** (preserve the force; concede the battle's Progress; the political cost of a retreat)
  - **Seize the ground** (a `MOVE`/`LABOR` operation; shift the terrain modifier; risk exposure)

  The command menu gives the PC commander *decisions* that the flat help-dice-add did not, and it makes the commander's choices the battle's strategic levers — the reserve, the rally, the retreat — which is what command actually is.

### Why it fits

A battle has phases, and the phased Operation models them. A commander makes decisions, and the command menu models them. Both give the mass-combat chapter a tactical and strategic depth the single Progress track lacked, and they make the attached PC a *commander* rather than a help-die bonus.

### Complexity: **medium–heavy.** Three sequential mini-Operations; a five-option command menu per Round. This is the right weight for the battle — it is the engine's largest scale, and it should feel commensurately heavy.

---

## Ch.25 — Robber Barons and Their Work

### Current weakness

The baron as a faction of one, with the work/opportunities table and the price of the regard, is good. The weakness is that the baron's **reach** is modeled as "Federal reach" (a tag), not as a *mechanical* network. A baron's power is his web — his hold on the legislature, the bench, the wire, the bank, the troop — and the flat `Standing` ladder cannot model the web's propagation. The party's relationship with a baron should feel like the relationship with a *system*, not a person.

### Proposed system — the Baron as a Faction Web at Territorial Scale + the Obligation Track (medium–heavy)

- **The Baron as a Faction Web** — model the baron as the **center of a faction web**: his holdings (the railroad, the bank, the land office, the bench, the troop he has influence over) are the *nodes*, and the bonds between them (the baron's control) are the *edges*. The party's `Standing` with the baron propagates through the web: helping the baron's railroad warms the baron's bank (the baron's allies); crossing the baron's land office chills the baron's bench (the baron's instruments). This is the **faction-web primitive** scaled to one baron's network, and it makes the baron's power *structural* — the party is not dealing with a man, but with the system the man commands.

- **The Obligation Track** (`yze-design/workshop/06` debt-and-obligation primitive): the party's relationship with a baron is not `Standing` alone — it is **Obligation**, a gauge (0–5) that rises every time the party takes the baron's work and decays slowly (the baron's favors are not free). At 3+, the baron may **call the obligation** (the debt-call procedure from the faction web) — demanding a service the party cannot refuse without making a Federal enemy. At 5, the party is the baron's instrument, and the engine should let that be a slow loss of agency the campaign tracks. The Obligation track is the baron chapter's distinct mechanic — no other faction has this cumulative hold — and it makes the baron's work *dangerous* in a way the flat `Standing` drop did not.

### Why it fits

A baron's power is his network, and the faction web models the network. The baron's work creates obligation, and the Obligation track models the accumulation. Together they make the party's relationship with a baron feel like the relationship with a *system* — structural, cumulative, and hard to escape — which is what the chapter says the baron is.

### Complexity: **medium–heavy.** The baron's web is 3–5 nodes (his holdings); the Obligation track is one gauge per baron. The work/opportunities table remains the frame for the baron's offers; the web and the track are the baron's *hold*.

---

## Ch.26 — The Political Scene of the 1870s

### Current weakness

The parties, the acts, and the year-by-year timeline are excellent *reference* material — the chapter is the book's best-researched. Its weakness is that the metaplot is a **timeline to read**, not a **system to run**. The GM applies the year's modifiers by hand, and the parties' rise and fall are static entries, not *live* engines. A campaign set in 1876 should *feel* the election in the mechanics, not just in the GM's narration.

### Proposed system — the Party Power Track + the National Modifier Engine (heavy)

This is the chapter's most ambitious proposal, and the one most worth doing.

- **The Party Power Track** — each national party (Republican, Democratic, plus the Liberal Republican and Greenback eruptions when active) has a **Power rating** (0–10) representing its current national strength. The Power rating is the party's *version* of the faction Standing, but at the national scale: it gates the party's access to federal patronage, the acts it can pass, the troop deployments, and the marshals' attention. The Power ratings **shift by the year**, per the timeline, but they are also *live* — a campaign's events (the party's work for a faction, a scandal, a war's outcome) can shift a party's Power up or down, making the metaplot *responsive* to the campaign, not just a script.

- **The National Modifier Engine** — the acts (the Enforcement Acts, the Specie Resumption, the Posse Comitatus, etc.) are not just timeline entries; they are **live modifiers** the GM applies to the county's gauges while the act is in force. Each act is a small rule:
  - **The Enforcement Acts** (1870–71): `+1` federal faction reach; the Committee/Redeemer factions' Standing shifts hostile; the troop may be used for law enforcement.
  - **The Panic of 1873** (1873–79): `-2` to all business rolls; the bank reserve gauges drop; the Greenback faction's Power climbs.
  - **The Compromise of 1877**: the Redeemer faction takes the South entirely; the freedmen's faction's federal protection drops to `-3`; the Republican party's Power drops; the Democratic party's Power climbs.
  - **The Posse Comitatus Act** (1878): the troop may no longer be used for domestic law enforcement (the troop's role shifts from law to war); the marshal's role widens.

  The engine makes the metaplot *mechanical* — the acts change the rules the county plays under, and the GM applies them as live modifiers, not as flavor. A campaign that runs across the decade *feels* the modifiers shift, and the party's choices (work for a faction, expose a scandal, win an election) can nudge the Power ratings, making the decade the *campaign's* decade, not a fixed script.

- **The Party Layer Above Factions** — the national parties are the layer *above* the county factions: each county faction is *aligned* with a national party (the cattleman's association is Republican; the immigrant union is Democratic; the Greenback caucus is its own). The party's Power rating shifts the aligned county factions' Influence pools (the factions chapter's system): a Republican faction in a Republican-ascendant year has a higher Influence cap; a Democratic faction in a Republican year is squeezed. This ties the national metaplot to the county's faction web mechanically — the decade's weather is the county's weather, through the party-power-to-faction-Influence link.

### Why it fits

The political scene is the book's national layer, and the Party Power Track + the National Modifier Engine make it a *system* rather than a reference. The party-layer-above-factions ties the national weather to the county's mechanics, so a campaign set in 1876 *feels* the election in the faction web, the bank reserves, and the troop's orders. This is the heaviest subsystem in the book, and it is the right weight — the political scene is the engine's ceiling, and the decade should be the campaign's climate, not its backdrop.

### Complexity: **heavy.** 2–4 Power ratings (one per active party); a small rule per act in force; the party-to-faction link is a modifier the GM applies. The heaviest part is the up-front setup (defining the county factions' party alignments and the campaign's starting year), which is a one-time cost that pays out across the whole campaign.
