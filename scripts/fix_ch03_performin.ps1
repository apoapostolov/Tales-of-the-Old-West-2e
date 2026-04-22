$f = "c:\git-public\Tales-of-the-Old-West-2e\corebook\03-rolling-the-bones.md"
$t = [System.Text.Encoding]::UTF8.GetString([System.IO.File]::ReadAllBytes($f))
Write-Host "Loaded len=$($t.Length)"

# The Performin' section has its heading + description + Failure displaced to the END of file.
# Current (wrong) order:
#   [MAKIN' stunts end: "- You show off."]
#   Success: ...
#   Stunts: ...
#   Being persuaded: ...
#   #### Performin' (Docity)
#   To convince another person...
#   Failure: ...   <-- end of file
#
# Correct order should be:
#   [MAKIN' stunts end: "- You show off."]
#   #### Performin' (Docity)
#   To convince another person...
#   Failure: ...
#   Success: ...
#   Stunts: ...
#   Being persuaded: ...

# Build the correct Performin' section text
$performin_heading = "#### Performin' (Docity)"
$performin_desc = "To convince another person to see things your way, reveal to them an emotional truth, capture their heart with song, hide your intentions, lie, or just convince them you are honorable, roll PERFORMIN'. Your chances are affected by your negotiating position (page 77)."
$performin_failure = "**Failure** : Your performance is transparent and clumsy. Your target is not won over"

# Find where the displaced section starts (the Success: block before the heading)
$displaced_success = "**Success** : If you succeed, you persuade them."

# Step 1: Remove the displaced heading+description+failure from end of file
# We need to cut from `#### Performin' (Docity)` onward (it's the last heading in the file)
$apos = [char]0x2019
$lastHeadingIdx = $t.LastIndexOf("#### Performin$apos (Docity)")
if ($lastHeadingIdx -lt 0) {
    Write-Host "ERROR: Performin heading not found"
    exit 1
}

# Extract the tail: heading + desc + failure (all content from last heading to EOF)
$tail = $t.Substring($lastHeadingIdx).TrimEnd()
Write-Host "Extracted tail: $($tail.Substring(0, [Math]::Min(80,$tail.Length)))"

# Find where the displaced Success: block begins (just before the heading appeared)
$successIdx = $t.IndexOf("**Success** : If you succeed, you persuade them.")
if ($successIdx -lt 0) {
    Write-Host "ERROR: Success block not found"
    exit 1
}

# The block to replace is from Success: through end of file
$displaced_block = $t.Substring($successIdx)
Write-Host "Displaced block starts: $($displaced_block.Substring(0,50))"

# Build the corrected block: heading + desc + failure + success + stunts + being persuaded
$crlf = "`r`n"
$new_block = $tail + $crlf + $crlf + $t.Substring($successIdx, $t.Length - $successIdx - $tail.Length - 4)

# Actually simpler: just do two replacements:
# 1. Remove the tail (heading+desc+failure) from end of file, leaving Success...Being persuaded
# 2. Insert the tail before the Success block

# Remove tail from where it appears at the end
$before_tail = $t.Substring(0, $lastHeadingIdx).TrimEnd()
$success_to_end = $t.Substring($successIdx, $lastHeadingIdx - $successIdx).TrimEnd()
Write-Host "success_to_end: $($success_to_end.Substring(0,[Math]::Min(50,$success_to_end.Length)))"

# Reconstruct: MAKIN ends, then Performin' section in correct order
$new_t = $before_tail + $crlf + $crlf + $tail + $crlf + $crlf + $success_to_end + $crlf

Write-Host "New len=$($new_t.Length)"

# Verify structure
if ($new_t.Contains("- You show off.`r`n`r`n#### Performin'")) {
    Write-Host "VERIFY: Heading follows Makin stunts correctly"
} elseif ($new_t.Contains("- You show off.`r`n`r`n#### Performin'".Replace("`r`n","`n"))) {
    Write-Host "VERIFY (LF): Heading follows Makin stunts correctly"
} else {
    Write-Host "VERIFY WARNING: check heading placement"
}

$idxP = $new_t.IndexOf("#### Performin'")
if ($idxP -ge 0) { Write-Host "Performin section: $($new_t.Substring($idxP,[Math]::Min(200,$new_t.Length-$idxP)))" }

[System.IO.File]::WriteAllBytes($f, [System.Text.Encoding]::UTF8.GetBytes($new_t))
Write-Host "ch03 saved."
Write-Host "Done"
