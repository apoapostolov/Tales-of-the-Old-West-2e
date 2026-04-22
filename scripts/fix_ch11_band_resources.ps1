$file = "c:\git-public\Tales-of-the-Old-West-2e\corebook\11-outlaws-of-the-old-west.md"
$text = [System.Text.Encoding]::UTF8.GetString([System.IO.File]::ReadAllBytes($file))
$em = [char]0x2014
$nl = "`r`n"
$bt = '`'

# ================================================================
# ADDITION 1: Band Resources section
# Insert after "Cohesion should not swing..." and before the blockquote
# ================================================================

$bandResources = @"
### Band Resources

An outlaw band tracks three resources beyond cash and Cohesion. They are not ledger entries. They are pressure gauges that tell the GM and the players how much room the gang still has to move.

#### Refuge

``Refuge`` measures how the gang stands with a single important settlement, camp, trading post, ranch, or hidden community. Track it only for places that actually matter to the gang's survival.

| Refuge | Meaning |
| --- | --- |
| ``+2`` | The place will hide you, feed you quietly, pass messages, and lie to the law if pressed. |
| ``+1`` | The place deals with you, but wants discretion and quick business. |
| ``0`` | No special help. You are just another party of riders. |
| ``-1`` | The place is wary, talks to strangers, and may refuse service. |
| ``-2`` | The place will warn the law, deny shelter, or sell you out. |

Refuge starts at 0 for any settlement the gang has not yet dealt with. Raise it by spending money, doing favors, or making yourself useful. Lose it by leaving a mess behind, killing someone local, cheating a merchant, or making the town look dangerous to outsiders. A town's ``Law``, ``Civic``, and ``Mercantile`` aspects all bear on what Refuge can do for the gang and what costs them.

#### Fence Access

``Fence Access`` measures whether the gang can turn stolen goods into clean money.

| Fence Access | Meaning |
| --- | --- |
| ``0`` | No fence. Hot loot sits in camp or must be sold openly at heavy risk. |
| ``1`` | A petty fence. Can move jewelry, guns, whiskey, and small goods at a fair discount. |
| ``2`` | A serious fence. Can move cattle, horses, payroll paper, and larger goods through a network. |

A fence is usually a notable gang member, a corrupt merchant, a Nuevo Mexicano trader, or a settlement contact reached through Refuge. Losing a fence$($em)through arrest, betrayal, or the law's attention$($em)drops Fence Access immediately. Building a new one takes time, goodwill, and often money.

#### Horseflesh

``Horseflesh`` measures the state of the gang's riding animals as a band resource.

| Horseflesh | Meaning |
| --- | --- |
| ``3`` | Fresh remounts, sound tack, and horses fit for hard flight or hard pursuit. |
| ``2`` | Serviceable. The gang can ride, but cannot outrun professionals for long. |
| ``1`` | Tired, lame, hungry, poorly shod, or too few mounts for the gang's size. |
| ``0`` | The gang cannot move fast or far. Flight is a stumble. |

Horseflesh drops after hard flight from a posse, a bad winter at the hideout, drought, poor grazing, or stolen mounts lost in a score gone wrong. Restore it by taking the ``Buy Through Fences`` hideout activity, rustling a fresh remuda, or dealing with a competent wrangler.

When Horseflesh is 0 or 1, any well-mounted pursuer gains an advantage overtaking the gang.

"@

$old1 = "Cohesion should not swing every session. Save changes for moments that really tell on the gang.$($nl)$($nl)> _Jeb Collier"
$new1 = "Cohesion should not swing every session. Save changes for moments that really tell on the gang.$($nl)$($nl)$($bandResources)> _Jeb Collier"

if ($text.Contains($old1)) {
    $text = $text.Replace($old1, $new1)
    Write-Host "Addition 1 (Band Resources) applied"
} else {
    Write-Host "Addition 1 NOT FOUND - checking..."
    $idx = $text.IndexOf("Cohesion should not swing every session")
    Write-Host "  Cohesion line at: $idx"
    if ($idx -ge 0) { Write-Host "  Context: $($text.Substring($idx, 100))" }
}

# ================================================================
# ADDITION 2: Loot Categories
# Insert after "Until then they are trouble wrapped in canvas." and before "#### Gang Expenses"
# ================================================================

$lootCategories = @"

#### Loot Categories

Not all take converts to cash the same way. Three categories cover most of what outlaws steal:

| Category | Examples | How It Converts |
| --- | --- | --- |
| ``Clean Cash`` | Coin, notes, payroll money pulled directly from a box | Spendable at once. No fence required. |
| ``Hot Goods`` | Jewelry, guns, whiskey, watches, express packages, negotiable bonds | Requires ``Fence Access 1`` or better to move at reasonable value. Without a fence, sells at a fraction of value or raises Exposure. |
| ``Hot Stock`` | Cattle, horses, mules | Requires ``Fence Access 2`` or special local conditions$($em)an altered brand, a trusted drover, a territory where no one is asking. The longer it sits, the more it talks. |

Most scores will produce a mix. A bank vault yields Clean Cash. A stage hold-up is mostly Hot Goods with some cash if the passengers have coin. A cattle raid is entirely Hot Stock. The gang that steals cattle has a resource and a problem in the same animal.

"@

$old2 = "Stolen stock, jewelry, bonds, silverware, church plate, or railroad goods are not cash until fenced. Until then they are trouble wrapped in canvas.$($nl)$($nl)#### Gang Expenses"
$new2 = "Stolen stock, jewelry, bonds, silverware, church plate, or railroad goods are not cash until fenced. Until then they are trouble wrapped in canvas.$($lootCategories)#### Gang Expenses"

if ($text.Contains($old2)) {
    $text = $text.Replace($old2, $new2)
    Write-Host "Addition 2 (Loot Categories) applied"
} else {
    Write-Host "Addition 2 NOT FOUND - checking..."
    $idx = $text.IndexOf("trouble wrapped in canvas")
    Write-Host "  Canvas line at: $idx"
}

# ================================================================
# ADDITION 3: Pursuer Classes
# Insert before "#### Escalation" in the Wanted Men section
# ================================================================

$pursuerClasses = @"
#### Who Is Chasing You

Different pursuers work in different ways. A county sheriff and a railroad detective are both trouble, but they are not the same trouble.

| Pursuer | How They Pressure the Gang |
| --- | --- |
| Sheriff and Posse | Quick local response. Neighbors and townsmen. Short pursuit that fades after two hard days in rough country if no blood was spilled. |
| Ranch Outfit or Range Detectives | Know the stock, the brands, and the trails. Best at tracing stolen animals and tracking across cattle country. May work quietly before acting. |
| Railroad or Express Detectives | Company money and station networks. They travel ahead by telegraph. Stay interested long after a county sheriff has moved on. |
| Federal Marshals | Warrants, persistence, cross-jurisdiction authority. Slower to arrive but harder to lose. A federal warrant does not stop at the county line. |
| Rival Gang | No interest in due process. Will take horses, fence access, hideout location, and heads if the price is right. Can also be bought or bargained with. |

Each pursuer class has different tactics. A ranch outfit confiscates horses and shuts down the local fence. A railroad detective buys informants and watches the wire. A federal marshal crosses county lines. The gang that knows who is chasing them can make better choices about what to give up and where to run.

"@

$old3 = "#### Escalation$($nl)$($nl)| D6 | Who Comes Next?"
$new3 = "$($pursuerClasses)#### Escalation$($nl)$($nl)| D6 | Who Comes Next?"

if ($text.Contains($old3)) {
    $text = $text.Replace($old3, $new3)
    Write-Host "Addition 3 (Pursuer Classes) applied"
} else {
    Write-Host "Addition 3 NOT FOUND - checking..."
    $idx = $text.IndexOf("#### Escalation")
    Write-Host "  Escalation at: $idx"
    if ($idx -ge 0) { Write-Host "  Context: $($text.Substring($idx, 60))" }
}

[System.IO.File]::WriteAllBytes($file, [System.Text.Encoding]::UTF8.GetBytes($text))
Write-Host "Done - file written"
