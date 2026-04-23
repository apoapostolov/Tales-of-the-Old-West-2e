# Playtesting

A playtest is not a performance. It is a diagnostic.

The adventure has been written. The author believes it
works. The playtest exists to find out what does not.
The author's job during a live playtest is to observe
and record — not to explain, not to patch, not to
intervene. Every time the author opens their mouth to
clarify something the text should have covered, the
text has failed.

## What playtesting is for

Structural failures that cannot be found on the page.
These failures are invisible to the author but
immediately visible to players:

- A clue that is in the text but is described in a way
  that no one in the room registers as a clue.
- An NPC whose motivation is clear to the author but
  opaque to the GM reading the entry cold.
- A scene that the author thinks is tense but lands flat
  because the players don't care about the stake.
- A pacing assumption (this scene takes twenty minutes)
  that is wrong by a factor of three.
- A branch that the author included as an option but that
  every group ignores because the incentive structure
  points elsewhere.

These failures cannot be caught by rereading the text.
They can only be caught at the table.

## Playtest types

### (a) Solo read-aloud pass

The author reads the chapter aloud to another person who
plays no character and knows nothing about the adventure.
The listener stops the reader any time they are confused.

Useful for: catching jargon, detecting missing information,
finding overlong read-aloud.

Limitations: does not simulate player agency. Misses
pacing failures and branch-selection problems.

Signal value: low. Run this as an early draft pass, not
as a final playtest.

### (b) Live table playtest

The adventure is run at a live table with real players.
The author is present as a silent observer, not as GM
(preferred) or as GM (acceptable if no other option
exists).

If the author must GM:

- Take no notes during play (you cannot observe while
  running).
- Immediately after the session, write a postmortem
  from memory: what stalled, what was faster than
  expected, which NPCs landed, which were ignored.

If the author observes:

- Sit to the side and take notes.
- Do not correct the GM's interpretations. The GM's
  misreadings are data: the text failed to communicate
  clearly.

Signal value: high. The standard minimum for publication.

### (c) Blind playtest

The author provides the document to another GM who has
never seen it. The other GM runs it without any briefing
from the author. The author may attend as a player or
may not attend at all.

This is the highest-signal playtest because it fully
removes the author's voice from the experience. Every
improvised ruling the GM makes is a gap the text didn't
fill. Every pause to search the document is a navigation
failure.

Signal value: highest. Required before large-scale
publication or release.

## The observer role

During any live or blind playtest, the author's work is:

1. Note the scene number (or a shorthand label) for each
   observation.
2. Use the shorthand notation below.
3. Do not speak unless the session is about to die
   completely (see intervention threshold below).
4. Do not explain NPC motivations to the GM.
5. Do not add information the text didn't supply, even
   if you know what the text "meant."

Your restraint is not politeness — it is data collection.
An intervention erases the data for that scene.

## Note-taking shorthand

Use this format: **[scene label] [code] [brief note]**

| Code | Meaning                                                       |
| ---- | ------------------------------------------------------------- |
| F    | Faster than designed — scene resolved too quickly             |
| S    | Slower than designed — scene ran long                         |
| Ø    | Skipped — players bypassed this scene entirely                |
| ?    | Player confusion — players stopped and looked uncertain       |
| !    | Unexpected player move — action outside designed paths        |
| ✓    | Scene landed as designed                                      |
| NPC+ | NPC connected with the players strongly                       |
| NPC- | NPC was flat, ignored, or didn't land                         |
| CLU? | Clue in this scene was not received or registered             |
| RPT  | Player verbally repeated what just happened (means it landed) |

Example log entries:

```
Scene 2 (S) ran 35 min, designed for 20. Social scene with Holt.
Scene 3 (Ø) Players skipped the mill entirely.
Scene 4 (?) Three players stopped and asked where to go next.
Scene 5 (!) Players attempted to bribe the marshal — not in text.
Scene 6 (NPC-) Aldermoor had no traction. Players moved past him fast.
Scene 7 (CLU?) The telegram clue was described. Players didn't engage.
```

## The intervention threshold

Intervene only when the session is dying — all players
have stalled with no forward motion and no one at the
table has any visible path.

This is rare. Players are usually more resourceful than
authors expect. A confused party will try something.
Let them try it.

If you must intervene:

- Do not explain the text's intent.
- Ask a question that a real-world bystander would ask:
  "What do you know so far?" or "What are you trying
  to find out?" These questions redirect without
  supplying the author's solution.

Stalls short of session death are not interventions.
Stalls are the best data you will collect from the
entire playtest. Note them and stay quiet.

## Pre-playtest checklist

Before the session begins:

- [ ] The text is complete (no [placeholder] sections
      remaining).
- [ ] Pre-generated characters are prepared if the
      adventure requires them.
- [ ] Any physical handouts are printed or in shareable
      digital form.
- [ ] You have identified the two or three scenes you
      most want to observe.
- [ ] Players have been told this is a draft and asked
      not to give feedback during the session.
- [ ] You have a notebook or equivalent for your
      observation log.

## Setting expectations with players

Tell players, before the session begins:

> This is a draft adventure. Play naturally — make the
> choices your characters would make. Don't adjust your
> play to help the adventure succeed. If the adventure
> is doing something that confuses you, that's useful
> information for the author. I'll ask for your feedback
> tomorrow.

Do not ask for feedback during play. Mid-session feedback
interrupts the experience, produces incomplete reactions,
and conflates emotional state with critique.

## Blind playtest protocol

1. Hand the GM the document. Do not explain anything
   beforehand.
2. Answer no questions from the GM before the session.
   If the GM has a question about the text, note that
   the text didn't answer it — do not answer verbally.
3. Attend as a player (preferred) or observe in silence.
4. After the session, before the debrief, write down:
   every time the GM made a ruling that the text should
   have covered; every time the GM paused to search the
   document; every moment you felt the gap between the
   text's intent and the table's experience.
5. The GM's debrief is the primary data source. The
   players' debrief is secondary. The author's post-
   session notes are tertiary.

## After the playtest

See `references/feedback-collection.md` for the debrief
protocol. Wait 12-24 hours before running the debrief.
Do not discuss the adventure in the gap between the
session and the debrief — the impressions need to settle.

## Online and VTT playtests

Most contemporary playtests happen on a virtual tabletop
(Roll20, Foundry, Owlbear) or over voice/video (Discord,
Zoom). The protocol above still applies, with adjustments.

**Observation differences online**:

- Body language is mostly invisible. You cannot read the
  table the way you can read a room.
- Long silences are harder to interpret — a player may be
  thinking, distracted, or muted by accident.
- Confused looks are not always visible. Lean on verbal
  signals: "wait, what?" or "I don't know what to do".

**Compensations**:

- Ask the GM (in advance) to record the session if all players
  consent. Reviewing the recording catches signals you missed
  in real time.
- Use the chat as a passive observation channel. Players who
  type asides reveal what they are processing.
- Ask one player in advance to be your "check" — they message
  you privately during the session if they notice something
  that seems important. This is not a substitute for the debrief;
  it is a real-time supplement.

**Asynchronous playtests** (play-by-post, forum games):

- Pacing collapses. A scene the author thought would take twenty
  minutes takes two weeks of posts.
- Read-aloud and atmosphere weaken. Compensate with tighter prose.
- Branch decisions are deliberated, not made under pressure.
  This surfaces structural problems faster but masks pacing
  problems entirely.
- Use async playtests as a structural pass, not a pacing pass.
  Run a live playtest separately for pacing.

## Observer fatigue

Observing a session is more cognitively expensive than playing
one. After 90 minutes of pure observation, your note quality
falls. After three hours, you are unreliable.

If the playtest runs longer than three hours, schedule a break
or accept that your notes will degrade. Mark the time on each
entry; later you will know which observations were sharp and
which came from a tired observer.

For multi-session playtests, do not observe every session.
Observe the first and the last; let the GM run the middle
sessions and write a postmortem from memory.
