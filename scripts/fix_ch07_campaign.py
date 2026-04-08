"""
Insert all campaign-seeding content from proposals/ch07-adventure-expansion.md
into corebook/07-the-west-in-the-1870s.md. Four insertion blocks:

A: New archetypes (after "The Manhunters" section, before "The Frontier Town")
B: Political/economic conflicts (after "The Railroads" section)
C: Cultural fault lines (after "The Code of the West" section)
D: Adventure seeds (before "Further Reading")
"""

import re

filepath = r'c:\git-public\Tales-of-the-Old-West-2e\corebook\07-the-west-in-the-1870s.md'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# ─────────────────────────────────────────────────────────────
# BLOCK A: New Archetypes — insert before "### The Frontier Town"
# ─────────────────────────────────────────────────────────────
BLOCK_A = """
### Roles to Fill in the West

The outlaw, the bounty hunter, and the farmer are well-worn archetypes—but the frontier was full of people who fit none of those categories and whose lives generated just as much drama. These are the overlooked roles: the characters who navigated the West's middle ground, who were neither completely lawless nor entirely respectable, and who saw the era from angles the dime novels never considered.

### The Con Artist and the Snake Oil Trade

Travelling medicine shows were a fixture of frontier life in the 1870s. A showman would roll into town in a brightly painted wagon, set up a stage, and spend two or three days performing—magic tricks, music, testimonials, comedy—before selling his patent medicines, elixirs, and guaranteed cures at premium prices. The shows were entertainment in a world with almost none, and crowds turned out eagerly. The medicines were almost universally fraudulent, containing whiskey, opium, cocaine, glycerine, and whatever else was cheap and produced a satisfying sensation. Clark Stanley's Snake Liniment, when actually tested by the federal government in 1917, was found to contain no snake oil whatsoever—just mineral oil, beef fat, red pepper, and turpentine.

The confidence man was a more sophisticated operator. The long con—a multi-day or multi-week fraud involving planted conspirators, fake opportunities, and the deliberate cultivation of a victim's greed—was practiced across the West. "Land fraud" was particularly common: selling deeds to land the seller didn't own, often to recent immigrants who couldn't read English. Mining claim fraud, stock fraud, and gold brick scams—selling painted lead bricks as gold—were widespread enough that the US Post Office established a mail fraud division specifically in response.

Jefferson "Soapy" Smith ran the most sophisticated criminal operation in Skagway, Alaska, including a fake telegraph office that charged customers for sending "messages" on a wire connected to nothing. He was shot dead in 1898 by a vigilante committee that had finally run out of patience. His story is the arc of the con artist's life compressed into a single biography: brilliant, profitable, and lethal.

For a campaign, the medicine show as a travelling party base—moving from town to town, performing, selling, gathering information, and staying one step ahead of angry former customers—is an excellent structure. The party may include a con artist or work as one. They may be hired to expose a fraud, run one, or find themselves the target of a long con they didn't see coming.

### The Frontier Press

Every town of any size had at least one newspaper, often two or three competing for readers and political patronage. Frontier editors wielded enormous influence: they shaped public opinion, backed political candidates, printed wanted notices, whipped up mob sentiment, and occasionally got shot for their opinions. The editor's office was frequently targeted by those he criticized—presses were smashed, editors were horsewhipped, and at least a few were murdered.

Yellow journalism was emerging in this period: the deliberate exaggeration, fabrication, or sensationalization of news to drive circulation. The James gang's sympathetic press coverage was a direct product of this environment—editor John Newman Edwards of the Kansas City Times practically invented Jesse James as a romantic outlaw, turning a violent bank robber into a folk hero through the power of print. A party working with or against a yellow journalist creates fascinating moral questions about truth, narrative, and consequences.

The newspaper editor as a patron NPC or party role is underused. He knows everything that happens in town—people come to him with tips, rumors, complaints, and grievances. He needs stories investigated, witnesses tracked down, and evidence gathered. He can print revelations that change the political landscape of a campaign in a single issue—or be silenced before he does. A reporter has been murdered before publishing a story. A rival paper is running a smear campaign that is destroying a fair election. A newspaper editor discovers that the town's most respected citizen is a wanted man. Each is a campaign engine.

### The Frontier Lawyer

Legal practice on the frontier was radically variable. Some frontier lawyers were genuine professionals who had read law in Eastern offices and passed bar examinations. Others had read a single law book and called themselves attorneys. The distinction was difficult to assess from the outside, and many a client was represented by someone who barely understood the proceedings.

Territorial courts were a political battleground. Federal judges were patronage appointments, often going to friends and allies rather than qualified jurists. A judge in the pocket of the railroad, the cattle barons, or the local political ring could destroy lives with impunity. Judge Roy Bean, "the law west of the Pecos," held court in his saloon and administered a charming, idiosyncratic, and occasionally arbitrary justice that is half comedy and half horror.

Land title litigation was one of the most consequential legal battles of the era. The Cartwright Land Grant cases in New Mexico, the California Land Act battles, the disputes over railroad grants—these were fought in courts and often decided as much by bribery and fraud as by evidence and law. A party retained to gather evidence for a land case, protect a witness, or serve a summons across hostile territory has a natural adventure framework rooted in real history. The lawyer as a party member sees the world through a different lens—seeking information, building arguments, identifying leverage. The lawyer who is crooked can be the campaign's most effective villain. The one who is honest is probably the most endangered person in the story.

### The Frontier Photographer

Photography was transformative in the 1870s West, and the frontier photographer is a wildly underused campaign archetype.

The technology was cumbersome: glass plate negatives coated with wet collodion emulsion had to be exposed and developed within minutes of preparation. This meant photographers traveled with a darkroom wagon—a rolling chemical laboratory weighing hundreds of pounds. Getting a photograph required coating the plate, rushing to take the exposure, and rushing back to develop before the emulsion dried. Working under these constraints in desert heat, winter cold, on precarious mountain ledges required physical courage as much as technical skill.

**William Henry Jackson** photographed the Hayden Survey and produced the first photographs of Yellowstone that helped convince Congress to protect it—images that literally changed history. **Timothy O'Sullivan** documented the geological surveys of the Southwest, producing haunting photographs of landscapes that few white Americans had ever seen. An expedition photographer is a party role that gets characters into remote, dangerous territory with a clear institutional patron.

The photographer's evidence was uniquely powerful in an era with no other form of objective documentation. A photograph of a massacre site, a corrupt official, or a stolen brand could be worth more than any testimony—and that made frontier photographers targets for anyone with something to hide. A photographer has images that prove a powerful man committed a crime. Getting those plates to a city newspaper alive is the mission. An expedition photographer discovers ruins in a remote canyon that don't fit any known history. A photographer's studio is broken into and every image of a particular subject has been taken or destroyed. Each is a ready campaign hook.

### The Army Scout and Guide

By the 1870s, the civilian scout and guide occupied one of the most respected and most morally complex positions on the frontier. The Army could not operate effectively without men who knew the terrain, could track, could communicate with Native languages and customs, and could survive in the wilderness indefinitely. These scouts were almost never regular soldiers: they were hunters, trappers, former mountain men, mixed-heritage frontiersmen, and a significant number of Native Americans scouting against rival tribes.

**Native American scouts** were used extensively throughout the Indian Wars, and their role is profoundly uncomfortable. Apache scouts helped track other Apaches. Crow scouts guided the Army against the Lakota. Pawnee scouts worked with the Army against the Sioux. These men had their own reasons—tribal rivalries, economic necessity, personal grievances—but the image of Native men helping the Army destroy Native resistance is one of the frontier's sharpest moral ironies.

**Kit Carson**, by the 1870s already a legendary figure in his own lifetime, spent his career as a trapper, scout, Army guide, and agent. His record was mixed: he was genuinely capable, genuinely respected, and he personally oversaw the forced removal of the Navajo on the Long Walk—burning crops, destroying orchards, killing livestock to force surrender. A scout's loyalties were always divided, their morality always tested. The scout-guide as a party role is the group's interface with the wilderness: he knows where the water is, which passes are guarded, and what the signs on the trail mean. He knows people on both sides of every conflict. He is invaluable, and he is permanently at risk.

### The Circuit Preacher and the Revival

The circuit preacher rode a regular route through scattered communities, performing baptisms, marriages, funerals, and Sunday services for communities too small and poor to support a full-time minister. These men were tough, pragmatic, and often remarkable—riding hundreds of miles a month in all weathers, carrying their church in their saddlebags. Some were genuine men of faith; some were frauds; most were somewhere in between.

**Camp meetings and revivals** were among the most significant social events on the frontier. A revival could draw crowds of thousands to a rural clearing, camping for days in a temporary city of tents. The emotional intensity—the preaching, the singing, the public confessions, the mass conversions—could border on mass hysteria. Critics documented seizures, involuntary shouting, rolling in the dirt ("the jerks"), and what they described as sexual licentiousness that followed the religious ecstasy.

Religious conflict was substantial. Methodists, Baptists, Presbyterians, Catholics, Mormons, and numerous smaller sects competed fiercely for souls, church buildings, political influence, and the allegiance of communities. The Mormon question was politically explosive throughout the 1870s—federal attempts to suppress polygamy pitting constitutional interpretation against religious freedom. Anti-Catholic sentiment, imported from the East, occasionally erupted in violence against Irish and Mexican communities.

A charismatic revival preacher is drawing enormous crowds and enormous donations—is he a genuine man of faith, a fraud, or something more sinister? A dying man confesses a crime to the circuit preacher during last rites. The minister possesses information that could save an innocent man and condemn a guilty one, and he needs help resolving it without violating his conscience. A small town is being torn apart by a religious feud between two congregations that has turned violent. Each is a complete adventure.

### The Surveyor and the Land Rush

The government surveyor was one of the most consequential figures in the West—and one of the most hated by Native peoples, Mexicans, and settlers who understood what a surveyor's arrival meant. Surveyors worked across the West for the General Land Office, running baselines and meridians, establishing township and section lines that divided the landscape into the geometric grid visible from the air today. Their work made the Homestead Act possible. Native communities understood that the surveyor's chains were the precursor to dispossession—when the surveyors came, the soldiers and settlers followed. Surveyors were attacked, kidnapped, and killed.

Land fraud was rampant. Surveyors who could be bribed filed false surveys awarding rich land to political allies. The Desert Land Act of 1877 and the Timber Culture Act were systematically defrauded by cattle barons and railroad companies. Dummy homestead entries—filed in the names of fictional or paid individuals—were how large interests assembled vast holdings against the intent of the law. A surveyor who couldn't be bribed, or who stumbled onto evidence of fraud, was a problem to be solved.

The **land rush**—the dramatic opening of territory to settlers racing to file claims—is one of the West's great spectacle events. The Oklahoma Land Rush of 1889 was the largest: settlers lined up along the border and raced at a gunshot to stake claims on 160-acre homesteads. "Sooners" who had sneaked into the territory early to claim the best ground gave their name to the state's football team. The competitive, legally complex, and physically dangerous scramble for land is natural adventure territory.

### The Immigrant in the West

The West of the 1870s was one of the most ethnically diverse places in North America, and the immigrant communities who built it are underrepresented as player archetypes.

**Irish immigrants**, many driven by the famine and subsequent economic collapse, dominated the labor force of the Union Pacific Railroad and the urban working class. The Irish were simultaneously discriminated against—"No Irish Need Apply" signs appeared in Eastern cities—and, being nominally white, given access to opportunities denied to Black and Asian workers. Irish communities in San Francisco, Denver, and Butte were tight-knit, politically powerful, and often in violent conflict with other immigrant groups.

**German immigrants** were the largest non-English immigrant group in the country by the 1870s. German political refugees from the failed 1848 revolutions—the "Forty-Eighters"—brought radical democratic and socialist ideas that would eventually fuel the American labor movement. German communities maintained their language, their culture, their beer gardens, and their political traditions with fierce pride.

**Scandinavian immigrants** settled heavily in the Dakotas and Minnesota, farming the northern plains. Norwegian, Swedish, and Danish communities established churches and community organizations that maintained their languages for generations. Their experience—isolated on the vast northern prairie, maintaining cultural identity against assimilation pressure—is a rich campaign background.

An immigrant character brings specific pressures to a game: language barriers, cultural isolation, suspicious neighbors, the difficulty of navigating legal systems they don't understand, and the constant tension between assimilation and identity. They also bring the motivation of someone who has sacrificed everything to be here and is not inclined to walk away from a fight.

"""

BLOCK_A_MARKER = "### The Frontier Town: Boomtown to Ghost Town"

# ─────────────────────────────────────────────────────────────
# BLOCK B: Political/Economic Conflicts — insert before "### Addiction"
# ─────────────────────────────────────────────────────────────
BLOCK_B = """
### Territorial Politics and Statehood

The question of whether a territory would become a state was one of the most consequential political battles of the era—and it was fought dirty.

Statehood meant self-governance: an elected governor instead of a federal appointee, elected judges, representation in Congress, and control over public land within state borders. The party in Washington had enormous financial and political incentive to delay statehood for territories they didn't control and to rush it for those they did. **Territorial rings**—the corrupt networks of officials, businessmen, and political allies who ran territories like private fiefdoms—were most powerful precisely because territories lacked the democratic oversight that states possessed. The Santa Fe Ring in New Mexico, the Whiskey Ring nationally, and the Star Route fraud in the postal system were all products of this environment. A party working to expose or bring down a territorial ring has a multi-session campaign framework with built-in escalation.

**Election fraud** was brazen. Ballot stuffing, voter intimidation, the voting of dead men, and the "repeater"—a man who voted under multiple names at multiple polling places—were standard practice. Armed men at polling places prevented certain voters from casting ballots. Election judges were bribed to certify fraudulent results. A pivotal election in a territory or state—with a corrupt machine on one side, reformers and their enemies on the other—is a natural campaign fulcrum.

### The Panic of 1873 and Economic Collapse

The Panic of 1873 was one of the most severe financial crises in American history, and its effects on the West were devastating and long-lasting.

The collapse of banking house Jay Cooke & Company in September 1873, which had overextended itself financing the Northern Pacific Railroad, triggered a bank run that closed the New York Stock Exchange for ten days. What followed was the "Long Depression"—a contraction that lasted until 1879. Banks foreclosed on farms and ranches. Unemployment in the cities reached 25%. Wages were cut repeatedly; workers who resisted were replaced. The depression drove waves of desperate men West, fueling both settlement and crime. Many of the outlaws of the late 1870s—the desperados filling Indian Territory and the mining camps—were men broken by the economic collapse who had nothing left to lose.

The **cattle market collapse** of the early 1880s compounded the misery. Overproduction, drought, the catastrophic winter of 1886-87, and falling beef prices destroyed the open range cattle industry. Ranch owners went bankrupt. Cowboys found themselves unemployed by the thousands. The economic despair that produced the range wars and the drift toward outlaw life was not a character flaw—it was the predictable result of an economic system that had collapsed on the people at the bottom of it.

For a campaign, the Panic of 1873 provides context for why so many people are desperate, angry, and willing to break the law. A boom-era bank calling in loans spawns a wave of foreclosures. A town whose economy was built on cattle finds itself ruined in a single bad winter. A desperate man who was a decent farmer three years ago becomes an outlaw because there is no other option. The economics of the period are a campaign engine.

### Water Wars

In the arid West, water was more valuable than gold—and who controlled it determined who survived.

**Prior appropriation**—the legal doctrine that established water rights based on first use rather than land ownership—created a permanent source of conflict. The man who arrived first and diverted a stream had the right to that water even against a downstream landowner. This drove upstream diversions, dam building, and the deliberate monopolization of water sources by those with the knowledge and resources to act first. Cattle barons who controlled the only water for twenty miles controlled everything around it.

**Irrigation disputes** in Arizona, New Mexico, and California produced their own violence. The acequia systems—communal irrigation networks built by Hispanic and Pueblo communities centuries before Anglo arrival—were targeted by speculators and settlers who wanted the water rights. Communities that had maintained these systems for generations found them legally stripped away or physically damaged by upstream diverters.

**Sheep and cattle** were another water-war fault line, distinct from the cattle baron versus nester conflicts. Sheep ate grass down to the root and fouled water sources in ways that cattle ranchers considered catastrophic. Cattlemen dynamited sheep herds in canyon passes. Sheepmen were run off range by armed riders. The violence was not just economic—it carried a class contempt, since in the culture of the open range, sheep were considered beneath cattle, and sheepmen beneath cattlemen. A water dispute or sheep-versus-cattle range conflict is an ideal short adventure: concrete stakes, clear antagonists, and a community whose survival literally depends on resolution.

### The Temperance Wars

The temperance movement—the campaign against alcohol—was one of the most powerful political forces of the 1870s West, and it generated fierce, sometimes violent conflict.

The **Women's Christian Temperance Union**, founded in 1874, rapidly became one of the most effective political organizations in the country—remarkable given that women couldn't vote in most places. WCTU members organized, lobbied, and demonstrated. Carry Nation, the most famous temperance activist, conducted "hatchetations"—entering saloons with a hatchet and destroying the bottles and fixtures—across Kansas. She was jailed dozens of times and treated imprisonment as an honor. Kansas enacted the first statewide prohibition law in 1880, and the battles over prohibition in individual towns and counties—saloons defying the law, sheriffs either enforcing or ignoring it based on who paid their salary, and temperance advocates taking matters into their own hands—are natural adventure settings.

The conflict was not simply moral; it was economic and ethnic. Saloon owners, gambling interests, and the "sporting" economy had enormous political power. Immigrant communities—Irish, German—saw drinking as cultural practice and viewed temperance as ethnic targeting dressed up as reform. Towns profiting from the vice economy fought back hard. Dry towns and wet towns in the same county meant that men rode long distances for a drink, that counties became battlegrounds over the question, and that the sheriff of a dry town who tried to close down a saloon backed by the most powerful men in the county was measuring his life expectancy in weeks.

"""

BLOCK_B_MARKER = "### Addiction, Whiskey, and Patent Medicine"

# ─────────────────────────────────────────────────────────────
# BLOCK C: Cultural Fault Lines — insert before "### Vigilante Justice"
# ─────────────────────────────────────────────────────────────
BLOCK_C = """
### Secret Societies and Fraternal Organizations

Secret societies were a major feature of 1870s American life, and the West was no exception—they provided mutual aid, political networks, and sometimes dangerous power.

The **Freemasons** were present in virtually every Western town of any size. Masonic membership provided social network, business connections, mutual aid, and a brotherhood that transcended local divisions. Many Western lawmen, politicians, and businessmen were Masons—Wyatt Earp was, as were numerous governors, judges, and generals. The Masons were not sinister in themselves, but their influence was real: a Mason who needed help found it among fellow Masons, and a non-Mason navigating a Masonic-dominated establishment was playing with a hand tied behind his back.

The **Knights of Labor**, founded in 1869, was the first major American labor organization, accepting workers regardless of craft, race, or gender. By the early 1880s it had over 700,000 members. In the mining West, KOL organizing produced strikes, confrontations with Pinkerton agents, and violent suppression by company-hired enforcers. The conflict between organized labor and corporate power played out in mining camps and railroad towns across the West in ways that make compelling campaign territory: a labor organizer is exactly as dangerous as an outlaw to the right kind of powerful man.

**Anti-Chinese tongs** and Chinese secret societies controlled much of the economic and social life of Chinese communities. Rival tongs conducted "tong wars"—assassinations, organized brawls, and commercial warfare—over control of gambling, prostitution, and business in Chinatowns. For outsiders, navigating Chinese community politics meant navigating tong structures; ignoring them was dangerous. A Chinese party member who has a history with one tong finds that history following him across the West.

The **Ku Klux Klan** and its successors—the White League, the Red Shirts—were active in the former Confederate states and extended their influence into parts of the West. Their capacity for organized violence, and the total inability of most local law enforcement to stop them, made them effective instruments of terror. The Klan is not a mystery or a secret in this period—its membership was often known and its political activities were open. It was a political organization that used murder as a policy tool, and it operated openly because the law was afraid of it.

### Utopian Communities and the Mormon Question

The 1870s West attracted not only individuals looking for opportunity but entire communities seeking to build alternative societies—and their grand experiments were fascinating, sometimes heroic, and often catastrophic.

**Mormon Utah** was the most successful and most controversial. Founded by Brigham Young in the Salt Lake Valley in 1847, the Utah Territory by the 1870s was a functioning theocratic community: the LDS Church controlled politics, economics, and social life. Polygamy—the "Principle"—was openly practiced and became the central flashpoint with the federal government. The Edmunds Act of 1882 criminalized polygamy and unleashed a wave of federal prosecution that drove polygamist families into hiding and exile. Federal marshals hunted polygamists across the territory; communities protected their own. A campaign set in Utah Territory in this period is set in a community that is simultaneously devout, self-sufficient, paranoid, and under siege—a pressure cooker with its own internal conflicts and a federal enemy bearing down from outside.

**Utopian secular communities** also proliferated: cooperative farming settlements, free-love communities, anarchist communes. Most failed within a few years. The collision between idealistic communal visions and the harsh pragmatics of frontier survival produced either transformation or collapse. A campaign involving a utopian community—its internal conflicts, its external enemies, and the question of what it is actually willing to compromise to survive—is rich territory. The community's founding ideals may be genuine; so may the failure of those ideals under pressure.

### Natural Disasters as Campaign Events

The frontier West was subject to natural violence of a scale that modern Americans rarely experience, and these events are underused as campaign catalysts.

**Prairie fires** killed people and livestock, destroyed homesteads, and could consume thousands of square miles in hours. They moved faster than a horse could run in some conditions. Frontier communities had organized fire-fighting systems—plowing firebreaks, burning back-fires—that required community cooperation and could still fail catastrophically. A prairie fire threatening a town, with suspected arson behind it, is the Western equivalent of a dungeon on fire: urgent, dangerous, and freighted with political consequences once the immediate crisis passes.

**The locust plagues** of 1874 to 1877 devastated the Great Plains. Clouds of Rocky Mountain locusts—sometimes covering thousands of square miles—descended and consumed everything green: crops, grass, wooden tool handles, leather harnesses, wool clothing. Farmers who had worked for years to build homesteads found them stripped bare in hours. The economic devastation was catastrophic and drove a massive exodus from the plains. A community staring down a plague of locusts, making decisions about whether to stay or go, is a campaign situation with no heroes and no clean answers.

**The Blizzard of 1886-87**—the "Great Die-Up"—destroyed the open range cattle industry and killed hundreds of people. Entire herds froze or starved. Ranch hands were caught on the range and died. Survivors found a changed landscape: the era of the open range was over, the cattle corporations were bankrupt, and an entire way of life had ended in a single winter. A campaign set in the aftermath of this disaster—people trying to survive, collect on debts, find missing persons, and salvage something from the wreck—writes itself.

**Flash floods and river floods** in the canyon lands and river bottoms regularly wiped out towns, ranches, and mining operations. The Missouri, the Kansas, and the Arkansas rivers all flooded catastrophically during this period. A flood as a campaign event—a town in danger, difficult choices about what to defend and who to save, the aftermath of wreckage—is a proven scenario structure that works at any level.

"""

BLOCK_C_MARKER = "### Vigilante Justice"

# ─────────────────────────────────────────────────────────────
# BLOCK D: Adventure Seeds — insert before "### Further Reading"
# ─────────────────────────────────────────────────────────────
BLOCK_D = """
### Campaign Seeds

The following are concrete scenario frameworks drawn from documented historical conditions, suitable for one to three sessions each. They are not complete adventures—they are ignition points.

**The False Survey.** A land agent has been filing fraudulent survey returns, claiming rich farmland as worthless desert to prevent homestead settlement and preserve a cattle baron's grazing access. A family has been driven off their legal claim by legal threats backed by guns. The party is hired to find the corrupt surveyor who can testify, gather the documentary evidence, and get both to the federal land office alive. The cattle baron has hired killers, and the local sheriff works for him.

**The Forged Deed.** A prosperous Mexican ranching family is being dispossessed through a forged land grant. Their title, valid under Spanish law and supposedly guaranteed by the Treaty of Guadalupe Hidalgo, has been replaced in the county records with a forgery. The original is missing. Someone has a copy—in a dead man's saddlebag, in a San Francisco lawyer's office, in the possession of a man who is afraid to come forward. Find it before the sheriff serves the eviction papers.

**The Poison Water.** A mining operation upstream has contaminated the only reliable water source for a small ranching community. The ranchers are dying—cattle first, then people. The mining company has lawyers, money, and friends in the territorial government. The party must gather evidence, find experts willing to testify, and get the case before a judge who isn't already in the company's pocket.

**The Election.** A territorial election is three days away. A reform candidate, if elected, will investigate the corruption that has run the territory for a decade. The machine is using every tool available: fraud, coercion, violence. The reform campaign needs protection, needs evidence of ballot fraud gathered and preserved, and needs its candidate alive. The party may be working for either side—or trying to ensure the election is actually free, which both sides will oppose for their own reasons.

**The Medicine Show Murder.** A traveling medicine show has left a dead man in the last three towns it visited. The deaths were ruled natural causes—heart failure, the doctor said—but the dead men each paid a very large sum for a private "treatment" the day before they died. The showman is charming, elusive, and always one town ahead. What is he selling, who are his real targets, and is he working alone?

**The Safe Passage.** A prominent witness to a major crime—or a family fleeing a range war, or a mixed-race couple trying to reach a state where their marriage is legal, or a government surveyor carrying reports of land fraud that would embarrass powerful men—needs to travel three hundred miles across territory where they will be killed if found. The party is hired to get them there. Pursuit is inevitable. The terrain is not cooperative.

**The Burned-Out Homestead.** The party arrives at a farm to find it burned, the family missing. The tracks lead in three different directions and the story that the nearest town tells doesn't add up. Was it raiders? The land company? A personal feud? One of the missing family members is still alive somewhere nearby, and someone in town knows more than they're saying.

**The Reporter's Story.** A young correspondent for an Eastern newspaper has ridden into the territory to report on conditions. She has found a story bigger than she expected—evidence of systematic fraud in federal Indian agency contracts that implicates men in Washington. She sent one wire before disappearing. The party has to find her, find what she found, and decide whether getting that story published will save lives or start a war.

**The Counterfeiter.** High-quality counterfeit banknotes—better than most people have ever seen—are circulating across three counties. The plates must have been made by a genuine engraver, possibly a former US Mint employee. The Secret Service, established in 1865 specifically to combat counterfeiting, has sent one agent who has been in town for two weeks and is running out of leads. He needs help from people who know the territory and the people in it. Not everyone he suspects is guilty. Some of the guilty ones are protected.

**The Circuit Court.** A travelling federal judge arrives in town to hold court for a week. The docket includes a dozen cases—civil claims, criminal charges, a disputed will, a murder. Half the cases involve powerful local interests; the judge's clerk has already been bribed once. The defendants and plaintiffs all want the party's help in different ways. Some are guilty; some are innocent; most are both, depending on which charge you're looking at. The judge is honest but mortal, and there are men who do not want him to reach the next town.

**The Telegraph Sabotage.** The telegraph line connecting this part of the territory to the outside world has been cut and the operator attacked—the morning before a large payroll shipment was due to pass through. Someone didn't want word to get out in either direction. Who cut the wire, what do they want, and what else is moving on the road today that the party should know about?

**The Quarantine.** A herd of cattle has been flagged as infected with Texas Fever—the tick-borne disease that could devastate local herds if it spread. The cattle must be destroyed or contained for weeks. The owner is a man who has borrowed everything to buy this herd and will be ruined if it's destroyed. He believes the quarantine is fraudulent—a competitor's trick to remove him from the market. Is he right? Is the fever real? A town's beef supply and a man's livelihood are both on the line, and someone is lying.

"""

BLOCK_D_MARKER = "### Further Reading"

# ─────────────────────────────────────────────────────────────
# Apply all four insertions
# ─────────────────────────────────────────────────────────────
def insert_before(content, marker, block):
    idx = content.find(marker)
    if idx == -1:
        raise ValueError(f"Marker not found: {marker!r}")
    return content[:idx] + block + content[idx:]

original_len = len(content)

content = insert_before(content, BLOCK_A_MARKER, BLOCK_A)
content = insert_before(content, BLOCK_B_MARKER, BLOCK_B)
content = insert_before(content, BLOCK_C_MARKER, BLOCK_C)
content = insert_before(content, BLOCK_D_MARKER, BLOCK_D)

# Clean up any triple+ blank lines
content = re.sub(r'\n{3,}', '\n\n', content)

with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print(f"Before: {original_len:,} chars")
print(f"After:  {len(content):,} chars")
print(f"Added:  {len(content) - original_len:,} chars")
