# Proposal: Lower-Friction Trouble for Chapter 11 Operations

**Status:** Draft proposal  
**Target:** `corebook/11-outlaws-of-the-old-west.md`  
**Scope:** Operation procedure only. No manuscript integration yet.

## Purpose

The operation rules in Chapter 11 want the right thing:

- scores should tighten as they go
- pushing should matter
- a job should be able to succeed and still turn ugly

The present danger is not dramatic weakness. It is handling friction.

If the table must choose, before each roll, how many Trouble Dice to assign from a wide range, the procedure asks for too much attention too often. The players must track:

- current Progress
- current Trouble
- the operation's size
- the scene's fictional danger
- whether to push
- how many Trouble Dice this one roll should carry

That is too much repeated pricing of danger.

Forbidden Lands 2e usually avoids this kind of friction by making risk decisions narrower:

- make the roll
- decide whether to push
- accept the known danger of failure or the push

The table rarely has to build a second custom risk pool on top of the ordinary one.

## Core Diagnosis

Open Trouble Dice create friction in three ways.

### 1. They add a second pool-building step

The player already assembles the normal dice pool. Asking them to also decide how many of those dice are special danger dice is a second design step before the roll has even happened.

### 2. They force repeated pre-pricing of danger

The table must keep asking:

- is this `2` Trouble Dice or `3`?
- is this check really more dangerous than the last one?
- are we pricing the fiction consistently?

That is not good tension. It is repeated calibration work.

### 3. They overlap with other existing risk channels

Outlaw operations already have good risk carriers:

- outright failure
- pushing
- deliberately loud or bloody choices
- poor band condition
- Trouble already on the track

If Trouble Dice sit on top of all of that, the subsystem risks charging for danger twice.

## Design Goals

Any replacement should:

1. keep rising pressure visible
2. keep player choice meaningful
3. reduce per-roll memory load
4. be teachable in a short paragraph
5. fit naturally beside the book's Year Zero logic

## Recommended Direction

The strongest model is a hybrid of:

- **Option A:** exposure categories declared by the GM
- **Option C:** Trouble mainly comes from failure, pushes, and hard choices

But with one added refinement:

- `Risky` and `Desperate` checks still read the rolled dice for extra Trouble through the number of `1`s

This keeps the visible feel of bad luck in the roll, without asking the table to build a separate Trouble pool.

## Recommended Player-Facing Rule

Before each operation check, the GM says whether the attempt is:

- `Safe`
- `Risky`
- `Desperate`

The players then roll the normal pool only.

No Trouble Dice are added to the pool.

### Trouble by Exposure

| Exposure | Trouble Rule |
| --- | --- |
| `Safe` | No Trouble from the roll itself unless the gang chooses noise, blood, speed, or some other plainly dangerous trade. |
| `Risky` | On `0` successes, mark `1` Trouble. Then count the `1`s rolled; for every two `1`s, mark `1` additional Trouble. |
| `Desperate` | On `0` successes, mark `1` Trouble. Then count the `1`s rolled; each `1` marks `1` additional Trouble. |

If a pushed check still fails, mark `1` additional Trouble.

### Why This Version Works

This keeps the key dramatic structure:

- the GM classifies danger once
- the player rolls normally
- the dice themselves tell you how much bad luck came with the failure

The table no longer asks:

- how many Trouble Dice are in this roll?

It asks only:

- is this `Safe`, `Risky`, or `Desperate`?

That is a much better question.

## Why This Is Better Than Open Trouble Dice

Your chosen structure preserves three valuable things:

### 1. Visible escalation

`Safe`, `Risky`, and `Desperate` are easy to understand at the table. They communicate tone and expected danger cleanly.

### 2. Bad luck inside the normal roll

Counting `1`s lets the roll itself produce collateral danger without needing separate red dice. That keeps the operation feeling volatile.

### 3. Pushes still matter

A pushed failure adding `1` Trouble keeps the Year Zero habit intact. The player still knows that forcing the issue can make things worse even when it does not save the roll.

## Why The `1`s Method Has Lower Friction

This method still uses information from the dice, but it removes the most awkward part of the prior concept.

The table no longer needs to:

- choose special dice
- remember which dice were Trouble Dice
- assign different Trouble Dice counts from roll to roll

It only needs to:

- know the exposure
- check whether the roll got `0` successes
- count `1`s if the exposure says to do so

That is much lighter handling.

## Recommended GM Guidance for Exposure

The category call should be fast and fiction-first.

### `Safe`

Use `Safe` when failure would be inconvenient but not immediately compromising.

Examples:

- watching a road from good cover
- spreading money among likely drifters in a rough camp
- reading a town from the edge before stepping in

### `Risky`

Use `Risky` when discovery, delay, suspicion, or narrowing options are plausible.

Examples:

- passing Hot Goods through a known but nervous fence
- slipping into town under local Wanted pressure
- moving the gang across watched ground

### `Desperate`

Use `Desperate` when the gang is trying to force a result under pressure and any ugly turn could cost them the operation's shape.

Examples:

- cracking the safe while the bank is already alert
- bluffing armed men at bad pistol range
- driving stolen stock through a choke point with trackers behind

## How Often Trouble Should Be Read

To keep the handling clean:

- `Safe` checks do not count `1`s
- `Risky` and `Desperate` checks only count `1`s when the roll gets `0` successes
- successful rolls ignore `1`s unless the fiction says the gang chose a loud or cruel method and the GM adds Trouble directly

That keeps the subsystem from turning into constant symbol-reading on every roll.

## Companion Rule: Hidden Bad-Luck Check for the GM

The old phase-based Trouble Die idea is more useful as a separate hidden GM procedure than as a player-facing roll.

It should not be another thing the players manage.

It should be a private tool the GM uses when the band has built a bad situation through repeated poor choices.

### Purpose

The hidden bad-luck check exists to answer a different question than Trouble:

- not "does this roll create immediate operational pressure?"
- but "has the band's pattern of choices now invited the sort of ugly coincidence or delayed consequence that outlaws fear?"

This is not ordinary bad luck.

It is bad luck that usually comes looking after the gang has already made at least two poor decisions.

### Recommended Trigger

The GM should consider a hidden bad-luck check only when at least two of the following are true in the same operation or immediate aftermath:

- the gang already chose noise over caution
- the gang already chose speed over concealment
- the gang left a witness, captive, or wounded man unresolved
- the gang pushed a key check and failed
- the gang kept operating after Trouble had already become serious
- the gang trusted a weak contact or shaky refuge anyway

In short:

- one bad decision is ordinary outlaw work
- two or more bad decisions begin to invite hard luck

### Recommended Procedure

The GM rolls a hidden `D6` only after that threshold is met.

| D6 | Hidden Bad-Luck Result |
| --- | --- |
| 1-3 | No fresh bad-luck consequence yet. Pressure is already represented by existing Trouble. |
| 4-5 | A delayed complication appears: a talkative witness, a lame horse, a deputy on the wrong road, a fence who grows cold, a missed rendezvous, or some similar follow-on problem. |
| 6 | A hard bad-luck turn: the posse chooses the right canyon, a captive gets free at the worst hour, the wrong man recognizes the gang, a frightened notable member panics, or the hideout's weakness matters now. |

### Why Keep This Hidden

If the players see this roll, it becomes another explicit subsystem they must price and anticipate.

If the GM keeps it hidden, it stays what it should be:

- a private check for whether compounded bad judgment has now ripened into ugly consequence

That preserves mood better than putting another visible die process on the player side.

### Why This Should Stay Separate from Trouble

Trouble is the open track.

The hidden bad-luck check is not another Trouble source to fire constantly. It is a rare GM-side escalation tool for when the band has already been gambling badly and the world is now ready to answer back.

That separation matters.

If both are folded together, the system gets muddy.

If they stay separate, each does one job well:

- Trouble tracks mounting operational exposure
- the hidden bad-luck check models delayed consequences from accumulated bad judgment

## Strengths of the Recommended Model

- No player-assigned Trouble Dice.
- Exposure categories are easy to teach.
- The dice still carry danger through counted `1`s.
- Pushing remains meaningful.
- The GM gets a separate hidden tool for compounded bad judgment.
- The system preserves an outlaw feel of bad luck, noise, witnesses, lame horses, and the wrong face in the wrong town.

## Weaknesses and Risks

- Counting `1`s is still some handling, though much less than building Trouble Dice pools.
- The `Desperate` category can escalate Trouble quickly if large pools fail.
- The hidden bad-luck check must be used sparingly or it will feel punitive.

These are manageable as long as the text is explicit about two boundaries:

1. only count `1`s on failed `Risky` or `Desperate` checks
2. only use the hidden bad-luck check after a visible pattern of bad choices

## Recommended Final Shape

For Chapter 11, the strongest final form is:

- player-facing `Safe / Risky / Desperate`
- no Trouble Dice in the pool
- `Risky` and `Desperate` failed rolls generate extra Trouble from `1`s
- pushed failures add `1` Trouble
- loud, bloody, or hurried choices can still add direct Trouble by fiction
- a hidden GM-side bad-luck check exists for compounded poor decisions

That preserves pressure, preserves outlaw ugliness, and removes the worst friction from the original Trouble Dice concept.

## Bottom Line

The core design mistake was asking the table to configure danger before each roll.

The better approach is:

- classify the attempt once
- roll normally
- let failure and bad faces on the dice tell you how ugly it gets

And when the gang has been stupid more than once, let the GM make a hidden bad-luck check to see whether the world now punishes the pattern, not just the individual roll.
