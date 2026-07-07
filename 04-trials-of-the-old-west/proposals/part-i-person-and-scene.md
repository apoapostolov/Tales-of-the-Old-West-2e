<!-- markdownlint-disable MD013 MD041 -->

# Part I — Person and Scene (Procedural Proposals)

> Ch.1 The Standoff · Ch.2 The Holdout
>
> These two are the lightest redesign. They are already scene-level
> frames, not Operations — the critique (rightly) says they should stay
> that way. The proposals here sharpen their *differentiation* from each
> other and from the corebook's combat, so the GM feels three distinct
> scene-shapes: the **duel** (1v1 formal), the **standoff** (multi-party
> tension), and the **holdout** (asymmetric siege).

---

## Ch.1 — The Standoff

### Current weakness

The Standoff Roll is a single opposed check that resolves to "draws first / backs down / fizzles." It works, but it is *one roll* — it does not model the **escalating tension** of a real standoff, where each beat of silence raises the stakes and the room's pressure builds toward a breaking point. A standoff that lasts three Rounds feels the same as one that lasts one.

### Proposed system — the Tension Track (light)

Add a small **Tension die** that climbs each Standoff Round the standoff holds unresolved, the way a brazier of coals heats up. The Tension die is the GM's dial for how long the room can hold its breath.

- **Tension starts at D6** and steps up one size each Standoff Round that ends in a draw or a 1-success margin (the standoff holds): D6 → D8 → D10 → D12.
- **The Tension die is rolled on the break.** When the standoff breaks (someone draws, someone backs down, a third party intervenes), the GM rolls the current Tension die:
  - On a **1**, the break is **messy** — collateral damage, a bystander hit, the keeper's mirror broken, the wrong man shot. The break has a cost beyond the standoff's resolution.
  - On a **6+**, the break is **clean** — the shot (or the backing-down) lands as intended, with no collateral.
  - In between, the break is **ordinary** — resolved as the Standoff Roll dictated.
- **Cultivating low tension.** A side may choose (as its Round action) to **defuse** instead of pressing — an `INSIGHT` or `PRESENCE` roll that, on success, steps the Tension die *down* one size and shifts the next Standoff Roll in the defuser's favor. This is the "let's all just calm down" play, and it costs the Round the defuser could have spent pressing the advantage.

### Why it fits

The Tension track gives the standoff a shape the single roll lacked: the longer it holds, the more dangerous the break, which pushes the table toward *resolving it* rather than letting it sit. A PC who wants a clean break is motivated to end it early; a PC who wants chaos (or who is stalling for the marshal's arrival) is motivated to let it cook. The defuse action gives the social/peacekeeper character a mechanical role in a scene that was previously all `Quick` and `SHOOTIN'`.

### Complexity: **light.** One extra die, rolled once at the break. No new pools, no bookkeeping between Rounds beyond the die size.

### The three scene-shapes, restated

- **Duel** (corebook) — 1v1, formal, the draw is the resolution. No Tension track; the duel is already structured.
- **Standoff** (this chapter) — multi-party, the Tension track is the engine, the break is the resolution.
- **Holdout** (next) — asymmetric, the Breach track is the engine, the dawn is the resolution.

---

## Ch.2 — The Holdout

### Current weakness

The Holdout uses a Breach track (attackers accumulate Breach; defenders hold until dawn) resolved by opposed Holdout Rounds. This is good and already distinct from combat. Its weakness is that the **defenders' interior** is abstracted away — the ammunition, the wounded, the fire, the cabin fever are all lumped into the Breach track's Trouble, so the GM cannot make the *inside* of the cabin feel like a place under siege.

### Proposed system — the Cabin as a small org (light–medium)

Model the cabin's interior with two small tracked resources the defenders manage, drawn from the org-lifecycle "upkeep" beat. These are **not** a second operation — they are the *contents* of the Breach track's Trouble, made concrete.

- **Ammunition as a resource die** (the corebook's consumables rule, applied here). The cabin starts at a die set by what the defenders laid in (D6 for a few boxes, D10 for a stocked cabin). Each Holdout Round of sustained fire steps it down on a 1–2. At D4 exhausted, the defenders are down to sidearms and edged weapons, and every shot is a decision. *This is the same primitive the outlaw band's Provisions die uses — the engine already knows it.*
- **The Wounded as a gauge** (1–5, mirroring Cohesion). Each defender taken down a condition ladder rung steps the Wounded gauge up. At 3+, the cabin has a medical problem (the `DOCTORIN'` roll under fire, the infection risk if the siege runs long). At 5, the cabin is a hospital with guns, and the engine should let that tell on the defenders' rolls.
- **The Fire as an escalating Trouble** — not a gauge, but a procedure: once the attackers fire the roof (assault tactic 2), the fire is a **second clock** running alongside the Breach track. Each Round the fire is unchecked, it spreads (one room closer to the cellar), and the defenders must spend actions fighting it (`LABOR`, `MAKIN'`) or abandon rooms. The fire is the holdout's most cinematic pressure and it deserves its own small procedure, not a Trouble step.

### Why it fits

The cabin-as-org gives the interior the weight the Breach track alone could not. The defenders are not just rolling to hold a wall; they are *managing* a shrinking supply of shots, a growing roster of wounded, and a fire that is eating the house. Each is a decision: do we shoot (spend the ammo) or hold fire (let them mass for the rush)? Do we fight the fire (lose a Round of defense) or abandon the room (lose the ground)? The fire especially turns the holdout from a numbers grind into a spatial, escalating crisis.

### Complexity: **light–medium.** Two gauges (ammo die, wounded) and one procedure (the fire). The Breach track remains the outer frame; these are its interior contents made playable. A GM who wants the simplest version ignores the fire and runs only the ammo die; a GM who wants the full siege runs all three.

### Integration

- The **ammo die** hooks the corebook's consumables-as-resource-dice rule and the outlaw `Provisions` die — the same primitive, the cabin's version.
- The **wounded gauge** hooks the sickness chapter (infection in a siege) and the corebook's `DOCTORIN'`.
- The **fire** hooks the corebook's non-typical-harm fire rules and the weather chapter (a fire in a blizzard is a different crisis than a fire in a drought).
- The **dawn** remains the natural clock; the cabin-as-org is what the defenders are managing until it arrives.
