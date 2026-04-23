$f       = "c:\git-public\Tales-of-the-Old-West-2e\corebook\11-outlaws-of-the-old-west.md"
$t       = [System.Text.Encoding]::UTF8.GetString([System.IO.File]::ReadAllBytes($f))
$apos    = [char]0x2019
$emdash  = [char]0x2014
$crlf    = "`r`n"
$bt      = [char]0x60
Write-Host "Loaded len=$($t.Length)"

# ============================================================
# BLOCK 1: Calling on Refuge — tiered roll procedure
# ============================================================
$b1 = $crlf +
      "#### Calling on Refuge" + $crlf + $crlf +
      "When the gang needs something from a settlement" + $emdash +
      "shelter from a posse, a doctor for the wounded, supplies, a safe stable, or word about law activity" + $emdash +
      "the character with the strongest relationship there makes a " +
      "${bt}PRESENCE${bt} or ${bt}PERFORMIN${apos}${bt} roll. Add dice equal to the current Refuge score if positive, or remove dice equal to its absolute value if negative." + $crlf + $crlf +
      "**0 successes:** The place will not help and the refusal has consequences. A merchant talks to the wrong man, a farmer bolts his door and sends his boy to town, or an innkeeper quietly passes word to the deputy. Reduce Refuge with this settlement by 1." + $crlf + $crlf +
      "**1 success (limited):** Help is given, but grudgingly and at a price" + $emdash +
      "higher costs, visible discomfort, or conditions attached. The gang spent goodwill to get this. Refuge holds but the debt is felt." + $crlf + $crlf +
      "**2 successes (full):** The settlement does what the gang needs without incident or complaint. Refuge holds steady." + $crlf + $crlf +
      "**3 successes or more:** The place goes further than the gang asked. A warning about a posse they had not heard of, an introduction to a potential fence, or something quietly set aside against a harder day. Consider raising Refuge by 1 if the relationship has been well tended." + $crlf

# ============================================================
# BLOCK 2: Turning Hot Goods to Cash — tiered fencing roll
# ============================================================
$b2 = $crlf +
      "#### Turning Hot Goods to Cash" + $crlf + $crlf +
      "When the gang wants to move Hot Goods or Hot Stock through a fence, the character handling the deal makes a ${bt}PRESENCE${bt} or ${bt}PERFORMIN${apos}${bt} roll. Apply the following modifiers:" + $crlf + $crlf +
      "| Condition | Modifier |" + $crlf +
      "| --- | --- |" + $crlf +
      "| Fence Access is 2 | ${bt}+1 die${bt} |" + $crlf +
      "| Refuge with the fence${apos}s town is ${bt}+1${bt} or higher | ${bt}+1 die${bt} |" + $crlf +
      "| Refuge with the fence${apos}s town is ${bt}-1${bt} or lower | ${bt}-1 die${bt} |" + $crlf +
      "| The goods are clearly connected to a recent notorious crime | ${bt}-1 die${bt} |" + $crlf +
      "| Selling Hot Stock with only Fence Access 1 | ${bt}-2 dice${bt} |" + $crlf + $crlf +
      "**0 successes:** The deal falls through. The fence is nervous, cuts contact, or refuses this batch. Hot Goods stay Hot. If the gang presses, the fence${apos}s fear makes them a liability" + $emdash +
      "they may talk, drift away, or cost the gang Fence Access." + $crlf + $crlf +
      "**1 success (limited):** The fence takes the goods but drives a hard bargain. Receive half the fair value, or receive full value with a delay of weeks that raises the gang${apos}s Exposure and risks a Wanted escalation." + $crlf + $crlf +
      "**2 successes (full):** Clean deal at the fence${apos}s usual rate. Receive fair value after the fence${apos}s cut." + $crlf + $crlf +
      "**3 successes or more:** The fence has a ready buyer or unusually good terms. Receive better-than-fair value and learn something useful" + $emdash +
      "law movements, an upcoming opportunity, or a contact worth having." + $crlf + $crlf +
      "If the gang has no fence (${bt}Fence Access 0${bt}), they may still try to sell Hot Goods openly, but the roll becomes ${bt}PERFORMIN${apos}${bt} at ${bt}-2 dice${bt}, and even a limited success generates heat." + $crlf

# ============================================================
# BLOCK 3: Towns and Outlaw Life — new section
# ============================================================
$b3 = "### Towns and Outlaw Life" + $crlf + $crlf +
      "Towns are not neutral ground. They have economic interests, political divisions, moral tolerances, and men with guns. The outlaw who walks into one without reading it first has already made a mistake." + $crlf + $crlf +
      "#### Reading a Town" + $crlf + $crlf +
      "The town aspects from Chapter 6 do double work in outlaw play. Each one answers a different question for the gang." + $crlf + $crlf +
      "| Aspect | What It Tells the Gang |" + $crlf +
      "| --- | --- |" + $crlf +
      "| ${bt}Law${bt} | How fast the town organizes pursuit, posts notices, and supports the sheriff or marshal |" + $crlf +
      "| ${bt}Mercantile${bt} | Whether there are fences, corrupt clerks, liquid markets for stolen goods, or buyers who ask few questions |" + $crlf +
      "| ${bt}Civic${bt} | Whether the town stands together against trouble or is divided by old grudges, class hatred, and competing loyalties |" + $crlf +
      "| ${bt}Welfare${bt} | Whether strangers can disappear quietly, find a doctor without comment, stable horses without remark, and rent a room without filling out a ledger |" + $crlf + $crlf +
      "A town with high Law and low Mercantile will hunt you hard and refuse your money. A town with low Law and high Mercantile will deal with you if you keep things quiet. The same town can be lawful on paper and corrupt in practice. That is more western than any flat lawful/lawless distinction." + $crlf + $crlf +
      "#### Town Tags for Outlaw Play" + $crlf + $crlf +
      "For settlements that matter to the campaign, the GM may add one of the following tags to capture its character for outlaw purposes. These can be derived from existing aspects rather than tracked separately if preferred." + $crlf + $crlf +
      "| Tag | Meaning |" + $crlf +
      "| --- | --- |" + $crlf +
      "| ${bt}Soft Town${bt} | Weak law, divided interests, or enough vice that a gang can vanish there briefly without drawing attention |" + $crlf +
      "| ${bt}Fence Town${bt} | Stolen goods can be moved here through merchants, drovers, gamblers, or rail contacts. Fence Access rolls gain ${bt}+1 die${bt} in this town |" + $crlf +
      "| ${bt}Sheriff${apos}s Town${bt} | The local law, ranchers, and merchants cooperate quickly against trouble. Law is treated as one step higher for outlaw purposes |" + $crlf + $crlf +
      "The same town can hold more than one tag. A cattle market town might be both a ${bt}Fence Town${bt} and a ${bt}Sheriff${apos}s Town${bt} during roundup season, which is a western truth of its own." + $crlf + $crlf +
      "#### Doing Business in a Dangerous Town" + $crlf + $crlf +
      "When an outlaw character does business in a town" + $emdash +
      "buying supplies, moving goods, consulting a doctor, or sitting in a saloon" + $emdash +
      "roll ${bt}PERFORMIN${apos}${bt} to stay hidden, or ${bt}PRESENCE${bt} if brazing it through. Apply the following modifiers:" + $crlf + $crlf +
      "| Condition | Modifier |" + $crlf +
      "| --- | --- |" + $crlf +
      "| Town has ${bt}Soft Town${bt} tag | ${bt}+1 die${bt} |" + $crlf +
      "| Refuge with this town is ${bt}+1${bt} or better | ${bt}+1 die${bt} |" + $crlf +
      "| Disguise or convincing false name in play | ${bt}+1 die${bt} |" + $crlf +
      "| Refuge with this town is ${bt}-1${bt} or worse | ${bt}-1 die${bt} |" + $crlf +
      "| Wanted is Regional | ${bt}-1 die${bt} |" + $crlf +
      "| Wanted is Federal | ${bt}-2 dice${bt} |" + $crlf +
      "| Town has ${bt}Sheriff${apos}s Town${bt} tag | ${bt}-1 die${bt} |" + $crlf + $crlf +
      "**0 successes:** Someone recognizes the gang or draws the wrong conclusion. The law is notified or a reward poster is pulled from a drawer and studied. Reduce Refuge with this town by 1 and test Cohesion if the business was critical." + $crlf + $crlf +
      "**1 success (limited):** Business done, but not cleanly. Someone noticed. The town grows warier. If Refuge is ${bt}0${bt} or less, reduce it by 1." + $crlf + $crlf +
      "**2 successes (full):** In and out without incident." + $crlf + $crlf +
      "**3 successes or more:** Business done and something useful learned or gained" + $emdash +
      "a rumor about a posse${apos}s movements, a contact who might serve as a fence, a piece of intelligence about an upcoming score, or a stranger who nods instead of staring." + $crlf + $crlf +
      "#### Seasonal Town Interaction" + $crlf + $crlf +
      "At each ${bt}Turn of the Season${bt}, the gang should answer these questions for any settlement important to their survival:" + $crlf + $crlf +
      "- Did the gang strengthen or damage Refuge here this season?" + $crlf +
      "- Did events in town" + $emdash +
      "a marshal passing through, a booming market, a crop failure, a political shift" + $emdash +
      "change what this town can or will offer?" + $crlf +
      "- Did the gang invest money, favors, or fear to keep one place open to them?" + $crlf + $crlf +
      "If the gang invested money or effort to maintain a good relationship, no roll is needed" + $emdash +
      "just note it. If they left a mess behind, killed someone local, or cheated a merchant, reduce Refuge by 1 without a roll." + $crlf

# ============================================================
# APPLY INSERTION 1: Calling on Refuge
# After: "aspects all bear on what Refuge can do for the gang and what costs them."
# Before: "#### Fence Access"
# ============================================================
$m1_end = "aspects all bear on what Refuge can do for the gang and what costs them."
$old1   = $m1_end + $crlf + $crlf + "#### Fence Access"
$new1   = $m1_end + $crlf + $b1 + $crlf + "#### Fence Access"
if (-not $t.Contains($old1)) { Write-Host "ERROR: Insertion 1 marker not found"; exit 1 }
$t = $t.Replace($old1, $new1)
Write-Host "Insertion 1 (Calling on Refuge) applied"

# ============================================================
# APPLY INSERTION 2: Fencing roll
# After: "The gang that steals cattle has a resource and a problem in the same animal."
# Before: "#### Gang Expenses"
# ============================================================
$m2_end = "The gang that steals cattle has a resource and a problem in the same animal."
$old2   = $m2_end + $crlf + $crlf + "#### Gang Expenses"
$new2   = $m2_end + $crlf + $b2 + $crlf + "#### Gang Expenses"
if (-not $t.Contains($old2)) { Write-Host "ERROR: Insertion 2 marker not found"; exit 1 }
$t = $t.Replace($old2, $new2)
Write-Host "Insertion 2 (Turning Hot Goods to Cash) applied"

# ============================================================
# APPLY INSERTION 3: Towns and Outlaw Life section
# After the Jeb Collier blockquote line ending "...one night.*"
# Before: "### Recruitment, Notable Members, and Loyalty"
# ============================================================
$m3_end = "The camp stayed ugly but it stayed a camp. That was enough for one night."
# find what immediately follows in file
$idx3 = $t.IndexOf($m3_end)
$after3 = $t.Substring($idx3 + $m3_end.Length, 40)
Write-Host "After Jeb quote: $(($after3 -replace '[\r\n]', '<LF>'))"
# Should be: "*<CR><LF><CR><LF>### Recruitment"
# Try with trailing *
$old3 = $m3_end + "*" + $crlf + $crlf + "### Recruitment, Notable Members, and Loyalty"
$new3 = $m3_end + "*" + $crlf + $crlf + $b3 + $crlf + "### Recruitment, Notable Members, and Loyalty"
if (-not $t.Contains($old3)) {
    Write-Host "Trying without asterisk..."
    $old3 = $m3_end + $crlf + $crlf + "### Recruitment, Notable Members, and Loyalty"
    $new3 = $m3_end + $crlf + $crlf + $b3 + $crlf + "### Recruitment, Notable Members, and Loyalty"
    if (-not $t.Contains($old3)) { Write-Host "ERROR: Insertion 3 marker not found"; exit 1 }
}
$t = $t.Replace($old3, $new3)
Write-Host "Insertion 3 (Towns and Outlaw Life) applied"

# ============================================================
# SAVE
# ============================================================
[System.IO.File]::WriteAllBytes($f, [System.Text.Encoding]::UTF8.GetBytes($t))
Write-Host "Saved. New len=$($t.Length)"

# ============================================================
# VERIFY
# ============================================================
$tv = [System.Text.Encoding]::UTF8.GetString([System.IO.File]::ReadAllBytes($f))
Write-Host "Calling on Refuge:            $($tv.Contains('Calling on Refuge'))"
Write-Host "Tiered successes in Refuge:   $($tv.Contains('3 successes or more'))"
Write-Host "Turning Hot Goods to Cash:    $($tv.Contains('Turning Hot Goods to Cash'))"
Write-Host "Towns and Outlaw Life:        $($tv.Contains('Towns and Outlaw Life'))"
Write-Host "Reading a Town:               $($tv.Contains('Reading a Town'))"
Write-Host "Town Tags for Outlaw Play:    $($tv.Contains('Town Tags for Outlaw Play'))"
Write-Host "Doing Business in a Dangerous Town: $($tv.Contains('Doing Business in a Dangerous Town'))"
Write-Host "Seasonal Town Interaction:    $($tv.Contains('Seasonal Town Interaction'))"
Write-Host "Fence Town tag:               $($tv.Contains('Fence Town'))"
Write-Host "Done"
