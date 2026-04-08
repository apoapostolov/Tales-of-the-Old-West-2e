"""
Add optimism, adventure tropes, and expanded outlaw/bounty hunter content to Ch07.
Balances the chapter's darkness with genuine hope, resilience, and adventure hooks.
"""

filepath = r"c:\git-public\Tales-of-the-Old-West-2e\corebook\07-the-west-in-the-1870s.md"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

changes = 0

# ============================================================
# 1. After the intro paragraphs (before "### The Land"),
#    insert a framing section on adventure and optimism
# ============================================================

ADVENTURE_FRAME = '''\
### The Promise of the West

For all its darkness\u2014and this chapter does not shy from the darkness\u2014the West was also a place of genuine possibility, and that is what drew people to it in their millions. The promise was real even when the reality was brutal. A man with nothing could stake a claim and build something. A woman fleeing an abusive marriage in Philadelphia could reinvent herself in a Colorado mining town where nobody knew her name. A formerly enslaved man could ride for a cattle outfit where his skill in the saddle mattered more than the color of his skin\u2014at least some of the time.

The West attracted dreamers, schemers, idealists, and the desperate in roughly equal measure. It attracted people who had failed everywhere else and people who had never been given the chance to try. For every ruthless cattle baron, there was a schoolteacher who rode twenty miles through snow to reach her students. For every corrupt Indian agent, there was a missionary or doctor who genuinely tried to help. For every town built on vice, there was a community of homesteaders who built a church, dug a well, started a school, and looked after their neighbors.

This is what makes the West compelling for a campaign: not that it was Hell, but that it was a place where ordinary people confronted extraordinary circumstances and had to decide, every day, what kind of person they were going to be. The darkness provides the stakes. The possibility of decency provides the hope. A game that has both is a game worth playing.

### The Lure of Adventure

The West offered something that the settled, industrialized East could not: the genuine unknown. Beyond the next ridge, past the next river, over the horizon\u2014there were places no white person had mapped, caves no one had explored, ruins no European had seen. The frontier was the edge of the known world, and it called to a particular kind of person.

**Mountain men** like Jim Bridger, Kit Carson, and Jedediah Smith had blazed trails across the Rockies and the Great Basin decades before the settlers followed. By the 1870s the era of the solitary trapper was over, but the type persisted: scouts, guides, hunters, and self-taught naturalists who knew the country better than anyone alive. These men\u2014and a few women\u2014moved between the white and Native worlds, speaking multiple languages, understanding both cultures, trusted by neither entirely. They are perfect player characters: people with rare skills, divided loyalties, and an intimate knowledge of a landscape that could kill the unprepared.

**Treasure and lost mines** were a genuine obsession of the frontier. The legend of the Lost Dutchman\u2019s Mine in Arizona\u2019s Superstition Mountains, the rumored Aztec gold caches of New Mexico, the lost Spanish missions supposedly hiding fortunes in silver\u2014these stories circulated endlessly, and people died searching for them. Some were pure fiction. Others were based on real finds: prospectors did stumble onto fortunes. The Comstock Lode was found by accident. The Tombstone silver strike made Ed Schieffelin rich after he was told the only thing he\u2019d find in Apache country was his own tombstone. The possibility of sudden, transformative wealth\u2014just over the next hill\u2014motivated thousands and makes for irresistible campaign hooks.

**Frontier exploration** was still ongoing in the 1870s. John Wesley Powell\u2019s harrowing expedition down the Colorado River through the Grand Canyon occurred in 1869, with a second expedition in 1871\u201372. Ferdinand Hayden\u2019s geological surveys of Wyoming led directly to the creation of Yellowstone National Park in 1872\u2014the world\u2019s first. These expeditions were genuinely dangerous: men drowned, starved, were injured, or simply vanished. They were also thrilling, producing some of the most dramatic first-person accounts in American literature. An expedition-based campaign\u2014mapping unknown territory, cataloguing species, photographing landscapes never before seen by outsiders\u2014is a rich adventure framework rooted in real history.

**Stagecoach travel** was the connective tissue of the West before the railroads reached everywhere. The Butterfield Overland Mail, Wells Fargo, and dozens of smaller lines ran coaches across thousands of miles of wilderness, connecting towns, mining camps, and military posts. A stagecoach journey was an adventure in itself: days of bone-jarring travel on unsprung coaches, through dust and mud, across rivers, over mountain passes, with the ever-present possibility of robbery, breakdown, or Indian attack. Stage stations\u2014rough buildings every ten to fifteen miles where horses were changed and passengers could eat\u2014were isolated outposts staffed by hard men and women, and every one of them has a story. For a campaign, the stagecoach is the quintessential mobile adventure setting: strangers thrown together in a confined space, crossing dangerous country, each with their own secrets and purposes.

'''

marker = "### The Land"
idx = content.find(marker)
if idx >= 0:
    content = content[:idx] + ADVENTURE_FRAME + content[idx:]
    changes += 1
    print("1. Inserted adventure/optimism frame before 'The Land'")
else:
    print("1. FAILED")


# ============================================================
# 2. After "Bounty Hunting and the Pinkerton Agency",
#    before "Vigilante Justice" — insert expanded outlaw
#    bands and bounty hunter content
# ============================================================

OUTLAW_EXPANSION = '''\

### The Great Outlaw Gangs

The outlaw gangs of the West were not the freewheeling bands of romantic rebels depicted in dime novels. They were organized criminal enterprises\u2014some sophisticated, some brutal, most both\u2014and their stories offer some of the richest campaign material the period has to offer.

The **James-Younger Gang** (c. 1866\u20131882) was the prototype. Led by Jesse and Frank James with Cole, Jim, John, and Bob Younger, they robbed banks, trains, and stagecoaches across Missouri, Iowa, Kansas, Kentucky, and beyond. What made them distinctive was not their skill\u2014they were competent but not extraordinary\u2014but their public relations. Jesse James cultivated a Robin Hood image through sympathetic newspaper editors, particularly John Newman Edwards, who portrayed the gang as Confederate heroes striking back against Yankee banks and carpetbagger railroads. It was largely fiction\u2014their victims were ordinary people and the gang kept the money\u2014but it worked. Jesse James was arguably America\u2019s first media-manufactured celebrity outlaw. The gang\u2019s end came at Northfield, Minnesota in 1876, when a bank robbery went catastrophically wrong. Armed citizens shot the gang to pieces; the Youngers were captured riddled with bullets. Jesse and Frank escaped, but the gang was finished. Jesse was assassinated by gang member Robert Ford in 1882 for the $10,000 reward.

The **Wild Bunch** (c. 1896\u20131901), led by Butch Cassidy (Robert LeRoy Parker) and the Sundance Kid (Harry Longabaugh), was the last of the great outlaw gangs and in some ways the most successful. Operating from the remote \u201cHole-in-the-Wall\u201d hideout in Wyoming\u2014one of several outlaw refuges in the West\u2019s remote terrain\u2014the Wild Bunch specialized in train and bank robbery and were remarkably effective at evading pursuit. They used relay horses, planned escape routes in advance, and exploited the vastness of the empty West. But the world was closing in: the railroad companies, tired of being robbed, deployed dedicated posses and Pinkerton agents who pursued the gang relentlessly. Cassidy and Sundance eventually fled to South America. Their ultimate fate remains disputed\u2014legend says they died in a shootout in Bolivia in 1908, but some evidence suggests Cassidy may have returned to the US and lived quietly into old age.

The **Dalton Gang** (1890\u20131892) tried to outdo the James boys by robbing two banks simultaneously in their hometown of Coffeyville, Kansas. It was a catastrophic miscalculation. Armed townspeople were waiting. In the space of twelve minutes, four out of five gang members were killed in a storm of gunfire. The citizens of Coffeyville lost four dead as well. The sole surviving Dalton, Emmett, was shot twenty-three times and somehow lived. He served fourteen years in prison, was pardoned, moved to Hollywood, and became a screenwriter. His story\u2014from outlaw to convict to filmmaker\u2014is almost too strange for fiction.

**Sam Bass** ran a short-lived but prolific gang in Texas in the late 1870s, robbing four trains in the Dallas area in rapid succession. Bass was popular with locals\u2014he was generous with money and had a reputation for treating victims with courtesy. He was betrayed by a gang member, Jim Murphy, who informed on him in exchange for dropped charges. Bass was shot by Texas Rangers at Round Rock in 1878 and died two days later on his 27th birthday. His last words, when asked to name his accomplices: \u201cIt is against my profession to blow on my pals. If a man knows anything, he ought to die with it in him.\u201d

The **outlaw hideouts** of the West are campaign settings unto themselves. **Hole-in-the-Wall** in Johnson County, Wyoming, was a valley accessible only through a narrow canyon, easily defended by a handful of men\u2014outlaws used it for decades. **Robbers Roost** in the canyonlands of southeastern Utah was so remote that posses rarely attempted to enter it. **Brown\u2019s Hole** (or Brown\u2019s Park), straddling the Utah-Colorado-Wyoming border, was a haven for rustlers, horse thieves, and fugitives. These were not mythical places\u2014they were real, mapped locations where outlaws rested, planned, and spent their money. A campaign centered on delivering a warrant into one of these refuges, or on the outlaws defending it, writes itself.

### The Manhunters

If the outlaw gangs provide the quarry, the men who hunted them provide the pursuit\u2014and their stories are just as morally complex.

**Bass Reeves** was a formerly enslaved man who became one of the most effective lawmen in Western history. Working as a Deputy US Marshal in Indian Territory (modern Oklahoma) from 1875 to 1907, Reeves made over 3,000 arrests and is said to have killed fourteen men in the line of duty\u2014never once being wounded himself. He spoke multiple Native American languages, used disguises, and operated largely alone in some of the most dangerous territory in the country. Indian Territory was a haven for fugitives from surrounding states, and the jurisdiction of the federal court at Fort Smith, Arkansas\u2014under the notorious \u201changing judge\u201d Isaac Parker\u2014extended across the entire territory. Reeves tracked fugitives for weeks through rough country, and his reputation was so formidable that some men surrendered at the sound of his name. He once arrested his own son for murder\u2014a fact that speaks to his unbending sense of duty and the painful contradictions of frontier justice.

**Judge Isaac Parker** and the Fort Smith court deserve their own mention. From 1875 to 1896, Parker presided over the federal court with jurisdiction over Indian Territory\u2014an area of roughly 74,000 square miles teeming with fugitives, displaced peoples, and violence. He sentenced 160 men to death, of whom 79 were actually hanged\u2014earning him the nickname \u201cHanging Judge.\u201d His deputy marshals\u2014over 200 served during his tenure\u2014rode into Indian Territory to bring back fugitives. Sixty-five of them were killed in the line of duty. The Fort Smith jurisdiction was the most dangerous law enforcement beat in the country, and the deputy marshals who worked it were some of the toughest and most resourceful men in the West.

**Tom Horn** walked the razor\u2019s edge between lawman and hired killer. He worked as an Army scout, a Pinkerton detective, and a \u201cstock detective\u201d for Wyoming cattle barons. In reality, he was an assassin. Hired by ranchers to eliminate suspected rustlers, Horn operated with a signature: he placed a rock under the head of each victim. He was efficient, ruthless, and worked alone. In 1901 he shot and killed 14-year-old Willie Nickell, mistaking the boy for his father. Horn was arrested, convicted\u2014largely on the basis of a drunken confession\u2014and hanged in 1903. His story encapsulates the moral rot at the heart of \u201cstock detective\u201d work: a man employed by wealthy interests to murder inconvenient people, protected until he became inconvenient himself.

**Heck Thomas, Bill Tilghman, and Chris Madsen**\u2014the \u201cThree Guardsmen\u201d of Oklahoma Territory\u2014were Deputy US Marshals who spent years tracking the Doolin-Dalton gang and other outlaw bands through Indian Territory. Thomas killed Bill Doolin with a shotgun in 1896. Tilghman captured \u201cLittle Bill\u201d Raidler. These were men who operated with minimal backup across enormous distances, using tracking skills, local informants, and sheer persistence. Tilghman later became a reformer and film consultant; he was shot and killed in 1924 by a corrupt Prohibition agent. The trajectory\u2014from frontier manhunter to murder victim at the hands of the very kind of lawlessness he\u2019d spent his career fighting\u2014is tragically fitting.

The **Wells Fargo detective** was a different breed. Wells Fargo\u2019s express division maintained its own force of investigators, shotgun messengers, and special agents dedicated to protecting shipments and tracking down robbers. James B. Hume served as Wells Fargo\u2019s chief detective for over thirty years and was one of the most capable investigators in the West. Hume built a systematic approach to criminal investigation that was decades ahead of most law enforcement: he maintained detailed records, studied criminal methods, and used what we\u2019d now call profiling. He personally tracked Black Bart across 28 stagecoach robberies. The Wells Fargo detectives operated in a grey area\u2014private agents enforcing corporate interests, but also providing genuine law enforcement in areas where no one else would.

### The Frontier Town: Boomtown to Ghost Town

Understanding the life cycle of a Western town is essential for any campaign, because the town is not just a backdrop\u2014it\u2019s a character.

A **boomtown** began with a discovery: gold, silver, copper, or the announcement that the railroad was coming through. Within weeks, a bare patch of ground could sprout hundreds of tents, shacks, and rough-hewn buildings. The first businesses were always a saloon, a general store, and a livery stable. Gamblers, prostitutes, merchants, and confidence men arrived almost simultaneously with the miners or cowboys who were their customers. A boomtown had no law, no sanitation, no plan, and no permanence\u2014it was a scramble for money, raw and unregulated.

If the boom held, order emerged\u2014not from above, but from necessity. Merchants who needed stable conditions for trade would push for a town marshal. Property owners would organize a \u201ccitizens\u2019 committee.\u201d A church would be built, then a school. The wildest elements would be pushed, gradually and not always successfully, to the margins. Some boomtowns became real cities: Denver started as a mining camp. San Francisco was a tent city during the Gold Rush. Tombstone went from bare desert to a town of thousands in under two years.

But most booms ended. The mine played out. The railroad chose a different route. The cattle market crashed. And the town died\u2014sometimes slowly, sometimes almost overnight. People packed up and left, taking what they could carry. Buildings were abandoned, sometimes dismantled for lumber, sometimes simply left to the weather. The West is dotted with **ghost towns**\u2014the remains of communities that flourished for a few years and then vanished. Some are just foundations and rubble. Others are eerily preserved, with buildings still standing, furniture still inside, as if the inhabitants simply walked away one morning and never came back. For a campaign, a ghost town is a ready-made adventure location: abandoned structures, hidden cellars, forgotten mines, and the lingering question of what went wrong.

The **cattle town** had its own rhythm. Towns like Dodge City, Abilene, and Wichita existed at the end of the great cattle trails, where the drives from Texas terminated and the herds were loaded onto railcars for Eastern markets. During the season\u2014roughly May through September\u2014these towns exploded with cowboys, money, and mayhem. After the drives ended, the towns went quiet, the transient population vanished, and the permanent residents were left with the mess. The marshals hired for the wild season\u2014men like Wyatt Earp, Bat Masterson, and Wild Bill Hickok\u2014were often let go once the need for them passed. The seasonal nature of cow town life creates a natural campaign calendar: months of anticipation, weeks of chaos, and a long, cold aftermath.

### Resilience, Resistance, and Quiet Heroism

For every atrocity documented in this chapter, there were acts of courage, compassion, and defiance that deserve equal recognition\u2014not to soften the history, but because they are as real and as important as the darkness.

**Native American resistance** was not merely military. It was cultural, spiritual, and existential. Languages were kept alive in secret. Ceremonies were practiced despite prohibition. Children who had been sent to boarding schools returned to their communities and taught what they could to the next generation. The survival of Native cultures through the systematic attempt to destroy them is one of the most remarkable achievements of human resilience in the historical record. Leaders like Chief Joseph, who led the Nez Perce on a 1,170-mile fighting retreat in 1877 while caring for women, children, and elderly\u2014and who surrendered with the words \u201cFrom where the sun now stands, I will fight no more forever\u201d\u2014demonstrated a dignity that shamed the forces arrayed against them.

**Black communities** built lives in the face of relentless hostility. The Exodusters\u2014thousands of formerly enslaved people who migrated to Kansas in 1879\u2014established all-Black towns like Nicodemus, where they built homes, schools, churches, and businesses from nothing on the open prairie. It was an act of extraordinary collective courage: families with almost no resources, traveling hundreds of miles to a place they\u2019d never seen, betting everything on the possibility of freedom. Nicodemus nearly failed\u2014the first winter was brutal, and many settlers left\u2014but it survived, and it stands today as evidence of what determination could accomplish even in the most hostile circumstances.

**Chinese communities** survived through solidarity. Tongs\u2014fraternal organizations often dismissed as criminal gangs\u2014provided mutual aid, dispute resolution, and protection for communities that the law would not protect. The Chinese Six Companies in San Francisco fought discriminatory legislation, funded legal challenges, and organized community defense. When the law was weaponized against them and the society around them was openly hostile, Chinese Americans built institutions of survival that sustained their communities through decades of persecution.

**Women** carved out spaces of agency in a world designed to deny them any. Schoolteachers in one-room prairie schools educated a generation. Frontier doctors like Susan Anderson saved lives with almost no resources. Women like Biddy Mason\u2014born into slavery, she walked behind her owner\u2019s wagon train from Mississippi to California, won her freedom in court, became a nurse, a midwife, and one of the first Black women to own property in Los Angeles\u2014demonstrated that the West\u2019s promise of reinvention was real, even if you had to fight for every inch of it.

**Ordinary human decency** existed alongside the brutality. Neighbors helped neighbors build homes, raise barns, and survive winters. Communities organized to care for the sick. Strangers on the trail shared food and water. Not every encounter between settlers and Native people ended in violence\u2014there were genuine friendships, alliances, and acts of mutual aid. The story of the West is not only a story of what people did to each other at their worst. It is also a story of what they did for each other when it mattered most.

### The Sounds of the West

One overlooked dimension of frontier life that brings a campaign alive is what people actually heard\u2014and what they listened to.

Music was everywhere. Cowboys sang to calm the cattle on night watch\u2014slow, monotonous songs that kept the herd settled. The songs were practical, but they were also the origin of the cowboy ballad tradition. In town, saloons had pianos\u2014or tried to. A piano was one of the most valuable objects in a frontier town, worth hundreds of dollars, and piano players were in demand. The music was popular songs of the day, Stephen Foster melodies, minstrel tunes, dance hall numbers, and whatever the pianist knew. Fiddles were more common than pianos and cheaper; a fiddler at a dance was worth his weight in whiskey.

Mexican and Hispanic communities brought a rich musical heritage: corridos (narrative ballads), rancheras, and the guitar traditions that would eventually merge with Anglo folk music to produce the sound we now think of as \u201cWestern.\u201d Native American music\u2014drumming, chanting, flute\u2014was the oldest music on the continent and continued to be practiced, both openly and in secret, throughout the period.

Church hymns were a staple of community life. In Black communities especially, the spiritual tradition carried over from slavery was a powerful force\u2014music that was simultaneously worship, protest, story, and survival. Camp meetings, revivals, and Sunday services filled the West with singing. A campaign that includes what people sang, hummed, and listened to is a campaign that feels alive.

### The Code of the West

There was no written \u201cCode of the West,\u201d but there were unwritten rules that most people on the frontier understood and generally respected\u2014and violating them could get a person shunned, beaten, or killed.

**Hospitality** was sacred. If a stranger arrived at your homestead, you fed him and offered him a place to sleep. This wasn\u2019t mere courtesy\u2014it was survival. On the frontier, anyone might need help, and refusing it could mean a death sentence. The expectation of hospitality extended to everyone, regardless of whether you liked the stranger or not. Taking advantage of someone\u2019s hospitality\u2014stealing from a host, betraying their trust\u2014was considered one of the lowest offenses.

**A man\u2019s word was his bond.** Written contracts were rare on the frontier. Deals were sealed with a handshake, and breaking your word was a serious matter\u2014not just socially, but practically. In a world without courts, lawyers, or enforceable contracts, your reputation was your currency. A man known to be unreliable couldn\u2019t get work, couldn\u2019t get credit, and couldn\u2019t be trusted as a partner. This is why cattle deals worth thousands of dollars were conducted on a handshake, and why promise-breaking was treated so seriously.

**Don\u2019t steal a man\u2019s horse.** Horse theft was often punished more harshly than murder\u2014and for practical reasons. In the open West, a stolen horse could mean death. A man left afoot in hostile territory, far from water, had a real chance of dying. Horse theft was treated as a potentially lethal act, and the punishment reflected it.

**Mind your own business** was the practical philosophy of people living at close quarters in a lawless environment. A man\u2019s past was his own. Asking too many questions about where someone came from or what they\u2019d done was considered rude at best and dangerous at worst. Many people in the West had things they\u2019d rather not discuss, and the frontier ethic was to let them keep their secrets. This created a culture in which a person was judged by what they did in front of you, not by what they might have done somewhere else\u2014a second-chance ethos that was one of the West\u2019s genuinely appealing qualities.

These unwritten rules coexisted with the violence and exploitation documented throughout this chapter. They didn\u2019t redeem the West, but they did make it livable. For a campaign, the Code provides a framework for social interaction: a set of expectations that every character understands, that creates consequences when violated, and that gives the game world a sense of lived-in authenticity.

'''

marker2 = "### Vigilante Justice"
idx2 = content.find(marker2)
if idx2 >= 0:
    content = content[:idx2] + OUTLAW_EXPANSION + content[idx2:]
    changes += 1
    print("2. Inserted outlaw gangs, manhunters, frontier towns, resilience, sounds, and Code before 'Vigilante Justice'")
else:
    print("2. FAILED")


# ============================================================
# Write result
# ============================================================
with open(filepath, "w", encoding="utf-8", newline="\n") as f:
    f.write(content)

print(f"\nDone. {changes} changes applied.")
print(f"Final file length: {len(content):,} chars")
