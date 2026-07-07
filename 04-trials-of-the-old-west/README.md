<!-- markdownlint-disable MD013 MD024 -->

# Trials of the Old West

A mechanics expansion for _Tales of the Old West 2E_. Floating chapters
that fill the gaps the corebook and the 1870s supplement leave open,
built from the engine the game already has.

## What is in this directory

### Core chapters (drafted)

- `01-introduction.md` — what this book is, what it brings, how to use it
- `vignettes-and-cast.md` — the recurring ensemble whose vignettes open
  the chapters and whose voices carry every example
- `02-factions-and-standing.md` — the Standing engine and the Faction
  Roll that makes the world act on its own
- `03-weather-and-the-trail.md` — a regional weather generator and three
  disaster operations (blizzard, fire, flood) plus the drought
- `04-justice-trial-incarceration.md` — the law's grip, closing the loop
  the outlaw chapter's `Wanted` opens
- `05-train-robbery.md` — the iron horse as score and setpiece, with the
  railroad as a faction that remembers
- `06-cattle-drives.md` — the drive as operation, the stampede, the
  ranch as seasonal enterprise
- `07-mining-claims.md` — prospecting, the claim, the working mine, the
  company and the union
- `08-mass-combat.md` — unit-scale skirmishes, attached player
  characters, the battle as operation
- `09-running-trade-and-resources.md` — moving goods across distance as
  a livelihood; the freighting outfit, the supply run, the iron horse as
  commerce, the railhead as trade hub
- `10-saloons-and-the-trade.md` — the saloon and brothel as seasonal
  enterprise; the keeper, the girls, the games, the trouble
- `11-sickness-and-the-fever.md` — the diseases of the West as a pressure
  on characters, camps, towns, and drives
- `12-families-and-feuds.md` — designing families, their nationalities,
  their traits, their properties, and the feuds and allegiances that
  bind them
- `13-robber-barons-and-their-work.md` — the great operators of the
  period and the jobs and opportunities they offer a party
- `14-atrocities-and-human-trade.md` — marauding, captive-taking, and the
  trade in people, as outlaw operations and as the setting's hard truth

### Scaffolded (in development)

- `15-the-standoff.md` — the multi-party pre-shootout tension scene;
  who breaks first, who backs down, the door into the fight
- `16-the-wire.md` — the telegraph as a mechanical system; cost, speed,
  cutting, interception, the wire-down condition
- `17-mail-and-the-post.md` — the U.S. Mail as routes, cargo, score, and
  vocation; the star-route contract as a faction lever
- `18-banking-and-the-vault.md` — the bank job as operation; deposits,
  safekeeping, the time-lock, the vault, the bank run
- `19-weddings-funerals-and-the-church.md` — the ceremonial scenes; the
  wedding as alliance, the funeral as accounting, the revival as event
- `20-the-holdout.md` — the PC-scale homestead and cabin siege; the
  defense track, the assault tactics, the dawn
- `21-winter-and-wintering.md` — winter as the season of scarcity; the
  provisions/fuel/feed attrition, the spring-thaw resolution

## Where the engine understanding lives

`/docs/design-bible.md` (at the repository root) is the agnostic
engineering spec behind this book: the gauge catalog, the resolution
vocabulary, the table formats, the downtime spine, and the integration
map. Read it first if you intend to extend, audit, or build alongside
this book.

## How the chapters relate

The chapters are written to be read in order, but each is a complete
subsystem that can stand alone. The dependency order of the core set is:

```
Ch.2 Factions ──► Ch.4 Justice ──► Ch.8 Mass Combat
                  Ch.5 Train Robbery
Ch.3 Weather ──►  Ch.6 Cattle Drives
                  Ch.7 Mining Claims
```

- **Factions (Ch.2)** is foundational. Justice, Mass Combat, Mining, and
  Cattle Drives all reference Standing and the Faction Roll.
- **Weather (Ch.3)** is cross-cutting. It touches travel, drives,
  campaigns, and any scene in the open.
- **Justice (Ch.4)** and **Train Robbery (Ch.5)** are the crime-and-law
  spine, fed by the outlaw chapter of the corebook.
- **Cattle Drives (Ch.6)** and **Mining (Ch.7)** are the economic pair,
  built on the corebook's business-outfit rules.
- **Mass Combat (Ch.8)** consumes factions, weather, morale, and the
  operation framework — read it last.

The in-development chapters will lean on Factions (Ch.2), the season
rules, and the outlaw operation framework, in roughly that order.

## Design discipline

This book invents no new resolution mechanic and no new gauge size. It
is recombination of the corebook's existing pieces: the success ladder,
the Progress-versus-Trouble operation track, the engine's integer
gauges, the modifier cap, and the D66 tables with their Calamity and
Jackpot conventions. All prose is written through the `western-writing`
and `western-rpg-design` skills. See `/docs/design-bible.md` for the
full specification.
