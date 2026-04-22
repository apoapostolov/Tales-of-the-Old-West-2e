$f = "c:\git-public\Tales-of-the-Old-West-2e\corebook\05-conflict-and-damage.md"
$em = [char]0x2014   # em-dash
$rs = [char]0x2019   # right single quote / apostrophe
$nl = "`r`n"

$bytes = [System.IO.File]::ReadAllBytes($f)
$t = [System.Text.Encoding]::UTF8.GetString($bytes)
Write-Host "Loaded len=$($t.Length)"

# =============================================================
# FIX 1: Range Table
# =============================================================
$oldRange = "Range Description Right next to you${em}any hand-to-hand fighting with fists or clubs, knives, toma- Arm${rs}s Length hawks and so on, happens at this range Within a few meters${em}weapons can be thrown at this range, and firearms can be Near pretty brutal this close in Up to 25 meters away${em}gunfights at this range can be deadly, and you can${rs}t lasso a Short steer or horse beyond this range Up to about 50 meters away${em}it${rs}s harder to hit a target with a pistol at this range, Medium and fighting here really calls for a rifle Long Up to about 150 meters away${em}a decent rifle is your only choice for this range Distant Over 150 meters, up to a maximum of 1000 meters, at the GM${rs}s discretion"

$newRange = "| Range | Description |${nl}| --- | --- |${nl}| Arm${rs}s Length | Right next to you${em}any hand-to-hand fighting with fists or clubs, knives, tomahawks and so on, happens at this range. |${nl}| Near | Within a few meters${em}weapons can be thrown at this range, and firearms can be pretty brutal this close in. |${nl}| Short | Up to 25 meters away${em}gunfights at this range can be deadly, and you can${rs}t lasso a steer or horse beyond this range. |${nl}| Medium | Up to about 50 meters away${em}it${rs}s harder to hit a target with a pistol at this range, and fighting here really calls for a rifle. |${nl}| Long | Up to about 150 meters away${em}a decent rifle is your only choice for this range. |${nl}| Distant | Over 150 meters, up to a maximum of 1000 meters, at the GM${rs}s discretion. |"

if ($t.Contains($oldRange)) {
    $t = $t.Replace($oldRange, $newRange)
    Write-Host "Fix 1 (Range Table) applied"
} else {
    Write-Host "Fix 1 NOT FOUND - diagnosing..."
    $idx = $t.IndexOf("Range Description")
    if ($idx -ge 0) {
        Write-Host "  'Range Description' at $idx"
        $snip = $t.Substring($idx, 50)
        [int[]][char[]]$snip
    }
}

# =============================================================
# FIX 2: Conflict Modifications table
# =============================================================
$oldFactor = "Factor Modification Aimed shot / All-out attack +2 Called Shot / Strike -3 Aiming / All-out attack on +1 Called Shot / Strike Quick Shot -2 Active Target at Arm${rs}s Length -3 Inactive Target at Arm${rs}s Length +3 Near range +1 Short range 0 Medium range -1 Long range -2 Distant range -3 Target in Partial Cover -1 Target in Good Cover -2 Called Shots Target in Heavy Cover only Large target +2 Small target -2 Dim light -1 Darkness -3 Initiated the grapple +2"

$newFactor = "| Factor | Modification |${nl}| --- | --- |${nl}| Aimed shot / All-out attack | +2 |${nl}| Called Shot / Strike | -3 |${nl}| Aiming / All-out attack on Called Shot / Strike | +1 |${nl}| Quick Shot | -2 |${nl}| Active Target at Arm${rs}s Length | -3 |${nl}| Inactive Target at Arm${rs}s Length | +3 |${nl}| Near range | +1 |${nl}| Short range | 0 |${nl}| Medium range | -1 |${nl}| Long range | -2 |${nl}| Distant range | -3 |${nl}| Target in Partial Cover | -1 |${nl}| Target in Good Cover | -2 |${nl}| Target in Heavy Cover | Called Shot only |${nl}| Large target | +2 |${nl}| Small target | -2 |${nl}| Dim light | -1 |${nl}| Darkness | -3 |${nl}| Initiated the grapple | +2 |"

if ($t.Contains($oldFactor)) {
    $t = $t.Replace($oldFactor, $newFactor)
    Write-Host "Fix 2 (Conflict Modifications) applied"
} else {
    Write-Host "Fix 2 NOT FOUND"
    # Try without apostrophe in Arm's
    $idx = $t.IndexOf("Factor Modification")
    if ($idx -ge 0) { Write-Host "  'Factor Modification' found at $idx"; $t.Substring($idx, 100) }
}

# =============================================================
# FIX 3: Sneak Attack range modifier table
# =============================================================
$oldSneak = "Sneak attack Range modifier Arm${rs}s Length -2 Short -1 Medium 0 Long +1 Ambush +2"

$newSneak = "| Sneak attack | Range modifier |${nl}| --- | --- |${nl}| Arm${rs}s Length | -2 |${nl}| Short | -1 |${nl}| Medium | 0 |${nl}| Long | +1 |${nl}| Ambush setup | +2 |"

if ($t.Contains($oldSneak)) {
    $t = $t.Replace($oldSneak, $newSneak)
    Write-Host "Fix 3 (Sneak Attack table) applied"
} else {
    Write-Host "Fix 3 NOT FOUND"
    $idx = $t.IndexOf("Sneak attack")
    if ($idx -ge 0) { $t.Substring($idx, 80) | ForEach-Object { [int[]][char[]]$_ } }
}

# =============================================================
# FIX 4: Barrier Cover Rating table
# =============================================================
$oldBarrier = "Barrier Cover rating Bush 1 Wicker Fence 2 Furniture 3 Wooden Door 4 Wooden Wall 5 Adobe Wall 8"

$newBarrier = "| Barrier | Cover rating |${nl}| --- | --- |${nl}| Bush | 1 |${nl}| Wicker Fence | 2 |${nl}| Furniture | 3 |${nl}| Wooden Door | 4 |${nl}| Wooden Wall | 5 |${nl}| Adobe Wall | 8 |"

if ($t.Contains($oldBarrier)) {
    $t = $t.Replace($oldBarrier, $newBarrier)
    Write-Host "Fix 4 (Barrier Cover table) applied"
} else {
    Write-Host "Fix 4 NOT FOUND"
}

# Save
[System.IO.File]::WriteAllBytes($f, [System.Text.Encoding]::UTF8.GetBytes($t))
Write-Host "ch05 saved. New len=$($t.Length)"
Write-Host "Done"
