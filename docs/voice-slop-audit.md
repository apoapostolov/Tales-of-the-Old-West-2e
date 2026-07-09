<!-- markdownlint-disable MD013 -->

# Book 04 Voice Slop Audit

This audit tracks the second rescue pass: not terminology cleanup, but prose behavior. The problem is not only banned words. The manuscript often sounds generated because chapters share the same rhetorical machinery, announce themselves before saying anything useful, and land on summary where a published supplement should land on table consequence.

## Repeated Templates Found

The strongest repeated structures are:

- **Book-self-announcement:** "This is _Trials of the Old West_, a book..." The sentence states the cover instead of preparing the reader.
- **Corebook gap contrast:** "The corebook handles X. It does not handle Y. This chapter gives..." This appears across multiple chapters and makes the manuscript sound like a design memo.
- **Use / do not need mirror:** "Use these rules when..." followed by "You do not need these rules..." The saloon, trade, mining, cattle, mass-combat, and baron chapters all show this shape.
- **Abstract purpose phrase:** "and its work" headings paired with paragraphs explaining why the chapter exists before giving the reader a concrete table situation.
- **A chapter that gives... closers:** concluding paragraphs that summarize the chapter's function instead of ending on consequence, choice, or use.
- **Negative parallelism:** repeated "not a single roll," "not just," "not only," and "more than" constructions.
- **Three-part cadence:** repeated lists of three or more items joined by commas for weight rather than utility.
- **Over-neat examples:** many examples begin by naming the procedure, then listing the result. They teach the rule but sometimes sound like worked answer keys rather than table scenes.
- **Mechanical nouns presented as prose:** "gauge," "track," "operation," "procedure," "menu," and "layer" are sometimes necessary rules terms, but the manuscript overuses them as rhetorical nouns.

## Rewrite Standard

Each chapter should open with a concrete historical or table situation, then move naturally into what the rules let a GM and players do. A reader should know when to use the chapter because the situation is vivid, not because the paragraph says "Use these rules when."

Paragraphs must earn their place by doing one of four jobs:

- introduce concrete period material;
- clarify a rule or choice;
- explain a consequence the table can play;
- connect this chapter to another rule in language a GM can use.

Paragraphs that only announce structure should be cut or folded into the first useful rule.

## Pass Checklist

- [x] Rewrite `00-introduction.md` so it prepares the reader instead of describing the book to itself.
- [x] Remove or sharply reduce "This chapter gives..." openings.
- [x] Remove mirrored "Use these rules / You do not need these rules" pairs.
- [x] Vary chapter openings so each has its own rhetorical path.
- [x] Vary chapter closings or cut summary closers.
- [x] Reduce comma-stacked list cadence where it exists for pathos rather than information.
- [x] Keep game terms where needed, but stop using them as the emotional center of the prose.
- [x] Run final phrase scan only after the full pass.

## Pass Notes

The second voice pass rewrote the chapter openings and the most repetitive closers across `00` through `25`. The largest visible changes were:

- `00-introduction.md` now opens from table situations and county consequences rather than self-description.
- Chapter headings no longer repeat the "and its work" structure in the numbered manuscript.
- Mirrored "Use these rules / You do not need these rules" pairs were removed or folded into concrete scope paragraphs.
- "A chapter that gives..." closers were replaced with consequences, future hooks, or cut entirely.
- Several repeated "not a single roll" and "not only" constructions were varied where they served cadence rather than rule precision.
