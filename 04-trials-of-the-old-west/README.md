<!-- markdownlint-disable MD013 MD024 -->

# Trials of the Old West

A mechanics expansion for _Tales of the Old West 2E_. Floating chapters
that fill the gaps the corebook and the 1870s supplement leave open,
built from the engine the game already has.

## What is in this directory

### Front matter

- `00-introduction.md` — what this book is, what it brings, how to use it
- `/docs/vignettes-and-cast.md` — the recurring ensemble whose vignettes open
  the chapters and whose voices carry every example

### Part I — Person and Scene

- `01-the-standoff.md` — the multi-party pre-shootout; who breaks first, the door into the fight
- `02-the-holdout.md` — the PC-scale homestead and cabin siege; the defense track and the dawn

### Part II — Hearth and Trade

- `03-sickness-and-the-fever.md` — the diseases of the West as a spreading pressure; the outbreak as operation
- `04-saloons-and-the-trade.md` — the saloon and brothel as seasonal enterprise; the house gauge, the keeper's trouble
- `05-running-trade-and-resources.md` — the spatial economy; freighting, the supply run, the iron horse as commerce
- `06-cattle-drives.md` — the drive as operation, the stampede, the ranch as business
- `07-mining-claims.md` — prospecting, the claim, the working mine, the company and the union
- `08-logging-fur-trade-and-hunting.md` — the wild land's extractive trades; the river drive, the trapline, the market hunt
- `09-banking-and-the-vault.md` — the bank job as operation; deposits, the safe-crack, the bank run

### Part III — Crime and the Law

- `10-train-robbery.md` — the iron horse as score; the anatomy, the stop, the railroad as a faction
- `11-justice-trial-incarceration.md` — the law's grip; the trial, the sentence, the jail, the rope
- `12-atrocities-and-human-trade.md` — the atrocity as operation; the trades in people; the army and the Committee at their worst

### Part IV — The County

- `13-factions-and-standing.md` — the Standing engine and the Faction Roll that makes the world act on its own
- `14-families-and-feuds.md` — designing families; nationalities, trait tags, properties, the Feud Clock, the family events (wedding, funeral, church), and the Generational Clock
- `15-inheritance-land-office-and-speculation.md` — the paper war; the land office, the probate, insurance, speculation
- `16-the-wire.md` — the telegraph as a mechanical system; cost, speed, cutting, the wire-down condition
- `17-mail-and-the-post.md` — the U.S. Mail as routes, cargo, score, and vocation; the star-route contract
- `18-the-press-and-the-election.md` — the press as faction instrument; the election as multi-session operation

### Part V — The Wild Country

- `19-weather-and-the-trail.md` — a regional weather generator and three disaster operations, plus the drought
- `20-deep-wild-land-exploration.md` — river, forest, and mountain as three modes of wilderness travel
- `21-regional-encounter-tables.md` — states grouped by terrain and temper; shared D66 encounter tables
- `22-winter-and-wintering.md` — winter as the season of scarcity; the count, the attrition, the spring thaw

### Part VI — The Nation and the Decade

- `23-mass-combat.md` — unit-scale skirmishes, attached player characters, the battle as operation
- `24-robber-barons-and-their-work.md` — the great operators; the baron as faction, the work table, historical profiles
- `25-the-political-scene-of-the-1870s.md` — the national party layer; the acts, the year-by-year metaplot timeline

### Scaffolded (in development)

The remaining situational gaps await development when a campaign calls
for them: the deep exploration of specific river systems (the Missouri,
the Colorado), the survey party as operation, the doctor as a business,
the bounty-hunter vocation, and the holiday and festival calendar. Each
has its raw material already written in the corebook and the 1870s
supplement; the work is conversion, not invention.

## Where the engine understanding lives

`/docs/design-bible.md` (at the repository root) is the agnostic
engineering spec behind this book: the gauge catalog, the resolution
vocabulary, the table formats, the downtime spine, and the integration
map. Read it first if you intend to extend, audit, or build alongside
this book.

## How the chapters relate

The chapters are written to be read in order, but each is a complete
subsystem that can stand alone. The dependency order of the core set is:

The book is organized into six parts, by the scope of the pressure each
addresses — from the single tense moment, through the hearth and the
work, through crime and the law, through the county's web, out into the
wild country, and up to the nation. Within each part the chapters lean
on one another, but any chapter can stand alone.

- **Factions (Ch.13)** is the one to read early, even though it sits in
  Part IV. Half the book reaches for it — crime, the county, the nation.
- **The operation engine** (Progress-versus-Trouble, from the outlaw
  chapter of the corebook) is the frame most chapters build on: the
  drive, the robbery, the trial, the outbreak, the holdout, the battle.
- **The season and the town** (corebook Ch.8) is where the long arc
  lives; most seasonal enterprises (Ch.4–9) and the Winter Quarter
  (Ch.22) resolve there.
- **Crime (Part III) feeds the law**: train robbery and the atrocity
  produce the `Wanted` that the trial and the rope (Ch.11) answer.
- **The county (Part IV) is the social layer** above the individual and
  below the nation — factions, families, paper, the wire, the mail, the
  press.
- **The nation (Part VI) is the weather** the county sits in — mass
  combat resolves the wars, the robber barons press from above, and the
  political scene sets the decade's climate.

## Design discipline

This book invents no new resolution mechanic and no new gauge size. It
is recombination of the corebook's existing pieces: the success ladder,
the Progress-versus-Trouble operation track, the engine's integer
gauges, the modifier cap, and the D66 tables with their Calamity and
Jackpot conventions. All prose is written through the `western-writing`
and `western-rpg-design` skills. See `/docs/design-bible.md` for the
full specification.
