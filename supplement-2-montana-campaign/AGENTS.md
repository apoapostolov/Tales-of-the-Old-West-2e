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

## Settlement Depth Standard

Use the New Mexico campaign chapter as the benchmark for what settlement material must actually carry. A Montana settlement entry is too thin if it only names a place, lists a few offices, and drops a hook or two. The book needs local pressure that can survive table play.

### Content types that must be expanded

- Opening description: state terrain, economy, transport, settlement origin, and current pressure in concrete prose.
- Historical setup: include how the place began and why it became what it is now, not just a founding date.
- Power map: identify the visible local blocs, their leaders, and what each one controls.
- Civic offices: name the officeholders or closest real authorities, and show why they matter.
- Notable people: give each person role, social position, affiliation, leverage, want, need, fear, and at least one useful relationship.
- Hooks and adventures: include setup, complication, escalation, and consequence; do not stop at premise.
- Standalone seeds: make them actionable, not atmospheric. A seed should point to a scene, suspect, route, object, or decision.
- Neighboring nodes: settlements are rarely isolated. Show the nearby farms, forts, crossings, stations, and road links that shape the place.
- Amenities: each item should be tied to a real date, a season, and a settlement function. Avoid bare lists.
- Settlements under faction pressure: show how outside forces change the town, not just who is present there.
- Travel network: every settlement must be placed in a readable travel web with distance and time to nearby nodes.

### Minimum depth by tier

- Primary settlements: `3-4` substantial opening paragraphs, `10-12` notable people, `3` campaign adventures, `3` standalone tales, and `6-8` usable seeds or rumors.
- Secondary settlements: `2-3` strong opening paragraphs, `3-5` notable people, `2` hooks or short adventures, and `2-4` usable seeds or rumors.
- Tertiary settlements: `1-2` strong paragraphs, `1-3` named people or households, and `1-2` concrete hooks, threats, or reasons the site matters.

### Quality standards

- No settlement element should be reduced to a label when it needs explanation.
- No people entry should stop at a name and role if the person is expected to matter in play.
- No hook should remain at premise level if the place is meant to be playable.
- No town should feel interchangeable with another; the material must show what makes it economically, politically, and socially distinct.
- If a paragraph does not change what the GM can do at the table, it is probably too short.

### Word Floor Standard

Use the New Mexico chapter as the baseline, then write Montana at a higher density because the target product is a full 200-300 page sandbox book.

Measured New Mexico reference points:

- full chapter: about `17,000` words
- flagship town entries: about `2,900-4,100` words each
- endgame package: about `1,000` words
- real-town gazetteer entries: about `250-400` words each

Montana minimums should exceed those floors.

#### Primary settlements

- Total entry length: `4,500-7,000` words minimum.
- Opening description and historical setup: `350-600` words.
- Power map and local pressure: `250-450` words.
- Civic offices and statblock interpretation: `150-250` words.
- Neighboring nodes and local orbit: `150-300` words.
- Notable people roster: `1,000-1,800` words total, with `90-150` words per major NPC.
- Three campaign adventures: `300-500` words each.
- Three standalone tales or seeds: `150-250` words each.

#### Secondary settlements

- Total entry length: `1,600-2,800` words minimum.
- Opening description and historical setup: `220-380` words.
- Power map and pressure summary: `150-280` words.
- Civic offices and statblock interpretation: `100-180` words.
- Nearby nodes and transport links: `80-180` words.
- Notable people roster: `260-600` words total, with `80-130` words per person.
- Two hooks, short adventures, or one hook plus one complication track: `180-350` words each.
- Additional seeds or rumors: `120-300` words total.

#### Tertiary settlements

- Total entry length: `450-1,100` words minimum.
- Opening description and historical setup: `120-220` words.
- Site pressure or why it matters: `80-180` words.
- Owner / operator / household / garrison notes: `60-180` words total.
- Hooks, dangers, or local complications: `80-220` words total.
- Amenities, if used, still need dates and functions; do not let the table replace the prose.

#### Tertiary special cases

- Farms and ranch clusters: keep the owner table and amenity table, but still provide enough prose to show labor pattern, market dependence, vulnerability, and local conflict.
- Small villages: if they have a real statblock, they need at least one paragraph of local history and one paragraph of pressure beyond the table.
- Military posts, ferries, road stations, and agency-adjacent sites: they may omit a people roster if the site function is stronger than any one person, but they still need a clear operational role, current pressure, and at least `2` usable complications.

#### Element-level floor rules

- Description paragraphs must do more than identify the place; they must carry terrain, economy, transport, and conflict.
- Notable people entries must not be label-only. Each one needs role, leverage, want, need, fear, and at least one useful relationship or pressure point.
- Hooks must be playable from the page. Each hook needs enough words to show the setup, the immediate friction, and the likely consequence.
- Seeds can be shorter than hooks, but they must still point at a scene, a suspect, a route, an object, or a decision.
- Adventures need enough room for a setup, a starting action, and a finale. If a planned adventure cannot reach that shape, it is not ready.
- Amenities need enough description to show why they matter in the settlement’s growth, not just what was built.
- Faction and neighbor notes need enough detail to show movement across the map, not just who is present.

### Travel Network Rule

This is mandatory for every settlement chapter and settlement file.

- Every primary settlement chapter must include a `Settlement Web` mind map in plain text or ASCII showing the chapter hub, its secondary settlements, and its tertiary settlements.
- Every primary and secondary settlement must include distance and fair-weather travel time to its nearest primary hub or regional center.
- Every secondary settlement must also include distance and travel time to at least `1` nearby tertiary node or neighboring secondary node.
- Every tertiary settlement, farm cluster, military post, ferry, or small community must include distance and travel time to at least `1` nearby primary or secondary settlement.
- Use both `horseback` and `wagon` times when roads exist. If wagon travel is unrealistic, say so plainly.
- Add a short seasonal caution where mud, snow, river height, or military danger can materially change travel time.
- Do not hide travel information in prose alone. Use a dedicated travel table, ledger, or compact travel note the reader can scan quickly.
- Distances may be approximate if the chapter says they are route distances rather than survey-perfect measurements.

## Immediate Conventions

- the current opening chapter is [book-content/00-welcome-to-montana.md](/mnt/c/git-public/Tales-of-the-Old-West-2e/supplement-2-montana-campaign/book-content/00-welcome-to-montana.md)
- the former root-level manuscript file should not be used as the primary book file any longer
- future final chapters should be added under `book-content/` in sequence
