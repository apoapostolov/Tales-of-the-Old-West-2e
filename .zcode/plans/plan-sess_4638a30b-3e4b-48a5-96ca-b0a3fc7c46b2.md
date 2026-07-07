# Implement Part I Proposals — Chapters 1 & 2

Two surgical revisions, adding the proposed subsystems without rewriting the chapters wholesale. The existing material is good; the proposals add the missing texture.

## Chapter 1 — The Standoff: add the Tension Track

**Where it goes:** A new `### The Tension Track` section, inserted between `### The Standoff Round` (line 21) and `#### Who Is in the Standoff` (line 27). This is the natural place — the Tension die is a property of the standoff-as-a-whole, introduced before the per-Round procedure.

**What it adds:**
- The **Tension die** (D6 → D8 → D10 → D12), stepping up each Standoff Round that ends in a draw or 1-success margin.
- The **break roll**: when the standoff breaks, GM rolls the current Tension die — `1` = messy (collateral, the wrong man shot), `6+` = clean, in-between = ordinary.
- The **defuse action**: a side may spend its Round action on an `INSIGHT`/`PRESENCE` roll to step the Tension die *down* and shift the next Standoff Roll in the defuser's favor. Gives the social/peacekeeper PC a mechanical role.
- A short worked-fiction blockquote showing the Tension die in play (using the cast — Riddle in the saloon vignette).

**What changes elsewhere:** The "Reading the Standoff Roll" section (line 64) gets a one-paragraph addendum noting that the break's *quality* (messy/clean) is rolled on the Tension die after the break's *direction* is decided by the Standoff Roll. The "A Word on the Table" closer (line 98) gets a sentence acknowledging the Tension die as the one die the GM rolls in the scene (versus the players' Standoff Rolls).

**New section header ref:** `### The Tension Track` — no chapter cross-references affected.

## Chapter 2 — The Holdout: add the Cabin-as-Org interior

**Where it goes:** Three additions, woven into the existing structure rather than appended:

1. **A new `### The Cabin's Interior` section**, inserted between `### The Holdout Round` (line 33) and `#### The Attackers' Pool` (line 37). This is the natural place — it defines the defenders' tracked resources before the opposed-roll procedure that uses them.

2. **Ammo as a resource die** — the cabin's ammunition tracked as a stepped die (D6 for a few boxes, D8–D10 for a stocked cabin), stepping down on a 1–2 per Round of sustained fire. At D4 exhausted, the defenders are down to sidearms and edged weapons. Explicitly named as the same primitive as the outlaw `Provisions` die.

3. **The Wounded gauge** (1–5, mirroring Cohesion's shape) — steps up as defenders take condition-ladder damage; at 3+, a medical problem; at 5, the cabin is a hospital with guns.

4. **The Fire as a procedure** (not a gauge) — once the attackers fire the roof (assault tactic 2), the fire is a second clock: each Round unchecked, it spreads one room closer to the cellar; the defenders must spend actions fighting it (`LABOR`/`MAKIN'`) or abandon rooms.

**What changes elsewhere:**
- The `### Assault Tactics Table` entry for tactic 2 (`Fire the roof`) gets a one-paragraph expansion pointing to the new Fire procedure, so the cross-reference is live.
- The `### Reading the Holdout Round` section gets a short addendum: a Round of sustained fire steps the ammo die; a defender down a condition rung steps the Wounded gauge.
- The `### The Holdout and the Other Rules` integration section gets two bullet additions: ammo die → corebook consumables + outlaw `Provisions` die; Wounded gauge → sickness chapter (infection) + `DOCTORIN'`.
- A short worked-fiction blockquote showing the interior gauges in play (the Calder cabin-vignette).

**New section header ref:** `### The Cabin's Interior` — no chapter cross-references affected.

## What I am NOT changing

- The core Standoff Roll procedure, the Holdout Round procedure, the Assault Tactics Table, the Breach track, the Dawn, or any integration/cross-reference. These are already good; the proposals add the texture the flat tracks lacked.
- No renumbering, no new files, no touched cross-references.

## Verification after implementation

- Grep for the new section headers to confirm insertion.
- Grep for any broken cross-references (none expected — both additions are self-contained).
- Confirm both chapters still end on their existing closers.