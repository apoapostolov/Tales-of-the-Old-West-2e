# 1870s: The Old West - Illustration Prompt Pack

This document plans the interior illustration set for the supplement.
It is written for a dense hardcover A4 layout with historical realism,
not poster art. The prompts are structured for `nanobanana-pro` /
`openai-image-2` style use: one clear subject, one clear location in the
text, concrete period detail, and explicit composition constraints.

## Global Art Direction

- Visual target: hard-edged historical western realism
- Mood: dusty, lived-in, unsentimental, physically specific
- Preferred framing: readable scenes with one dominant action
- Avoid: modern clothing, cinematic exaggeration, fantasy glow, text,
  watermarks, logo marks, anachronistic gear, clean studio styling
- Text policy: no captions or in-image labels unless a later plate
  explicitly calls for typography
- People policy: specific ethnic and regional identity, not generic
  "cowboy" imagery
- Composition policy: prioritize one moment, one environment, one
  historically grounded object cluster

## Production Checklist

- [ ] Lock the illustration language and art direction
- [ ] Confirm the chapter opener list and page placements
- [ ] Review prompts for historical accuracy and period objects
- [ ] Generate the front matter and chapter opener set
- [ ] Add secondary spot art only where pagination needs it
- [ ] Final pass for repetition, overlap, and visual balance

## Prompt Template

Use this structure for each image prompt:

```text
Use case: historical-scene
Asset type: interior book illustration for an A4 roleplaying supplement
Primary request: <what the illustration should show>
Scene/backdrop: <where the scene takes place>
Subject: <main subject or subjects>
Style/medium: historical western illustration, realistic, detailed
Composition/framing: <wide / medium / close, placement of figures>
Lighting/mood: <time of day, weather, emotional tone>
Color palette: <earth tones, smoke, sage, brass, etc.>
Materials/textures: <cloth, leather, dust, wood, iron, hide, stone>
Constraints: period-correct 1870s American West only
Avoid: text, watermark, modern objects, fantasy styling, caricature
```

## Front Matter

### Cover

- Illustration purpose: establish the book as a hard-country western
  reference, not a movie-poster western; use as the main cover image.
- Placement: front cover.
- Prompt:

```text
Use case: historical-scene
Asset type: book cover illustration for an A4 roleplaying supplement
Primary request: a wide frontier scene showing the 1870s American West
as a working country of dust, horses, rail, settlement, and distance
Scene/backdrop: open country at the edge of a town, with rail, stock,
and distant hills or plains
Subject: mixed western life in one scene - a mounted cowhand, a woman
near a wagon, a Black soldier or freighter, a Native rider at distance,
and a town edge with smoke and timber
Style/medium: realistic historical western illustration, painted, rich
detail, no cinematic glamour
Composition/framing: broad panoramic composition, strong foreground
figure, deep landscape, space for title placement
Lighting/mood: late afternoon light, wind, dust, weight, realism
Color palette: umber, ochre, faded denim, saddle brown, smoke gray
Materials/textures: worn leather, horsehide, cotton, raw timber, dust,
iron rail, canvas
Constraints: period-correct 1870s equipment and clothing only
Avoid: fantasy silhouettes, modern branding, clean studio look, text,
watermark
```

### Title Page / Opening Plate

- Illustration purpose: a quieter tone-setting image for the opening
  spread; reinforces the book's documentary register.
- Placement: title page or first interior spread.
- Prompt:

```text
Use case: historical-scene
Asset type: opening plate for an A4 roleplaying supplement
Primary request: a solitary frontier road cutting through dust and grass,
with a rider or wagon at long distance, emphasizing distance and silence
Scene/backdrop: empty western road or track, broad sky, low country
Subject: one rider and one working animal, small against the land
Style/medium: realistic historical western illustration, restrained,
documentary feel
Composition/framing: vertical or square-friendly composition, strong
negative space for title spread use
Lighting/mood: morning haze or evening blue light, spare and severe
Color palette: pale sky, brown earth, gray-blue shadow, muted green
Materials/textures: dust, dry grass, leather tack, weathered cloth
Constraints: no action clutter; keep it simple and emblematic
Avoid: dramatic poses, modern roads, text, watermark, fantasy effects
```

## Chapter 1 - The Peoples and the Conflict

- Illustration purpose: show the West as a crowded, contested social
  field, not a one-people frontier; illustrates the opening survey of
  Anglo-Americans, Mexicans, Black Americans, Chinese labor, Native
  nations, and conflict.
- Placement: chapter opener, before the first people subsection.
- Prompt:

```text
Use case: historical-scene
Asset type: chapter opener illustration for an A4 roleplaying supplement
Primary request: a frontier town street crowded with different peoples
of the 1870s West, all working or passing through the same place
Scene/backdrop: a main street at the edge of a rail or cattle town
Subject: Anglo merchant, Tejano vaquero, Black cowboy, Chinese laborer,
Native rider, and a federal or territorial lawman in the same frame
Style/medium: realistic historical western illustration, observational,
not romanticized
Composition/framing: medium-wide street scene with strong human variety
and layered depth
Lighting/mood: dry daylight, busy but uneasy, social tension visible
Color palette: dusty neutrals, faded cloth, leather, tin, sun-bleached
wood
Materials/textures: hats, boots, horse tack, freight wagons, timber
fronts, stovepipe, work shirts
Constraints: accurate 1870s clothing and gear; no anachronisms
Avoid: caricature, stereotype framing, text, watermark, glossy movie
lighting
```

## Chapter 2 - Native Cultures: The Daily Physical World

- Illustration purpose: show the material world of Native life through
  shelter, horse wealth, and family work; best paired with the Comanche
  section and echoed later with Lakota material detail.
- Placement: after the introduction to the chapter, before `Southern
  Plains - the Comanche`.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a Comanche camp at work, with women raising or tending
the tipi, horses nearby, and family gear laid out in use
Scene/backdrop: southern Plains camp in open country with low grass and
clear sky
Subject: Comanche family life, tipi, travois, horse herd, hide work,
and camp logistics
Style/medium: realistic historical western illustration, ethnographic
but living, not museum-diorama
Composition/framing: medium-wide camp scene with a clear central action
Lighting/mood: bright high-plains daylight, practical and active
Color palette: rawhide, earth, sage, white canvas-like hide, horse brown
Materials/textures: tipi hide, bone awl, parfleche, beads, leather,
horses, dust
Constraints: specific 1870s Native material culture only; no generic
pan-Indian imagery
Avoid: headdresses on everyone, war paint everywhere, fantasy styling,
text, watermark
```

## Chapter 3 - The Borderlands

- Illustration purpose: illustrate the border as a lived corridor of
  trade, language, cattle movement, and law rather than a clean line on
  a map; works best with the geography and cattle trade section.
- Placement: after `The Geography of the Border`, before `Population
  and Language`.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a Rio Grande border crossing with cattle, riders, and
border trade moving through a shallow river or ford
Scene/backdrop: border country between Texas and northern Mexico
Subject: cowmen moving stock, a Tejano rider, a ranger or rurales figure
at distance, and a working crossing point
Style/medium: realistic historical western illustration with clear
geographic storytelling
Composition/framing: wide landscape with human figures small against
the country
Lighting/mood: hot afternoon light, dry wind, cautious motion
Color palette: sand, river green, scrub brown, faded red cloth, iron
Materials/textures: cattle hide, saddles, ropes, wet river stones, dust
Constraints: 1870s border equipment and clothing only
Avoid: modern border imagery, fences everywhere, propaganda framing,
text, watermark
```

## Chapter 4 - Childhood on the Frontier

- Illustration purpose: show the daily labor and vulnerability of
  frontier children across homestead, ranch, town, and mining-camp life;
  best aligned to the age-by-age section and the small grave material.
- Placement: after `The Day, by Age and Place`, before the nursery and
  mortality sections.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a frontier child carrying water or wood near a hard-
used cabin or camp, with school or burial ground implied in the distance
Scene/backdrop: homestead edge, with a rough dwelling, fence, and work
ground around it
Subject: a child in practical frontier clothing doing labor, not posing
Style/medium: realistic historical western illustration, quiet and
observant
Composition/framing: medium scene with the child as the visual anchor
Lighting/mood: cool morning or late afternoon, serious and ordinary
Color palette: faded calico, brown earth, dull tin, pale wood, muted sky
Materials/textures: rough boards, iron bucket, worn shoes, dust, cloth
Constraints: age-appropriate clothing and period domestic detail
Avoid: sentimental Victorian nursery fantasy, modern school gear, text,
watermark
```

## Chapter 5 - The Women of the West

- Illustration purpose: show women as workers, managers, and anchors of
  household and camp economies, not decorative background figures.
- Placement: in the homestead woman section, before the chapter moves
  into ranch, town, mining-camp, and Hispanic women.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a frontier woman managing a hard domestic workday at a
stove, table, and wash basin while children or supplies crowd the room
Scene/backdrop: a homestead kitchen or ranch house interior
Subject: a working woman with visible competence, and the tools of the
household around her
Style/medium: realistic historical western illustration, intimate and
unsentimental
Composition/framing: medium interior scene with strong use of hands
and work surfaces
Lighting/mood: window light or stove light, practical and steady
Color palette: wood brown, iron black, flour white, faded cloth, soot
Materials/textures: cast iron, enamel, linen, crockery, broom corn, dust
Constraints: period-correct domestic work and clothing only
Avoid: glamor portrait, modern appliances, romanticized cleanliness,
text, watermark
```

## Chapter 6 - Food and Drink

- Illustration purpose: show the trail cook and the home kitchen as the
  two great food systems of the West.
- Placement: on the chuckwagon section, before the homestead kitchen
  section.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a chuckwagon cook serving a hard meal to cowhands at
camp, with pot, fire, coffee, and trail gear all visible
Scene/backdrop: open range camp with wagon, fire ring, and herd nearby
Subject: cook, serving line, Dutch ovens, coffee pot, tin plates, men
waiting for food
Style/medium: realistic historical western illustration, tactile and
busy, with clear food detail
Composition/framing: medium-wide camp scene centered on the wagon and
fire
Lighting/mood: firelight or early morning, workmanlike, hungry
Color palette: black iron, flame orange, flour dust, coffee brown,
canvas tan
Materials/textures: cast iron, enamelware, wood, smoke, meat, biscuit
Constraints: period trail food only; no modern cookware
Avoid: clean picnic fantasy, modern camp cookware, text, watermark
```

## Chapter 7 - Work and Trades

- Illustration purpose: show the labor economy of ranching, mining, and
  rail construction in one book-safe visual; use the mining or rail
  section depending on page design.
- Placement: after `Mining` or `The Railroad`, depending on pagination.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: working men at a railroad or mining task, with tools,
timber, and dirty labor dominating the frame
Scene/backdrop: a rail grade, cutting, or mining camp work site
Subject: laborers handling rail, timber, ore, or heavy tools under hard
conditions
Style/medium: realistic historical western illustration, documentary
work scene
Composition/framing: medium-wide labor scene with a strong diagonal of
work activity
Lighting/mood: harsh daylight, sweat, dust, fatigue
Color palette: steel gray, coal black, dirt brown, rusty red, faded
shirt blue
Materials/textures: wood, iron, rope, ore, sweat-stained cloth, soot
Constraints: accurate 1870s trade tools and clothing
Avoid: modern safety gear, industrial machinery from later decades,
text, watermark
```

## Chapter 8 - Material Culture: Iron, Leather, Cloth

- Illustration purpose: show the object world of the West - firearms,
  blades, saddles, and tack - as handled tools rather than fetish pieces.
- Placement: in the firearms or tack sections, depending on page flow.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a careful, realistic layout of western gear on a
blanket or workbench, with revolver, rifle, saddle, reins, knife, and
small tools all present
Scene/backdrop: plain work surface in a bunkhouse, tack room, or shop
Subject: the everyday material kit of a western working person
Style/medium: realistic historical illustration, object-focused, not
catalog clean
Composition/framing: tabletop or bench composition with layered gear
Lighting/mood: side light, practical, quiet
Color palette: leather brown, iron blue-black, oiled wood, cloth tan
Materials/textures: worn leather, blued steel, wood grain, stitching,
grease, dust
Constraints: 1870s weapon and tack forms only
Avoid: modern firearms, polished showroom look, text, watermark
```

## Chapter 9 - Language, Literacy, and the Paper World

- Illustration purpose: show the paper and print world - telegraph,
  newspaper, ledger, letter, and schoolroom - as the chapter's visual
  center.
- Placement: after the kill list or in the period slang / registers
  section.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a small western print office or telegraph room with
ledger, type, paper, and a worker in the act of reading or composing
Scene/backdrop: town print shop or telegraph office
Subject: editor, telegrapher, or clerk at work among papers and tools
Style/medium: realistic historical western illustration, precise and
workmanlike
Composition/framing: medium interior with strong desk foreground
Lighting/mood: lamp light or window light, cerebral and practical
Color palette: paper white, ink black, wood brown, brass, soot gray
Materials/textures: paper stacks, lead type, ink, telegraph key, wood
Constraints: period office technology only
Avoid: modern office clutter, glowing screens, text-heavy overlays,
watermark
```

## Chapter 10 - Religion and Faith

- Illustration purpose: show the circuit rider and the mixed faith world
  of the West, with church, chapel, or camp meeting atmosphere.
- Placement: on the circuit rider section, before the work subsection.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a frontier preacher or circuit rider addressing a
small congregation in a rough western church or meeting place
Scene/backdrop: plain wooden chapel, schoolhouse, or outdoor meeting
spot
Subject: preacher, listeners, worn benches, hymn book, and rough walls
Style/medium: realistic historical western illustration, sober and
human
Composition/framing: medium interior with the preacher slightly off
center and listeners visible
Lighting/mood: late afternoon or lamp light, earnest, austere
Color palette: pine wood, black coat, white paper, earth tones, muted
cloth
Materials/textures: rough boards, benches, Bible, hymn book, dust
Constraints: accurate 1870s denominational dress and setting
Avoid: theatrical revival spectacle, modern church fixtures, text,
watermark
```

## Chapter 11 - Frontier Survival and the Hunt

- Illustration purpose: show the country and the hunt as immediate
  survival knowledge, especially water, weather, and tracking.
- Placement: at the start of the water or weather section.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a lone traveler finding or testing water in harsh
frontier country while weather builds in the distance
Scene/backdrop: arid plains, creek bed, or river edge under open sky
Subject: rider or hunter reading the country, with water source and
tracks visible
Style/medium: realistic historical western illustration, survival and
terrain focused
Composition/framing: wide outdoor scene with land and sky as major
elements
Lighting/mood: tense weather light, dry wind, practical caution
Color palette: sand, scrub green, pale sky, cloud gray, mud brown
Materials/textures: canteen, saddle, hoofprints, dry grass, stone, mud
Constraints: 1870s survival gear only
Avoid: adventure-poster theatrics, modern camping gear, text, watermark
```

## Chapter 12 - What Existed and What Did Not

- Illustration purpose: turn the technology timeline into a visual
  comparison by showing period-true goods, tools, and transport.
- Placement: at the technology timeline opening.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a mercantile counter or workbench crowded with
period-correct 1870s goods, tools, and packaged supplies
Scene/backdrop: general store or supply room
Subject: a storekeeper or customer handling the stock of the decade
Style/medium: realistic historical western illustration, object-led and
accurate
Composition/framing: medium interior still-life with a human anchor
Lighting/mood: daylight through the store front, orderly but plain
Color palette: paper labels, wood, tin, glass, flour dust, tobacco brown
Materials/textures: crates, sacks, jars, ironware, cloth bolts, boots
Constraints: only items that truly exist in the 1870s
Avoid: later-century products, modern packaging, text, watermark
```

## Chapter 13 - Prices and Anchors

- Illustration purpose: ground the chapter's numbers in concrete pay and
  purchase reality; best served by a wage or payment moment rather than
  an abstract chart.
- Placement: after the wage section or on the saloon / mercantile price
  section.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a working man being paid in cash, or counting wages
and expenses, in a frontier interior
Scene/backdrop: saloon back room, mercantile counter, or bunkhouse
Subject: hand-to-hand wage payment, coin, paper money, ledger, and a
working outfit in view
Style/medium: realistic historical western illustration, economic and
concrete
Composition/framing: medium close scene with hands, money, and ledger
prominent
Lighting/mood: indoor light, practical, exact, slightly grim
Color palette: brass, paper white, tobacco brown, black ink, wood
Materials/textures: coins, banknotes, ledger paper, boots, worn cloth
Constraints: 1870s currency and goods only
Avoid: modern banking imagery, stylized money piles, text, watermark
```

## Chapter 14 - Towns, Economy, and Law

- Illustration purpose: show a western town block as a live civic and
  commercial machine, with saloon, bank, store, and law tension.
- Placement: on the town types opening or on the saloon/bank section.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a busy western street corner with saloon, bank,
mercantile, and lawman presence in one readable scene
Scene/backdrop: cattle town or mining camp main street
Subject: saloon front, bank, store, marshal or deputy, wagon, and
customers moving between buildings
Style/medium: realistic historical western illustration, civic and
commercial
Composition/framing: medium-wide town scene with architectural detail
Lighting/mood: clear afternoon light, tense but ordinary
Color palette: weathered wood, dust, brass, window glass, faded paint
Materials/textures: timber fronts, porch boards, signs, horses, wagons
Constraints: period town architecture and law enforcement only
Avoid: movie-set symmetry, modern storefronts, text, watermark
```

## Chapter 15 - Competence and Procedure

- Illustration purpose: show a hands-on procedure moment, such as roping,
  saddling, or watering, because the chapter is fundamentally about
  bodily skill.
- Placement: on the horsemanship procedure opening.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a cowboy performing a precise horse-handling task,
with clear hand placement and working tack
Scene/backdrop: open corral, remuda, or working yard
Subject: one rider executing a rope, saddle, or horse control procedure
Style/medium: realistic historical western illustration, instructional
but alive
Composition/framing: medium action scene with the hands and horse
visible
Lighting/mood: hard daylight, concentrated, practical
Color palette: leather, sweat, dust, horse coat, rope fiber, wood
Materials/textures: rawhide, horsehair, rope, steel hardware, dirt
Constraints: physically plausible procedure only
Avoid: stunt poses, modern gear, text, watermark
```

## Chapter 16 - Cowboy Life

- Illustration purpose: show the trail drive as the central occupational
  image of cowboy life, ideally with herd, wagon, and weather.
- Placement: at the `The Cattle Drive` section, especially the trail or
  railhead subsection.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a cattle drive moving across open country with the
trail boss, riders, herd, and dust all visible
Scene/backdrop: open plains or river crossing on the long trail north
Subject: cowhands moving cattle in a disciplined line
Style/medium: realistic historical western illustration, expansive and
physical
Composition/framing: wide landscape with herd movement as the main
shape
Lighting/mood: sunrise or late-day dust light, weary and purposeful
Color palette: dust tan, herd brown, sky blue, saddle leather, dark
shirts
Materials/textures: cattle hide, reins, hats, boots, canvas, dust
Constraints: 1870s trail drive gear and habits only
Avoid: romantic horse spread, modern fences, text, watermark
```

## Chapter 17 - Horse Culture

- Illustration purpose: make the horse itself the subject, with breed,
  breaking, and tack culture visible.
- Placement: on the mustang or mustanging sections.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a horseman working a mustang or remuda horse in a
corral, showing the raw relationship between rider and animal
Scene/backdrop: corral or open horse camp
Subject: one horse being handled, with a rider, rope, and other horses
in the background
Style/medium: realistic historical western illustration, animal-focused
and tense
Composition/framing: medium action composition centered on the horse
Lighting/mood: bright daylight, dust, muscle, motion
Color palette: chestnut, sorrel, bay, leather brown, dirt gray
Materials/textures: horse coat, hide rope, wood rails, saddle, sweat
Constraints: 1870s horse culture and tack only
Avoid: romantic equestrian portrait, show-ring polish, text, watermark
```

## Chapter 18 - Mining Camps

- Illustration purpose: show the underground mine as a dark, engineered
  workplace with labor and timber dominating the scene.
- Placement: on the underground section or the shift section.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: miners working underground in a timbered shaft or
drift, with lamps, ore, and tools visible
Scene/backdrop: hardrock mine interior
Subject: two or three miners at the face, drilling, mucking, or loading
Style/medium: realistic historical western illustration, dark and
claustrophobic
Composition/framing: tight medium scene with strong lamp pools of light
Lighting/mood: dim lamplight, soot, fatigue, danger
Color palette: black, ochre, lantern gold, timber brown, iron gray
Materials/textures: rock, timber, powder smoke, iron tools, wet dirt
Constraints: period mine gear only
Avoid: modern hard hats, electric light, heroic fantasy mining, text,
watermark
```

## Chapter 19 - Army Life

- Illustration purpose: show a frontier post as a machine of routine,
  hierarchy, and isolation; good fit for the post layout or cavalry
  column.
- Placement: on the frontier post opening or the Buffalo Soldier
  section.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a frontier army post with soldiers at work, horses,
flag, and barracks in a hard institutional setting
Scene/backdrop: western military post
Subject: troopers, officers, supply buildings, mounted horses, and the
post flag
Style/medium: realistic historical western illustration, disciplined
and worn
Composition/framing: medium-wide post scene with a clear hierarchy of
space
Lighting/mood: dry daylight, regulated, tired, formal
Color palette: olive drab, khaki, dusty brown, flag red, weathered wood
Materials/textures: canvas, leather, rifles, tent cloth, timber, dust
Constraints: 1870s U.S. Army uniforms and post layout only
Avoid: later uniforms, parade polish, modern bases, text, watermark
```

## Chapter 20 - Outlaw Craft

- Illustration purpose: show the outlaw economy as planning, hiding, and
  escape rather than swagger; best tied to the hideout or posse section.
- Placement: on the hideout opening or posse section.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: outlaws in a rough hideout counting supplies, checking
weapons, and planning a ride out
Scene/backdrop: canyon hideout, shack, cave, or remote camp
Subject: two or three outlaws around gear, horses outside, and a map or
ledger on the floor
Style/medium: realistic historical western illustration, tense and
practical
Composition/framing: medium interior scene with shadows and exit space
Lighting/mood: firelight or low lamplight, secretive and worn
Color palette: dark brown, ash gray, dull steel, horsehide, smoke
Materials/textures: rifles, bedrolls, saddlebags, rope, tattered cloth
Constraints: period outlaw gear and behavior only
Avoid: romantic robber glamour, modern weapons, text, watermark
```

## Chapter 21 - Gambling

- Illustration purpose: show the table as a social and criminal space,
  with the game and the room both mattering.
- Placement: on the faro or poker section.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a gambling table in a saloon with players, dealer,
cash, and tension in the room
Scene/backdrop: frontier saloon interior
Subject: faro or poker game, gambler, dealer, watchers, and money on
the table
Style/medium: realistic historical western illustration, close and
tense
Composition/framing: medium close tabletop scene with faces and hands
Lighting/mood: lamp light, smoke, suspicion, concentration
Color palette: amber light, green felt, black coats, brass, whiskey
Materials/textures: cards, chips, coins, glass, felt, cigar smoke
Constraints: period gaming equipment and attire only
Avoid: neon colors, modern casino polish, text, watermark
```

## Chapter 22 - Music and Entertainment

- Illustration purpose: show the saloon or dance hall as a social stage
  where music, dancing, and performance overlap.
- Placement: on the fiddle and dance hall section or the rodeo section.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a frontier dance hall with a fiddler, dancers, and
onlookers packed into a working room
Scene/backdrop: saloon dance hall, rough hall, or traveling show tent
Subject: fiddler, dancers, stamped floor, lamps, and crowded audience
Style/medium: realistic historical western illustration, lively but
grounded
Composition/framing: medium-wide interior with motion in the center
Lighting/mood: warm lamp light, noise, sweat, and motion
Color palette: amber, red-brown, black, white shirt sleeves, brass
Materials/textures: fiddle wood, boots, dust, sawdust, hats, glass
Constraints: 1870s instruments, dress, and venue only
Avoid: concert hall polish, modern stage lighting, text, watermark
```

## Chapter 23 - Medicine and Death

- Illustration purpose: show the sickroom or the aftermath of violence as
  the chapter's emotional center, with medical tools and mortality in
  view.
- Placement: on the doctor or wound-treatment sections.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a frontier doctor treating a wounded patient in a
plain sickroom with the tools of period medicine visible
Scene/backdrop: cabin sickroom, boarding house room, or camp shelter
Subject: doctor, patient, attendant, and bedside medical gear
Style/medium: realistic historical western illustration, sober and
unsparing
Composition/framing: medium interior with the bed as the visual anchor
Lighting/mood: dim window light or lamp light, grim and quiet
Color palette: white cloth, brown wood, iron black, pale skin tones,
medicine glass
Materials/textures: bandages, saw, bottles, basin, blanket, bloodstain
Constraints: 1870s medicine only; no antiseptic theater or modern
equipment
Avoid: melodrama, gore spectacle, text, watermark
```

## Chapter 24 - The Dark Frontier

- Illustration purpose: handle the book's hardest material with restraint;
  the best visual is ominous rather than explicit.
- Placement: on the chapter opener or the sexual violence / lynching
  section depending on layout needs.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a dark frontier scene that implies danger, violence,
and fear without turning into spectacle
Scene/backdrop: night exterior near a shack, tree line, or rough camp
Subject: a fearful figure, a closed door, a rope, or a shadowed group
in the distance
Style/medium: realistic historical western illustration, severe and
restrained
Composition/framing: low-light composition with strong negative space
Lighting/mood: night, fire glow, fear, isolation
Color palette: black, dark brown, ember orange, bruised gray, faded red
Materials/textures: rough timber, rope, dirt, torn cloth, soot
Constraints: suggest the horror without explicit exploitation
Avoid: sensational violence, sexualization, gore focus, text, watermark
```

## Chapter 25 - Regional Landscapes

- Illustration purpose: make the West's regional variety visible by
  giving the landscape the lead role, with a small human scale.
- Placement: on the regional overview or the best-known landscape
  section for the book's intended audience.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a wide landscape of one major western region with a
tiny human figure, horse, or wagon to show scale
Scene/backdrop: one of the major 1870s western regions, emphasizing
terrain, weather, and distance
Subject: land first, people second, with the region clearly named by
its physical character
Style/medium: realistic historical western illustration, atmospheric
and geographic
Composition/framing: wide panoramic composition with strong horizon
Lighting/mood: region-specific light, weather, and seasonal tone
Color palette: vary by region but keep it natural and restrained
Materials/textures: rock, grass, dust, snow, scrub, river, timber
Constraints: no scenic fantasy, no modern road cuts, no text, watermark
Avoid: postcard prettiness and over-saturated color
```

## Final QA Pass

Before generating, check that every prompt:

- names one dominant subject
- specifies one placement in the book
- uses period-correct objects only
- avoids text unless the plate is intentionally typographic
- keeps the visual language consistent across the whole supplement

## Secondary Spot Illustration Queue

Use these if the layout needs more art density than one opener per
chapter. They are written to cover the long or visually important
subsections without repeating the chapter opener.

### Spot 1 - Native camp logistics

- Illustration purpose: show the working surface of Native camp life,
  especially hide work, gear storage, and daily movement.
- Placement: Chapter 2, after `The woman's kit`.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: Native women working hides and gear at camp while
children and horses move through the background
Scene/backdrop: Plains camp edge with tipi, drying lines, and horse
bundles
Subject: hide work, storage, and domestic logistics in active use
Style/medium: realistic historical western illustration, intimate and
observational
Composition/framing: medium camp scene with hands and tools visible
Lighting/mood: daylight, practical, industrious
Color palette: rawhide, bead blue, earth, horse brown, sage
Materials/textures: hide, awl, rope, parfleche, basket, dust
Constraints: specific nation and period only; no ceremonial overload
Avoid: generic pan-Indian symbols, fantasy styling, text, watermark
```

### Spot 2 - Border trade and translation

- Illustration purpose: show language exchange as practical labor.
- Placement: Chapter 3, after `The languages in the room`.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a borderland interior where Spanish and English are
being used in trade, with interpreters, money, and goods on the table
Scene/backdrop: adobe room, mercantile, or customs-adjacent space
Subject: traders, interpreter, ledger, and mixed-language conversation
Style/medium: realistic historical western illustration, social and
documentary
Composition/framing: medium interior with hands, faces, and goods
Lighting/mood: midday indoor light, watchful, transactional
Color palette: sun-bleached plaster, wood brown, paper white, faded red
Materials/textures: ledger, coin, cloth bolts, rope, crate wood
Constraints: 1870s border realities only
Avoid: modern customs imagery, caricature, text, watermark
```

### Spot 3 - Childhood and mortality

- Illustration purpose: pair child labor with the book's mortality note.
- Placement: Chapter 4, after `Mortality and the Small Grave`.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a small frontier grave or grave marker on the edge of
a working homestead or camp, with a child-sized presence implied
Scene/backdrop: rough burial ground near a cabin or camp
Subject: plain grave, family tokens, and the surrounding work country
Style/medium: realistic historical western illustration, quiet and
somber
Composition/framing: restrained medium-wide landscape with the grave
off-center
Lighting/mood: overcast or late-day light, mournful, austere
Color palette: gray earth, faded flowers, weathered wood, pale grass
Materials/textures: rough board marker, dirt, stone, dry grass, cloth
Constraints: no melodrama; keep the death ordinary and real
Avoid: supernatural glow, gothic decoration, text, watermark
```

### Spot 4 - Women's work beyond the house

- Illustration purpose: show women doing ranch or town labor, not only
  domestic labor.
- Placement: Chapter 5, after `The Ranch Wife` or `The Town Woman`.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a frontier woman at a practical working task beyond
the kitchen, such as bookkeeping, sewing repair, or tending stock
Scene/backdrop: ranch room, boarding house, or shop back room
Subject: a woman at work with ledger, needle, or supplies
Style/medium: realistic historical western illustration, skilled and
unsentimental
Composition/framing: medium interior with a work surface foreground
Lighting/mood: window light, calm, capable
Color palette: cloth gray, brown wood, ink black, muted blue
Materials/textures: paper, thread, leather, crockery, iron stove
Constraints: period-true labor and dress only
Avoid: portrait glamour, modern office items, text, watermark
```

### Spot 5 - Home kitchen economy

- Illustration purpose: show preservation, storage, and cooking as a
  system.
- Placement: Chapter 6, after `The preservation`.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a frontier kitchen full of preserved food, jars,
smoke, and working surfaces
Scene/backdrop: homestead kitchen or pantry
Subject: jars, hanging meat, bread, tins, and a woman or man at work
Style/medium: realistic historical western illustration, domestic and
exact
Composition/framing: medium interior with shelves and hanging items
Lighting/mood: stove light, practical, abundant but hard-won
Color palette: amber, flour white, jam red, tin gray, wood brown
Materials/textures: glass jars, crockery, cloth, smoke, wood, cured meat
Constraints: 1870s food storage only
Avoid: modern pantry goods, sterile kitchen styling, text, watermark
```

### Spot 6 - Railroad labor

- Illustration purpose: make railroad construction physical and risky.
- Placement: Chapter 7, after `Construction`.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: railroad laborers laying track or handling a rail
joint under harsh conditions
Scene/backdrop: rail grade in rough country
Subject: workers, rail, spikes, hammer, ties, ballast, and dirt
Style/medium: realistic historical western illustration, heavy labor
Composition/framing: diagonal work scene with strong tool shapes
Lighting/mood: hard daylight, sweat, strain, dust
Color palette: iron gray, wood brown, dirt ochre, shirt blue
Materials/textures: steel rail, spikes, timber, ballast, canvas, sweat
Constraints: 1870s railroad construction only
Avoid: later machinery, safety gear, text, watermark
```

### Spot 7 - Store counter and gear

- Illustration purpose: show the material culture chapter in a shop
  environment.
- Placement: Chapter 8, after `The realities of period firearms` or
  `Other tack`.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a western store counter with firearms, tack, tools,
and cloth goods being handled by a clerk and customer
Scene/backdrop: gunsmith, mercantile, or saddlery
Subject: clerk, customer, and the goods of the country
Style/medium: realistic historical western illustration, object-rich
Composition/framing: medium interior with counter foreground
Lighting/mood: practical daylight, businesslike
Color palette: wood brown, brass, iron blue-black, cloth tan
Materials/textures: leather, steel, rope, cloth bolts, paper labels
Constraints: period inventory only
Avoid: modern retail display, weapon fantasy, text, watermark
```

### Spot 8 - Telegraph and newspaper

- Illustration purpose: support the paper world with a more specific
  communications image.
- Placement: Chapter 9, after `The Slurs` or `Registers`.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a telegraph operator and newspaper clerk sharing a
small office filled with paper, key, and type
Scene/backdrop: town office or print room
Subject: operator, editor, forms, and news waiting to move
Style/medium: realistic historical western illustration, cramped and
busy
Composition/framing: medium interior with desk clutter and human focus
Lighting/mood: lamp light, late work, concentration
Color palette: ink black, paper white, brass, wood, smoke gray
Materials/textures: telegraph key, paper, type, lamp glass, ledger
Constraints: 1870s communications only
Avoid: modern office equipment, screen glow, text, watermark
```

### Spot 9 - Religious procession or camp meeting

- Illustration purpose: capture the public side of faith more broadly.
- Placement: Chapter 10, after the denomination section.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a frontier religious gathering outside a church or in
a brush arbor with plain people gathered around
Scene/backdrop: small settlement meeting place
Subject: preacher, singers, benches, wagons, and listeners
Style/medium: realistic historical western illustration, communal and
plainspoken
Composition/framing: medium-wide gathering with the preacher in front
Lighting/mood: late afternoon or evening, earnest, restrained
Color palette: white shirt, black coat, pine wood, earth, lantern glow
Materials/textures: hymn books, benches, wood, dust, cloth
Constraints: period-accurate denomination and dress
Avoid: revival spectacle, modern church furniture, text, watermark
```

### Spot 10 - Water and weather

- Illustration purpose: give the survival chapter a tighter weather
  image.
- Placement: Chapter 11, after `Weather`.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a traveler or camp near dangerous weather, reading the
sky and protecting water and gear
Scene/backdrop: open country as storm or cold front arrives
Subject: rider, horse, canteen, shelter, and approaching weather
Style/medium: realistic historical western illustration, tense and
environmental
Composition/framing: wide landscape with a small human figure
Lighting/mood: storm light, wind, pressure, urgency
Color palette: gray sky, brown earth, pale grass, dark horse coat
Materials/textures: clouds, dust, saddle, water container, canvas
Constraints: period travel conditions only
Avoid: dramatic disaster framing, modern gear, text, watermark
```

### Spot 11 - Wage and price comparison

- Illustration purpose: make the prices chapter feel concrete and
  transactional.
- Placement: Chapter 13, after the wages tables.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a working man comparing wages against a small pile of
goods and bills in a frontier room
Scene/backdrop: bunkhouse, saloon back room, or mercantile counter
Subject: cash, ledger, tobacco, boots, and simple goods in one frame
Style/medium: realistic historical western illustration, exact and
economical
Composition/framing: medium close still life with human hands visible
Lighting/mood: indoor light, sober, calculating
Color palette: brass, paper, brown leather, faded cloth, black ink
Materials/textures: coins, banknotes, ledger, boots, tobacco pouch
Constraints: 1870s prices and goods only
Avoid: modern consumer goods, abstract money symbols, text, watermark
```

### Spot 12 - Town law and lawmen

- Illustration purpose: show legal authority as a street-level presence.
- Placement: Chapter 14, after `The town types`.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a town marshal or deputy standing at the edge of a
street while the town goes about business
Scene/backdrop: western main street
Subject: lawman, horses, storefronts, and people watching from cover
Style/medium: realistic historical western illustration, restrained
and tense
Composition/framing: medium-wide street scene with the lawman as anchor
Lighting/mood: afternoon light, watchful, hard
Color palette: dust, black coat, pine wood, brass badge, faded paint
Materials/textures: badge, gun belt, boots, porches, timber fronts
Constraints: 1870s law enforcement only
Avoid: action-poster gunfight, modern policing gear, text, watermark
```

### Spot 13 - Horse handling in detail

- Illustration purpose: support the procedure chapter with a specific
  rope or saddle action.
- Placement: Chapter 15, after `Throwing a rope - head catch`.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a cowboy roping and controlling a horse in a detailed
working moment
Scene/backdrop: corral or open yard
Subject: rope, horse head, rider position, and tack in motion
Style/medium: realistic historical western illustration, instructional
and kinetic
Composition/framing: medium action scene with the rope path visible
Lighting/mood: bright daylight, focus, effort
Color palette: horse brown, rope tan, leather, dust, sky blue
Materials/textures: rawhide rope, sweat, wood rails, saddle leather
Constraints: physically plausible roping only
Avoid: stunt composition, modern tack, text, watermark
```

### Spot 14 - Cattle drive hazards

- Illustration purpose: show the trail and river-crossing danger in the
  cowboy chapter.
- Placement: Chapter 16, after `River crossings` or `Stampedes`.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a cattle drive at a river crossing or stampede edge,
with riders fighting to keep order
Scene/backdrop: river ford or rough open country
Subject: cowhands, herd, river, and weather stress
Style/medium: realistic historical western illustration, expansive and
dangerous
Composition/framing: wide action scene with moving herd and strong flow
Lighting/mood: stormy light or hard morning light, urgency
Color palette: mud brown, water gray, cattle hide, sky blue, dust tan
Materials/textures: wet hide, rope, hoofprints, spray, canvas
Constraints: 1870s trail drive reality only
Avoid: heroic slow-motion action, modern fences, text, watermark
```

### Spot 15 - Mine face and timbering

- Illustration purpose: show the engineering detail of underground work.
- Placement: Chapter 18, after `Square-set timbering` or `Loading and
  firing`.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: miners and timber supports in a narrow underground
workface with ore and tools around them
Scene/backdrop: hardrock mine interior
Subject: timbered shaft, tools, ore car, and miners at work
Style/medium: realistic historical western illustration, cramped and
technical
Composition/framing: tight interior with beams and tools forming the
frame
Lighting/mood: lamplight, dust, strain
Color palette: coal black, lantern gold, timber brown, iron gray
Materials/textures: rock, timber, ore, sweat, powder smoke
Constraints: period mine engineering only
Avoid: later mining machinery, modern lights, text, watermark
```

### Spot 16 - Army column and Buffalo Soldiers

- Illustration purpose: show the Army as a moving institution, not just
  a fixed post.
- Placement: Chapter 19, after `The cavalry column` or `The Buffalo
  Soldier Regiments`.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a mounted army column moving across open country with
Black troopers among the line
Scene/backdrop: plains or desert campaign route
Subject: cavalry column, officers, pack gear, and troop horses
Style/medium: realistic historical western illustration, disciplined
and expansive
Composition/framing: wide moving column with strong rhythm and scale
Lighting/mood: hard daylight, dust, endurance
Color palette: olive, khaki, horse brown, dust gray, flag red
Materials/textures: saddles, rifles, packs, canvas, horse sweat
Constraints: 1870s Army uniform and equipment only
Avoid: later military gear, parade polish, text, watermark
```

### Spot 17 - Outlaw escape and pursuit

- Illustration purpose: tighten the outlaw chapter with motion and
  consequences.
- Placement: Chapter 20, after `The Posse` or `The Train Robbery`.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: outlaws riding hard away from a rough pursuit through
country that offers no cover
Scene/backdrop: canyon mouth, badland track, or open ridgeline
Subject: mounted outlaws, exhausted horses, and distant pursuers
Style/medium: realistic historical western illustration, tense and raw
Composition/framing: wide chase scene with strong forward motion
Lighting/mood: late-day dust, urgency, risk
Color palette: dust, brown, black, faded shirt blue, smoke gray
Materials/textures: saddle, reins, dust, sweat, rifle, bedroll
Constraints: period outlaw equipment only
Avoid: cinematic stunt riding, modern weapons, text, watermark
```

### Spot 18 - Gambling tension

- Illustration purpose: show the social pressure around the table.
- Placement: Chapter 21, after `Cheating` or `Women at the Gambling
  Table`.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a gambling room with a table under tension, where the
people at the edge of the room matter as much as the hand
Scene/backdrop: saloon interior
Subject: dealer, gambler, watcher, drink, and concealed risk
Style/medium: realistic historical western illustration, close and
uncomfortable
Composition/framing: medium close scene with hands and faces
Lighting/mood: smoke, lamp glow, suspicion, stillness
Color palette: amber, green felt, black coat, brass, whiskey brown
Materials/textures: cards, chips, glass, cigar smoke, felt, wood
Constraints: 1870s game room only
Avoid: casino glamour, modern chips, text, watermark
```

### Spot 19 - Performance and dance

- Illustration purpose: show entertainment as a working social event.
- Placement: Chapter 22, after `The Saloon and the Dance Hall`.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a dance hall moment with musicians and dancers moving
in a crowded frontier room
Scene/backdrop: saloon or dance hall
Subject: fiddler, dancer, boots, lamps, and packed audience
Style/medium: realistic historical western illustration, lively and
physical
Composition/framing: medium-wide interior with motion in the center
Lighting/mood: warm lamp light, noise, energy
Color palette: amber, sawdust tan, red-brown, black, white shirt
Materials/textures: fiddle wood, boots, smoke, sawdust, hats
Constraints: period instruments and attire only
Avoid: stage show glamour, modern lighting, text, watermark
```

### Spot 20 - Sickroom and death

- Illustration purpose: support the medicine chapter with a quiet, hard
  image of the sickroom.
- Placement: Chapter 23, after `Infection - The Real Killer` or `The
  Dying - What It Actually Looks Like`.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a frontier sickroom with a patient, watcher, and the
plain tools of 1870s care
Scene/backdrop: cabin room or boarding-house room
Subject: doctor bag, basin, bandages, and an exhausted bedside vigil
Style/medium: realistic historical western illustration, quiet and
severe
Composition/framing: medium interior centered on the bed
Lighting/mood: dim light, waiting, grief
Color palette: white cloth, brown wood, iron black, pale skin, gray
Materials/textures: bandages, bottles, blanket, basin, dust
Constraints: 1870s medicine only
Avoid: gore spectacle, romantic death, text, watermark
```

### Spot 21 - Dark frontier aftermath

- Illustration purpose: keep the chapter on violence restrained and
  suggestive.
- Placement: Chapter 24, after `Lynching, Mob Violence, and the Pogrom`
  or `Domestic Violence and the Family Killing`.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: an aftermath scene that implies violence through
absence, fear, and the ruined setting rather than explicit injury
Scene/backdrop: night exterior, damaged room, or abandoned yard
Subject: broken object, closed door, or figure in retreat
Style/medium: realistic historical western illustration, severe and
understated
Composition/framing: low-light composition with strong shadow blocks
Lighting/mood: darkness, ember light, dread
Color palette: black, ash gray, ember orange, dirt brown
Materials/textures: rope, splintered wood, torn cloth, soot, dust
Constraints: do not sensationalize trauma
Avoid: explicit gore, spectacle, text, watermark
```

### Spot 22 - Landscape as subject

- Illustration purpose: give the regional landscape chapter a second
  image that is almost all land.
- Placement: Chapter 25, after `The Regions in Brief` or before the
  vignette.
- Prompt:

```text
Use case: historical-scene
Asset type: interior illustration for an A4 roleplaying supplement
Primary request: a vast western landscape with a tiny rider, horse, or
wagon to show scale and regional character
Scene/backdrop: one named western region, chosen for its specific land
forms and weather
Subject: the land itself, with one small working human figure
Style/medium: realistic historical western illustration, atmospheric
and geographic
Composition/framing: panoramic wide scene with low human presence
Lighting/mood: regional light, seasonal, distant, severe or clear
Color palette: region-specific but natural and restrained
Materials/textures: grass, stone, snow, scrub, sky, dust, river
Constraints: no scenic fantasy, no modern roads, no text, watermark
Avoid: postcard prettiness, oversaturated skies
```
