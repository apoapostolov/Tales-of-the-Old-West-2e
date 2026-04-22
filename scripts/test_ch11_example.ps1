$f="c:\git-public\Tales-of-the-Old-West-2e\corebook\11-outlaws-of-the-old-west.md"
$bytes=[System.IO.File]::ReadAllBytes($f)
$text=[System.Text.Encoding]::UTF8.GetString($bytes)
$em=[char]0x2014

$oldFrag = "The Harper gang consists of two player characters, four ordinary hands, and one notable member called Mexican Joe, who acts as scout and horse wrangler. That makes them a ``Hideout Crew``. Their Cohesion is 3 and they have a concealed hideout in the bad hills north of town from the old Outlaws Group Concept."

Write-Host "Fragment found: $($text.Contains($oldFrag))"
