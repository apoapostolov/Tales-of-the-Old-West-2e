<!-- markdownlint-disable MD013 MD041 -->

# Procedural Redesign Proposals

> **The problem.** Book 4 has 26 chapters, but they share one mechanic too
> often: the **Progress-vs-Trouble Operation** (the outlaw score frame).
> A bank robbery, a season of ranching, a political campaign, a winter,
> and a feud all resolve the same way mechanically, which flattens them.
> The GM cannot *feel* the difference between running a saloon, fighting
> an election, and surviving the blizzard, because the engine treats them
> as the same shape of scene.
>
> **The goal.** Give each chapter a procedural subsystem that fits its
> subject, so different encounter types *feel* like different systems.
> More complex subjects (business, politics, factions) get more dials;
> simpler ones (the standoff, the wire) stay light. The YZE design skill
> supplies the vocabulary: the **org lifecycle** (founding → functions →
> upkeep → events → scale), the **Influence/decay pool**, the **faction
> relationship web**, **Social Combat** (Composure + leverage + distance
> + audience), **resource dice**, **activity menus**, and the
> **reinvention operators** that transplant these primitives into new
> domains.

## How to read these proposals

Each Part has one file. Each chapter within it gets a proposal with:

- **The current weakness** — what feels flat or repetitive.
- **The proposed system** — the procedural flow or subsystem, with its
  dials and stages. Named after the YZE primitive it is built from.
- **Why it fits** — the design intent and the felt experience it produces.
- **Complexity rating** — light / medium / heavy, by how much the subject
  warrants. Not every chapter needs a heavy system; some should stay
  light. The point is *variety*, not uniform depth.

## The proposals

- `part-i-person-and-scene.md` — Ch.1 Standoff, Ch.2 Holdout
- `part-ii-hearth-and-trade.md` — Ch.3–10 (the business/economy core, the heaviest redesign)
- `part-iii-crime-and-the-law.md` — Ch.11 Train Robbery, Ch.12 Justice, Ch.13 Atrocities
- `part-iv-the-county.md` — Ch.14–19 (factions, families, paper, comms, press/election — the political layer)
- `part-v-the-wild-country.md` — Ch.20–23 (weather, wild land, encounters, winter)
- `part-vi-the-nation-and-the-decade.md` — Ch.24–26 (mass combat, barons, the political scene)

## A note on the primitives

The proposals draw on these YZE workshop modules and engine primitives.
Each is summarized in the design bible (`/docs/design-bible.md`); full
detail lives in the `skills/yze-design/` skill.

- **Org lifecycle** (`yze-design/references/07`) — founding → functions
  → upkeep → events → scale. The shape every business, base, and band
  should follow.
- **Influence / decay pool** (`yze-design/workshop/01`) — spendable
  standing that *decays* if not cultivated, with scandals as the
  bane-equivalent. The model for political capital and faction regard.
- **Faction relationship web** (`yze-design/workshop/02`) — a graph of
  bonds and debts between factions, with propagation (helping A warms
  A's allies and chills A's enemies) and callable debts. The model for
  the faction and family chapters.
- **Social Combat** (`yze-design/workshop/03`) — full tactical social
  conflict: action economy, social-distance range bands, leverage as
  consumable weapon-dice, Composure as social HP, a Broken-equivalent
  Fallout table. The model for trials, elections, sermons, and any
  high-stakes persuasion.
- **Resource dice** (`yze-design/references/16` P5) — the stepped die
  (D6→D12) that depletes on a 1–2. Already in the corebook for
  consumables; the proposals extend it to feed, fuel, morale, and take.
- **Activity menus** (`yze-design/references/16` P6) — the downtime
  choice list (each PC picks one action per cycle). The model for the
  season and the winter quarter.

The proposals do not require the GM to learn all of these. Each chapter
takes the *one* primitive it needs and discards the rest, so a table
running only the ranch chapter never sees the faction web, and a table
running only the election never sees a resource die.
