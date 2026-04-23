# Supplement 2 Agents Guide

This file defines how work inside `supplement-2-montana-campaign/` is organized.

## Purpose

This directory is building a full book-length sandbox supplement for _Tales of the Old West 2e_ set in Montana Territory in `1873`.

The supplement has two different kinds of files:

- final manuscript content
- research, planning, and production scaffolding

Do not mix them.

## Directory Rules

### `book-content/`

This folder is for final book manuscript text only.

Rules:

- chapter-facing prose goes here
- file names should be book-order numeric, for example `00-welcome-to-montana.md`
- prose should be publication-facing, not planning-facing
- no checklists, TODOs, or rough research notes in this folder
- any in-progress manuscript chapter that is meant to survive into the book belongs here

### `research/`

This folder is for research, audits, structure notes, historical analysis, web source ledgers, and scenario design notes.

Rules:

- planning documents stay here
- source collection stays here
- chapter analysis and product architecture stay here
- if a file explains how to write a chapter rather than being the chapter, it belongs here

### `villages/`

This folder is for settlement templates, settlement planning, and pre-manuscript town scaffolds.

Rules:

- templates and indices stay here
- rough town skeletons stay here until promoted to full manuscript
- once a settlement becomes finished book prose, move or rewrite it into `book-content/`

### `factions/`

This folder is for faction design, presence matrices, and faction planning notes.

### `outlaw-bands/`

This folder is for outlaw-band planning, ledgers, and development notes.

## Writing Standard

When writing manuscript prose for this supplement:

- follow the `western-writing` skill guidance
- run a mandatory final pass against `skills/western-writing/references/anti-ai-patterns.md`
- use [research/07-npc-creation-helper.md](/mnt/c/git-public/tales-of-the-old-west-2e/supplement-2-montana-campaign/research/07-npc-creation-helper.md) whenever creating named NPCs, generic NPCs, or appendix statblocks
- use [research/08-location-statblock-helper.md](/mnt/c/git-public/tales-of-the-old-west-2e/supplement-2-montana-campaign/research/08-location-statblock-helper.md) whenever creating settlement, village, farm, ranch, camp, ferry, roadhouse, fort-orbit, or other location statblocks
- keep chronology locked to `1873`
- distinguish verified history from plausible synthesis and fictionalized table content
- preserve the gritty, concrete, non-generic prose register used elsewhere in the repo
- avoid planning language in manuscript files

## Mandatory Tone

This is mandatory for final prose in `book-content/`.

- write in hard, plain, concrete sentences
- prefer physical facts over thematic explanation
- end paragraphs on weight: a noun, a body, a piece of weather, a threat, a refusal
- do not write in essay voice, blog voice, hype voice, or summary voice
- do not stack abstract contrasts when a concrete example will do the work
- do not use AI-signature phrasing from `anti-ai-patterns.md`
- if a sentence sounds like it is explaining the setting from above it, rewrite it from the ground
- if a paragraph could fit in a generic RPG sourcebook, cut it and write it again
- **Vary Sentence Length and Structure**: Do not exclusively use short, declarative sentences. Mix long, rhythmic sentences carrying sensory detail with occasional short, punchy sentences for dramatic impact. Never start three consecutive sentences with the same pronoun or noun.
- **Show, Don't Tell (No Signposting)**: Do not write sentences holding the reader's hand like "This distinction matters to a campaign because..." or "Players should note that...". Present the brutal realities of the setting (weather, bribery, distances) and let those facts inherently prove why they matter.
- **Avoid 'AI Meta-Commentary'**: Never address the reader's expectations directly (e.g., "If your knowledge comes from films..." or "Foreign readers should note..."). Write with total narrative confidence.
- **Banish Formulaic Transitions & Paragraphs**: Do not use words like _Furthermore, Moreover, In conclusion, As such, It is important to note_. Ban the "five-paragraph essay" structure (topic sentence, three supporting lines, concluding summary). Let the ideas flow naturally from one paragraph into the next based on narrative momentum.
- **Ground Descriptions in the Concrete**: Instead of saying "the economy was expanding," describe what that looks like: "the sudden arrival of assay offices, fraudulent deeds, and heavy freight wagons choking the muddy roads."
- **Kill the Adjectives and Adverbs**: Delete words like _rugged, menacingly, suddenly, very, extremely_. Rely on strong verbs and precise nouns. Instead of saying the man "walked dangerously," say he "carried a shotgun loose across his saddle pommel."
- **Ban AI Cliché Language**: Absolutely no usage of words like _tapestry, crucible, delve, testament to, stark reminder, navigate, landscape of, bustling, vibrant_.
- **Unflinching Realism**: Do not sanitize the Old West. Write plainly about the disease, the freezing mud, the starvation, the overt racism, and the cruelty. Do not apologize for it, over-explain it, or romanticize it. Treat the setting with a cold, documentary eye.
- **Dialogue Formatting**: Whenever the manuscript includes read-aloud text or direct spoken lines, use proper quotation marks and italicize the spoken words. For stand-alone spoken lines in scene text, prefer blockquote formatting, for example `> _"Saddle up."_`
- **Preserve all Markdown Structure**: Maintain all bullet lists, numbered lists, blockquotes, and tables exactly as they are architected. Rewrite the content inside the structures, but never flatten a list into a paragraph.
- **No Information Loss**: You are changing the tone, not the data. Every period price, named historical figure, date, and defined game term must survive the translation. Do not delete facts to achieve a sparser tone. Minimal removal of historical text—if you remove detail the reader may want, recover it.
- **1-to-1 Translation of Dictionaries/Lists**: When encountering a list of slang, items, or gear, translate each item on its own dedicated line.

## Structural Standard

The Montana supplement should mirror the usability of the New Mexico campaign chapter, but at full-book scale.

Core principle:

- `book-content/` is the book
- everything else exists to support the book

## Immediate Conventions

- the current opening chapter is [book-content/00-welcome-to-montana.md](/mnt/c/git-public/Tales-of-the-Old-West-2e/supplement-2-montana-campaign/book-content/00-welcome-to-montana.md)
- the former root-level manuscript file should not be used as the primary book file any longer
- future final chapters should be added under `book-content/` in sequence
