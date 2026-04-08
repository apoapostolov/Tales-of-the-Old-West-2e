---
name: rpg-synergy-analysis
description: Use when auditing talent combinations, ability stacking, character builds, or any multi-rule interaction for balance-breaking potential. Triggers on questions like "is this combo broken", "what are the strongest builds", "does this talent stack with that ability", "can players exploit this", or any request to stress-test a rule interaction. Also use when designing new talents or abilities that might create unintended synergy with existing content. This skill distinguishes between creative high-risk play (healthy) and one-decision dominant lines (unhealthy).
---

# RPG Synergy Analysis

A well-designed RPG encourages players to combine talents, abilities, gear,
and conditions in creative ways that tip dangerous situations in their favor.
That is the game working as intended. The problem this skill exists to catch
is different: combinations that require only a single obvious
character-creation or advancement decision, carry no meaningful risk or
tradeoff, and then quietly dominate the game from that point forward.

## When To Use It

- Auditing a proposed talent or ability for unintended interactions with existing rules.
- Stress-testing a character build for dominant lines.
- Reviewing a new rule or subsystem for synergy risk before it enters the manuscript.
- Answering player or designer questions about whether a specific combo is broken.
- Scanning the talent and ability chapters for systemic exploitation surfaces.

## Source Of Truth

Always ground analysis in the actual manuscript:

- `corebook/04-talents.md` — all talent paths and special abilities
- `corebook/05-conflict-and-damage.md` — action economy, initiative, combat
- `corebook/02-your-player-character.md` — character creation, attributes, abilities
- `corebook/03-rolling-the-bones.md` — core dice mechanics, pushing, opposed rolls
- `corebook/06-life-in-the-old-west.md` — equipment, property, daily life

Read the relevant sections before making claims. Do not argue from memory alone.

## The Core Distinction

Healthy synergy and unhealthy synergy look similar in output but differ in
input cost.

### Healthy synergy

The combo requires:

- deliberate setup in play (positioning, timing, resource spend)
- risk exposure (pushing, condition vulnerability)
- coordination between multiple players or multiple turns
- a tradeoff that closes off other options

The payoff is dramatic and memorable because the cost was visible.

### Unhealthy synergy

The combo requires:

- a single character-creation or advancement decision
- no ongoing risk, setup, or meaningful tradeoff
- no coordination — it works every time, automatically
- nothing stops a player from choosing it once they know about it

The payoff is routine and dominant because the cost was invisible or absent.

## The Five Tests

Apply these sequentially to any suspected synergy. If a combo fails even one
test, it needs correction.

### 1. Decision Cost Test

How many meaningful decisions does the player need to make to activate
this combo?

- **Healthy:** Multiple decisions across play — positioning, resource spend, timing, risk acceptance.
- **Unhealthy:** One decision at character creation or advancement. The combo activates automatically from that point.

Count the decisions. If the answer is one, the combo is suspect.

### 2. Risk Exposure Test

What does the player risk when they use this combo?

- **Healthy:** Resource drain, pushing banes, condition vulnerability, positional danger.
- **Unhealthy:** Nothing meaningful. The combo either avoids all risk channels or refunds its own cost.

Trace the resource flow. If resources spent come back through the same loop,
the risk is cosmetic.

### 3. Opportunity Cost Test

What does the player give up by committing to this build?

- **Healthy:** Other strong talents, different ability paths, gear flexibility.
- **Unhealthy:** Nothing important. The build still has access to most of what matters.

Check whether the combo leaves adjacent niches intact. If it also covers what
other builds specialize in, it is too broad.

### 4. Repeatability Test

How often can the combo fire per session, per encounter, per scene?

- **Healthy:** Once or twice per encounter, with setup required each time.
- **Unhealthy:** Every round, automatically, with no cooldown or re-setup cost.

Multiply the per-use power by expected frequency. A moderate effect used every
round is stronger than a devastating effect used once per session.

### 5. Campaign Erosion Test

Does the combo hollow out a pressure channel the campaign depends on?

- **Healthy:** The combo solves one problem well but leaves other pressures intact.
- **Unhealthy:** The combo removes an entire category of challenge — resource attrition, travel danger, injury fear, social opposition, action economy limits.

Name the pressure channel. If the combo deletes it rather than temporarily
relieving it, the campaign will flatten.

## Analysis Method

For any suspected combo, follow this procedure:

### Step 1 — Identify the components

List every talent rank, ability, gear property, and condition involved.

### Step 2 — Trace the interaction

Describe exactly how the pieces connect. Which rule feeds into which?
What triggers what?

### Step 3 — Apply the five tests

Run the decision cost, risk exposure, opportunity cost, repeatability,
and campaign erosion tests. Score each as healthy, borderline, or unhealthy.

### Step 4 — Check the pressure stack

Name which pressure channels the combo relieves and which it leaves intact.

### Step 5 — Compare to baselines

What does a character without this combo look like in the same situation?
If the gap is enormous with no corresponding cost, the combo is dominant.

### Step 6 — Recommend

One of:

- **Clean** — the combo is strong but earned. No action needed.
- **Monitor** — the combo is borderline. Flag for GM awareness but do not change rules.
- **Cap** — add a frequency limit, resource ceiling, or cooldown to one component.
- **Restructure** — one component needs a redesign to close the loop.
- **Separate** — the components should not be available to the same character without a significant gate.

## Output Format

When reporting a synergy analysis, use this structure:

```text
## [Combo Name]

**Components:** [list of talents, abilities, gear involved]
**Build cost:** [what character creation and advancement decisions are required]
**Activation cost:** [what the player spends each time they use it in play]

### How it works
[Describe the interaction chain]

### Five-test results
| Test | Result | Reasoning |
|------|--------|-----------|
| Decision cost | Healthy/Borderline/Unhealthy | ... |
| Risk exposure | ... | ... |
| Opportunity cost | ... | ... |
| Repeatability | ... | ... |
| Campaign erosion | ... | ... |

### Pressure channels affected
[Which pressures does this relieve or delete?]

### Baseline comparison
[What does the same situation look like without this combo?]

### Verdict
[Clean / Monitor / Cap / Restructure / Separate]

### Recommended correction
[If needed, what specific change fixes it?]
```
