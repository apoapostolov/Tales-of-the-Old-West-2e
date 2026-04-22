$file = "c:\git-public\Tales-of-the-Old-West-2e\corebook\10-patience-is-a-virtue.md"
$text = [System.IO.File]::ReadAllText($file, [System.Text.Encoding]::UTF8)

$rsq = [char]0x2019  # RIGHT SINGLE QUOTATION MARK (curly apostrophe)
$lsq = [char]0x2018  # LEFT SINGLE QUOTATION MARK (used in 'bout)
$em  = [char]0x2014  # EM DASH
$ldq = [char]0x201C  # LEFT DOUBLE QUOTATION MARK
$rdq = [char]0x201D  # RIGHT DOUBLE QUOTATION MARK
$nl  = "`r`n"        # CRLF

# FIX 1: Rockcliffe rationale for hiring strangers
# Old: vague "he'd like to keep it quiet—hence asking strangers"
# New: explains that his real men are deployed, and strangers with no local ties
#      have no reason to doubt him and no allies to go to if they find something worse
$old1 = "- He can$($rsq)t send his own men after her as she would only run away if she saw them and, as he has a standing in the town, he$($rsq)d like to keep the whole episode quiet$($em)hence asking for the player characters$($rsq) help to find and return her, quickly and quietly."
$new1 = "- He can$($rsq)t send his own men after her$($em)Halliday and Friar are needed in town, and his other trusted hands are already deployed. As he has a standing in the town, he$($rsq)d like to keep the whole episode quiet. New arrivals with no local ties are exactly the kind of help he wants: they have no reason to doubt his account, and every reason to value the goodwill of a leading man in the community."
if ($text.Contains($old1)) { $text = $text.Replace($old1, $new1); Write-Host "Fix 1 applied" } else { Write-Host "Fix 1 NOT FOUND" }

# FIX 2: INSIGHT test pacing at the Rockcliffe meeting
# Old: 1 success already reveals "Annette is terrified" -- too much too fast
# New: graduated reveals; 1 success = subdued/quiet; 2 = something deeper; 3 = hiding grief
$old2 = "- If they fail the roll they glean nothing.$($nl)- For one success they can tell that Annette is terrified of her husband, and that Ellis seems to be taking this situation very calmly for a man who claims to love his daughter.$($nl)- For two successes they can tell that Annette is fidgety and seems like she wants to be anywhere but here, and Ellis can$($rsq)t hide his repressed irritation at her.$($nl)- For three successes they can tell that Ellis is hiding something and that Annette knows what it is but is too frightened of her husband to do or say anything about it."
$new2 = "- If they fail the roll they glean nothing.$($nl)- For one success, Annette seems unusually subdued: she answers only when directly asked, keeps her eyes on her needlework, and lets her husband speak where she could speak for herself. Ellis, for a father in distress, is very composed.$($nl)- For two successes, what passed for shyness in Annette runs deeper. She flinches$($em)barely, but there$($em)when Ellis shifts his weight or raises a hand to gesture. His composure is something closer to control.$($nl)- For three successes, it is plain that Annette knows what has happened and is afraid to say it. Ellis is performing a grief he does not feel."
if ($text.Contains($old2)) { $text = $text.Replace($old2, $new2); Write-Host "Fix 2 applied" } else { Write-Host "Fix 2 NOT FOUND" }

# FIX 3: GM note about going to the law
# Added between the INSIGHT test result and The Expert Tracker section
# Flags that Sheriff Fletcher is in Bertrand's pocket; no complaint goes anywhere without evidence
$old3 = "- For three successes, it is plain that Annette knows what has happened and is afraid to say it. Ellis is performing a grief he does not feel.$($nl)$($nl)#### The Expert Tracker"
$new3 = "- For three successes, it is plain that Annette knows what has happened and is afraid to say it. Ellis is performing a grief he does not feel.$($nl)$($nl)> **GM Note$($em)Going to the Law:** Players may think of taking their suspicions to Sheriff Fletcher before or during the investigation. Fletcher answers to Samuel Bertrand$($em)he takes unofficial payments from Bertrand on top of his county wages, as anyone who has spent a few days in Steaming Rock can learn. Rockcliffe is a leading man in the community. Any complaint about his behavior, without hard evidence in hand, goes nowhere. Fletcher will take note of who is asking, and that note will reach Rockcliffe.$($nl)$($nl)#### The Expert Tracker"
if ($text.Contains($old3)) { $text = $text.Replace($old3, $new3); Write-Host "Fix 3 applied" } else { Write-Host "Fix 3 NOT FOUND" }

# FIX 4: False trail consequence
# Currently undefined what players find if they follow the false trail south
# New: tracks vanish in rocky ground after 8-10 miles; Higgins blames a wagon/stagecoach; costs a day
$old4 = "Higgins won$($rsq)t fight the player characters unless it$($rsq)s clear they intend to kill him, in which case he will make a run for it, using his wilderness skills to get away.$($nl)$($nl)#### Higgins Comes Clean"
$new4 = "Higgins won$($rsq)t fight the player characters unless it$($rsq)s clear they intend to kill him, in which case he will make a run for it, using his wilderness skills to get away.$($nl)$($nl)Should the players follow the false trail south, after eight or ten miles the tracks vanish in rocky ground. There is nothing to find. Higgins will claim this confirms what he suspected$($em)that Patience hired a wagon or caught a stage toward Fort Cummings. Backtracking to Canyon Creek Ridge from that point will cost the better part of a day, and they will reach the junction in failing light.$($nl)$($nl)#### Higgins Comes Clean"
if ($text.Contains($old4)) { $text = $text.Replace($old4, $new4); Write-Host "Fix 4 applied" } else { Write-Host "Fix 4 NOT FOUND" }

# FIX 5: Mary's murder moral weight in Peyton's speech
# Old: "Pity 'bout poor li'l Mary--she shoulda just stayed home" -- throwaway dismissal
# New: Peyton names the murder and offers payment for their silence, making the moral stakes explicit
$old5 = "_$($ldq)Pity $($lsq)bout poor li$($rsq)l Mary$($em)she shoulda just stayed home and not gotten involved.$($rdq)_"
$new5 = "_$($ldq)You boys already seen what happened to the maid. That ain$($rsq)t a comfortable thing to carry. Mr Rockcliffe$($rsq)s the kind of man who makes it worth your while not to.$($rdq)_"
if ($text.Contains($old5)) { $text = $text.Replace($old5, $new5); Write-Host "Fix 5 applied" } else { Write-Host "Fix 5 NOT FOUND" }

# FIX 6: Kinnear intervention window in Epilogue A
# Old: "unless they intervene" with no mechanism described
# New: players find Kinnear in the street before he reaches Rockcliffe; can intercept with PERFORMIN'/PRESENCE
$old6 = "When the player characters return to town they are immediately accosted by Maxwell Kinnear, Patience$($rsq)s cowhand boyfriend. He has heard they are looking for her, but accuses them, and Rockcliffe, of leaving her to die. In his fury he heads off towards the Rockcliffes$($rsq) home to have it out with Ellis. Unless the player characters intervene Kinnear is confronted by Halliday and Friar on the field in front of Rockcliffe$($rsq)s home. Gunplay ensues and Kinnear is killed."
$new6 = "When the player characters return to town they are immediately accosted by Maxwell Kinnear, Patience$($rsq)s cowhand boyfriend. He has heard they are looking for her and has been asking questions all day. He accuses them, and Rockcliffe, of leaving her to die. He is already on his feet and heading for Rockcliffe$($rsq)s home$($em)not in a listening mood, but not yet beyond reach. Players who act fast can intercept him here; a successful PERFORMIN$($rsq) or PRESENCE roll gives them a chance to stop him long enough to hear what they know. If the player characters do nothing, or fail to stop him, Kinnear reaches the field in front of Rockcliffe$($rsq)s home where Halliday and Friar are waiting. Gunplay ensues and Kinnear is killed."
if ($text.Contains($old6)) { $text = $text.Replace($old6, $new6); Write-Host "Fix 6 applied" } else { Write-Host "Fix 6 NOT FOUND" }

# FIX 7: Rockcliffe knows the player characters know (Epilogue B)
# Old: Rockcliffe is just puzzled by Patience's behavior -- story wraps up cleanly
# New: flags that Rockcliffe knows the PCs were at the shack; his gratitude is genuine but temporary;
#      men who know about Mary are a liability he will deal with in his own time
$old7 = "Rockcliffe is surprised and relieved, but wonders why the impetuous Patience is behaving in such a measured way."
$new7 = "Rockcliffe is surprised and relieved, but wonders why the impetuous Patience is behaving in such a measured way. He has not forgotten that the player characters were at Peyton$($rsq)s shack and know what happened to Mary. His gratitude is genuine$($em)for now. But Ellis Rockcliffe does not let dangerous knowledge walk loose in his own town. Men who know what happened to that girl are a liability, and he will decide in his own time what to do about them."
if ($text.Contains($old7)) { $text = $text.Replace($old7, $new7); Write-Host "Fix 7 applied" } else { Write-Host "Fix 7 NOT FOUND" }

[System.IO.File]::WriteAllText($file, $text, [System.Text.Encoding]::UTF8)
Write-Host "Done - file written"
