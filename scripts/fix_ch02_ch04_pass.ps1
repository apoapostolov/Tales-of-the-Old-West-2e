$f02 = "c:\git-public\Tales-of-the-Old-West-2e\corebook\02-your-player-character.md"
$f04 = "c:\git-public\Tales-of-the-Old-West-2e\corebook\04-talents.md"
$nl = "`r`n"
$em = [char]0x2014
$lq = [char]0x201C   # left double quote
$rq = [char]0x201D   # right double quote
$rs = [char]0x2019   # right single quote / apostrophe

# Load ch02
$bytes = [System.IO.File]::ReadAllBytes($f02)
$t02 = [System.Text.Encoding]::UTF8.GetString($bytes)

Write-Host "ch02 loaded, len=$($t02.Length)"

# --- FIX 1: Epigraph (Fitzgerald -> True Grit / Portis) ---
$oldEpigraph = "> _${lq}IT${rs}S NEVER TOO LATE TO BECOME WHO YOU WANT TO BE. I HOPE YOU LIVE A LIFE THAT YOU${rs}RE PROUD OF, AND IF YOU FIND THAT YOU${rs}RE NOT, I HOPE YOU HAVE THE STRENGTH TO START OVER.${rq}_${nl}>${nl}> ${em} F. SCOTT FITZGERALD"
$newEpigraph = "> _${lq}YOU MUST PAY FOR EVERYTHING IN THIS WORLD ONE WAY AND ANOTHER. THERE IS NOTHING FREE EXCEPT THE GRACE OF GOD.${rq}_${nl}>${nl}> ${em} MATTIE ROSS, *TRUE GRIT*, CHARLES PORTIS"

if ($t02.Contains($oldEpigraph)) {
    $t02 = $t02.Replace($oldEpigraph, $newEpigraph)
    Write-Host "Fix 1 (Epigraph) applied"
} else {
    Write-Host "Fix 1 NOT FOUND - searching..."
    $idx = $t02.IndexOf("IT")
    Write-Host "  'IT' at $idx"
    $idx2 = $t02.IndexOf("NEVER TOO LATE")
    Write-Host "  'NEVER TOO LATE' at $idx2"
    if ($idx2 -ge 0) {
        $snippet = $t02.Substring([Math]::Max(0,$idx2-20), 100)
        [int[]][char[]]$snippet | Select-Object -First 30
    }
}

# --- FIX 2: Bat Masterton -> Bat Masterson ---
if ($t02.Contains("Bat Masterton")) {
    $t02 = $t02.Replace("Bat Masterton", "Bat Masterson")
    Write-Host "Fix 2 (Bat Masterson) applied"
} else {
    Write-Host "Fix 2 NOT FOUND"
}

# --- FIX 3: Lawman Big Dream broken bullet ---
$oldLBD = "You will not rest until every lawbreaker has${nl}  - been driven from your town."
$newLBD = "You will not rest until every lawbreaker has been driven from your town."
if ($t02.Contains($oldLBD)) {
    $t02 = $t02.Replace($oldLBD, $newLBD)
    Write-Host "Fix 3 (Lawman Big Dream) applied"
} else {
    Write-Host "Fix 3 NOT FOUND"
    $idx3 = $t02.IndexOf("every lawbreaker has")
    if ($idx3 -ge 0) { Write-Host "  Found 'every lawbreaker has' at $idx3"; $t02.Substring($idx3, 80) }
}

# --- FIX 4: Lawman Faith - Quaker ---
$oldLF1 = "As a Quaker I am uplifted by my Society of${nl}  - Friends."
$newLF1 = "As a Quaker I am uplifted by my Society of Friends."
if ($t02.Contains($oldLF1)) {
    $t02 = $t02.Replace($oldLF1, $newLF1)
    Write-Host "Fix 4 (Lawman Faith Quaker) applied"
} else {
    Write-Host "Fix 4 NOT FOUND"
    $idx4 = $t02.IndexOf("Society of")
    Write-Host "  'Society of' at $idx4"
}

# --- FIX 5: Lawman Faith - wide open plain ---
$oldLF2 = "The wide open plain and the river give me${nl}  - everything I need."
$newLF2 = "The wide open plain and the river give me everything I need."
if ($t02.Contains($oldLF2)) {
    $t02 = $t02.Replace($oldLF2, $newLF2)
    Write-Host "Fix 5 (Lawman Faith plain) applied"
} else {
    Write-Host "Fix 5 NOT FOUND"
    $idx5 = $t02.IndexOf("wide open plain")
    Write-Host "  'wide open plain' at $idx5"
}

# --- FIX 6: Ranch Hand Big Dream broken bullet (has em-dash) ---
$oldRH = "you must protect it from${nl}  - the settlers and pass it on to future generations."
$newRH = "you must protect it from the settlers and pass it on to future generations."
if ($t02.Contains($oldRH)) {
    $t02 = $t02.Replace($oldRH, $newRH)
    Write-Host "Fix 6 (Ranch Hand Big Dream) applied"
} else {
    Write-Host "Fix 6 NOT FOUND"
    $idx6 = $t02.IndexOf("you must protect it from")
    Write-Host "  'you must protect it from' at $idx6"
    if ($idx6 -ge 0) { [int[]][char[]]($t02.Substring($idx6, 80)) }
}

# --- FIX 7: Tracker archetype BOW MASTER description ---
$oldBM02 = "The bow is the weapon of a true man from a more civilized culture. You can use a bow up to Long range with no penalties."
$newBM02 = "Most men have forgotten the bow. You have not. You can use a bow up to Long range with no penalties."
if ($t02.Contains($oldBM02)) {
    $t02 = $t02.Replace($oldBM02, $newBM02)
    Write-Host "Fix 7 (Tracker BOW MASTER) applied"
} else {
    Write-Host "Fix 7 NOT FOUND"
}

# Save ch02
[System.IO.File]::WriteAllBytes($f02, [System.Text.Encoding]::UTF8.GetBytes($t02))
Write-Host "ch02 saved"

# --- Ch04: Bow Master talent description ---
$bytes04 = [System.IO.File]::ReadAllBytes($f04)
$t04 = [System.Text.Encoding]::UTF8.GetString($bytes04)
Write-Host "ch04 loaded, len=$($t04.Length)"

$oldBM04 = "The bow is the weapon of a true man from a more civilized culture."
$newBM04 = "The bow is a weapon of patience and silence. Most men who carry iron have never had to learn it."
if ($t04.Contains($oldBM04)) {
    $t04 = $t04.Replace($oldBM04, $newBM04)
    Write-Host "Fix 8 (Ch04 Bow Master) applied"
} else {
    Write-Host "Fix 8 NOT FOUND"
}

[System.IO.File]::WriteAllBytes($f04, [System.Text.Encoding]::UTF8.GetBytes($t04))
Write-Host "ch04 saved"
Write-Host "Done"
