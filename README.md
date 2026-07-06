<!-- markdownlint-disable MD013 MD024 -->

# Tales of the Old West 2E

<div style="display: flex; width: 90%; gap: 1%; align-items: stretch;">
  <div style="flex: 1 1 0; aspect-ratio: 210 / 297; overflow: hidden;">
    <img src="01-corebook/00-cover.jpg" alt="Tales of the Old West 2E corebook cover" style="display: block; width: 100%; height: 100%; object-fit: cover; object-position: center top;">
  </div>
  <div style="flex: 1 1 0; aspect-ratio: 210 / 297; overflow: hidden;">
    <img src="02-the-1870s/00-cover.png" alt="Supplement 1: The 1870s cover" style="display: block; width: 100%; height: 100%; object-fit: cover; object-position: center top;">
  </div>
</div>

Unofficial manuscript set for _Tales of the Old West_ — a gritty tabletop
 RPG set on the American frontier of the 1870s.

This is a fan-made package for groups who want a sharper, more usable version
of the game: one complete corebook, one full setting supplement, and the skill
tools to keep new material in the same hard, western voice.

## What is in this repository

- `01-corebook/` — the complete player-facing game
- `02-the-1870s/` — the 1870s setting book with history, people, danger, and
  an example adventure
- `03-adventures/` — the standalone adventure domain, separate from the books
- `skills/western-writing/` — the prose and lore skill bundle
- `skills/yze-design/` — the master Year Zero Engine design skill for building new YZE games across any genre
- `CHANGELOG.md` — the version-by-version development record
- `LICENSE.md` — the rights and notice file for this repository

## The two books, and the adventures domain

### Book 01 — _Tales of the Old West_

The corebook carries the game forward as a full working rules volume. It keeps
the core loop tight, playable, and grounded in frontier pressure.

What this book brings:

- character creation and player-facing guidance
- the core dice engine and resolution procedures
- talents and special abilities
- conflict, damage, injuries, and recovery
- life in the Old West, including work, gear, and settlement pressure
- the west in the 1870s as a usable historical frame
- campaign tools, GM-facing guidance, and starter support
- the New Mexico campaign chapter
- the Patience Is a Virtue adventure
- outlaws, pursuit, and the shape of frontier trouble

### Book 02 — _Supplement 1: The 1870s_

The 1870s supplement turns the broader American West into a usable setting
book. It gives the table hard facts, hard choices, and the feel of a country
that can reward the wrong people.

What this book brings:

- peoples, conflict, and frontier social pressure
- Native cultures and borderlands context
- childhood, women, food, work, and material culture
- language, literacy, print, religion, and faith
- frontier survival, hunting, and the costs of travel
- availability, prices, towns, economy, law, and procedural detail
- cowboy life, horse culture, mining camps, and army life
- outlaw craft, gambling, music, entertainment, medicine, and death
- the dark frontier and regional landscapes
- a full example adventure: `The Yellowstone Line`
- appendix material for named NPCs and handouts

## The Adventures domain — `03-adventures/`

Adventures live in their own domain, not as chapters of either book. Each
entry is a complete, runnable campaign module with its own setting, cast,
and consequence tracks, built to stand alone or to hook into a wider
sandbox.

What this domain brings:

- `01-quiet-title.md` — _Quiet Title_, a northern New Mexico campaign set in
  the spring of `1873` in the Maxwell Land Grant country of the Sangre de
  Cristos. A dead federal surveyor, a hidden field book, and a quiet-title
  suit drive a fight over land, gold, a railroad right of way, and the
  eastern boundary of the grant itself.
- `01A-towns-trails-road-to-cimarron.md` — the sandbox companion:
  keyed gazetteers for San Esteban, Elizabethtown, and Cimarron, plus
  pointcrawl travel procedures, route timings, and encounter/event tables
  for the country between them.
- `01B-dramatis-personae-and-statblocks.md` — the expanded cast: full
  profiles, wants, needs, fears, and statblocks for every named figure and
  every generic profile in the campaign.
- `01C-handouts.md` — player-facing papers, notices, extracts, and
  field-book leaves sized for table use.
- `01D-historical-facts-and-authenticity.md` — the historian's treatise.
  Documents the real Maxwell Land Grant history the campaign is built on,
  the surveyor's trade, the plaza's life, the mercury in the creek, and the
  psychology of the operators, with an explicit ledger of what is invented
  and what is on the record.

## Why it matters

The point of the repository is simple: keep the game readable, keep the
setting sharp, and make new material feel like it belongs in the same hard,
dry country.

## AI and campaign work

This repository is built so a GM, designer, or AI agent can do more than read
it. The skill bundle helps you understand the game line, create new material
in the same register, and keep your own campaign consistent.

### Install the skills in another repository

If your agent supports repo-local skills, copy or symlink the desired folders
from this repository's `skills/` directory into your own local skill path.

Common workspace-local destinations are:

- `.github/skills/` for repo-scoped shared use
- `.agents/skills/` for repo-scoped agent workflows

Keep the folder names and each `SKILL.md` entry point intact.

Only carry over the skills you actually need:

- `western-writing`
- `western-rpg-design`
- `rpg-synergy-analysis`
- `rpg-balance-analysis`
- `adventure-writing`
- `yze-design`

### What each skill is for

| Skill | Use it for |
| --- | --- |
| `yze-design` | Build a new Year Zero Engine game for any genre; invent, transplant, and stress-validate mechanics from proven YZE primitives |
| `western-writing` | Final prose, rules voice, examples, flavor, and manuscript register |
| `western-rpg-design` | New rules, subsystems, procedures, and campaign mechanics |
| `rpg-synergy-analysis` | Balance stress-testing, dominant combos, loopholes, and exploit surfaces |
| `rpg-balance-analysis` | Balance and synergy catalogs for the West game line |
| `adventure-writing` | Adventure structure, plot, NPC design, and campaign framing |

### Recommended skill stacks

- **New YZE game for any genre:** `yze-design`
- **New region or campaign frame:** `western-writing` and `adventure-writing`
- **New subsystem or house rule:** `western-rpg-design` and `rpg-synergy-analysis`
- **Adventure or campaign material:** `adventure-writing` and `western-writing`

## License and notice

This repository is an unofficial project that references _Tales of the Old
West_, a tabletop roleplaying game created and published by Galloping Horse
Games.

This project is not affiliated with, sponsored by, or endorsed by Galloping
Horse Games.

Read `LICENSE.md` before publishing, distributing, or remixing material from
this repository.
