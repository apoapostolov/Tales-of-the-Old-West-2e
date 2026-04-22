$f = "c:\git-public\Tales-of-the-Old-West-2e\corebook\03-rolling-the-bones.md"
$t = [System.Text.Encoding]::UTF8.GetString([System.IO.File]::ReadAllBytes($f))
$len0 = $t.Length
Write-Host "Loaded len=$len0"

# Fix 1: Reconstruct truncated NATURE stunt
# The fragment "HAWKEYE when they try to track you..." is missing its bullet prefix
$minus = [char]0x2212  # U+2212 MINUS SIGN (as used in the file)
$old1 = "`r`nHAWKEYE when they try to track you. You can choose this stunt multiple times if you roll several extra successes."
$new1 = "`r`n- You cover your tracks, imposing a ${minus}1 penalty to any HAWKEYE roll when they try to track you. You can choose this stunt multiple times if you roll several extra successes."
if ($t.Contains($old1)) {
    $t = $t.Replace($old1, $new1)
    Write-Host "Fix 1 (NATURE stunt rebuild) applied"
} else {
    Write-Host "Fix 1 NOT FOUND - trying LF variant"
    $old1lf = "`nHAWKEYE when they try to track you. You can choose this stunt multiple times if you roll several extra successes."
    $new1lf = "`n- You cover your tracks, imposing a ${minus}1 penalty to any HAWKEYE roll when they try to track you. You can choose this stunt multiple times if you roll several extra successes."
    if ($t.Contains($old1lf)) {
        $t = $t.Replace($old1lf, $new1lf)
        Write-Host "Fix 1 LF variant applied"
    } else {
        Write-Host "Fix 1 FAILED"
    }
}

# Fix 2: Remove orphaned truncated DOCTORIN' bullet
# "- You give an opponent a -1 penalty to their" (dangling, incomplete, between Recovery and Save a Life)
$old2 = "`r`n- You give an opponent a ${minus}1 penalty to their`r`n"
if ($t.Contains($old2)) {
    $t = $t.Replace($old2, "`r`n")
    Write-Host "Fix 2 (DOCTORIN orphan removal) applied"
} else {
    Write-Host "Fix 2 NOT FOUND - trying LF variant"
    $old2lf = "`n- You give an opponent a ${minus}1 penalty to their`n"
    if ($t.Contains($old2lf)) {
        $t = $t.Replace($old2lf, "`n")
        Write-Host "Fix 2 LF variant applied"
    } else {
        Write-Host "Fix 2 FAILED"
    }
}

[System.IO.File]::WriteAllBytes($f, [System.Text.Encoding]::UTF8.GetBytes($t))
Write-Host "ch03 saved. New len=$($t.Length)"

# Verify
$tv = [System.Text.Encoding]::UTF8.GetString([System.IO.File]::ReadAllBytes($f))
Write-Host "NATURE stunt has bullet: $($tv.Contains('- You cover your tracks'))"
Write-Host "DOCTORIN orphan gone: $(-not $tv.Contains('penalty to their'))"
Write-Host "Done"
