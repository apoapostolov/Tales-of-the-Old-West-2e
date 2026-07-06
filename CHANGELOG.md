<!-- markdownlint-disable MD013 MD024 -->

# Changelog

All notable changes to My big project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project follows Semantic Versioning.

## [Unreleased]

### Added

- **`yze-design` — master Year Zero Engine design skill.** A comprehensive engine-agnostic design system for the Year Zero Engine (YZE) by Free League Publishing. Reverse-engineers Forbidden Lands 2E and Tales of the Old West 2E into a unified three-layer design toolkit:
  - **UNDERSTAND** — core resolution, character, conflict, harm, power, travel, organizations, gear, GM procedures, philosophy, design dials, and a complete FL-vs-West divergence map.
  - **INVENT** — 15 reusable mechanical primitives, a dual-use matrix showing how each primitive produces opposite player psychologies at different calibrations, and a 5-operator reinvention method for transplanting primitives into new systems (Domain Transfer, Inversion, Recalibration, Fusion, Abstraction-Climb).
  - **VALIDATE** — an executable balance and synergy pipeline (expected-success math, attrition curves, exploit taxonomy, synergy stress-testing) plus a player-psychology layer (loss aversion, flow, perceived randomness, the abstraction-authenticity dial) and an integrating review protocol.
  - Use it to build a new YZE game for any genre, invent rules from proven primitives, or stress-validate either for math and table feel.

- **`03-adventures/` domain.** Adventures now live in their own folder,
  separate from the two books, so a campaign module is not filed as a
  chapter of a setting or rules volume.
  - `03-adventures/01-quiet-title.md` — _Quiet Title_, a standalone northern
    New Mexico campaign set in the spring of `1873`. The plaza of San
    Esteban sits inside the Maxwell Land Grant boundary as the foreign-backed
    grant company draws it, and a dead federal surveyor's hidden field book
    is the lever that can break a quiet-title suit, free the Baldy Mountain
    gold diggings, or be sold to a railroad that only wants a clean right of
    way. The module carries a four-track consequence ledger, a full cast with
    statblocks, a fully written opening arc (the plaza, the supper, the
    willows killing, the night raid), and written arcs through the gold
    camp, the cañón, and the Cimarron hearing.
  - `03-adventures/01A-towns-trails-road-to-cimarron.md` — the
    sandbox companion for _Quiet Title_: keyed gazetteers for San Esteban,
    Elizabethtown, and Cimarron, plus pointcrawl travel procedures, route
    timings, and encounter/event tables for both settlement pressure and the
    country between nodes.
  - `03-adventures/01B-dramatis-personae-and-statblocks.md` — the expanded
    cast for _Quiet Title_: backstory, wants, needs, fears, and how-to-play
    notes for every named NPC, plus statblocks and generic profiles for the
    chapter's muscle (Company riders, chainmen, Elizabethtown toughs, plaza
    hands, Jicarilla scouts, Pinkerton men).
  - `03-adventures/01C-handouts.md` — a player-facing handout appendix for
    _Quiet Title_, including notices, ledger extracts, register excerpts,
    field-book leaves, letters, and other study-worthy papers sized for use
    at the table.
  - `03-adventures/01D-historical-facts-and-authenticity.md` — the historian's
    treatise for _Quiet Title_. Documents the real Maxwell Land Grant history
    the campaign is built on (the `1841` grant, the `1870` syndicate sale,
    the eastern-boundary survey fraud, the Santa Fe Ring, the `1887` Supreme
    Court decision), the GLO deputy-surveyor's trade, the Hispano plaza and
    the acequia, the mercury amalgamation poisoning the gold camp, and the
    psychology of the operators, with an explicit ledger separating the
    invented characters from the real history they stand in for.

### Changed

- Moved the adventure previously drafted as `02-the-1870s/27-quiet-title.md`
  into the new `03-adventures/` domain and renumbered it `01-quiet-title.md`.
  It was never committed under the old path.

## [1.0] - 2026-04-27

This first release replaces the loose `Unreleased` bucket with a real versioned
record. It locks in the two-book manuscript set, the western-writing skill
bundle, and the repo structure that supports both.

### Added

- **`Tales of the Old West`.** The corebook is now a complete player-facing
  volume instead of a loose set of chapters.
  - `01-welcome-to-the-old-west.md` — the introduction and tone-setting opening
  - `02-your-player-character.md` — character creation and player-facing setup
  - `03-rolling-the-bones.md` — core dice, checks, and resolution
  - `04-talents.md` — talents and special abilities
  - `05-conflict-and-damage.md` — conflict, damage, injuries, and recovery
  - `06-life-in-the-old-west.md` — work, property, gear, settlement life, and
    daily pressure
  - `07-the-west-in-the-1870s.md` — the historical frame and period context
  - `08-campaigns-in-the-old-west.md` — GM tools and campaign structure
  - `09-the-new-mexico-campaign.md` — the New Mexico campaign chapter
  - `10-patience-is-a-virtue.md` — the adventure module
  - `11-outlaws-of-the-old-west.md` — outlaw play and frontier crime
  - `00-cover.jpg` — cover art for the volume

- **`Supplement 1: The 1870s`.** The setting supplement now reads as a full
  manuscript book with an example adventure and support appendices.
  - `00-introduction.md` — setting introduction and editorial framing
  - `01-peoples-and-conflict.md` through `05-women.md` — peoples, conflict,
    Native cultures, borderlands, childhood, and women in the frontier West
  - `06-food-and-drink.md` through `11-frontier-survival-and-hunt.md` — daily
    life, work, material culture, literacy, religion, and survival
  - `12-availability.md` through `15-competence-and-procedures.md` —
    availability, prices, towns, law, and practical procedure
  - `16-cowboy-life.md` through `19-army-life.md` — cowboy life, horse culture,
    mining camps, and army life
  - `20-outlaw-craft.md` through `22-music-and-entertainment.md` — outlaw
    craft, gambling, and music and entertainment
  - `23-medicine-and-death.md` through `25-regional-landscapes.md` — medicine,
    death, the dark frontier, and regional landscapes
  - `26-the-yellowstone-line.md` — the example adventure chapter
  - `26A-dramatis-personae-and-statblocks.md` — named NPCs and generic
    statblocks
  - `26B-handouts-and-clues.md` — handouts, clue carriers, and table props
  - `illustration-prompts.md` — prompt pack support for the book
  - `00-cover.png` — cover art for the supplement

- **`western-writing`.** The repo-local skill bundle for voice, history, and
  editorial consistency.
  - prose guidance for the western manuscript line
  - lore and historical grounding support
  - atmospheric scene and example-text guidance
  - cleanup and style notes for western RPG copy

- **Repository layout cleanup.**
  - added the `01-corebook/` and `02-the-1870s/` book structure
  - documented the repo as a two-book project
  - replaced the old loose `Unreleased` release-note approach
