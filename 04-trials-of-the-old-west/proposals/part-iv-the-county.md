<!-- markdownlint-disable MD013 MD041 -->

# Part IV — The County (Procedural Proposals)

> Ch.14 Factions · Ch.15 Families · Ch.16 Inheritance ·
> Ch.17 The Wire · Ch.18 Mail · Ch.19 Press/Election
>
> This is the political layer, and it is where the workshop modules land
> hardest. The proposals replace the flat `-3`/`+3` Standing ladder and
> the single-roll faction call with the **Influence/decay pool**, the
> **faction relationship web**, and **Social Combat** — the three
> primitives that make political play feel like a system, not a
> modifier. The comms chapters (Wire, Mail) stay light; the political
> chapters (Factions, Families, Press/Election) get the heavy redesign.

---

## Ch.14 — Factions and Standing

### Current weakness

The Standing ladder (`-3` to `+3`) and the Faction Roll (one D6 per faction per season) are clean and playable, but they model each faction as an **isolated silo** — helping the railroad does not mechanically warm the railroad's allies or chill its enemies. The county's factions are a *web*, and the flat ladder cannot model the web. The "Calling on a Faction" roll is also a single check, which makes political play a series of isolated persuasions rather than a strategic contest.

### Proposed system — the Faction Web + the Influence Pool (heavy)

This is a direct adoption of two `yze-design` workshop modules, calibrated to the West.

- **The Faction Relationship Web** (`yze-design/workshop/02`): track the **bonds** (`-5` to `+5`) and the **directional debts** (`-3` to `+3`) *between factions*, not just the party's standing with each. When the party's `Standing` with faction A changes by Δ, it **propagates**: every faction B shifts its standing with the party by `floor(Δ × Bond[A,B] / 5)`. Helping the railroad warms its allies and chills its enemies, mechanically. The web also has a **Relationship Event table** (D66) rolled each season — the friction, the marriage, the betrayal, the debt called — that shifts the graph under the party. This is the single highest-value change in the book: it makes the county's politics *relational* rather than siloed, and it makes every choice a commitment.

- **The Influence Pool** (`yze-design/workshop/01`): convert the party's (or each PC's) `Standing` with a faction into a **spendable, decaying Influence pool** (cap 10, starts at 4 in the home faction). Influence is spent to compel, gain access, absorb social failures, and shift faction decisions; it is earned by public witnessed acts; and it **decays** at each season boundary unless cultivated. This replaces the flat "Calling on a Faction" roll — Influence is a *managed resource*, not a modifier, and its decay makes standing a current rather than a reservoir. A party that hoards Influence watches it evaporate; a party that spends it must rebuild it, which is the rhythm of political life.

- **The Faction Clock** becomes the **debt-call procedure**: a faction owed a debt can *call it* — a GM action, not a roll — demanding a service, a vote, a non-aggression pact. The party may pay (debt steps down, standing up), refuse (debt voided, standing drops to hunted, propagates), or renegotiate (a Social Combat or social-conflict roll). Called debts are the web's primary pressure valve, and they turn past favors into current traps.

### Why it fits

The county's factions are a web of interests, and the flat ladder modeled them as a list. The web makes the relational dimension mechanical; the Influence pool makes standing a managed resource; the debt-call makes favors dangerous. A political campaign with these three primitives plays *nothing* like a campaign without them — every choice propagates, every favor is a trap, and standing must be cultivated or lost.

### Complexity: **heavy.** The web is 3–5 factions with tracked bonds (the GM should cap at 4 to control bookkeeping); the Influence pool is per-PC per-faction (cap at 1–2 tracked factions per PC); the debt-call is a procedure. This is the right weight for the factions chapter — it is the political spine, and half the book reaches for it.

---

## Ch.15 — Families and Feuds

### Current weakness

The family-design system (nationality, traits, holdings, generations) and the Feud Clock are good and distinctive. The weakness is that the Feud Clock is a one-dimensional track (segments filled toward open war), which models the feud's *temperature* but not its *shape*. A real feud has raids, lawsuits, retaliations, mediations, and truces — it is a **campaign inside the campaign** with distinct moves, not a single升温 track.

### Proposed system — the Feud as a Faction Web (scoped) + the Feud Move Menu (medium–heavy)

- **The Feud as a Faction Web** (scoped to two families): the two feuding families are a two-node faction web, with the party's `Standing` with each propagating between them (helping one family chills the other, by the bond strength). The feud's escalation is tracked on **two axes** — the **Bond** (how hot the feud is, the existing Feud Clock's role) and the **Debt** (who owes whom, and what a called debt would demand). This gives the feud the relational depth the single track lacked, and it makes the party's every action in the county a move in someone's feud.

- **The Feud Move Menu** — each season a feud runs, each side may take one **feud move** (an activity menu):
  - **The raid** (take stock or property; a small Operation; raises the Bond's heat)
  - **The lawsuit** (the inheritance chapter's paper war; a civil Operation; does not raise heat but shifts the Debt)
  - **The slander** (the press chapter's smear; a single check; shifts `Standing` in the county)
  - **The mediation** (a Social Combat scene; a third party brokers; can step the Bond down)
  - **The retaliation** (a violent response to the last move; raises the Bond sharply)
  - **The truce** (a formal pause; steps the Bond down; either side may break it for a future move)

  The move menu makes the feud a *strategic contest* between the two families, with the party (and the party's `Standing`) as the lever each side works. This is the **activity-menu primitive** applied to the feud's seasonal cycle.

### Why it fits

A feud is not a thermometer; it is a back-and-forth with distinct moves. The two-axis web (Bond + Debt) and the move menu give the feud the strategic shape the single track lacked, and they give the party a role in the feud's moves (each move can involve, implicate, or target the party).

### Complexity: **medium–heavy.** The scoped web is two factions (light bookkeeping); the move menu is six options per season. The existing trait system and family-design framework are retained.

---

## Ch.16 — Inheritance, Land Office, and Speculation

### Current weakness

The land-office contest is an Operation (parallel to the trial), the probate is a short Operation, and speculation is a downtime gamble. All three resolve as Progress-vs-Trouble, which flattens the paper war into another heist.

### Proposed system — the Paper War as an Evidence-Economy + the Speculation as a Market Track (medium)

- **The Paper War as an Evidence-Economy** (`yze-design/workshop/05` investigation primitive, inverted): the land-office contest and the probate are not Operations — they are **evidence economies**. Each side **gathers evidence** (the prior filing, the witness, the survey, the forged codicil, the clerk's testimony) as a currency, and **spends evidence** at the hearing to shift the judge's or the land-office's opinion. Evidence is gathered through casing-like actions (the `INSIGHT`/`HAWKEYE`/`BOOKLEARNIN'`/`LIGHT-FINGERED` work of finding the document, reading the survey, bribing the clerk, forging the codicil), and the hearing is a Social Combat where the evidence is the leverage. This makes the paper war a *preparation-and-revelation* contest, not a Progress grind — the side with the better evidence wins, and the gathering is the play.

- **The Speculation as a Market Track** — the speculation gamble becomes a **tracked market** (one or two commodities the party has a position in), with the price shifting each season by a roll modified by the party's information, the faction's moves, and the national weather (the political-scene chapter's acts). The party may **hold, add, or sell** each season — a three-option activity menu — and the market's movement is the engine's honest accounting of the speculative risk. This is the **protected-dial primitive** applied to the market: the party cannot control the price, only their position.

### Why it fits

The paper war is a contest of *evidence*, not of attrition, and the evidence-economy models that. The speculation is a *market bet*, not a single roll, and the market track makes it a multi-season strategic decision. Both distinguish the paper war from the heist and the trial.

### Complexity: **medium.** The evidence economy reuses the investigation primitive (gathering clues as currency); the market track is one or two tracked commodities with a seasonal roll.

---

## Ch.17 — The Wire

### Current weakness

The wire is clean and light — cost table, cut procedures, wire-down condition. This is the right weight for a comms utility chapter. Its only weakness is that the **operator as a faction contact** is underspecified; the rest is good.

### Proposed system — the Operator as an Influence Contact (light)

- Adopt the **Influence pool** (from the factions proposal) scoped to the operator: the party's `Standing` with the operator is a small Influence pool (cap 5), spent to send a wire the company would rather not, delay a wire, read the traffic, or learn what's on the wire about the party. The operator's Influence decays if not cultivated (a bribe, a favor, a Christmas bottle), the way all Influence does. This is a light touch — it makes the operator a *managed contact* rather than a `Refuge`-style flat modifier, and it ties the wire chapter to the factions chapter's Influence system without adding new mechanics.

### Why it fits

The operator is a person, not a switch, and the Influence pool models the relationship's maintenance. The rest of the chapter is already the right weight.

### Complexity: **light.** One small Influence pool per operator; no other changes.

---

## Ch.18 — Mail and the Post

### Current weakness

The route table, the mailbag contents, and the mail-run/mail-robbery Operations are good. The weakness is that the **mail as the county's regular visitor** — the rhythm the county sets its clock by, and the thing that carries news, money, and legal documents on a schedule — is narrative, not mechanical. The mail arrives when the GM says it does.

### Current weakness (second)

The mail robbery is "the train robbery's older, poorer cousin" and runs on the same Operation. It should feel *smaller and meaner* than the train job — a roadside affair, not a set-piece.

### Proposed system — the Mail Schedule as a Metronome + the Roadside Ambush (light)

- **The Mail Schedule as a Metronome** — the mail arrives on a **known schedule** (the route table's delivery time, rolled into a campaign calendar). The party knows when the mail comes; the county knows when the mail comes. The schedule is a **strategic lever**: a faction that wants to control information times its moves to the mail's arrival; a party that wants to intercept or send knows the window. This is the **schedule-as-metronome** primitive (the trade chapter's rhythm), made explicit and tracked on the campaign calendar.

- **The Roadside Ambush** (distinct from the train Operation): the mail robbery is not a set-piece — it is a **roadside ambush**, resolved as a single extended scene (not a multi-stage Operation), with the mail's federal protection as the central fact (the hanging offense, raised `Wanted`). The roadside ambush is mechanically *lighter* than the train job — one or two checks, not a Progress track — which makes it the poor man's score the chapter says it is. The distinction is the *weight*, not just the nouns: the train job is a campaign event; the mail job is a risky errand.

### Why it fits

The mail's schedule is its strategic value, and making it explicit lets the party and the factions time their moves. The roadside ambush's lighter weight distinguishes the mail job from the train job mechanically, not just in flavor.

### Complexity: **light.** The schedule is a campaign-calendar entry; the roadside ambush is a single extended scene. No new subsystems.

---

## Ch.19 — The Press and the Election

### Current weakness

The press is a single-check faction instrument; the election is a multi-session Operation (vote-share as Progress). Both are thin for the chapter's ambition — the press and the election are the county's *peaceful weapons*, and they should feel as tactically rich as the gunfight and the trial.

### Proposed system — the Press as a Reputation Engine + the Election as a Social Combat Campaign (heavy)

- **The Press as a Reputation Engine** (`yze-design/workshop/01` Influence primitive, scaled to county): the newspaper is not a single check — it is an **Influence engine** that shifts the *county's* Influence pool (the aggregate of all factions' and families' regard for a subject) over time. Each edition is an **investment**: the editor spends resources (the column, the ink, the informant's payment) to produce a story, and the story shifts a chosen target's county-wide Influence by the story's weight (the puff, the smear, the revelation, the suppression). The press's power is its *reach* — it shifts Influence at scale, which no single social conflict can — and its risk is the libel suit, the suppression raid, and the rival paper. This makes the press a *strategic asset* the factions fight to own, not a single-check tool.

- **The Election as a Social Combat Campaign** — the election is not a Progress track; it is a **series of Social Combat scenes** (the debate, the rally, the back-room negotiation, the press exchange) whose **audience track** is the **electorate** — a tracked pool (the votes) that each scene shifts. The campaign's tactics (the canvass, the stump, the press, the money, the machine, the fraud) are the **leverage** and the **activity menu** that feed the Social Combats. The election resolves on the electorate pool's final count, not on a Progress target, which makes it a *cumulative contest* across scenes rather than a single Operation. The fraud tactic is the high-risk leverage — it shifts the pool sharply but risks the marshal and the press, the way the chapter's current table says it does.

### Why it fits

The press and the election are the county's political battlefield, and Social Combat plus the Influence engine give them the tactical depth the single check and the Progress track lacked. The press's reach (Influence at scale) is its distinct power; the election's cumulative-contest shape (many scenes feeding one pool) is its distinct structure. A political campaign with these primitives plays like a political campaign, not like a heist with different nouns.

### Complexity: **heavy.** The Influence engine is the factions chapter's system, extended to county scale; the Social Combat is the justice chapter's system, applied to the campaign trail. This is the right weight — the press/election chapter is the county's political climax, and it should feel as rich as the trial and the gunfight.
