# Investigation Structure

An investigation adventure has a factual target. Something
happened. The truth is fixed. The players' job is to
reconstruct it.

This distinguishes investigation from sandbox: a sandbox
has a situational target (what _will_ happen), not a
historical one. In investigation design, the author must
know the crime before the players do.

## Design the crime first

Write the crime or central event from the perpetrator's
point of view before designing anything else. Write it
as a chronological account:

> On the evening of June 3rd, Durance Holt rode to the
> north pasture. He found Weaver there alone. He shot
> Weaver twice and dragged the body to the creek. He
> returned to the bunkhouse before midnight and told the
> cook he'd been checking the fence.

Every step in this account leaves residue: a witness
who saw Holt ride north, a cook who can verify the
time of return, two bullet wounds with a distinctive
caliber, drag marks to the creek, Holt's horse's tracks
in the mud.

The perpetrator's account is the adventure's hidden
spine. The players are reading the evidence; the author
is watching them reconstruct the spine.

## The suspect web

Draw a relationship diagram with the perpetrator at the
center and four rings outward:

1. **The perpetrator**: what they did, their alibi, the
   evidence they can't suppress.
2. **Direct witnesses**: saw or heard something that
   directly implicates or exonerates the perpetrator.
3. **Adjacent parties**: near the crime but didn't
   witness the key event. They have partial information
   and their own reasons to be evasive.
4. **False leads**: individuals who look guilty for
   circumstantial reasons and whose innocence must be
   established through investigation.

For each node in the suspect web, write:

- What they know.
- What they will say freely.
- What requires pressure or persuasion.
- What they will never say (and why).

## Clues versus conclusions

**Clues are observable facts**. The stain on the
floorboards. The date on the telegram. The callus
pattern on a dead man's hands. The GM describes these.

**Conclusions are player theories**. The stain is from
the right-caliber slug. The telegram was sent before
the murder, not after. The dead man was a carpenter,
not a soldier. The players supply these.

The adventure supplies clues. The players supply
conclusions.

Do not embed the solution in the clue text. A clue
entry should never say: "This is the murder weapon."
It should say: "A Colt .45 revolver, two rounds
discharged, smelling of recent use, tucked beneath
the hay in stall three."

The conclusion that this is the murder weapon belongs
to the players. The GM confirms it only when the
players present sufficient evidence.

## Observable versus deducible clues

**Observable clues** are directly visible and require
no prior knowledge to notice. A locked drawer that
should be unlocked. A missing portrait from a wall
with a clean rectangle where it hung. These can be
found by anyone who looks at the right location.

**Deducible clues** require the observer to notice
that something contradicts a prior assertion. The
victim's coat is dry, but he supposedly walked in the
rain. The clock on the mantle is twenty minutes fast.
These require the players to hold two pieces of
information simultaneously and notice the contradiction.

Both are valid. Deducible clues are riskier — they
can be missed entirely if the prior assertion wasn't
received. Treat deducible clues as secondary carriers,
not primary ones.

## Clue distribution by scene

For every critical fact the players must establish
to solve the case, place at least three carriers in
the adventure using the rule from
`references/clue-discipline.md`. The minimum for an
investigation adventure is three, and Arc I carriers
should be highest-density.

Build a clue distribution table before drafting:

| Critical fact                 | Carrier 1                 | Carrier 2               | Carrier 3                    |
| ----------------------------- | ------------------------- | ----------------------- | ---------------------------- |
| Holt was at the north pasture | Stable hand saw the horse | Mud on Holt's boots     | Cook's timeline              |
| The caliber of the weapon     | Wound pattern             | Shell casing in stall 3 | Missing rounds in Holt's gun |

Any critical fact with fewer than three carriers is
a single-point failure. Fix it before drafting.

## The escalating timeline

An investigation needs structural urgency. The villain
is not standing still while the party investigates.

Build a countdown of villain actions, victim
deterioration, or public pressure events. Advances
when the party takes significant time, rests, fails
publicly, or triggers a watch trigger.

See `references/clocks-and-timers.md` for clock
mechanics. For investigation specifically:

- **Evidence destruction clock**: the perpetrator can
  destroy specific evidence after a certain number of
  advances. Name what is destroyed. The investigation
  becomes harder but does not end.
- **Victim clock**: someone is in danger. Advances
  when the party delays. The victim can be rescued at
  any clock level but the cost rises.
- **Public pressure clock**: if the case attracts
  outside attention (press, a rival investigator, a
  political deadline), the pressure rises with each
  advance.

## Node-based investigation design

See `references/node-based-design.md` for node
mechanics. For investigations specifically:

Every scene where the players might find a clue,
interview a witness, or confront a suspect is a node.
Each node has:

- **Entry condition**: what brought the party here?
- **Clues available**: what can be found and how?
- **Suspect behavior**: what is this NPC's posture
  in this scene? What will they freely say? What
  requires pressure?
- **Exit paths**: where can the party go next from
  here, and what does each exit reveal?
- **What changes**: what is different in this node
  the second time the party visits?

Floating clues — critical facts that are not locked
to a single node — appear at any relevant node the
party visits. If the party skipped the mill and the
mill had Carrier 2 of a critical fact, Carrier 2 floats
to the next relevant scene.

## Red herrings

A red herring is a false lead that points to the wrong
suspect and can be disproved through investigation.

Three rules for red herrings:

1. **They must be falsifiable**: the players can disprove
   the red herring by finding evidence, not by the GM
   deciding to tell them they're wrong.
2. **The false suspect must be sympathetically drawn**:
   a flat, obviously guilty-looking false suspect is not
   a red herring — it is a decoy. A false suspect who
   has real motive, real opportunity, and real reasons
   to be evasive is a red herring worth pursuing.
3. **The false suspect has their own secret**: the reason
   they look guilty. Usually a different, smaller secret
   (an affair, a debt, a past they're hiding) that
   explains their suspicious behavior without implicating
   them in the crime.

## The open-loop ending

An investigation adventure can end without a conviction.
The players may know the truth and be unable to prove
it legally. This is a structurally valid ending —
one of the four minimum endings.

Build endings for:

1. The party has legal proof and delivers it to the
   appropriate authority.
2. The party has the truth but cannot prove it. They
   must decide what to do with that knowledge.
3. The party is wrong and acts on their best theory.
4. The clock ran out and the perpetrator acted before
   the party found enough.

Ending 2 is often the most dramatically rich and the
most commonly skipped by inexperienced adventure authors.
It is not a failure state — it is a consequence that
demands a moral decision. See `references/dilemmas.md`.

## Horror and investigation

When the truth is cosmically dangerous to know — when
the investigation reveals something that should not
be revealed — the investigation structure changes.

- Clues do not just lead to the truth; they destroy
  the investigator's certainty about the world.
- The revelation is not resolution. It is escalation.
- Some investigators may choose to suppress what they
  found rather than reveal it.

For full horror investigation design, load
`references/horror-design.md` alongside this file.

## Investigation audit checklist

Before publication or playtest:

1. [ ] The perpetrator's account is written and includes
       at least four steps that leave residue.
2. [ ] The suspect web has at least one false lead with
       a falsifiable secret.
3. [ ] Every critical fact has three minimum carriers
       in the clue distribution table.
4. [ ] Arc I carries the highest clue density.
5. [ ] The escalating timeline names at least two
       clock advances before the adventure ends.
6. [ ] Every investigation node has: entry condition,
       clues, suspect behavior, exits, what changes.
7. [ ] At least two of the four ending states are
       built (one including the open-loop option).
8. [ ] No clue text embeds a conclusion ("this is the
       murder weapon") — clues are observable facts only.

## Core clues vs. supplementary clues

GUMSHOE-style design distinguishes between **core clues** (the
facts the investigation cannot proceed without) and
**supplementary clues** (texture, alternate angles, deeper
colour). The distinction matters even when the system is not
GUMSHOE.

- Core clues should be _automatically_ delivered when the
  party arrives at the carrier and engages with it. Do not
  gate core clues behind a roll. The roll determines _how_
  the party gets the clue (clean, costly, partial), not
  _whether_ they get it.
- Supplementary clues can be gated behind rolls, careful
  searches, or specific NPC pivots. Missing them does not
  block the investigation; finding them deepens it.
- Tag every clue in the distribution table as `CORE` or
  `SUPP`. A roll-gated CORE clue is a single-point failure
  even if it has three carriers, because all three carriers
  use the same gate.

The three-clue rule applies to core clues. Supplementary clues
can be unique — the loss is texture, not the case.

## The verification beat

Before the players act on a theory — arresting a suspect,
confronting the antagonist, presenting evidence to authority
— they need a way to test the theory cheaply.

A verification beat is a low-cost moment where a theory can
be confirmed or disproved without committing to action. A
fingerprint matched. A timeline checked against a witness
found earlier. A second visit to a location to look for the
specific thing the theory predicts should be there.

Without verification beats, the players must commit to their
best guess and discover its correctness through consequences.
That is sometimes the right design (open-loop ending), but as
a default it punishes investigation. Players who reason
correctly should be able to confirm before they act.

Write at least one verification beat per critical conclusion
the investigation can produce. The beat is in the GM notes,
not the scene list — it triggers when the players seek it.
