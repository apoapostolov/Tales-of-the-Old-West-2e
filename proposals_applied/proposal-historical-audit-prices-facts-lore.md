# Proposal: Historical Audit of Prices, Facts, and Lore

**Status:** Draft proposal  
**Target:** `Tales of the Old West 2e` manuscript  
**Scope:** price anchors, period availability, factual flavor, and lore wording  
**Primary local sources:**  
- `skills/western-writing/knowledge/prices-and-anchors.md`  
- `skills/western-writing/knowledge/1870s-availability.md`  
- `skills/western-writing/knowledge/material-culture.md`  
- `skills/western-writing/knowledge/towns-economy-law.md`  
- `skills/western-writing/knowledge/documents-and-print.md`  
- `skills/western-writing/knowledge/horse-culture.md`  
- `skills/western-writing/knowledge/medicine-and-death.md`  
- `skills/western-writing/knowledge/borderlands.md`  
- `skills/western-writing/knowledge/peoples-and-conflict.md`

**Selective external checks:**  
- NPS `1870 Catalogue of Goods`  
- Union Pacific early passenger fares (`June 24, 1870` timetable notes)

## Purpose

The manuscript is already strong in broad western tone. The problems are mostly not tone problems. They are anchor problems.

The main risks are:

- prices that are too high or too low for the 1870s by a large margin
- gear entries that quietly slide across the decade line
- descriptive text that is true for the later 1870s but too broad for a game framed around `1873`
- a few lore sentences that flatten Mexican and borderland realities too much
- horse and outlaw economy text that mixes different market contexts without saying so

This proposal identifies the places where the manuscript should be corrected, and separates them from places where the current abstraction is still defensible.

## Audit Stance

The standard should be:

- correct the hard factual errors
- preserve abstraction where the rule needs it
- distinguish early-`1873` reality from late-`1870s` myth when necessary
- avoid replacing one error with over-specific museum prose

In other words, the game does not need to become a catalogue. But where it names a number, a gun, a service, or a historical relationship, that anchor should pull in the right direction.

## Summary of Highest-Priority Corrections

The most urgent fixes are:

1. `corebook/06-life-in-the-old-west.md` basic services table: several prices are materially off.
2. `corebook/06-life-in-the-old-west.md` firearms table: the `Deringer` and `Colt 45 Peacemaker` prices are inflated, and some availability wording is too broad for `1873`.
3. `corebook/06-life-in-the-old-west.md` firearm flavor text: the `Sharps Rifle 1874` note is chronologically wrong.
4. `corebook/11-outlaws-of-the-old-west.md` horse-price guidance mixes retail-town and range-country markets and should be separated.
5. `corebook/01-welcome-to-the-old-west.md` chapter-1 wording about Mexicans being “mollified” by U.S. policy should be rewritten.

## Detailed Findings

## 1. Prices and Services

### 1.1 Basic services table needs correction

**Location:** `corebook/06-life-in-the-old-west.md:622-645`

These are the clearest hard mismatches in the manuscript.

| Entry | Current | Better historical anchor | Basis |
| --- | --- | --- | --- |
| `Barbering` | `$2` | split into `Haircut 25c`, `Shave 10c`, `Bath 25c` | `towns-economy-law.md:251` |
| `Coffee, 1 cup` | `25c` | `5c` | `prices-and-anchors.md:203-204` |
| `Stabling costs` | `25c/day` | `50c-$1/day`, or `75c-$1.50` with feed | `prices-and-anchors.md:269-272`, `towns-economy-law.md:188-193` |
| `Undertaking services` | `$10+` | more like `$25-$100` depending on town and ceremony | `prices-and-anchors.md` funeral anchor |

**Recommendation:**

- Replace `Barbering` with three separate entries.
- Reduce `Coffee, 1 cup` to `5c`.
- Raise `Stabling costs` to at least `50c/day`, and consider a second line for `stall + feed`.
- Raise `Undertaking services` to a broader range.

### 1.2 Railroad fare is too high as a default line item

**Location:** `corebook/06-life-in-the-old-west.md:639`

`Railroad, coast to coast $300` is too high as the default rulebook anchor.

The `June 24, 1870` Union Pacific timetable notes show `New York to San Francisco` at:

- `first class $136`
- `second class $110`
- immigrant / lower class passage substantially below that depending on route and class

**Recommendation:**

Replace the single line with a range, for example:

- `Railroad, transcontinental emigrant passage $65-$110`
- `Railroad, transcontinental first class $135-$150`

If the design wants one simple line only, a better broad anchor is roughly `$110-$150`, not `$300`.

### 1.3 Stagecoach fare is defensible

**Location:** `corebook/06-life-in-the-old-west.md:641`

`Stagecoach ticket 10c/mile` is not a problem.

Short western and overland stage fares are commonly anchored at `10-15 cents per mile`.

**Recommendation:** keep as is.

### 1.4 Some prices are already correct or close enough

The following entries are basically sound:

- `Homestead Act filing fee $14`
- `Meal, basic 25c`
- `Whiskey in single-bit bar 10c`
- `Whiskey in two-bit bar 25c`
- `Beer 10c` is a little high against the common `5c` schooner, but still plausible for bottled beer, a dearer house, or a town with weak supply

**Recommendation:** no immediate change needed except perhaps a note that `Beer 5-10c` better reflects range by place.

## 2. Commodity and Gear Price Anchors

### 2.1 Whiskey bottle prices are too low

**Location:** `corebook/06-life-in-the-old-west.md:592-593`

Current:

- `Whiskey, sipping (bottle) 50c`
- `Whiskey, good (bottle) $2`

Local anchors are closer to:

- rotgut bottle: `$1-$2`
- decent / bonded bottle: `$3-$5`

**Recommendation:**

Replace with something like:

- `Whiskey, rough bottle $1-$2`
- `Whiskey, decent bottle $2-$3`
- `Whiskey, bonded / named bottle $3-$5`

`50c` is too low for the bottle line as written.

### 2.2 Deringer price is badly inflated

**Location:** `corebook/06-life-in-the-old-west.md:746`

Current:

- `Deringer ... $32`

That is far above the normal anchor for a common Remington Double Derringer style pocket pistol, which is closer to `about $5-$8`.

**Recommendation:**

- Drop the common derringer price sharply.
- If the design wants a very expensive concealed pistol, make that a deluxe engraved or imported variant, not the default row.

### 2.3 Colt 45 Peacemaker price is too high for the default anchor

**Location:** `corebook/06-life-in-the-old-west.md:737`

Current:

- `Colt 45 Peacemaker ... $28`

Local material-culture guidance places the retail price closer to `about $17 in 1873`.

This does not mean the game must use `$17` exactly. Frontier markup exists. But `$28` is too high as the table’s ordinary anchor before scarcity modifiers.

**Recommendation:**

- Move the base price down into roughly `$17-$22`
- let `Rarity`, scarcity, and market conditions push it upward when appropriate

## 3. Firearms, Chronology, and Availability

### 3.1 The book needs firmer `1873` year-sensitivity

**Core issue:** the manuscript often talks about “the 1870s” broadly while chapter 1 frames the game very specifically around `1873`.

That matters for:

- `Colt Single Action Army`
- `Winchester Model 1873`
- `Sharps Model 1874`
- later-decade reputation claims

### 3.2 Colt 45 flavor text overstates early-decade dominance

**Location:** `corebook/06-life-in-the-old-west.md:753-754`

Current text says the Peacemaker is “perhaps the most commonly used weapon in the Old West of the 1870s.”

That is too broad for a game anchored to `1873`. In `1873` it is new. By `1875` and after, the claim becomes much more defensible.

**Recommendation:**

Rewrite along these lines:

> Introduced in `1873`, the Colt Single Action Army quickly became one of the defining revolvers of the later `1870s` West, especially among soldiers, lawmen, and men who could afford a modern cartridge arm.

### 3.3 Smith & Wesson Model 3 text conflicts with its own rarity logic

**Location:** `corebook/06-life-in-the-old-west.md:743`, `765-766`

Current table:

- `Smith & Wesson Model 3 ... Rare`

Current flavor:

- “It’s readily available in the Old West.”

Those two statements are pulling against each other.

The historical reality is more nuanced:

- important
- modern
- admired
- present in the West
- but not “readily available” in all rough towns, especially in the early `1870s`

**Recommendation:**

Rewrite to match the table, for example:

> The Model 3 is a modern cartridge revolver prized by officers, lawmen, gamblers, and well-heeled gunmen. It is present in the West, but in `1873` it is still a dearer and less common sight than older percussion arms.

### 3.4 Sharps 1874 note is chronologically wrong

**Location:** `corebook/06-life-in-the-old-west.md:793`

Current:

- “The 1874 model was first produced in 1871.”

This is simply wrong.

The `Sharps Model 1874` is a `1874` model. Earlier Sharps rifles existed long before that, but this exact line should not date the `1874` pattern to `1871`.

**Recommendation:**

Rewrite along these lines:

> Sharps rifles had existed for years before, but the `Model 1874` became one of the signature buffalo rifles of the great hide hunts.

### 3.5 `Deringer` / `Derringer` naming should be cleaned up

**Location:** `corebook/06-life-in-the-old-west.md:746`, `771`

Current text says:

- `Deringer`
- “sometimes mis-spelled Derringer”

This is backwards for modern reader recognition and awkward for a generic game table. The common generic form is `Derringer`, while `Deringer` properly refers to the original maker Henry Deringer.

**Recommendation:**

- Use `Derringer` in the table and generic prose
- if desired, note once that the generic name ultimately comes from Henry Deringer

### 3.6 Wells Fargo coachgun flavor is overstated

**Location:** `corebook/06-life-in-the-old-west.md:807`

“ubiquitous across the West” is too broad.

The better flavor is:

- known
- iconic
- associated with express and stage defense
- but not literally everywhere

**Recommendation:**

Tone this down and consider foregrounding the period term `messenger's gun`.

## 4. Horse Culture and the Outlaw Economy

### 4.1 The horse-price section mixes separate markets

**Location:** `corebook/11-outlaws-of-the-old-west.md:217-227`

This section currently blends:

- broken mustang / rough country stock
- town retail horse market
- military remount logic
- elite or specialist saddle stock

The result is not all wrong, but it is muddy.

The strongest mismatch is:

- `rough mustang, mixed trail horse, or tired remount $80-$120`

That is too high for the “broken mustang” end of the market. Local horse-culture guidance puts:

- broken mustang: `about $10-$25`
- top cow horse: `about $50-$100`
- cavalry remount contract horse: `about $100-$150`

At the same time, the NPS `1870 Catalogue of Goods` gives:

- average work horse: `$150`
- good saddle horse: `$200`
- saddle: `$30`

So the manuscript is not uniformly wrong. It is mixing retail-town and country-trade contexts.

**Recommendation:**

Split the guidance into two subcontexts:

### Country / stolen / mustang market

- broken mustang or rough remount: `$10-$40`
- useful trail or cow horse: `$40-$100`

### Town retail / respectable purchase

- average work horse: `$125-$150`
- good saddle horse: `$175-$200`
- prime trained stock: `$225+`

That will preserve both the rough-country reality and the catalog-town reality.

### 4.2 The “prime stock” line uses a weak classification scheme

**Location:** `corebook/11-outlaws-of-the-old-west.md:224`

Current:

- `prime runner, Appaloosa, Cayuse, Arabian, or similar top stock`

This is not a clean historical category. It mixes:

- type
- tribal / regional labeling
- imported prestige

It is better to classify horses by function and local reputation than by a grab bag of names.

**Recommendation:**

Replace with something like:

- `prime cow horse, race-bred runner, first-rate remount, or prized Indian-bred stock`

If the game wants a breed example, use it cautiously and regionally.

### 4.3 Upkeep text should make its assumptions clearer

**Location:** `corebook/11-outlaws-of-the-old-west.md:671-688`

The seasonal upkeep numbers are abstractions, which is fine. But because the text now cites specific horse prices, the reader is more likely to audit the math.

**Recommendation:**

Make one sentence even more explicit:

- these costs assume grazing, theft, improvisation, and local credit already reduce what a law-abiding town household would actually pay

That is enough to preserve the abstraction without inviting a false one-to-one accounting challenge.

## 5. Chapter 1 Lore and Social History

### 5.1 The line about Mexicans being “mollified” is historically weak

**Location:** `corebook/01-welcome-to-the-old-west.md:43`

Current wording:

> Political realism has seen many Mexicans... mollified by the US government

This is the weakest lore sentence in the opening chapter.

The borderlands and peoples notes point to a more accurate frame:

- the Treaty of Guadalupe Hidalgo promised citizenship and property rights
- many Mexican and Tejano communities remained central to the Southwest
- land loss, legal dispossession, unequal enforcement, and endemic anti-Mexican violence persisted

So the problem is not just tone. The sentence points in the wrong historical direction.

**Recommendation:**

Rewrite toward:

> Many Mexican residents of the ceded territories became U.S. citizens on paper, but citizenship did not spare them from land loss, legal manipulation, racial violence, or the steady pressure of Anglo expansion.

That preserves clarity and is much closer to the actual borderlands situation.

### 5.2 Chapter 1 should lean harder into the bilingual Southwest

**Location:** `corebook/01-welcome-to-the-old-west.md:37-49`

This is not a hard error, but it is an underplayed reality.

The game’s western frame is stronger if chapter 1 reminds the reader that much of the Southwest in `1873` remained:

- Spanish-speaking
- legally and culturally hybrid
- only partly absorbed into Anglo institutions

**Recommendation:** low-priority flavor improvement.

## 6. Literacy, Print, and Education

### 6.1 The new `Educated` talent is basically sound

**Location:** `corebook/04-talents.md:20-26`, `163-169`

This change is historically defensible and should stay.

The strongest point in its favor is that it does not claim universal illiteracy. It correctly treats literacy as uneven and dependent on:

- schooling
- class
- distance
- language
- war
- access to books and institutions

**Recommendation:** keep the current rule.

### 6.2 A useful nuance could be added later

Not everyone without `Educated` was entirely unable to decode marks on paper.

A possible later nuance:

- some characters may sign their name, recognize simple labels, read scripture by rote, or understand familiar marks without full practical literacy

This is not necessary for the current pass, but it would refine the historical picture.

## 7. Places Where the Manuscript Is Already Defensible

These areas do not need correction right now:

- `Homestead Act filing fee $14`
- basic meal and whiskey-by-the-shot anchors
- stagecoach fare at `10c/mile`
- broad rarity treatment for early `1873` cartridge arms being less common than later western myth suggests
- the `Educated` talent as a literacy gate
- the outlaw provisions burden logic in chapter 11

## Proposed Change List

### Immediate manuscript corrections

1. Fix the basic-services prices in chapter 6.
2. Reprice `Derringer`, `Colt 45 Peacemaker`, and bottled whiskey in chapter 6.
3. Correct the `Sharps Model 1874` chronology.
4. Rewrite `Peacemaker` and `Smith & Wesson Model 3` flavor to be explicitly year-sensitive.
5. Rewrite the chapter-1 Mexican-borderlands sentence.

### Next-pass clarifications

1. Separate horse prices into `country trade` and `town retail`.
2. Replace the current “prime stock” examples with functional horse categories.
3. Add one sentence clarifying the assumptions behind outlaw seasonal upkeep.
4. Optionally add a literacy nuance note for non-`Educated` characters.

## Recommended Priority Order

### Priority 1: hard factual fixes

- chapter 6 services
- chapter 6 gun prices
- Sharps chronology
- chapter 1 Mexican-borderlands wording

### Priority 2: contextual historical tightening

- Peacemaker and Model 3 flavor
- horse-market separation
- whiskey bottle anchors

### Priority 3: polish and nuance

- `Derringer` naming cleanup
- Wells Fargo coachgun wording
- literacy nuance

## Closing Judgment

The manuscript does not have a broad historical-authenticity failure. Its main problem is narrower and easier to solve:

- a small set of bad numerical anchors
- a few decade-drift firearm descriptions
- one weak borderlands sentence
- one horse-economy section that needs cleaner market logic

If those are corrected, the book will feel materially more trustworthy without becoming heavier or more pedantic.
