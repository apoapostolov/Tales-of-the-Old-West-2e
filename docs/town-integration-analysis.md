<!-- markdownlint-disable MD013 -->

# Town Integration Analysis

This pass checks the corebook town mechanics against _Trials of the Old West_ and records how the new subsystems should connect to the town statblock, amenities, Prosperity, Settlement Points, property, business, and Town Fortune rules.

## Corebook Town Mechanics

The corebook town is built from six aspect tallies and ranks:

- `Farming`
- `Mercantile`
- `Natural Riches`
- `Law`
- `Civic`
- `Welfare`

Each aspect begins at rank `1` with `1` tally point. Amenities add or subtract tally points. Aspect rank determines town modifiers for Season Business and Congregation rolls. Prosperity is the sum of all six aspect ranks, from `6` to `36`, and modifies Town Fortune rolls. Welfare modifies Personal Fortune rolls. Settlement Points let the group buy additional amenities during the Turn of the Season.

The corebook already has an important guardrail: a player character can own a business, property, saloon, church, or similar place without automatically granting the town the matching amenity. The town only gains an amenity when the community, campaign, and Turn of the Season rules make that public development real.

## Integration Rule Added

_Trials of the Old West_ now has a shared town-consequence rule in `00-introduction.md` under **The Town Tracker**. It gives four scales:

| Scale | Effect |
| --- | --- |
| Local scene | Shift `Standing`, `Refuge`, Competition, or one named roll; no tally change. |
| Seasonal pressure | Add or remove `1` tally point from the most affected aspect. |
| County event | Add or remove `2` tally points, or add/remove `1D3` SP if public will changes. |
| Public work | Make a fitting amenity available at `3` SP, or count the work as the season's chosen amenity. |

The cap is deliberate: no single _Trials of the Old West_ event should move the same aspect by more than `2` tally points unless a Town Fortune, amenity, or explicit chapter rule says so. This prevents runaway Prosperity gains from repeated profitable business rolls or repeated faction favors.

## Chapter Integration Map

| Chapter | Town Interaction |
| --- | --- |
| `01-the-standoff.md` | Scene-scale only. A public backing-down or bloodless defusal should move `Standing`, `Refuge`, or `Reputation`, not town tallies, unless it becomes a Town Fortune seed. |
| `02-the-holdout.md` | Scene-to-county scale depending on target. A single cabin siege moves feud, `Standing`, and `Refuge`; a defended town or public raid can feed Ch.23 siege or town `Law`/`Welfare`. |
| `03-sickness-and-the-fever.md` | Now explicitly removes `Welfare`, and sometimes `Mercantile`, for seasonal outbreaks; successful public health can discount or unlock `Doctor`, `Public Latrines`, `Wells`, or `Hospital`. |
| `04-saloons-and-the-trade.md` | Crossroads and House Refuge now feed `Mercantile`, `Law`, `Civic`, or `Welfare` only when the house becomes public life. This keeps one profitable saloon from automatically becoming a town amenity. |
| `05-running-trade-and-resources.md` | Scarcity now maps goods shortages to town aspects, and relief runs can cancel losses, restore a point, or earn SP. |
| `06-cattle-drives.md` | Clean drives can mirror the corebook Cattle Drive fortune; range war, drought, and stampede can damage `Law`, `Civic`, `Welfare`, or `Farming`; cattle public works can discount livestock and road amenities. |
| `07-mining-claims.md` | Strikes and assay booms can improve `Natural Riches` or `Mercantile`; cave-ins, dust scandals, and claim fights can damage `Welfare`, `Law`, or `Civic`; mining amenities can be discounted. |
| `08-logging-fur-trade-and-hunting.md` | Extractive seasons now feed `Natural Riches`, `Mercantile`, `Civic`, and `Welfare`; market hunting Decline can reduce the town's natural base when the town depends on the herds. |
| `09-banking-and-the-vault.md` | Bank Reserve and bank failure now write to `Mercantile`, `Welfare`, and `Civic`; sound banking can discount finance and exchange amenities. |
| `10-train-robbery.md` | Railroad jobs now affect town aspects only when the line's public confidence, payroll, depot, or service changes. |
| `11-justice-trial-incarceration.md` | Fair courts can improve `Law` or `Civic`; lynching, corruption, jail fever, and riots can damage `Law`, `Civic`, or `Welfare`; legal amenities can be discounted. |
| `12-atrocities-and-human-trade.md` | Public refusal, rescue, and testimony can improve `Civic` or `Law`; tolerated atrocity or captive trade damages `Civic`, `Law`, or `Welfare` and can cap `Refuge` for the harmed people. |
| `13-factions-and-standing.md` | Faction Rolls can now move the town tracker only when ordinary people can see the result in work, safety, trade, institutions, or health. |
| `14-families-and-feuds.md` | Family holdings, marriages, rites, feuds, and collapses now connect to aspect tallies and civic/family amenities. |
| `15-inheritance-land-office-and-speculation.md` | Fair paper can improve `Civic` or `Law`; fraud, swindles, and destructive corners can damage `Law`, `Civic`, or `Mercantile`; land and courthouse amenities can be discounted. |
| `16-the-wire.md` | Telegraph service now ties to civic infrastructure amenities; cut lines can damage `Mercantile`, `Law`, or `Civic` when they cost the town a season. |
| `17-mail-and-the-post.md` | Reliable routes can improve `Civic` or `Mercantile`; lost contracts and swindles can damage `Civic`, `Mercantile`, or `Law`; route amenities can be discounted. |
| `18-the-press-and-the-election.md` | Clean elections, reform, and true reporting can improve `Civic` or `Law`; fraud, suppression, and contested counts can damage them; political amenities can be discounted. |
| `19-weather-and-the-trail.md` | Weather writes to the town tracker only at seasonal scale: drought, floods, fire, closed roads, and public preparation. |
| `20-deep-wild-land-exploration.md` | Discoveries can improve `Natural Riches`, `Mercantile`, or `Welfare`; failed public expeditions can damage `Welfare` or `Civic`. |
| `21-regional-encounter-tables.md` | Repeated road reputation, not one-off encounters, can move `Mercantile`, `Welfare`, `Civic`, or `Law`. |
| `22-winter-and-wintering.md` | Thaw reckoning can improve `Civic` or `Welfare`, or damage `Welfare`, `Farming`, and `Natural Riches`; winter preparation can feed public-work amenities. |
| `23-mass-combat.md` | Battles, sieges, occupations, raids, and defense works now write to `Law`, `Civic`, `Welfare`, and `Mercantile` through the shared scale. |
| `24-robber-barons-and-their-work.md` | Baron projects can improve real infrastructure while marking ownership; exploitative work can damage the town aspects the baron stripped or poisoned. |
| `25-the-political-scene-of-the-1870s.md` | National acts move town aspects only when they land locally; most national pressure remains a modifier, faction move, or Town Fortune seed. |

## Balance Notes

- **Reward control:** The new hooks mostly add or remove `1` tally point, not ranks. Since ranks require increasing tally thresholds, this is meaningful without letting one scene jump a town from camp to city.
- **No free amenities:** _Trials of the Old West_ can make amenities available at `3` SP or count a season of public work as the chosen amenity, but a private outfit still does not gift the town an amenity.
- **No double-dipping by default:** If a Town Fortune already moved an aspect for the same event, the chapter hook should explain the fiction or discount an amenity, not stack another tally change unless the event truly grew beyond the Fortune.
- **Player agency:** Most negative town changes can be mitigated by play: relief runs, quarantine, fair trials, public works, road defense, winter preparation, or exposing fraud.
- **GM workload:** The GM only checks town consequences at the Turn of the Season unless a chapter explicitly says otherwise. That keeps the town tracker out of ordinary scene resolution.
- **Campaign incentive:** The hooks reward public-minded play without turning the campaign into a city builder. Players can save a town, exploit it, or profit while it decays, but the tracker will remember the choice.
