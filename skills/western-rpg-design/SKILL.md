---
name: western-rpg-design
description: Use when explaining, designing, auditing, or extending the mechanics of the Tales of the Old West 2E repo. This skill maps the rules, design space, design logic, integration points, and gameplay logic so new mechanics fit the existing engine and manuscript structure.
---

# Western RPG Design

Use this skill for rules analysis and design work in the Tales of the Old West 2E repo.

## Source Of Truth

Start with:

- relevant files in `corebook/`
- the `AGENTS.md` file if present

If the task includes manuscript drafting, also use the western-writing skill.

## When To Use It

Use it when you need to:

- explain how a rule actually works in play
- design a new subsystem or variant rule
- audit a proposal for deep integration
- trace how one rule touches talents, abilities, gear, conditions, conflict, or recovery
- convert vague ideas into mechanically coherent game text

## Design Method

For each mechanic, analyze these layers:

1. Rule loop
   - trigger
   - player decision
   - roll or resolution step
   - consequence
   - downstream state change
2. Design purpose
   - what behavior the rule encourages
   - what pressure it creates
   - what kind of story or table feeling it supports
3. Integration map
   - linked chapters
   - linked subsystems
   - terms that must stay consistent
4. Table behavior
   - player-facing complexity
   - GM burden
   - speed in live play
   - ambiguity risk

## Core Design Space To Check

When evaluating new rules, always look at:

- attributes, abilities, and dice pools
- pushing rolls and risk
- conditions and recovery
- resource tracking and attrition
- scene and session pacing
- initiative, action economy, and positioning
- talent and ability interactions
- injury severity, survivability, and campaign consequences
- scarcity, survival, and the cost of safety in the frontier

## Output Structure

When answering a design question, prefer this order:

1. Current mechanics
2. Design logic
3. Gameplay logic
4. Integration points
5. Risks or edge cases
6. Recommended revision

## Standards For Good Design

- The rule must produce a clear table behavior, not just evocative text.
- It must use existing terms unless there is a strong reason to add a new one.
- It must create a meaningful decision or pressure point.
- It must not silently break adjacent systems.
- It must fit the game's harsh, practical frontier survival logic.
- If it increases realism, it must still preserve playability and campaign function.

## NPC Statblock Table Format

All NPC and creature statblocks use a fixed 8-column table structure unique to this game. Never use flat wide tables that list attributes as columns.

**Header row** — attribute name + value, paired across four attribute columns:

```
| GRIT | <value> | QUICK | <value> | CUNNING | <value> | DOCITY | <value> |
| --- | --- | --- | --- | --- | --- | --- | --- |
```

**Skill rows** — abilities are placed under the column of the attribute they belong to. Ability name in the label cell, value in the adjacent value cell. Empty cells fill gaps where no ability applies. Attribute-ability mappings:

- GRIT: FIGHTIN', LABOR, PRESENCE, RESILIENCE
- QUICK: LIGHT-FINGERED, MOVE, OPERATE, SHOOTIN'
- CUNNING: ANIMAL HANDLIN', HAWKEYE, INSIGHT, NATURE
- DOCITY: BOOKLEARNIN', DOCTORIN', MAKIN', PERFORMIN'

**Talents line** — placed immediately after the closing row of the table as a standalone bold paragraph. Markdown tables do not support colspan, so talents must not be placed inside the table.

**Example (Ellis Rockcliffe):**

```markdown
| GRIT       | 4   | QUICK | 3   | CUNNING | 5   | DOCITY | 3   |
| ---------- | --- | ----- | --- | ------- | --- | ------ | --- |
| PRESENCE   | 3   |       |     | HAWKEYE | 2   |        |     |
| RESILIENCE | 1   |       |     | INSIGHT | 2   |        |     |

**Talents:** AUTHORITY (Advanced), CHARMING (Advanced), COLD BLOODED (Basic), BUSINESS MINDED (Advanced).
```

Creature/animal statblocks (wolves, dogs) that don't use the four standard attributes keep a simpler inline table — do not force them into the 8-column format.

## Proposal Review Checklist

When auditing a proposal, explicitly check:

- rules completeness
- cross-chapter integration
- recoverability and permanence logic
- player agency after the rule lands
- whether catastrophic outcomes are playable, retirement-default, or dead ends
- whether the text belongs in proposal space or final manuscript space
