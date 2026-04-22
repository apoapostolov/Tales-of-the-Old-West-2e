"""Replace the timeline section in chapter 07."""
import re

filepath = r"c:\git-public\Tales-of-the-Old-West-2e\corebook\07-the-west-in-the-1870s.md"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Find the timeline section boundaries
start_marker = "### Key Events of the Nineteenth Century West"
end_marker = "\n### Territorial Governance"

start_idx = content.index(start_marker)
end_idx = content.index(end_marker)

old_section = content[start_idx:end_idx]
print(f"Found timeline section: {len(old_section)} chars")
print(f"First 100 chars: {repr(old_section[:100])}")
print(f"Last 100 chars: {repr(old_section[-100:])}")

new_timeline = """### Key Events of the Nineteenth Century West

**1836** : Texas declares independence.

**1841** : The Bidwell-Bartleson wagon train takes the first migrants on the Oregon Trail, the eventually well-worn route used by thousands of settlers, from the east to the northwest.

**1845** : Texas is incorporated into the Union as a state. This starts the chain of events that leads to the Mexican\u2013American War, which breaks out in hostilities the following year.

**1848** : The US defeats Mexico and enormous swathes of once-Mexican territory in the west are ceded to the US. As a result of this, along with the Gadsden Purchase, the borders of the Wild West are now set. The Treaty of Guadalupe Hidalgo guarantees the land and citizenship rights of Mexicans remaining in the ceded territories\u2014promises that will be systematically broken in the decades to come.

**1849** : Following the discovery of gold along the American River, the California Gold Rush takes place. Thousands flock west in search of their fortunes. The influx triggers a wave of violence against California\u2019s Native peoples. Within a year, miners, settlers, and state-funded militia units begin organized campaigns of killing, kidnapping, and enslavement targeting Native communities.

**1850** : The population of the West reaches about 500,000, and stagecoach services are becoming more widespread. California is incorporated as a state. The California Act for the Government and Protection of Indians is passed, legalizing the kidnapping and forced indenture of Native Americans, including children. The state\u2019s Foreign Miners\u2019 Tax targets Mexican and Chinese miners with punitive fees designed to drive them from the goldfields.

**1851** : California Governor Peter Burnett declares in his State of the State address that \u201ca war of extermination will continue to be waged between the races, until the Indian race becomes extinct.\u201d The state legislature funds militia campaigns to carry out this policy, appropriating over $1 million for volunteer militias engaged in killing Native people. Over the next two decades, California\u2019s Native population will plummet from roughly 150,000 to approximately 30,000.

**1855\u20131858** : The Northwest Wars between the US Army and Natives of the region are caused by the white settlers\u2019 treaty violations. Unwilling to go quietly on to reservations, the local tribes resist, but are inevitably defeated by the firepower and resources ranged against them.

**1857** : Smith & Wesson introduce the Model 1, the first commercially successful cartridge-firing revolver, making reloading far faster than the cap-and-ball revolvers that preceded it.

**1859** : Oregon becomes a state. Its constitution, ratified in 1857, explicitly bans Black people from residing in, owning property in, or making contracts within the state\u2014one of the most restrictive exclusion laws in the country.

**1860** : The population of the West is about 1,335,000. Russell, Majors and Waddell start the Pony Express, which only lasts as a service until 1861.

**1861** : The American Civil War begins. Kansas is incorporated as a state of the Union.

**1862** : The Homestead Act is signed into law by President Lincoln on May 20th. It takes effect on January 1st, 1863, offering 160 acres of public land to settlers\u2014land that, of course, was taken from Native American peoples. In practice, the Act also excluded most Black Americans, and much of the best land was acquired by speculators and railroad companies rather than small farmers.

**1863** : President Lincoln signs the Emancipation Proclamation, and telegraph lines reach Denver, Colorado.

**1864** : At Sand Creek in Colorado Territory, Colonel John Chivington leads 675 militia troops in a dawn attack on a peaceful Cheyenne and Arapaho camp flying both a US flag and a white flag of surrender. Chief Black Kettle had been assured by US officers that his people were under protection. Chivington\u2019s men slaughter between 150 and 200 people, the majority women, children, and the elderly. Soldiers mutilate the dead\u2014taking scalps, fingers, and genitalia as trophies. Chivington reportedly displays these at a Denver theater to audience applause. A Congressional investigation later condemns the massacre, but no one is punished. The atrocity triggers the retaliations of 1865, known as \u201cthe Bloody Year on the Plains\u201d. Nevada becomes a state of the US.

In the same year, the US Army under Kit Carson forces approximately 8,000\u20139,000 Navajo people on a 300-mile forced march to Bosque Redondo, a desolate reservation at Fort Sumner in New Mexico Territory. This becomes known as the Long Walk. Hundreds die on the march from exposure, starvation, and violence. Hundreds more die at the reservation over the next four years from disease, contaminated water, and crop failures. The Navajo are not permitted to return to their homeland until 1868.

**1865** : The Union wins the Civil War, and Congress finally ratifies the Thirteenth Amendment, abolishing slavery\u2014except, crucially, \u201cas a punishment for crime.\u201d This exception becomes the legal foundation for convict leasing, a system that will funnel thousands of newly freed Black Americans back into forced labor.

**1866** : Southern and Western states begin passing \u201cBlack Codes\u201d\u2014laws specifically designed to criminalize Black life and restrict the freedoms of the newly emancipated. Offenses such as vagrancy, loitering, lacking proof of employment, or violating curfew carry heavy sentences. Convicts are leased to private businesses\u2014mines, railroads, plantations\u2014under conditions frequently worse than antebellum slavery. Mortality rates among leased convicts are staggering, sometimes exceeding 30\u201340% per year. The system will persist in various forms for decades.

**1867** : Alfred Nobel patents his invention, dynamite, and it quickly finds widespread use as a better and safer explosive than black powder. Nebraska is incorporated as a state.

**1868** : Secretary of State William Seward signs the Burlingame Treaty, allowing unrestricted immigration by Chinese people\u2014a provision that will be reversed just fourteen years later.

**1869** : The Central Pacific and Union Pacific Railroads meet at Promontory Summit, Utah, on May 10th, completing the First Transcontinental Railroad. The Central Pacific, built largely by Chinese laborers working in brutal and often fatal conditions, runs from Sacramento east. The Union Pacific runs from Omaha west. A ferry connects Sacramento to San Francisco. Wyoming Territory passes a law granting women the vote, and the right to hold public office and serve on juries\u2014the first territory or state to do so.

**1870** : The 1870 census records the population as 2,187,000. The concept of \u201cGhost Dancing\u201d appears within Native American culture when a Paiute shaman prophecies that fallen warriors will rise from the dead, and the whites will fall. Utah Territory grants women the right to vote, the second territory to do so.

**1871** : The Indian Appropriation Act is passed, ending any federal recognition for tribes as \u201cindependent nations\u201d and effectively nullifying every previous treaty made with Native American communities. In Los Angeles, a mob of around 500 white and Hispanic men attacks the Chinese community, murdering at least 18 Chinese people in what becomes known as the Chinese Massacre of 1871. Eight men are convicted; all convictions are later overturned on technicalities.

**1874** : Barbed wire is patented and appears as a commodity, transforming the open range and accelerating conflicts over land.

**1874\u20131876** : Gold is discovered in the Black Hills in Dakota Territory, land that is sacred to the Sioux and which has been guaranteed to them by treaty. The influx of white settlers, in breach of the treaty, leads to the Great Sioux War. Despite victory at the Little Big Horn, the Sioux and Cheyenne are ultimately defeated and forced on to reservations.

**1875** : The Page Act is passed, effectively barring Chinese women from entering the US under the pretext of preventing \u201cimmoral\u201d immigration. In practice, it is used to restrict nearly all Chinese women, leaving the already-beleaguered Chinese communities in the West overwhelmingly male and isolated.

**1876** : Colorado Territory is incorporated as a state.

**1877** : The prominent Native American war leader, Crazy Horse, and the Lakota tribe surrender to the US Cavalry at Fort Robinson, Nebraska, ending the Great Sioux War. Four months later Crazy Horse is bayoneted to death by a soldier while allegedly \u201cresisting\u201d confinement.

**1878** : The Lincoln County war, over cattle interests and involving the infamous William H Bonney, aka Billy the Kid, takes place in New Mexico.

**1879** : Captain Richard Henry Pratt founds the Carlisle Indian Industrial School in Pennsylvania, the first federally funded off-reservation boarding school for Native American children. Operating under Pratt\u2019s stated philosophy\u2014\u201cKill the Indian in him, and save the man\u201d\u2014the school becomes the model for dozens of similar institutions. Children are forcibly taken from their families, forbidden to speak their languages or practice their religions, and subjected to military-style discipline. Physical and sexual abuse is rampant. Many children die of disease, malnutrition, and neglect; mass graves have been found at several former school sites across the country. The boarding school system will operate for decades, with devastating consequences for Native languages, cultures, and families.

**1880** : The census records a population of nearly 5 million.

**1882** : The Chinese Exclusion Act is signed into law, banning Chinese laborers from immigrating to the US and barring Chinese residents from becoming naturalized citizens. It is the first federal law to exclude an entire ethnic group from immigration, and will remain in force until 1943. The Edmunds Act, outlawing polygamy, is also passed into law.

**1885** : At Rock Springs, Wyoming Territory, a mob of white miners attacks the Chinese community, murdering at least 28 Chinese people, wounding 15 others, and burning 79 homes. No one is ever convicted.

**1886** : The so-called \u201cIndian War\u201d in the south, principally against the Apache, is brought to a conclusion by the tribe\u2019s eventual defeat and the surrender of Geronimo.

**1887** : At Chinese Massacre Cove on the Snake River in Oregon, a gang of horse thieves and ranchers murders 34 Chinese gold miners. The killers are identified but acquitted, the bodies left unburied.

**1889** : Dakota, Montana and Washington Territories are incorporated as states of the Union. In roughly twenty years of industrial-scale slaughter\u2014driven by the hide trade, the railroads, and deliberate US military policy to starve the Plains tribes into submission\u2014the American bison has been driven to the edge of extinction. Once numbering an estimated 30 to 60 million, fewer than 600 individuals remain. General Philip Sheridan told the Texas legislature that buffalo hunters \u201chave done more to settle the vexed Indian question than the entire regular army.\u201d Colonel Richard Irving Dodge was more blunt: \u201cKill every buffalo you can. Every buffalo dead is an Indian gone.\u201d

**1890** : The massacre at Wounded Knee sees approximately 250\u2013300 Lakota men, women and children slaughtered by the 7th Cavalry\u2014some estimates run higher. Many are shot while fleeing. The soldiers later receive Medals of Honor. Idaho and Wyoming Territories become states.

**1896** : Utah Territory is incorporated as a state.

**1907** : Oklahoma Territory is incorporated as a state.

**1912** : Arizona and New Mexico Territories are incorporated as states.
"""

content = content[:start_idx] + new_timeline + content[end_idx:]

with open(filepath, "w", encoding="utf-8", newline="\n") as f:
    f.write(content)

print("Timeline section replaced successfully.")
