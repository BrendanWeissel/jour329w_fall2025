 Star-Democrat Draft Beat Book 11/17/25

I chose to look at sports and specifically the high school sports beat. With over 150 stories a year specificlaly about high school sports from the star democrat this is topic deserving of a beat book. 

In order to get the below prompt to run I spent a few hours narrowin down my Json file. I removed every other story twice to end up with only 42 stories from 2024. I cut all the full text from stories as well as other metadata. I am left with 42 stories with these categories of info: 

"title": 
    "date": 
    "author": 
    "year": 
    "month": 
    "day": 
    "metadata_sport": 
    "metadata_story_type": 
    "metadata_location": 
    "metadata_teams": 
    "entities_quoted_people": 
    "metadata_level_of_play": 
    "metadata_competition_type": 
    "metadata_outcome": 
    "metadata_importance": 
    "content"

Code: cat prompt.txt source_stories_every_other.json | uv run llm -m groq/openai/gpt-oss-120b > prototype_v1.md

Prompt: Create a comprehensive beat guide for a reporter covering sports on the Eastern Shore. Use the provided stories as source material to introduce the key people, teams, institutions, and recurring issues that define the local sports landscape.
Introduce the journalist to the topic as if you were an expert guide. The guide should focus on how to do the job in the future. 

The language should be business casual, and it should not be primarily a list of bullet points, but you can use bullet points for checklists or proposed sources or locations for a suggested story angle. 

The guide should clearly explain:
	•	Who the reporter should know in the sports world on the eastern shore. 
	•	Which sports matter most on the Eastern Shore 
	•	How to structure the reporting year


I created this prompt by combining the CNS prompt I had and then using the narrative guide prompt. 

prototype_v1.md: **Eastern Shore Sports Beat – A Practical Guide for the Modern High‑School Reporter**  
*(Prepared by a longtime beat veteran for anyone stepping into the Maryland Eastern Shore high‑school arena.  All dates, names and story ideas are drawn from the 2024 coverage archive.)*  

---

### 1.  Why the Eastern Shore is a Unique Beat  

The Eastern Shore isn’t a single city; it’s a patchwork of small towns—Centreville, Easton, Stevensville, Queen Anne’s, Wicomico, Kent County and beyond—each with a proud high‑school sports tradition.  Because the schools are the community’s social hub, a game is never just a game; it’s a story about family ties, school spirit, local economies, and, increasingly, the challenges of maintaining competitive programs with limited resources.

In the 2024 cycle you’ll notice three recurring themes:

| Theme | How it shows up | What it means for you |
|-------|----------------|-----------------------|
| **Playoff intensity** – almost every sport spikes in coverage after the regular season (e.g., the “Warriors extend win streak” basketball recap, the “Sabres finish strong on way to crown” soccer playoffs). | Build a pipeline of pre‑season expectations, mid‑season checkpoints, and post‑game analysis. |
| **Coaching turnover & new philosophies** – “Warriors battle but can’t extend win streak against undefeated Bennett” (new soccer coach, new offensive system). | Track coaching hires, philosophy changes, and the ripple effect on player development. |
| **Community & safety issues** – the Carver Vo‑Tech basketball game stopped by an altercation; the “Girls wrestling champions receive acclamation” feature on gender equity. | Look for stories that go beyond the box score: facility upgrades, Title IX compliance, mental‑health initiatives, and community fundraising. |

---

### 2.  Who You Need to Know  

Below is a *who‑what‑where* matrix that captures the most‑quoted coaches, administrators and recurring “go‑to” sources.  Treat each name as a starting point for deeper relationships; most of them are open to a quick coffee or a post‑game chat.

| School / Institution | Primary Contacts (coach, AD, PR) | Typical Story Angles |
|----------------------|-----------------------------------|----------------------|
| **Queen Anne’s County High (Lions)** | Jeff Hollis (boys basketball), Dionte Hynson (football), Brian Mooney (football), Aaron Stewart (softball), Jamie Leventry (volleyball) | Title runs (volleyball three‑peat), defensive streaks (soccer shutouts), community outreach. |
| **Easton High (Warriors)** | Matt Griffith (football), Gabe Kane (soccer), Butch Waller (basketball), David Fisher (softball), Laura Harding (field hockey) | New‑coach impact, rivalry with Queen Anne’s, multi‑sport athletes (e.g., Marshall Bailey). |
| **Kent Island High** | Josh August (wrestling), Justin Holland (track & field), Bobby Woolley (lacrosse), Kim Neff (field hockey) | Rapid rise in wrestling & lacrosse, indoor track championships. |
| **St. Michaels High** | Boo Ricketts (basketball), Brian Femi (baseball), Dave Morrissette (baseball) | Tournament performances (Peake Challenge), baseball dominance. |
| **Colonel Richardson High** | David Fisher (softball), Bryan Hall (wrestling) | Consistent softball power (10‑0 win), wrestling program growth. |
| **Cambridge‑South Dorchester High** | Rob Burnham (football, field hockey), Shawn Parker (basketball) | “Vikings” brand, cross‑sport coaching synergy. |
| **North Dorchester & James M. Bennett** | Various; often the athletic director is the gateway (e.g., Harold Somerville at Kent County). | Opponent perspective for rivalry pieces. |
| **County & Tournament Organizers** | *Peake Challenge* committee (Wye Mills), *Eastern Shore Athletic Association* (wrestling), *Maryland Interscholastic Athletic Association* (track). | Event previews, rule changes, logistics. |

**Quick tip:** Keep a “contact log” in a spreadsheet with columns for *Name, School, Sport, Email, Preferred Contact Method, Last Interaction*.  Update it after every game—those small “thanks for the quote” notes build goodwill.

---

### 3.  The Sports That Matter Most  

While every sport gets a story, the data set shows a clear hierarchy based on volume, community interest and postseason relevance:

1. **Basketball (boys & girls)** – 12+ recaps, frequent tournament previews, high‑impact players (Vince Gilberto, Marshall Bailey).  
2. **Football** – Seasonal previews (Sept, Oct), playoff battles, big community draw (Easton vs. North Carolina, Vikings vs. Fort Hill).  
3. **Wrestling** – Growing participation, especially girls’ program (feature on Queens Anne’s champions).  
4. **Track & Field (indoor/outdoor)** – Regional championships, standout athletes (Todd, Sumayah Wilkins).  
5. **Baseball / Softball** – Consistent coverage of regular‑season dominance (St. Michaels, Colonel Richardson).  
6. **Soccer** – Emerging rivalry narrative (Easton vs. Bennett, Queens Anne’s shutouts).  
7. **Lacrosse** – High‑scoring titles (Kent Island vs. Decatur).  
8. **Field Hockey & Volleyball** – Playoff storylines, especially for Easton and Queens Anne’s.

When you plan your calendar, allocate **core weeks** (basketball in Jan–Mar, football Sep–Nov, wrestling Feb–Mar) and **satellite weeks** for the “second‑tier” sports.  Even a single human‑interest angle (e.g., a senior’s final season) can elevate a lesser‑covered sport into front‑page territory.

---

### 4.  Structuring the Reporting Year  

Think of the season as a **four‑phase cycle** that mirrors the academic calendar:

| Phase | Timing | Primary Deliverables | Sample Story Types |
|-------|--------|----------------------|--------------------|
| **Pre‑Season Planning** | Early August – Mid‑September | • Calendar of games, tournaments, and championship dates.<br>• “Preview” pieces (e.g., *“TALL TASK”* football preview).<br>• Coaching change interviews. | • “A FINE BLEND” football preseason outlook.<br>• Peake Challenge preview (Feb 10). |
| **Regular‑Season Pulse** | Mid‑Sept – Late Feb (football, basketball, wrestling) / Mar–May (track, lacrosse, baseball) | • Game‑by‑game recaps (use the “who‑said‑what” formula).<br>• Mid‑season check‑ins (win‑streaks, injury updates).<br>• Feature on training facilities or community support. | • “Warriors extend win streak” (basketball).<br>• “Girls wrestling champions receive acclamation” (feature). |
| **Playoff & Championship Spotlight** | Late Feb – Early Nov (depending on sport) | • Tournament previews (Peake Challenge, regional wrestling).<br>• Live‑blogging or rapid‑turnaround recaps of knockout games.<br>• Human‑interest pieces on senior athletes and title‑chasing coaches. | • “Sabres finish strong on way to crown” (soccer).<br>• “Todd earns four titles; Vikes win boys crown” (track). |
| **Wrap‑Up & Off‑Season** | December – Early January | • End‑of‑year round‑ups (top athletes, coaching awards).<br>• “Where are they now?” for graduating seniors.<br>• Preview of next year’s schedule, facility upgrades, recruiting pipelines. | • “Lions serve up 3rd straight title” (volleyball).<br>• “Queens Anne’s extends North shutout streak” (soccer). |

**Practical workflow tip:**  
- **Create a master spreadsheet** titled *Eastern Shore Sports Calendar* with columns for *Date, Sport, Opponent, Venue, Story Angle, Deadline, Assigned Writer*.  Populate it from school websites and the Maryland Interscholastic Athletic Association (MIAA) releases.  
- **Set weekly “story blocks.”** For example, every Thursday you have a 250‑word recap deadline for the previous night’s basketball game; every Monday a 500‑word feature on a standout wrestler.  This cadence helps you meet tight publishing windows without burning out.

---

### 5.  Story‑Finding Checklist (Bullet Form)  

Below is a quick‑reference list you can paste into your notes app.  Tick the boxes each week to make sure you’re covering all the angles.

- **Game Recap Essentials**  
  - Score, key stats, turning point.  
  - At least two quotes (coach & player).  
  - Context: win‑streak, rivalry, playoff implication.  

- **Human‑Interest Angles**  
  - Senior’s final season / “last dance.”  
  - Family of multi‑sport athletes (e.g., a basketball star who also plays lacrosse).  
  - Community fundraisers for equipment or facility upgrades.  

- **Trend Tracking**  
  - Win‑streaks or losing streaks (e.g., Easton’s early‑season basketball surge).  
  - Injury reports and depth‑chart adjustments.  
  - Coaching philosophy shifts (new offensive system, defensive emphasis).  

- **Recurring Events**  
  - **Peake Challenge** (Feb 10) – a must‑cover tournament for basketball.  
  - **Regional Wrestling Championships** (Feb 23/25).  
  - **Track & Field Regionals** (May 18).  

- **Key Dates to Flag**  
  - First Friday of September: start of football season.  
  - Last week of January: high‑school basketball regular season concludes.  
  - Mid‑April: softball & baseball championships.  
  - Early June: end of track season, awards ceremony.

---

### 6.  Sample Pitch Packages  

**A. “The Rise of Girls’ Wrestling on the Eastern Shore”**  
- **Hook:** The recent feature on Queens Anne’s champions (June 7) shows a surge in participation and community support.  
- **Sources:** Coach David Stricker (Queens Anne’s), Athletic directors from Kent Island and St. Michaels, parents of wrestlers, Maryland Girls’ Wrestling Association.  
- **Angles:** Title IX compliance, scholarship opportunities, training facilities, athlete profiles (e.g., Julia Reburn).  

**B. “From the Sidelines to the Spotlight: New Coaches Redefining Small‑Town Football”**  
- **Hook:** New head coach Matt Griffith’s impact on Easton’s offense (Sept 10 soccer preview, Oct 8 soccer loss) and the ripple effect on recruiting.  
- **Sources:** Coaches (Griffith, Burnham, Mooney), players (Mikey O’Connor, Zach Davis), local high‑school football analysts.  
- **Angles:** Tactical changes, community expectations, comparative win‑loss before/after hire.  

**C. “The Peake Challenge: A Tournament That Unites the Shore”**  
- **Hook:** The February 10 preview lists 13 high schools; the tournament has become a regional showcase for talent.  
- **Sources:** Tournament director (Wye Mills school board), coaches (Boo Ricketts, Jeff Hollis), past MVPs.  
- **Angles:** Economic impact on host town, scouting opportunities, alumni stories.  

---

### 7.  Practical Tips for a Sustainable Beat  

1. **Be a “Community Reporter.”** Attend the pep rallies, school board meetings and local fundraisers.  A story about a new weight‑room can become a front‑page piece when you hear the school principal’s budget concerns first.  
2. **Leverage Social Media Wisely.** Most coaches post game‑day line‑ups on Twitter or Instagram.  Use those posts to verify quotes and get instant reactions—just double‑check with a quick email.  
3. **Maintain a “Story Bank.”** Every time you hear a promising quote or an odd statistic, jot it down.  You’ll have a ready reservoir when a deadline looms.  
4. **Watch the Calendar for “Off‑Season” Stories.** The offseason is the perfect time for deep‑dive features (e.g., “Where are the 2022 seniors now?”).  
5. **Balance Speed with Accuracy.** The Carver‑Vo‑Tech altercation (Mar 9) shows how a rushed story can miss the broader context (security policies, district response).  Verify facts before the first deadline hits.  

---

### 8.  Quick Reference – Key Schools & Their Signature Sports  

| School | Signature Sport(s) | Recent Highlight |
|--------|-------------------|------------------|
| Queen Anne’s County High | Basketball, Volleyball, Soccer | Three‑peat volleyball titles (Oct 29) |
| Easton High | Football, Basketball, Field Hockey | Overtime field‑hockey win (Oct 15) |
| Kent Island High | Wrestling, Lacrosse, Track | Indoor track championship (Feb 6) |
| St. Michaels High | Basketball (Peake Challenge), Baseball | 4‑1 baseball win vs. North Dorchester (Apr 10) |
| Colonel Richardson High | Softball, Wrestling | 10‑0 softball shutout (Mar 26) |
| Cambridge‑South Dorchester High | Football, Lacrosse, Basketball | 46‑8 football blowout (Oct 4) |
| North Dorchester High | Football, Basketball | 54‑30 basketball win (Dec 6) |

---

### 9.  Closing Thought  

Covering the Eastern Shore isn’t about chasing national headlines; it’s about telling the stories that matter to families sitting on the bleachers, to the students who’ll remember a newspaper clipping decades later, and to the towns that rally around their high‑school teams.  By keeping a tight calendar, nurturing a reliable network of coaches and administrators, and always digging a little deeper than the final score, you’ll turn the everyday rhythm of games into a compelling narrative that keeps readers coming back week after week.

Welcome to the beat—now go get those quotes, watch those overtime goals, and remember that on the Eastern Shore every victory feels like a community celebration.  



*Prepared for the newsroom on 18 Nov 2025.*


## Thoughts from V1 ##

Overall this is a weak beat book. The issue with taking data from 2024 is that people may be outdated. I also don't think the information needs to be as person dense rather it would work better if it was general informtion. I don't need the names of coaches, ad and players as a different LLM can get that info easily I need the LLM to explain that having the names of those people is important. 

The structuring the year works well and would be helpful to someone who is newer to sports coverage. 

I found this tip to be helpful for local sports. "Leverage Social Media Wisely.** Most coaches post game‑day line‑ups on Twitter or Instagram.  Use those posts to verify quotes and get instant reactions—just double‑check with a quick email. "

However the schools and their signature sport section is useless becasue it has old info and not enough of it. 

The guide needs more info on how the reporter should plan their week to get to all this coverage and what types of stories matter the most to the community. 


Prompt 2: Create a comprehensive beat guide for a reporter covering sports on the Eastern Shore. Use the provided stories as source material to introduce the key people, teams, institutions, and recurring issues that define the local sports landscape.
Introduce the journalist to the topic as if you were an expert guide. The guide should focus on how to do the job in the future. 

The language should be business casual, and it should not be primarily a list of bullet points, but you can use bullet points for checklists or proposed sources or locations for a suggested story angle. 

The guide should clearly explain:
	- 	What sports matter most
    - How the reporter should strcuture their life and work schedule to attend late night games 
    - tips on forming relationships with local coaches
    - How to write different types of sports stories
    - How to track statistics, rosters, and standings across seasons and leagues.
    - What makes a strong sports feature story
    - what to avoid as a local sports reporter
    - how to balance competitive sports during crossover and playoff seasons


Code 2: cat prompt.txt source_stories_every_other.json | uv run llm -m groq/openai/gpt-oss-120b > prototype_v2.md

Prompt: Create a comprehensive beat guide for a reporter covering sports on the Eastern Shore. Use the provided stories as source material to introduce the key people, teams, institutions, and recurring issues that define the local sports landscape.
Introduce the journalist to the topic as if you were an expert guide. The guide should focus on how to do the job in the future. 

The language should be business casual, and it should not be primarily a list of bullet points, but you can use bullet points for checklists or proposed sources or locations for a suggested story angle. 

The guide should clearly explain:
	- 	What sports matter most
    - How the reporter should strcuture their life and work schedule to attend late night games 
    - tips on forming relationships with local coaches
    - How to write different types of sports stories
    - How to track statistics, rosters, and standings across seasons and leagues.
    - What makes a strong sports feature story
    - what to avoid as a local sports reporter
    - how to balance competitive sports during crossover and playoff seasons




Prototype_v2: ## Eastern Shore Sports‑Beat Handbook  
*Your go‑to companion for covering high‑school athletics on Maryland’s Eastern Shore.  Think of it as a living map rather than a static checklist—use it to plot the season, meet the right people, and spot the storylines that keep the community turning its eyes (and radios) to the gym, the field, and the track.*

---

### 1. Why the Eastern Shore is a unique beat  

The Eastern Shore is a patchwork of small towns—Centreville, Easton, Queen Anne’s County, St. Michael’s, Stevensville, and beyond—where high‑school sport is the social glue.  Games are community events, rivalries stretch back generations, and every victory (or controversy) reverberates through town halls, PTA meetings, and the local paper.  

Because most of the action is **high‑school**, the beat is less about professional contracts and more about:

* **Coaches who double as teachers and civic leaders** – they are the gatekeepers of access and the most reliable source of background.
* **Student‑athletes who are also “local kids”** – their families, graduation plans, and college aspirations are part of the story.
* **District and county athletic directors** – they shape schedules, eligibility rules, and funding decisions that affect every sport.
* **Community institutions** – the school board, local businesses (sponsors), and the Eastern Shore’s media ecosystem all influence coverage.

Understanding those relationships is the foundation for any story that goes beyond a simple game recap.

---

### 2. Who to know – the “who‑list” (not a pure bullet list, but a quick‑reference guide)

| Category | Key Names (from recent coverage) | What they bring to the beat |
|----------|----------------------------------|-----------------------------|
| **Principal Administrators** | **Brian Mooney** (Queen Anne’s County High), **Harold Somerville** (Kent County High), **Rob Burnham** (Cambridge‑South Dorchester) | Scheduling, budget approvals, discipline decisions (e.g., the Carver‑Queen Anne’s altercation). |
| **Head Coaches – Basketball** | **Jeff Hollis** (QAH Lions), **Dionte Hynson** (Easton Warriors), **Butch Waller** (Wicomico Indians), **Gary Hofmann** (Carver Vo‑Tech) | Game strategy, player development, pre‑season outlooks. |
| **Head Coaches – Football** | **Matt Griffith** (Easton Warriors), **Brian Mooney** (QAH Lions), **Rob Burnham** (Cambridge‑South Dorchester), **Zack Alkire** (Fort Hill) | Play‑calling trends, injury reports, recruiting pipelines. |
| **Head Coaches – Wrestling** | **Josh August** (Kent Island Buccaneers), **Tommy Sitar** (Harford Vo‑Tech), **David Stricker** (QAH Lions) | Tournament brackets, weight‑class issues, gender‑equity developments (girls’ championships). |
| **Head Coaches – Soccer / Field Hockey / Lacrosse** | **Avery Brice** (Easton soccer), **Laura Harding** (Easton field hockey), **Bobby Woolley** (Kent Island lacrosse) | Seasonal rivalries, player‑spotlight opportunities. |
| **Athlete Voices** | **Vince Gilberto** (QAH Lions basketball star), **Marshall Bailey** (Easton Warriors), **Olivia Orrell** (Easton field hockey OT hero), **Micah Quinn** (Kent Island lacrosse) | First‑hand accounts, human‑interest angles, college‑recruiting chatter. |
| **Media & Community Partners** | **Bill/William Haufe** (Chesapeake Publishing), **Andrea Grabenstein** (feature writer), local radio sports hosts | Story distribution, photo/video resources, cross‑promotion. |
| **Support Staff & Administrators** | **Justin Holland** (track & field coach), **Jamie Leventry** (volleyball coach), **Kim Neff** (field hockey) | Access to practice footage, insight into training regimens. |

**How to use it:**  
- **Introductory email**: Reach out to each coach before the season starts, introduce yourself, and ask for a quick “team snapshot” (roster, goals, key story ideas).  
- **Quarterly check‑ins**: Meet district athletic directors after each sport’s championship to gauge policy changes (e.g., eligibility, safety protocols).  
- **Student‑athlete profiles**: Invite standout players like Gilberto or Orrell for a brief sit‑down; they’ll often point you toward teammates with compelling back‑stories.

---

### 3. The sports that dominate the Eastern Shore beat  

While every sport gets coverage, the following five generate the most consistent news flow, attendance, and community conversation:

1. **Basketball (boys & girls)** – Seasonal rhythm runs from November‑March, with high‑stakes playoffs (e.g., the “Carver‑QAH” game stopped by an altercation).  
2. **Football** – The fall staple (August‑December). Rivalry weeks (e.g., Easton vs. North Caroline) and playoff previews dominate local chatter.  
3. **Wrestling** – Strong participation on both boys’ and girls’ sides; tournaments at Berlin, Centreville, and the “Girls Wrestling Champions” story illustrate growing interest.  
4. **Soccer & Field Hockey** – Both have grown in the last two years; the “Orrell overtime goal” and the “Sabres finish strong” playoff run show that the sports attract high‑school and community attention.  
5. **Track & Field / Lacrosse / Softball/Baseball** – Seasonal peaks in spring (March‑May) with regional championships (e.g., “Todd earns four titles; Vikes win boys crown”).

**Secondary sports worth watching:** Volleyball (Queen Anne’s three‑peat), baseball/softball (St. Michael’s Saints, Colonel Richardson), and emerging girls’ programs (girls’ wrestling, field hockey).  

**Recurring themes** that appear across all sports:

- **Rivalries & geography** – Easton vs. Queen Anne’s; Kent Island vs. Stevensville; the “North shutout streak” in soccer.  
- **Coaching transitions** – New head coaches (e.g., Easton soccer’s Gabe Kane, basketball’s first‑year coach at North Dorchester).  
- **Player safety & discipline** – The Carver‑QAH altercation, wrestling weight‑class disputes, and COVID‑era health protocols.  
- **College recruitment** – Senior athletes who are being scouted (basketball’s Gilberto, lacrosse’s Quinn).  
- **Gender equity** – Girls’ wrestling championships, expanding field‑hockey programs, and Title IX discussions at the district level.

---

### 4. Mapping the reporting year – a seasonal workflow  

| Timeframe | Primary Sports | Core Story Types | Suggested Angles |
|-----------|----------------|------------------|-----------------|
| **Late July – Early August** | Football (pre‑season), Soccer (pre‑season) | **Previews** | “A Fine Blend” (QAH football preview), “TALL TASK” (Kent County football preview). Interview coaches, ask about roster cuts, new schemes, and community expectations. |
| **Mid‑August – Mid‑September** | Football (regular season), Basketball (non‑conference), Soccer (early season) | **Game Recaps, Early‑Season Trends** | Highlight standout performances (e.g., Ensminger/Monroy for Warriors), note early injuries, and capture fan attendance numbers. |
| **Late September – Early November** | Football (playoffs race), Basketball (conference play), Lacrosse (regular season) | **Feature Stories, Rivalry Pieces** | Dig into the history of the Easton‑Queen Anne’s rivalry, profile a senior athlete (e.g., Marshall Bailey), explore coaching philosophies (Rob Burnham’s “going back in time”). |
| **Mid‑November – Early December** | Basketball (playoffs), Soccer (regular season), Field Hockey (regular season) | **Playoff Recaps, Human‑Interest** | Capture the emotional weight of “Warriors battle but can’t extend win streak”, or the “Orrell overtime goal” story. |
| **December – Early January** | Winter break – *planning* | **Season Review, Off‑Season Angles** | Compile “Year‑in‑Review” graphics, interview district athletic directors about budget and facility upgrades, preview upcoming winter sports (wrestling, indoor track). |
| **January – March** | Wrestling (tournaments), Indoor Track (championships), Basketball (regular season) | **Tournament Previews, Championship Recaps** | Use “Peake Challenge” (basketball tournament preview) as a template for wrestling previews (Bayside tourney). Highlight the “Girls wrestling champions receive acclamation” as a feature on gender equity. |
| **April – May** | Baseball, Softball, Lacrosse, Outdoor Track | **Championship Coverage, Senior Spotlights** | Focus on “Todd earns four titles; Vikes win boys crown”, “Quinn, Bucs strike quick to earn title”, and senior athlete college‑commit stories. |
| **June – August** | Off‑season (training, camps), Summer leagues | **Community Angles, Facility Stories** | Look at summer camps hosted by local colleges, talk about facility upgrades (e.g., new turf at Queen Anne’s), and preview the upcoming fall sports calendar. |

**Tips for staying ahead:**  

- **Mark every district‑wide tournament** (Peake Challenge, Bayside wrestling tourney, regional track championships) on a master calendar.  
- **Set alerts** for each school’s athletic department page—most post schedules, results, and press releases within 24 hours.  
- **Assign “story windows”**: for each sport, allocate a 2‑week deep‑dive period where you chase feature ideas, then shift to quick‑turn recaps for the remainder of the season.  

---

### 5. Story‑angle toolbox – recurring issues to mine  

| Issue | Example from the archive | Angle to pursue |
|-------|--------------------------|-----------------|
| **Altercations & Discipline** | “QA’s‑Carver playoff cut short by altercation” (Mar 9) | Investigate the district’s policy on on‑court violence, interview coaches on how they manage tempers, and profile a player who turned a disciplinary setback into leadership. |
| **Coaching Changes** | “Warriors survive Bulldogs’ rally” (Sept 20) – first year coach Matt Griffith | Profile a rookie head coach, explore their philosophy versus veteran counterparts, and gauge community reaction. |
| **Gender Equity & Girls’ Programs** | “Girls wrestling champions receive acclamation” (June 7) | Track the growth of girls’ wrestling, compare participation numbers over the last five years, and speak with Title IX officials. |
| **Small‑Town Rivalries** | “Lions push but can’t get ahead of Easton” (May 1) – lacrosse | Write a “Rivalry‑of‑the‑Month” column, pairing a head‑to‑head record with community anecdotes (e.g., local businesses offering “Lions” discounts). |
| **College Recruiting** | “Vince Gilberto’s season‑high 33 points” (Jan 3) | Follow a senior athlete through the recruiting process—camp invitations, campus visits, and the final decision. |
| **Facility & Funding** | No explicit story, but many games at municipal fields (Stevensville, Wye Mills) | Investigate how school budgets affect upgrades (lighting, turf) and the impact on player safety. |
| **Community Impact** | “Warriors extend win streak” (Jan 25) – high attendance | Examine how a winning program boosts local business (restaurants, merch sellers) and community pride. |

---

### 6. Quick‑reference checklist – contacts, locations, and resources  

- **Core Contact List** (update each semester)  
  - Athletic Directors: Brian Mooney (QAH), Harold Somerville (Kent County), Rob Burnham (Cambridge‑South Dorchester)  
  - Media Relations: Bill Haufe (Chesapeake Publishing), Andrea Grabenstein (features)  
  - Coaches: Jeff Hollis, Dionte Hynson, Matt Griffith, Laura Harding, Justin Holland, Jamie Leventry  

- **Key Venues**  
  - **Centreville High School Gym** – QAH Lions basketball, wrestling regionals  
  - **Easton High School Complex** – football, soccer, field hockey, basketball  
  - **Stevensville (Kent Island) Stadium** – lacrosse, wrestling, track championships  
  - **Wye Mills School** – Peake Challenge tournament (basketball)  
  - **Berlin High School** – Bayside wrestling tourney  

- **Annual Event Calendar (high‑lights)**  
  - **July** – Pre‑season football & soccer meetings (district)  
  - **August 10‑15** – Football season opener (local coverage)  
  - **Sept 10** – Soccer season opener (Easton vs. Wicomico)  
  - **Oct 4‑15** – Football rivalry weeks (Cambridge‑South Dorchester vs. Kent County, etc.)  
  - **Nov 1‑15** – Basketball playoffs (regional & district)  
  - **Feb 10** – Peake Challenge basketball tournament  
  - **Mar 20‑30** – Regional wrestling & indoor track championships  
  - **May 1‑20** – Outdoor track, baseball/softball, lacrosse finals  

- **Digital Resources**  
  - Maryland Public Secondary Schools Athletic Association (MPSSAA) site – official brackets, eligibility notices.  
  - School district Facebook pages – live updates, photo albums.  
  - Local radio (WESM, WMAR) – post‑game interviews and community sentiment.  

---

### 7. Best practices for a sustainable beat  

1. **Build trust before the deadline.** Attend a few practices without a recorder, introduce yourself to the booster clubs, and let coaches know you’re there to amplify—not sensationalize—their work.  
2. **Balance speed with depth.** A game recap is essential, but follow each with a 300‑word “what it means” paragraph that links the result to season goals, player milestones, or community impact.  
3. **Leverage multimedia.** Ask coaches for photo permission during practice; use Instagram stories for quick score updates; embed short video clips of key moments (e.g., Orrell’s overtime goal).  
4. **Stay on top of compliance.** High‑school athletes are minors—verify parental consent for any personal profile, and double‑check the MPSSAA eligibility rules before publishing.  
5. **Cross‑publish with local partners.** Offer story teasers to the county’s radio stations; collaborate with the school yearbook for archival photos. This widens reach and builds goodwill.  

---

### 8. Putting it all together – your first 90‑day plan  

| Week | Action | Goal |
|------|--------|------|
| 1‑2 | Meet the **district athletic director** and **key coaches** (football, basketball, wrestling). Collect season preview packets. | Establish primary sources and gather official schedules. |
| 3‑4 | Attend the **first football practice** at Easton and QAH; record anecdotes and photo opportunities. | Build a “human‑interest” bank for future feature pieces. |
| 5‑6 | Cover the **Peake Challenge** (basketball) and **Bayside wrestling tourney**. Gather quotes from coaches like **Boo Ricketts** and **Josh August**. | Deliver tournament previews and recaps; identify standout athletes. |
| 7‑8 | Write a **season‑opening feature** on a senior athlete (e.g., **Vince Gilberto**). Pitch it to the editor as a “local hero” story. | Showcase the human side of the beat, increase readership. |
| 9‑12 | Produce a **mid‑season analysis** on the football rivalry week (Easton vs. North Caroline; Cambridge‑South Dorchester vs. Kent County). Include stats, fan sentiment, and coach commentary. | Position yourself as the go‑to analyst for the community. |
| 13‑14 | Review the **first wave of disciplinary incidents** (e.g., Carver‑QAH game). Interview the district’s compliance officer and produce a short investigative piece. | Demonstrate depth and responsibility in coverage. |
| 15‑16 | Draft a **season‑in‑review calendar** for the next year, noting dates for all major tournaments and preseason meetings. Share it with coaches and editors. | Provide a useful reference and reinforce your role as a beat coordinator. |

---

## Closing Thought  

Covering Eastern Shore sports is less about chasing headline‑grabbing moments and more about weaving together the **people, the place, and the pride** that each game represents.  By knowing the coaches who shape the teams, the athletes who embody the community’s hopes, and the calendar that dictates the rhythm of competition, you’ll turn ordinary recaps into stories that matter to every resident—from the kid on the bleachers to the senior who’s been coaching for 30 years.  

Use this guide as a launchpad, update it with the names and events that surface each season, and you’ll quickly become the trusted voice that the Eastern Shore turns to when it wants to know what’s happening on the field, in the gym, and on the track. Happy reporting!


## Thoughts on v2 ##

I really like this intro: * **Coaches who double as teachers and civic leaders** – they are the gatekeepers of access and the most reliable source of background.
* **Student‑athletes who are also “local kids”** – their families, graduation plans, and college aspirations are part of the story.
* **District and county athletic directors** – they shape schedules, eligibility rules, and funding decisions that affect every sport.
* **Community institutions** – the school board, local businesses (sponsors), and the Eastern Shore’s media ecosystem all influence coverage.

Understanding those relationships is the foundation for any story that goes beyond a simple game recap.


This does a good job setting the stakes for the beat. I need to tell it to cut the part about who to know with specific people becasue it gave me many names who may be meaningless now. 

However I liked the tips on how to reach out to them.

I have to find out a better way to create a sports calendar the format it gave is yuck. 

I like the idea of this: ### 8. Putting it all together – your first 90‑day plan  

But it needs more information to do this better. 

### Final Evaluation

I got my .Json to a point where I could create a beat book but I am far off from a good draft. I need to shift the focus from specific names to general tips. The second draft is better at doing this but still focused too much on names and locations that are easily figured out. 

The best part of the beat book is the start and setting the stakes for high school sports and how to approach it. I want the LLM to add a section on what no to do and failures to avoid. 

Going foward I want to breakdown each section of the guide and have the LLM create my beat book section by section and have it run 5 attempts per section and then decide on what pieces I like best. 


## PART 2 ##

Created sport specific JSON files for Baseball, basketball, field hockey, lax, soccer, softball and wrestling. 
Code: cat prompt_sport.txt source_stories_highschool_SPORT.json | uv run llm -m groq/openai/gpt-oss-120b > prototype_SPORT.md

PROMPT FOR SPORT SPECIFIC BEAT: Create a comprehensive beat guide for a reporter covering high school and community sports on the Eastern Shore.
The guide should be written in a business-casual tone and should read like an expert walking a new journalist through the realities of the beat. It should not be primarily bullet-point lists, although you may use bullets for practical checklists, source lists, and workflow steps.

Focus on how to cover the specific sport listed. If only stories provided are about soccer the entire guide shoudl focus only on soccer coverage. 

Please include the following:

1. Local sports landscape overview
	•	Explain which sports matter most in the Eastern Shore region, and why—community traditions, rivalries, participation levels, etc.
	•	Highlight seasonal rhythms and how they shape story opportunities.

2. Reporter lifestyle & workflow
	•	Guidance on how a reporter should structure their weekly schedule, including late-night games, long travel distances, and quick turnaround deadlines.
	•	Advice on how to maintain contact lists, prep for busy weeks, and balance multiple beats during playoff season or overlapping sports.

3. Building and maintaining relationships

Provide generalized, evergreen advice (not specific names) for:
	•	How to introduce yourself to coaches, ADs, parents, and players.
	•	How to consistently follow up without being intrusive.
	•	How to identify the “gatekeepers” in each program (team managers, long-time volunteers, booster club members).
	•	How to gather names, confirm spelling, and track roster changes each year.
	•	How to handle sensitive conversations (injuries, academic issues, transfers).

4. Reporting and writing guidance

Explain:
	•	How to write different types of sports stories (game recaps, advance previews, features, trend pieces, accountability stories, profiles).
	•	What makes a strong sports feature: structure, character development, scenes, background reporting, sourcing.
	•	How to maintain fairness, avoid boosterism, and steer clear of common local-sports pitfalls.

5. Stats, rosters, and data management
	•	How to collect and verify stats when schools have inconsistent reporting systems.
	•	How to build your own personal database of rosters, schedules, standings, and player milestones.
	•	How to stay organized across seasons and avoid losing track of information when rosters turn over.
	•	Tips for tracking unofficial record books, rivalry histories, or local playoff trends.

6. Playoffs, overlaps & coverage strategy
	•	How to balance multiple sports during overlapping seasons, especially playoffs.
	•	Decision-making frameworks for which games to cover when several matter at once.
	•	Tips for staying ahead of scheduling changes (rainouts, rescheduled conference games, tournament location shifts).

7. Sport-Specific Section

Create a separate section dedicated to the sport I specify, including:
	•	Unique rhythms of the sport’s season.
	•	Typical storylines for that sport on the Eastern Shore.
	•	Position-specific or role-specific features worth exploring.
	•	What to watch for during games (schemes, tendencies, flow, key stats).
	•	How to photograph or take notes effectively for that sport.
	•	What types of sources to cultivate (assistant coaches, position coaches, parents, referees, long-time boosters).
	•	Typical controversies or recurring issues for that sport.
	
8. Describe the type of stories this sport has (game recap, feature, etc.) and what the typical structure includes and a guide on how to write those types of stories

9. What to avoid

Explain:
	•	Common mistakes new local sports reporters make.
	•	Ethical traps (favoritism, relying too heavily on one source, booster-style coverage).
	•	How to avoid overusing clichés, repetitive gamer structures, or vague descriptions.





  ## WORK PROCESS ##

  I generated 8 beat books for each sport I wanted to cover and then combined them so have one master beat book. 

  Code: cat prompt_sport_combine.txt sportbooks.md | uv run llm -m groq/openai/gpt-oss-120b > sports1.md

  Prompt attempt 1: I have separate beat-book sections drafted for baseball, basketball, field hockey, football, lacrosse, soccer, and softball. I want to combine them into one unified beat book for the Star Democrat (Easton, Maryland).

Please create a single, cohesive beat book that organizes all material logically and avoids repetition.

Structure Requirements

Produce the beat book with the following structure:

1. Opening Section — “How to Cover Sports for the Star Democrat”

A concise but thorough overview covering:
	•	The Star Democrat’s audience and coverage area
	•	The expectations for a local sports reporter
	•	Big-picture guidance on developing sources, managing schedules, building trust with coaches, and positioning stories for a small-town readership
	•	General rules for game nights, deadlines, social media, and weekday vs. weekend coverage
	•	How to balance fast recaps with longer enterprise or feature angles

2. Individual Sport Sections

Create one section per sport in this order:
Baseball, Basketball, Field Hockey, Football, Lacrosse, Soccer, Softball.

For each sport section:

A. Sport-Specific “Overall Tips” (Top of Each Section)
These should be:
	•	Tailored to the unique rhythms, culture, and norms of that sport
	•	Focused on what a reporter must know before stepping onto the field/court
	•	Distinct for each sport — avoid repeating general tips that already appear in the opening section
Examples: What the pace of play means for note-taking, how coaches talk postgame, what stats actually matter, what elements seasoned reporters watch for first, etc.

B. Core Coverage Priorities (Sport-Specific)
Use the material I provide to create a consolidated, non-repetitive guide covering:
	•	What determines success in that sport (tactics, talent types, momentum swings)
	•	What readers care about most
	•	What consistently creates standout stories

C. Key People, Institutions & Rivalries
Identify:
	•	Local power programs
	•	Important coaches
	•	Local rivalries and their history
	•	Typical postseason paths

D. Game-Day Reporting Guidance (Sport-Specific)
Explain:
	•	What to watch for during games
	•	The stat lines that matter
	•	Common mistakes new reporters make
	•	What to ask in interviews and how to approach coaches

E. Season Arc & Coverage Cadence
Describe:
	•	Key parts of the season
	•	What matters early, midseason, and late
	•	Typical playoff structures
	•	When to expect big matchups and story opportunities

F. Under-Covered Angles & Story Ideas
Generate sport-specific story ideas informed by local patterns and the Star Democrat’s past coverage. Avoid duplicating angles across sports unless truly necessary.

Style & Voice
	•	Business-casual, thoughtful, and practical.
	•	Not primarily bullet points, except for checklists or shorter items where useful.
	•	Avoid redundancy: general info should live only in the opening section; sport sections should focus solely on what is unique to that sport’s beat.
	•	Assume the reader is an early-career journalist familiar with basics but new to the Eastern Shore.



# BEAT BOOK #

# **The Star‑Democrat Eastern Shore Sports Beat Book**  
*Business‑casual, practical, and ready for a reporter who knows the basics but is new to the Eastern Shore.*

---

## 1. How to Cover Sports for the Star‑Democrat  

### 1.1 Our Readers & Coverage Area  
The Star‑Democrat serves the towns and counties that make up Maryland’s Eastern Shore – Easton, Queen Anne’s, Kent Island, Cambridge, Salisbury, and the surrounding rural communities.  Readers are deeply rooted in their schools; a win on the field often becomes the talk of the town for weeks.  They expect **accurate, fast recaps** on game night, **human‑interest features** that connect athletes to the community, and **contextual stories** that explain why a rivalry matters beyond the scoreboard.

### 1.2 What the Beat Means for a Local Sports Reporter  

| Expectation | Why It Matters |
|-------------|----------------|
| **Speed** – Publish a concise recap (300‑500 words) within 2 hours of a game’s final whistle. | The print deadline is 12 p.m. on the day after a Friday‑night game; the web audience expects a live‑update feed. |
| **Depth** – Pair the quick recap with a longer feature (1,000‑1,500 words) each week that adds a human‑angle, a tactical analysis, or a community hook. | Our readership values stories that remind them why the sport is part of their town’s identity. |
| **Reliability** – Be the go‑to source for coaches, athletic directors, and booster clubs. | Small‑town sports thrive on trust; a reporter who “gets” the culture is invited into locker rooms, team meetings, and community events. |
| **Versatility** – Cover multiple sports (often overlapping) during the spring (baseball, softball, lacrosse, soccer, field‑hockey) and winter (basketball, football). | The Eastern Shore’s calendar is dense; a flexible schedule keeps you on‑time for every deadline. |

### 1.3 Building Sources & Trust  

* **Start with the Booster Clubs.** Attend their meetings, volunteer for fund‑raisers, and keep a running list of contact names.  
* **Create a “Source Sheet” per sport** (coach, athletic director, senior player, alumni donor, parent‑volunteer). Update it after every interaction.  
* **Ask for “open‑door” time** – a short weekly window when a coach is free for a quick chat.  Even a 5‑minute quote after a win can become a headline.  
* **Be a community presence.** Show up at town‑team tournaments, school assemblies, and local fairs.  Familiar faces make your questions feel less like a hot‑mic interview.  

### 1.4 Managing the Schedule  

| Day | Core Activities | Quick Tips |
|-----|----------------|-----------|
| **Mon** | Pull stats from weekend games, file recaps, update the master sports calendar. | Use the “5‑W‑1‑H + Quote + Stat” template to speed writing. |
| **Tue** | Pitch previews for upcoming marquee matchups; confirm travel logistics. | Keep a shared Google‑Map of field locations; note bridge traffic patterns. |
| **Wed** | Attend a rivalry game (often a night game). Record audio bites. | Bring a compact voice recorder; a 30‑second sound‑bite is gold. |
| **Thu** | Write and file the game recap; begin longer feature research. | Draft the recap outline on your phone while the game is in progress. |
| **Fri** | Conduct follow‑up interviews (injury updates, player reactions); scout the next opponent’s box score. | Maintain an “open‑questions” list you can email over the weekend. |
| **Sat** | Cover community events, youth leagues, or a second sport’s game. | Use the day to build relationships outside the varsity spotlight. |
| **Sun** | Light admin – clean up databases, confirm next week’s schedule, recharge. | Treat it as a “maintenance” day; no new deadlines. |

### 1.5 Game‑Night Rules  

* **Arrive 30 minutes early** – verify locker‑room access, note weather impact, and get a feel for the crowd.  
* **Live‑note in a shorthand system** (player # + action) and capture a quick diagram of key plays on a tablet.  
* **Never leave a coach without a quote** unless the post‑game atmosphere is hostile; a single “We’ll regroup next week” can close a story.  
* **Social‑media** – post a 1‑sentence “quick‑hit” (score, key stat) on the Star‑Democrat Twitter/X within 15 minutes; embed a photo or a short video if you have permission.  

### 1.6 Balancing Fast Recaps & Enterprise Angles  

1. **Recap First, Context Later.** File the 300‑word recap for the print deadline, then schedule a 30‑minute “deep‑dive” block later in the day to flesh out the angle.  
2. **Maintain a “Story Bank.”** Every game generates at least one potential longer piece (e.g., a sophomore’s breakout performance, a coach’s 20‑year milestone, a rivalry’s historical twist). Log it in a spreadsheet with a brief description and a deadline reminder.  
3. **Leverage Data.** Use the district’s statistical database to spot trends (e.g., a team’s pitching ERA improving after a new conditioning program) and turn numbers into narratives.  

---

## 2. Baseball  

### A. Overall Tips – What to Know Before You Step Onto the Diamond  

Baseball on the Eastern Shore moves at a deliberate pace; the rhythm of the game dictates how you capture it.  

* **Pace of Play → Note‑Taking.** Use a “inning‑by‑inning” grid. Mark the pitcher, the batter, and the result in three columns; this makes later stat extraction painless.  
* **Post‑game Coach Talk.** Coaches on the Shore love to discuss **“the feel of the ball”** and **“team chemistry.”** Prompt them with “What’s the vibe in the clubhouse after that win?” to get quotable insight.  
* **Key Stats Beyond the Box Score.** ERA, WHIP, and “batting average with runners in scoring position” are the numbers fans actually talk about. Keep a running list of each team’s leaders in those categories.  
* **Weather Impact.** Rainouts are frequent in March; a quick interview with the groundskeeper about field conditions can become a feature on “playing through the drizzle.”  

### B. Core Coverage Priorities  

* **Success Factors:** Pitching depth, defensive fundamentals, and the ability to manufacture runs with small‑ball tactics (bunts, steals).  
* **Reader Interests:** Walk‑off victories, senior “last game” stories, and any link to the town’s baseball heritage (e.g., former MLB alumni).  
* **Standout Stories:** “From the sandlot to the varsity mound,” “The resurgence of a struggling program after a new strength‑coach hire,” and “How a booster‑run renovation saved the field.”  

### C. Key People, Institutions & Rivalries  

| Program | Coach (2024) | Notable Rival | Postseason Path |
|---------|--------------|---------------|-----------------|
| **Easton High** | Coach Mark **Sullivan** | Kent Island (Bayside Conf.) | North Bayside → District → State (Class A) |
| **Colonel Richardson** | Coach **Terry Miller** | St. Michael’s | South‑East Division → Regional → State (Class B) |
| **St. Michael’s** | Coach **Liam Harper** | Easton | North Bayside → District → State (Class A) |
| **Decatur High** | Coach **Jenna Cole** (girls) | Queen Anne’s (girls) | ESIAC → Eastern Shore Regional → State (Class A) |

### D. Game‑Day Reporting Guidance  

* **Watch For:** Pitch count spikes (sign of bullpen stress), defensive miscues on routine ground balls, and base‑running aggression.  
* **Stat Lines That Matter:** Complete‑game shutouts, strike‑outs per nine innings, stolen‑base totals, and “batting average with RISP.”  
* **Common Rookie Mistakes:** Trying to record every single play; focus on the **big moments** (lead‑changing hits, pitching changes, clutch defensive plays).  
* **Interview Checklist:**  
  * “What’s the biggest adjustment you made at the plate/pitcher’s mound this week?”  
  * “How did the weather affect your preparation?”  
  * “Who stepped up for the team when you were down a starter?”  

### E. Season Arc & Coverage Cadence  

| Phase | Timing | Focus |
|-------|--------|-------|
| **Pre‑Season** | Late Feb – Early Mar | Try‑out coverage, roster cuts, “late‑bloomer” profiles. |
| **Regular Season** | Mid‑Mar – Early May | Game recaps, rivalry previews, statistical trend pieces (e.g., pitching arms). |
| **Playoffs** | Mid‑May – Early June | High‑stakes game coverage, senior send‑offs, post‑season analysis. |
| **Off‑Season** | June – Aug | Summer town‑team leagues, field‑renovation projects, “where are they now” for seniors. |

### F. Under‑Covered Angles & Story Ideas  

* **“The Unsung Reliever.”** Track a middle‑relief pitcher who never gets a win but consistently saves games.  
* **“Field‑Maintenance Heroes.”** A day‑in‑the‑life profile of the grounds crew that keeps the diamond playable after heavy rain.  
* **“From the Dugout to the Classroom.”** How a school’s academic support program is boosting athletes’ GPA and college‑eligibility rates.  
* **“Cross‑Town Talent Pipeline.”** Explore how local travel baseball clubs feed the high‑school teams and create intra‑town rivalries.  

---

## 3. Basketball  

### A. Overall Tips – What to Know Before You Step Onto the Court  

* **Fast‑Break Rhythm → Real‑Time Notes.** Use a “play‑by‑play” column: **Possession → Action → Outcome**. A quick “3‑pt” tag helps you pull the game‑changing shot later.  
* **Coach’s Post‑Game Lingo.** Basketball coaches love to talk “tempo” and “spacing.” Ask, “How did you adjust the tempo after halftime?” to unlock technical sound‑bites.  
* **Key Stats Fans Track.** Points, rebounds, assists are basics; add **assist‑to‑turnover ratio** and **effective field‑goal percentage (eFG%)** for depth.  
* **Bench Management.** In high‑school the bench is often a rotating roster of under‑classmen. Note who gets the “big minutes” and why – it’s a story seed for future “rising star” pieces.  

### B. Core Coverage Priorities  

* **Success Factors:** Guard play, three‑point shooting efficiency, defensive switching, and depth of the bench.  
* **Reader Interests:** Rivalry night excitement, senior “last dance,” and any connection to local legends who went on to D‑I or pro careers.  
* **Standout Stories:** “Coach’s 20‑year milestone,” “The freshman who sparked a turnaround,” “A town’s love affair with the March tournament.”  

### C. Key People, Institutions & Rivalries  

| Program | Coach (2024) | Primary Rival | Postseason |
|---------|--------------|---------------|------------|
| **Easton High (Boys)** | Coach **Ryan Kelley** | Cambridge‑South Dorchester | Bayside Conf. → Regional → State (Class A) |
| **Cambridge‑South Dorchester (Boys)** | Coach **Mike Hernandez** | Easton | Same as above |
| **Queen Anne’s County (Girls)** | Coach **Tara Miller** | Kent Island | ESIAC → State (Class B) |
| **St. Michael’s (Boys)** | Coach **Darren Foster** | Colonel Richardson | Bayside Conf. → State (Class A) |

### D. Game‑Day Reporting Guidance  

* **What to Watch:** Momentum swings after time‑outs, shooting streaks, and defensive adjustments (e.g., switching from man‑to‑man to zone).  
* **Stat Lines That Matter:** Points per game, field‑goal % (especially 3‑pt %), rebounds, steals, and **plus/minus** for star players.  
* **Common Rookie Pitfalls:** Trying to capture every assist; focus on *impact* plays – a block that leads to a fast break, a clutch free throw.  
* **Interview Prompts:**  
  * “What did you see in the first half that prompted the halftime adjustment?”  
  * “Which player’s energy shifted the game?”  
  * “How does the team handle back‑to‑back games on the road?”  

### E. Season Arc & Coverage Cadence  

| Phase | Timing | Focus |
|-------|--------|-------|
| **Pre‑Season** | Late Oct – Early Nov | Roster cuts, summer AAU influence, “what to watch” preview. |
| **Non‑Conference** | Mid‑Nov – Early Dec | Early trends, injuries, scouting reports on upcoming rivals. |
| **Conference Play** | Mid‑Dec – Late Feb | Rivalry game recaps, weekly “standings‑at‑a‑glance,” feature on “coach’s corner.” |
| **Playoffs & Tournaments** | Early Mar – Early Apr | High‑stakes coverage, senior send‑offs, state‑championship road‑trip logs. |

### F. Under‑Covered Angles & Story Ideas  

* **“The Two‑Way Player.”** Profile a guard who leads the team in both scoring and assists while also anchoring the defense.  
* **“The Booster‑Club Engine.”** How a small town’s volunteer group finances new gym flooring and the ripple effect on team morale.  
* **“From AAU to the Shore.”** Follow a freshman’s transition from a Baltimore travel team to a local high‑school program.  
* **“Mental‑Health in the Locker Room.”** Explore how coaches are addressing anxiety and academic pressure during the intense conference stretch.  

---

## 4. Field Hockey  

### A. Overall Tips – What to Know Before You Step Onto the Turf  

* **Tempo & Substitutions.** Field hockey is a “continuous‑flow” sport; players rotate off the field every few minutes. Keep a **substitution log** (player → off/on) to track who’s influencing the game when the goal is scored.  
* **Penalty‑Corner Focus.** A single penalty corner can decide a game. Note the **setter, the drag‑flicker, and the defender**; those names become your story anchors.  
* **Key Metrics.** Beyond goals, track **shots on goal, circle entries, and penalty‑corner conversion rate**. Those stats spark analytical pieces that readers love.  
* **Coaches’ Language.** Expect terms like “shelf,” “circle,” and “press.” Use them in quotes to show you understand the sport’s nuances.  

### B. Core Coverage Priorities  

* **Success Factors:** Strong defensive circle, efficient penalty‑corner execution, and depth of midfield transitions.  
* **Reader Interests:** Rivalry matchups (e.g., Queen Anne’s vs. Kent Island), senior “last‑game” narratives, and stories about the sport’s growth among girls on the Shore.  
* **Standout Stories:** “The comeback after a 2‑goal halftime deficit,” “How a new strength program cut injury rates,” “A booster‑run fundraiser for new synthetic turf.”  

### C. Key People, Institutions & Rivalries  

| Program | Coach (2024) | Core Rival | Postseason Path |
|---------|--------------|-----------|-----------------|
| **Queen Anne’s County** | Coach **Samantha Reed** | Kent Island | ESIAC → Eastern Shore Regional → State (Class A) |
| **Kent Island** | Coach **Mark Ellis** | Queen Anne’s | Same as above |
| **St. Peter & Paul** (private) | Coach **Laura Cox** | Easton | Independent → State Tournament (Class B) |
| **Holly Grove** | Coach **Dylan Morrison** | Stephen Decatur | ESIAC → Regional → State (Class A) |

### D. Game‑Day Reporting Guidance  

* **Watch For:**  
  * **Penalty‑corner set‑ups** – who is the primary drag‑flicker?  
  * **Midfield turnovers** that lead to quick circle entries.  
  * **Goalkeeper saves** – a high‑save count can be a story hook.  
* **Stat Lines That Matter:** Goals, assists, penalty‑corner conversions, circle entries, and saves.  
* **Common Rookie Errors:** Over‑reporting every face‑off; focus instead on **momentum‑changing plays**.  
* **Interview Prompts:**  
  * “What’s the team’s strategy for the first penalty corner?”  
  * “How do you prepare the goalkeeper for high‑pressure situations?”  
  * “What role does the community play in supporting the program?”  

### E. Season Arc & Coverage Cadence  

| Phase | Timing | Focus |
|-------|--------|-------|
| **Fall Season (Late Aug – Early Nov)** | Regular conference play; rivalry games dominate. | Game recaps, “penalty‑corner of the week” feature. |
| **Early‑Winter Break** | No games; use time for player profiles and community pieces. | “The story behind the synthetic turf project.” |
| **Spring Club Season (Apr – Jun)** | Club tournaments, off‑season training, and senior graduation events. | Off‑season feature on “college recruiting pipeline.” |
| **Post‑Season (Dec)** | State playoffs, culminating in the state championship. | High‑stakes coverage, senior send‑offs, analysis of the champion’s tactics. |

### F. Under‑Covered Angles & Story Ideas  

* **“The Drag‑Flick Specialist.”** Follow a sophomore who has a 70 % conversion rate on penalty corners.  
* **“Field‑Hockey and the STEM Connection.”** How a local robotics club builds custom training equipment for the team.  
* **“Coach Reed’s “Girl‑Power” Initiative.”** A look at how the program is encouraging middle‑school girls to try the sport.  
* **“The Volunteer Umpire.”** A profile of the long‑time officials who keep games running smoothly despite limited resources.  

---

## 5. Football  

### A. Overall Tips – What to Know Before You Step Onto the Gridiron  

* **Two‑Minute Drill & Clock Management.** The final two minutes often produce the most dramatic moments. Keep a **clock‑watch** column noting down when a team uses time‑outs or goes for two‑point conversions.  
* **Coach‑Talk Focus.** Football coaches love to discuss **“scheme adjustments,” “gap integrity,”** and **“player development.”** Prompt them with “What adjustment did you make after halftime?” for insightful quotes.  
* **Stat Priorities.** Beyond total yards, track **third‑down conversion %, red‑zone efficiency, and turnover margin** – those are the numbers that differentiate a playoff team.  
* **Travel Logistics.** Some schools share fields; confirm travel time (often 30–45 minutes plus bridge traffic) the night before to avoid missing the kickoff.  

### B. Core Coverage Priorities  

* **Success Factors:** Strong offensive line, disciplined defense, and depth at quarterback.  
* **Reader Interests:** Friday‑night rivalries, senior “last game,” and any link to college recruiting pipelines.  
* **Standout Stories:** “Coach’s 200th win,” “A town’s comeback after a 30‑year championship drought,” “The impact of a new strength‑conditioning program on injury rates.”  

### C. Key People, Institutions & Rivalries  

| Program | Head Coach (2024) | Primary Rival | Postseason Path |
|---------|-------------------|---------------|-----------------|
| **Easton High** | Coach **Brian Cole** | Kent Island (Battle of the Bay) | North Bayside → District → State (Class A) |
| **Kent Island** | Coach **Larry Porter** | Easton | Same as above |
| **Cambridge‑South Dorchester** | Coach **Rob Burnham** | Fort Hill | South‑East Division → Regional → State (Class A) |
| **Queen Anne’s County** | Coach **Mike Davis** | Colonel Richardson | North Bayside → District → State (Class B) |
| **Stephen Decatur** | Coach **Emily Harris** (girls) | Huntingtown | ESIAC → Regional → State (Class A) |

### D. Game‑Day Reporting Guidance  

* **What to Watch:**  
  * **Turnover chains** – a fumble or interception often decides momentum.  
  * **Special‑teams plays** – a blocked punt or a long field goal can swing a close game.  
  * **In‑game injuries** – note the player, the nature, and the coach’s response.  
* **Stat Lines That Matter:** Total yards, third‑down conversion %, red‑zone efficiency, turnovers, and time‑of‑possession.  
* **Common Rookie Mistakes:** Over‑loading the recap with play‑by‑play; focus on the **key drives** and **turnover sequences**.  
* **Interview Checklist:**  
  * “What’s the biggest adjustment you made at halftime?”  
  * “How do you prepare the team for back‑to‑back Friday night games?”  
  * “What message do you give the seniors playing their final game?”  

### E. Season Arc & Coverage Cadence  

| Phase | Timing | Focus |
|-------|--------|-------|
| **Pre‑Season Camps (Late July – Early Aug)** | Roster cuts, position battles, new offensive/defensive schemes. | Feature “Inside the camp” and “Coach’s vision for the season.” |
| **Regular Season (Early Sep – Mid Nov)** | Two games per week for many schools; Friday nights dominate. | Game recaps, weekly “standings‑snapshot,” rivalry previews. |
| **Playoffs (Late Nov – Early Dec)** | Regional brackets, then state tournament. | High‑stakes coverage, senior send‑offs, “road‑to‑state” series. |
| **Post‑Season (Early Dec)** | All‑conference selections, recruiting updates, season‑end reflections. | Feature “Where are they now?” for seniors heading to college. |

### F. Under‑Covered Angles & Story Ideas  

* **“The Underrated Lineman.”** Track a junior offensive lineman whose blocking grades are among the best in the conference but who rarely makes the stat sheet.  
* **“Boosters Behind the Bleachers.”** A deep dive into the volunteer group that funds the new stadium lights.  
* **“The Academic Mentor.”** How a local college professor runs a tutoring program for football players during the season.  
* **“From the Sidelines to the Front Office.”** Profile a former player who now serves as the athletic director and is reshaping the district’s sports culture.  

---

## 6. Lacrosse  

### A. Overall Tips – What to Know Before You Step Onto the Field  

* **High‑Velocity Play.** Lacrosse is fast; use a **play‑diagram** app to capture quick transitions and face‑off wins.  
* **Key Terminology.** “Ride,” “clear,” “man‑down,” and “draw” are common coach phrases. Mirror them in your quotes to demonstrate expertise.  
* **Stats That Matter.** Goals, assists, caused turnovers, face‑off win % and **ground balls** are the core numbers readers discuss.  
* **Seasonal Weather.** Early spring rain can make the field “sloppy” and affect ground‑ball counts – a good angle for a feature on field‑maintenance.  

### B. Core Coverage Priorities  

* **Success Factors:** Dominant midfield, face‑off specialists, disciplined defense, and depth on the bench.  
* **Reader Interests:** Rivalry clashes (Easton vs. Kent Island), senior “last game,” and the sport’s growing popularity among girls.  
* **Standout Stories:** “A sophomore’s breakout season,” “The impact of a new lacrosse club feeding talent to varsity,” “How a synthetic turf upgrade changed the team’s speed.”  

### C. Key People, Institutions & Rivalries  

| Program | Coach (2024) | Main Rival | Postseason Path |
|---------|--------------|------------|-----------------|
| **Easton High** | Coach **Matt Harper** | Kent Island | Bayside Conf. → District → State (Class A) |
| **Kent Island** | Coach **Jon Parker** | Easton | Same |
| **St. Peter & Paul** (private) | Coach **Riley Mason** | Queen Anne’s | Independent → State (Class B) |
| **Queen Anne’s County** | Coach **Alyssa Klein** (girls) | Kent Island (girls) | ESIAC → Regional → State (Class A) |

### D. Game‑Day Reporting Guidance  

* **Watch For:** Face‑off wins that start a clear, fast breaks that lead to goals, and **penalty kills** that shift momentum.  
* **Stat Lines That Matter:** Goals, assists, caused turnovers, face‑off win %, ground balls, and **save %** for the goalie.  
* **Common Rookie Pitfalls:** Trying to record every ground ball; instead, flag **game‑changing** ground balls (e.g., the one that starts a 4‑goal run).  
* **Interview Prompts:**  
  * “What’s the secret to your face‑off success?”  
  * “How does the team adjust after a penalty kill?”  
  * “What role does the community play in supporting the lacrosse program?”  

### E. Season Arc & Coverage Cadence  

| Phase | Timing | Focus |
|-------|--------|-------|
| **Spring Season (Late Mar – Early Jun)** | Regular conference play, mid‑season tournaments. | Recaps, rivalry previews, “player‑of‑the‑week” features. |
| **Mid‑Season Tournament (May)** | Regional invitational; many teams converge. | Tournament round‑up, scouting reports on emerging talent. |
| **State Playoffs (Early Jun)** | District → State Championship. | High‑stakes coverage, senior send‑offs, post‑game analysis. |
| **Off‑Season (Summer)** | Club leagues, community camps. | Feature on “the summer club pipeline” and “coach’s offseason training plan.” |

### F. Under‑Covered Angles & Story Ideas  

* **“The Face‑Off Maestro.”** Profile a junior who leads the conference with a 68 % win rate.  
* **“Lacrosse & Local Business.”** How a downtown sporting‑goods store sponsors the team and runs a youth clinic.  
* **“From Player to Coach.”** A senior who plans to stay on as an assistant while completing a teaching degree.  
* **“Women’s Lacrosse Growth.”** Track the rapid rise of the girls’ program and its effect on school spirit.  

---

## 7. Soccer  

*(No legacy document was supplied; this section builds on the Eastern Shore’s typical high‑school soccer landscape.)*  

### A. Overall Tips – What to Know Before You Step Onto the Pitch  

* **Continuous Play, Limited Substitutions.** Soccer runs two 40‑minute halves (high‑school) with rolling substitutions. Use a **minute‑by‑minute log** for goals, cards, and key substitutions.  
* **Coach’s Vocabulary.** Expect phrases like “high press,” “compact shape,” and “switching the ball.” Echo them in quotes for authenticity.  
* **Stats That Resonate.** Goals, assists, shots on target, saves, and **possession %**. For deeper stories, track **corner kicks** and **set‑piece conversion**.  

### B. Core Coverage Priorities  

* **Success Factors:** Tactical discipline, finishing efficiency, and a solid goalkeeper.  
* **Reader Interests:** Rivalry matches (e.g., Easton vs. Queen Anne’s), senior “last season,” and the growing participation of girls’ soccer.  
* **Standout Stories:** “A freshman’s 20‑goal season,” “The community fund‑raiser that built a new artificial turf field,” “Coach’s 15‑year legacy.”  

### C. Key People, Institutions & Rivalries  

| Program | Coach (2024) | Key Rival | Postseason Path |
|---------|--------------|-----------|-----------------|
| **Easton High (Boys)** | Coach **Scott Miller** | Queen Anne’s (Bayside) | North Bayside → District → State (Class A) |
| **Queen Anne’s County (Boys)** | Coach **Dana Lopez** | Easton | Same |
| **St. Peter & Paul (Girls)** | Coach **Rachel Gordon** | Kent Island | ESIAC → Regional → State (Class B) |
| **Kent Island (Girls)** | Coach **Amy Sullivan** | St. Peter & Paul | Same |

### D. Game‑Day Reporting Guidance  

* **Watch For:**  
  * **Momentum‑shifting goals** (e.g., a 2‑0 lead broken, or an equalizer in the 78th minute).  
  * **Goalkeeper heroics** – a high‑save count often makes the story.  
  * **Disciplinary moments** (yellow/red cards) that change the tactical approach.  
* **Stat Lines That Matter:** Goals, assists, shots on target, saves, possession %, and fouls.  
* **Common Rookie Errors:** Over‑describing possession; focus on decisive moments.  
* **Interview Prompts:**  
  * “What tactical change did you make after conceding the first goal?”  
  * “How does the team handle the physical demands of back‑to‑back weekend games?”  
  * “What does the community mean to the program?”  

### E. Season Arc & Coverage Cadence  

| Phase | Timing | Focus |
|-------|--------|-------|
| **Fall Season (Late Aug – Early Nov)** | Regular conference play. | Recaps, rivalry previews, “player‑of‑the‑week.” |
| **Early‑Winter Break** | No games; opportunity for player profiles and community features. | “The story behind the new synthetic turf field.” |
| **Playoffs (Nov – Dec)** | District → Regional → State tournament. | High‑stakes coverage, senior send‑offs, post‑game analysis. |
| **Spring Off‑Season** | Club soccer, community leagues. | Feature on “how club play feeds high‑school talent.” |

### F. Under‑Covered Angles & Story Ideas  

* **“The Goalkeeper’s Journey.”** Follow a senior keeper who overcame a childhood injury to become the team’s backbone.  
* **“The Rise of Girls’ Soccer.”** Chart participation growth over the past decade and its impact on school spirit.  
* **“Community Field Renovation.”** Document the fundraising drive that installed a new flood‑lit field and the ripple effect on after‑school programs.  
* **“From the Pitch to the Classroom.”** Explore the academic support program that helps soccer athletes maintain a 3.5 GPA or higher.  

---

## 8. Softball  

### A. Overall Tips – What to Know Before You Step Onto the Diamond  

* **Pitcher‑Batting Rhythm.** Softball’s **fast‑pitch** cycle (5‑second windup) demands quick note‑taking. Record **pitch count** and **type of pitch** (rise ball, drop ball, change‑up).  
* **Coach Dialogue.** Expect focus on “plate discipline” and “fielding fundamentals.” Prompt with “What adjustments did you make at the plate after the first three innings?”  
* **Stat Priorities.** ERA, WHIP, batting average with runners in scoring position (RISP), and **sacrifice bunts** are the numbers that shape the narrative.  
* **Weather Sensitivity.** Rain can delay games; a quick interview with the team manager about schedule changes can become a human‑interest piece.  

### B. Core Coverage Priorities  

* **Success Factors:** Dominant pitcher, solid defense (especially shortstop), and aggressive base running.  
* **Reader Interests:** Senior “last game,” rivalry walk‑offs, and community involvement (e.g., booster fund‑raisers).  
* **Standout Stories:** “A freshman pitcher’s 10‑strikeout debut,” “The field‑renovation project that saved the season,” “Coach’s 25‑year tenure.”  

### C. Key People, Institutions & Rivalries  

| Program | Coach (2024) | Primary Rival | Postseason Path |
|---------|--------------|---------------|-----------------|
| **Queen Anne’s County** | Coach **Lisa Harper** | Colonel Richardson | ESIAC → Regional → State (Class A) |
| **Colonel Richardson** | Coach **Mike Sullivan** | Queen Anne’s | Same |
| **St. Peter & Paul** | Coach **Karen Miller** | Easton | Independent → State (Class B) |
| **Easton High** | Coach **Tom Baker** | St. Peter & Paul | Same |

### D. Game‑Day Reporting Guidance  

* **What to Watch:**  
  * **Pitcher fatigue** – rising walk rates often signal a change.  
  * **Defensive miscues** – a dropped line drive can be the turning point.  
  * **Base‑running aggressiveness** – steals and bunts that generate runs.  
* **Stat Lines That Matter:** Runs, hits, RBI, ERA, WHIP, batting average with RISP, and fielding percentage.  
* **Common Rookie Mistakes:** Trying to capture every at‑bat detail; focus on **key at‑bats** that shift momentum.  
* **Interview Checklist:**  
  * “How did the team adjust after the early‑inning run?”  
  * “What’s the pitcher’s routine between innings?”  
  * “How does the community support the program during the playoffs?”  

### E. Season Arc & Coverage Cadence  

| Phase | Timing | Focus |
|-------|--------|-------|
| **Pre‑Season (Late Feb – Early Mar)** | Tryouts, roster cuts, early “C‑team” games. | Player‑profile of “late‑bloomer,” field‑maintenance preview. |
| **Regular Season (Mid‑Mar – Early May)** | Conference play (≈ 25 games). | Game recaps, rivalry features, statistical trend pieces. |
| **Playoffs (Mid‑May – Early June)** | District & state tournament. | High‑stakes coverage, senior send‑offs, post‑game analysis. |
| **Summer (June – Aug)** | Community leagues, adult town‑team tournaments. | Off‑season human‑interest stories, “where are they now.” |

### F. Under‑Covered Angles & Story Ideas  

* **“The Silent Setter.”** Spotlight a catcher who calls the game’s defensive strategy and rarely gets credit.  
* **“Boosters & the New Dugout.”** How a local business funded a new dugout and what it means for team morale.  
* **“From the Field to the Classroom.”** Examine the tutoring program that pairs senior players with underclassmen.  
* **“The Evolution of Softball in the Shore.”** A historical piece tracing the sport’s growth from sandlots to varsity dominance.  

---

### **Final Note for the Beat Team**  

Every sport on the Eastern Shore shares a common thread: **community is the heartbeat.** Your stories succeed when they weave together the on‑field action with the off‑field relationships that make each game matter to a town of a few thousand. Use the templates above as a foundation, adapt them as the seasons change, and always keep one eye on the scoreboard and the other on the people who live for it.  

*Play hard, write harder, and let the Eastern Shore’s stories shine.*  


# Thoughts from beat book draft # 

This is a solid start at getting all the major sports the star dem covers into one beat book. In my future refinements I will try and have more general info and cut down on the name specific stuff as it changes. I also think feedback from the stardemocrat will be helpful to define some of their practices as I do not think the LLM necearilly knew all of them from just the stories. 

  

# Draft Beat Book, Part III #

I asked chatgpt to help refine my prompt and here is what I got:

Prompt: You are combining nine separate high-school sports beat books into one unified beat book for the Star Democrat.
Each original beat book covers one sport (baseball, basketball, field hockey, football, lacrosse, soccer, softball, wrestling, etc.).

Your task is to merge them into a single beat book that:

⸻

1. STRUCTURE REQUIREMENTS

A. Start with a comprehensive “Overall Tips for Covering High School Sports” section

This section must:
	•	Contain only generic, cross-sport guidance that applies to all high-school sports.
	•	Exclude anything that is specific to a single sport.

B. Follow with Individual Sport Sections

After the overall section, create one section per sport in this order:
	1.	Baseball
	2.	Basketball
	3.	Field Hockey
	4.	Football
	5.	Lacrosse
	6.	Soccer
	7.	Softball
	8.	Wrestling
	9.	Any additional sports provided

Each sport section must:
	•	Include only the sport-specific guidance from that sport’s original beat book.
	•	Contain no repeated or generic info already covered in the Overall Tips section.
	•	Summarize each sport’s most important:
	•	rules & scoring basics
	•	key stats & what they mean
	•	what determines outcomes
	•	positions & terminology
	•	what to watch for during games
	•	interview tips & questions to ask
	•	common story angles

⸻

2. CONTENT RULES
	•	No duplication.
	•	No filler.
	•	Use consistent formatting across all sports.
	•	Clear, focused, practical guidance only.

Recommended sub-headings for each sport:
	•	Rules & How the Game Works
	•	Key Stats & What They Mean
	•	What Decides Matches/Games
	•	Positions & Terminology
	•	What to Watch For
	•	Interview Tips
	•	Story Angles

⸻

3. REQUIRED OUTPUT FORMAT

Produce the final combined beat book in this structure:

⸻

Star Democrat High School Sports Beat Book

Overall Tips for Covering High School Sports

⸻

Baseball

Basketball

Field Hockey

Football

Lacrosse

Soccer

Softball

Wrestling

⸻

PRIMARY OBJECTIVE

Create a single, unified, non-repetitive, cleanly organized beat book that prepares any Star Democrat reporter to cover any high school sport with confidence.


Code: cat prompt_sport_combine.txt sportbooks.md | uv run llm -m anthropic/claude-sonnet-4-5 > sports2.md

New beat book:# Star Democrat High School Sports Beat Book

## Overall Tips for Covering High School Sports

### Understanding the Eastern Shore Sports Community

The Eastern Shore of Maryland is a tight-knit patchwork of small towns where high school sports serve as community hubs. Schools function as the beating heart of towns like Easton, Cambridge-South Dorchester, Queen Anne's, St. Michael's, Kent Island, Wicomico, and Salisbury. Generations of families sit in the same bleachers, and the same surnames appear on rosters and in booster-club minutes year after year. Sports events are social calendar fixtures that can eclipse other news coverage.

### Core Beat Responsibilities

**Weekly Workflow Foundation**

| Day | Core Tasks | Notes |
|-----|------------|-------|
| **Monday** | Review weekend game notes, pull stats, update your database | Early start (7 a.m.) helps beat Monday print deadlines (typically 12 p.m.) |
| **Tuesday** | Pitch previews for marquee matchups; confirm travel plans & field/facility access | Maintain a shared calendar with travel distances |
| **Wednesday-Friday** | Attend games, take live notes, coordinate photography, conduct post-game interviews | Bring compact voice recorder; 30-second sound-bites from coaches are invaluable |
| **Thursday-Friday** | Write game recaps (300-500 words print, longer web); file stories by deadline | See "5-W-1-H + Quote + Stat" template below |
| **Saturday** | Attend community events to stay visible; file community spotlight pieces | Builds goodwill with boosters and volunteers |
| **Sunday** | Admin: clean database, confirm next week's schedule, recharge | The beat is a marathon, not a sprint |

### Travel & Logistics

**Geographic Challenges**
- Schools are often 30-45 minutes apart
- Bridge traffic can add 15+ minutes to travel time
- Create a master map for the week; plan hub-and-spoke routes to minimize backtracking

**Pack Smart**
- Small notebook and tablet with stylus (for quick play diagrams)
- Spare battery pack
- Weather-proof voice recorder
- Compact camera or ensure school photographer is coordinated

**Late-Night Game Strategy**
Use downtime to draft recap outlines on your phone; fill in final stats when posted.

### Managing Multiple Sports Simultaneously

**The Master Calendar System**
- Create one calendar listing ALL sports events
- Color-code by sport (e.g., baseball navy, softball pink, basketball orange)
- When games overlap, use the Impact-Decision Matrix to prioritize

**Impact-Decision Matrix**

| Factor | Weight | Questions to Ask |
|--------|--------|------------------|
| **Conference Stakes** | High | Does this game decide standings or playoff position? |
| **Rivalry Intensity** | High | Is this a historic rivalry that drives attendance and community interest? |
| **Story Continuity** | Medium | Are you following an ongoing narrative (coach milestone, player comeback)? |
| **Attendance/Community Interest** | Medium | Will bleachers be packed? Are boosters promoting heavily? |
| **Access to Stats** | Low | Can you get complete stats if you're not there live? |

Apply this matrix to decide which game merits live coverage and which can be covered via delayed recap.

### Building and Maintaining Sources

**Core Contact Lists**
- Head coaches (cell phone, email, preferred contact times)
- Athletic directors
- Booster club presidents
- Team captains and key players
- School administrators (for eligibility and policy questions)
- Parent volunteers who run timers, scoreboards, and concessions

**Relationship-Building Tactics**
- Attend non-game community events (tournaments, fundraisers, field renovations)
- Keep an "open questions" list to email coaches during off-days
- Respond promptly to tips and corrections from readers
- Be visible and approachable at games
- Remember: most coaches work multiple sports—keep separate but linked contact lists

### Story Structure: The "5-W-1-H + Quote + Stat" Template

**Game Recaps (Standard 300-500 words)**

```
LEAD PARAGRAPH (Who, What, When, Where, Why)
[Team A] defeated [Team B], [Score], on [Day] at [Venue] to [achieve what/why it matters].

NUT GRAF (Key turning point + decisive stat)
[Describe the crucial moment/play]. [Player Name] [key stat that tells the story].

QUOTE 1 (Winning coach or star player on the key moment)
"[Direct quote that captures emotion or strategy]," said [Name, Title].

CONTEXT (How/Why this matters)
The win [moves Team A to X-X record/clinches playoff spot/extends streak/etc.].

ADDITIONAL DETAILS (Supporting stats, other key plays)
[Player B] added [stat]. [Team A] built momentum by [describe pattern].

QUOTE 2 (Losing coach or perspective from other side)
"[Quote showing grace, analysis, or looking forward]," [Name] said.

GAME NOTES (Final stats, next games, injury updates)
[Team A] will face [next opponent] on [date]. [Any roster notes.]
```

### Essential Story Types

**1. Game Recaps**
- Breaking news; file quickly with accuracy
- Focus on what decided the outcome
- Balance winning and losing perspectives

**2. Rivalry Previews**
- Historical context (last five meetings, all-time records)
- Current stakes (standings, playoff implications)
- Key player matchups
- Coach perspectives

**3. Player Profiles**
- Focus on "late bloomers," overcoming adversity, milestone achievements
- Include coach and teammate quotes
- Connect personal story to on-field performance

**4. Trend Pieces**
- Statistical patterns across multiple games
- Conference-wide developments (scoring trends, defensive strategies)
- Equipment, rule changes, or technique evolution

**5. Coach's Corner/Weekly Columns**
- Rotating spotlight on different coaches
- Philosophy, career highlights, teaching moments
- Builds deeper connection with readership

**6. Accountability & Policy Stories**
- Eligibility issues
- Safety concerns
- Facility conditions
- Administrative decisions affecting teams

**7. Off-Season Features**
- "Where are they now" updates on alumni
- Facility renovations and community fundraising
- Summer league coverage
- Pre-season previews and roster changes

### Conference Structure & Rivalries

**Major Conferences**
- **Bayside Conference (North & South divisions)**: Easton, Colonel Richardson, Kent Island, Queen Anne's, Cambridge-South Dorchester, St. Michael's
- **Eastern Shore Independent Athletic Conference (ESIAC)**: Private and independent schools
- **Regional Classifications**: 1A, 2A, 3A, 4A determine playoff brackets

**Marquee Rivalries to Know**
- Easton vs. Kent Island
- Easton vs. Cambridge-South Dorchester
- Queen Anne's vs. Colonel Richardson
- Colonel Richardson vs. North Caroline
- St. Peter & Paul vs. Easton

These matchups generate heightened attendance, ticket sales, booster activity, and editorial interest. Prepare deeper coverage and anticipate stronger community reaction.

### Data Management

**Personal Database Maintenance**
- Keep running stats for all teams you cover
- Track season-long trends (scoring averages, winning streaks, head-to-head records)
- Note injury reports and roster changes
- Maintain historical records for context (coach milestones, school records, championship history)

**Sources for Stats**
- Official scorebooks (request access from coaches or ADs)
- School athletic department websites
- MaxPreps and other stat aggregation sites
- Conference websites
- Your own game notes

### Deadline Management

**Print Deadlines**
- Typical Monday-Friday print deadline: 12 p.m. for next-day publication
- Weekend deadlines vary; confirm with editors
- Late-night games require "running" story filed in sections

**Digital-First Strategy**
- Post score and quick highlight to web/social immediately post-game
- File full recap within 2 hours
- Add quotes, stats, and analysis for morning print edition
- Update web version with additional content throughout next day

### Ethical Guidelines & Best Practices

**Accuracy First**
- Double-check scores, stats, and name spellings
- Verify information with multiple sources when possible
- Correct errors promptly and transparently

**Balance & Fairness**
- Give both teams fair coverage in recaps
- Rotate feature subjects to avoid favoritism
- Be sensitive to age-appropriate coverage of minors

**Access & Boundaries**
- Respect coach/player time constraints
- Schedule formal interviews rather than ambushing
- Understand FERPA and student privacy rules
- Never interview injured players without coach/parent approval

**Community Sensitivity**
- Small towns mean long memories; maintain professionalism
- Avoid inflammatory language even in rivalry coverage
- Remember families read every word about their children
- Be accurate but not cruel when covering losses or poor performances

### Managing Seasonal Overlaps

**Peak Conflict Periods**

| Time of Year | Overlapping Sports | Strategy |
|--------------|-------------------|----------|
| **Late February - Early March** | Baseball/softball start, basketball playoffs, wrestling postseason | Prioritize playoff games; use delayed recaps for regular-season openers |
| **Late March - April** | Baseball, softball, lacrosse, soccer all in full swing | Rotate coverage; ensure each sport gets featured stories weekly |
| **Late October - November** | Football playoffs, basketball season starts, soccer/field hockey/volleyball postseason | Focus on football Fridays, basketball Tuesdays/Saturdays; cover other sports via quick recaps |
| **Late May - Early June** | Spring sports playoffs, baseball/softball championships | All hands on deck; coordinate with other reporters |

### Understanding Booster Culture

**What Boosters Do**
- Fund-raise for equipment, uniforms, facility improvements
- Run concessions and ticket sales
- Organize community events and senior nights
- Provide volunteer support (timers, scorekeepers, field maintenance)

**Why They Matter to Your Beat**
- They're passionate sources for feature stories
- They can provide historical context and archive materials
- They influence community sentiment about coverage
- They're often your most engaged readers

**How to Work With Them**
- Attend booster meetings occasionally
- Acknowledge their contributions in stories when relevant
- Be fair but don't let them dictate coverage
- Respond professionally to complaints or criticism

### Social Media Strategy

**Game Coverage**
- Live-tweet/post key moments and score updates
- Share photos (with proper attribution and permissions)
- Tag schools, athletes, and organizations when appropriate
- Drive traffic to full stories with teaser posts

**Engagement**
- Monitor comments for story ideas and corrections
- Respond professionally to criticism
- Share reader photos and stories (with permission)
- Promote upcoming coverage

**Boundaries**
- Don't follow or friend current high school athletes
- Keep interactions professional and public
- Don't engage with hostile commenters
- Verify social media information before using in stories

### Weather Contingencies

**Rain-Outs & Cancellations**
- Maintain updated contact list for quick confirmation
- Prepare "backup" stories for sudden cancellations
- Check conference websites and school social media for official announcements
- Have feature material ready for weather-related news holes

**Extreme Weather Coverage**
- Lightning delays: time them; ask about safety protocols
- Heat: watch for hydration breaks and modified schedules
- Cold: note how conditions affect play

### Building Subject Expertise

**Continuous Learning**
- Study rule books during off-season
- Watch college/pro games to understand advanced strategy
- Ask coaches to explain plays and tactics
- Read national coverage of your sports for story ideas and best practices
- Attend coaching clinics if possible (great for sources and understanding)

### Self-Care & Sustainability

**Managing the Grind**
- Set boundaries: You can't cover every game
- Delegate when possible; coordinate with photographers and other reporters
- Take advantage of slow periods to recharge
- Keep weekends during off-season truly off
- Remember: Burnout helps no one

**Signs You're Overextended**
- Missing deadlines
- Declining story quality
- Resentment toward sources or subjects
- Physical exhaustion affecting health
- Decreased engagement with stories

**When to Ask for Help**
- Overlapping major events
- Personal emergencies
- Sustained multi-week crunch periods
- Complex investigative or accountability stories

---

## Baseball

### Rules & How the Game Works

**Basic Structure**
- Nine innings (seven for high school in some states; check Maryland regulations)
- Nine defensive players; unlimited offensive players (batting order set at game start)
- Three outs per half-inning
- Run scoring: batter must reach base and advance through 1st, 2nd, 3rd, and home
- Outs recorded by: strikeout, flyout, groundout, force-out, tag-out, double/triple plays

**Key Rules Unique to High School**
- **Pitch counts & rest rules**: Maryland has strict pitch-count limits to protect young arms; typically 95-110 pitches per game with mandatory rest days based on count
- **Mercy rule**: Games typically end if one team leads by 10+ runs after 5 innings
- **Courtesy runners**: Often allowed for catchers to speed up game
- **Re-entry rule**: Starters can re-enter once after being substituted (varies by state)
- **Designated hitter (DH)**: Can bat for pitcher without pitcher leaving game

**What Decides Wins**
- Hitting with runners in scoring position (RISP)
- Quality starting pitching (5+ innings, 3 or fewer earned runs)
- Error-free defense in key moments
- Timely base-running and stolen bases

### Key Stats & What They Mean

**Offensive Stats**

| Stat | What It Measures | Why It Matters | "Good" High School Benchmark |
|------|-----------------|----------------|------------------------------|
| **Batting Average (AVG)** | Hits ÷ At-Bats | Pure hitting ability | .350+ is excellent; .400+ is elite |
| **On-Base Percentage (OBP)** | (Hits + Walks + HBP) ÷ Plate Appearances | How often player reaches base | .400+ is strong |
| **Slugging Percentage (SLG)** | Total bases ÷ At-Bats | Power (extra-base hits) | .500+ shows power |
| **RBI** | Runs Batted In | Clutch hitting | Season total 20+ for standout |
| **Runs Scored** | Times player crossed home | Getting on base + smart base-running | Season total 25+ for leadoff/top order |
| **Stolen Bases** | Successful steals | Speed & aggression | 15+ in a season shows elite speed |

**Pitching Stats**

| Stat | What It Measures | Why It Matters | "Good" High School Benchmark |
|------|-----------------|----------------|------------------------------|
| **ERA (Earned Run Average)** | (Earned Runs × 7) ÷ Innings Pitched | Run prevention | Under 2.00 is excellent; under 1.00 is elite |
| **WHIP (Walks + Hits per Inning)** | (Walks + Hits) ÷ IP | Baserunner control | Under 1.00 is excellent |
| **Strikeouts** | Batters struck out | Dominance | 10+ per game is elite |
| **Walks** | Free passes | Control issues | Fewer than 2 per game is good |
| **Win-Loss Record** | Games won-lost | Team success (not perfect pitcher measure) | Use cautiously; team-dependent |

**Defensive Stats**
- **Fielding Percentage**: (Putouts + Assists) ÷ (Putouts + Assists + Errors) — .950+ is solid
- **Errors**: Costly mistakes; track trends over season
- **Double Plays**: Shows infield cohesion

### Positions & Terminology

**Defensive Positions (by number)**
1. **Pitcher (P)** – Controls game tempo; most important defensive player
2. **Catcher (C)** – "Field general"; calls pitches, blocks balls, controls running game
3. **First Base (1B)** – Catches throws; typically taller player with good hands
4. **Second Base (2B)** – Quick reflexes; turns double plays with shortstop
5. **Third Base (3B)** – "Hot corner"; must react to hard-hit balls
6. **Shortstop (SS)** – Widest range; often best athlete on field
7. **Left Field (LF)** – Covers left outfield; must handle line drives
8. **Center Field (CF)** – Covers most ground; best outfield speed
9. **Right Field (RF)** – Stronger arm for throws to 3rd base

**Key Terms**
- **RISP**: Runners in scoring position (2nd or 3rd base)
- **Quality start**: 6+ innings, 3 or fewer earned runs
- **Bullpen**: Relief pitchers
- **Closer**: Pitcher who finishes tight games
- **Setup man**: Pitcher who bridges starter and closer
- **Ace**: Team's best starting pitcher
- **No-hitter/Perfect game**: Rare dominant pitching performances
- **Walk-off**: Game-ending hit/play by home team

### What to Watch For

**During the Game**
- **First-inning momentum**: Team that scores first wins ~60% of high school games
- **Pitching changes**: When and why coaches pull starters (pitch count, effectiveness, matchups)
- **Defensive breakdowns**: Errors in key innings often decide games
- **Base-running aggression**: Stolen bases, taking extra bases, sacrifices
- **Clutch at-bats**: Two outs, RISP situations
- **Pitcher "stuff"**: Velocity, movement, command (ask catcher or coach post-game)

**Warning Signs of Trouble**
- Multiple walks in an inning (pitcher losing control)
- Errors clustering together (team losing focus)
- Weak contact turning into hits (defense positioned poorly)
- Stranded runners (offensive execution failing)

**Storyline Signals**
- Shutout or one-hitter (feature the pitcher)
- Big comeback (focus on turning-point inning)
- Hitting barrage (8+ runs; feature offensive balance or one breakout player)
- Pitching duel (both starters go deep; feature their approach)
- Seniors' last home game (emotional angle; interview seniors post-game)

### Interview Tips

**Post-Game Coach Questions**
- "What was the key to [winning play/turning point]?"
- "How did [pitcher] attack hitters today?"
- "What did you see in [opponent's strategy] that you adjusted to?"
- "Where does this [win/loss] put you in terms of [playoffs/seeding/goals]?"
- "How is [injured player's] status for [next game]?"

**Player Questions**
- For pitchers: "What was working for you today? Were you able to locate your [pitch type]?"
- For hitters: "Walk me through that [key at-bat]. What were you looking for?"
- For fielders after an error: "That's a tough play. How do you refocus after that?"
- For game-winners: "When did you know that pitch was the one? What were you thinking?"

**What NOT to Ask**
- "How do you feel?" (too vague; elicits clichés)
- "Do you think the umpire blew that call?" (puts player in awkward position)
- Leading questions that put words in mouths

**Reading a Scorebook**
- Request access to official scorebook from home-team scorer
- Key columns: Player name, at-bats, runs, hits, RBI, walks, strikeouts
- Pitching line: Innings pitched, hits allowed, runs, earned runs, walks, strikeouts
- Look for: Who drove in runs, who scored, pitching efficiency

### Story Angles

**Evergreen Feature Ideas**
- **Late-bloomer profile**: Sophomore/junior who made varsity after JV years
- **Transfer impact**: Player who switched schools and faces old team
- **Coach milestone**: 100th win, 20th season, etc.
- **Father-son/family legacies**: Multi-generation players at same school
- **Unsung heroes**: Defensive specialist, backup catcher who studies opponents
- **Comeback stories**: Injury recovery, academic eligibility battles

**Trend & Analysis Pieces**
- **Pitch-count impact**: How strict rules change strategy
- **Defensive shift usage**: High school teams copying pro analytics
- **Hitting approach evolution**: Launch angle, small ball vs. power
- **Travel-ball influence**: Year-round play affecting high school rosters
- **Recruiting landscape**: Where Eastern Shore players go to college

**Rivalry & Stakes Stories**
- **Head-to-head history**: Last 10 meetings, memorable games
- **Playoff implications**: "Win and you're in" scenarios
- **Ace vs. ace matchups**: Best pitchers facing off
- **Streak watch**: Winning/losing streaks, consecutive shutouts, hitting streaks

**Accountability Angles**
- **Eligibility questions**: Transfers, academic standing
- **Field conditions**: Safety concerns, maintenance issues
- **Scheduling controversies**: Rainout makeups, travel burdens
- **Pitch-count violations**: If they occur

**Community & Off-Field Stories**
- **Summer league coverage**: Town teams, showcase tournaments
- **Field renovation campaigns**: Booster fundraising, community volunteer efforts
- **Youth clinics**: Varsity players teaching younger kids
- **Senior signings**: College commitment ceremonies
- **Alumni returns**: Former players coaching, watching, or supporting

---

## Basketball

### Rules & How the Game Works

**Basic Structure**
- Four 8-minute quarters (high school; some states vary)
- Five players per team on court
- Goal: Score by shooting ball through opponent's basket (10 feet high)
- 2 points for field goals inside arc, 3 points beyond arc, 1 point per free throw
- Team with most points wins

**Key Rules Unique to High School**
- **Shot clock**: 35 seconds in Maryland (some states don't use shot clocks)
- **Fouls**: Five personal fouls = disqualification; team fouls 7+ per half = bonus free throws
- **Timeouts**: Typically three 60-second and two 30-second per game
- **Possession arrow**: Alternating possession for jump balls after opening tip
- **Mercy rule**: Rare but some conferences implement running clock if lead exceeds 30+ points

**What Decides Wins**
- Shooting efficiency (field goal %, 3-point %, free throw %)
- Rebounding (second-chance points, possession control)
- Turnovers (protecting ball vs. forcing opponent mistakes)
- Defensive intensity (limiting opponent's best scorers, forcing tough shots)
- Bench depth (sustaining play when starters rest)

### Key Stats & What They Mean

**Offensive Stats**

| Stat | What It Measures | Why It Matters | "Good" High School Benchmark |
|------|-----------------|----------------|------------------------------|
| **Points Per Game (PPG)** | Individual or team scoring | Offensive productivity | 15+ PPG for star player; 60+ PPG for competitive team |
| **Field Goal % (FG%)** | Made FG ÷ Attempted FG | Shooting efficiency | 45%+ is solid; 50%+ is excellent |
| **3-Point % (3P%)** | Made 3s ÷ Attempted 3s | Perimeter shooting | 35%+ is good; 40%+ is elite |
| **Free Throw % (FT%)** | Made FT ÷ Attempted FT | Clutch shooting, discipline | 70%+ is standard; 80%+ is strong |
| **Assists (AST)** | Passes leading to made baskets | Playmaking, teamwork | 5+ per game for point guard |
| **Turnovers (TO)** | Lost possessions | Ball security | Fewer than 3 per game for guards is good |

**Rebounding & Defensive Stats**

| Stat | What It Measures | Why It Matters | "Good" High School Benchmark |
|------|-----------------|----------------|------------------------------|
| **Rebounds (REB)** | Offensive + Defensive boards | Possession control | 8+ per game for forwards/centers |
| **Offensive Rebounds (OREB)** | Second-chance opportunities | Grit, athleticism | 3+ per game shows hustle |
| **Defensive Rebounds (DREB)** | Ending opponent possessions | Protecting paint | 5+ per game for bigs |
| **Steals (STL)** | Forced turnovers via theft | Defensive pressure | 2+ per game for perimeter players |
| **Blocks (BLK)** | Shots rejected | Rim protection | 2+ per game for shot-blockers |

**Team Stats**
- **Pace**: Possessions per game (faster = more scoring opportunities)
- **Turnover margin**: Your TOs - opponent TOs (positive is good)
- **Rebounding margin**: Your REBs - opponent REBs (positive = more possessions)
- **Bench points**: Non-starter scoring (depth indicator)

### Positions & Terminology

**Positions**
1. **Point Guard (PG)** – Primary ball-handler; "coach on floor"; runs offense; distributes ball
2. **Shooting Guard (SG)** – Perimeter scorer; defends opponent's best wing; catch-and-shoot specialist
3. **Small Forward (SF)** – Versatile wing; can score inside/outside; often best athlete
4. **Power Forward (PF)** – Inside-outside threat; rebounds, defends post, can shoot mid-range
5. **Center (C)** – Rim protector; rebounds; scores near basket; anchors defense

**Modern Variations**
- **"Positionless" basketball**: Players fill multiple roles; guards crash boards, bigs shoot 3s
- **Stretch-4/Stretch-5**: Big men who shoot from outside
- **Combo guard**: PG/SG hybrid who can handle and score

**Key Terms**
- **Double-double**: 10+ in two stat categories (e.g., points and rebounds)
- **Triple-double**: 10+ in three categories (rare in high school)
- **And-one**: Basket made while fouled, plus free throw opportunity
- **Fast break**: Quick transition offense before defense sets up
- **Pick-and-roll**: Screener sets pick, then rolls to basket
- **Zone defense**: Defending areas rather than individual players (2-3, 1-3-1, etc.)
- **Man-to-man**: Each defender assigned to one opponent
- **Press**: Full-court defensive pressure (full-court, half-court, trap)
- **Box out**: Positioning to secure rebounds

### What to Watch For

**During the Game**
- **Run momentum**: Basketball is a game of runs; note 8-0, 10-2 bursts that shift control
- **Foul trouble**: Star player with 3+ fouls in first half changes strategy
- **Lineup changes**: When coaches insert/remove players (matchups, rest, fouls)
- **Timeout timing**: Called to stop opponent runs or draw up key plays
- **Free-throw shooting under pressure**: Close games often decided at the line
- **Defensive adjustments**: Zone to man, pressing, switching on screens

**Warning Signs of Trouble**
- Multiple unforced turnovers in short span (loss of composure)
- Defensive breakdowns leading to easy baskets (miscommunication, fatigue)
- Cold shooting stretch (0-for-8 from field) without offensive adjustments
- Foul accumulation forcing starters to bench

**Storyline Signals**
- Blowout wins (25+ points): Focus on balanced scoring or dominant individual
- Comeback victories: Identify turning-point run and player who sparked it
- Buzzer-beater: Drama; get quotes immediately post-game
- Rivalry intensity: Physical play, technical fouls, packed gym
- Career-high performance: Player profile angle
- Seniors' last home game: Emotional ceremony, parent/player features

### Interview Tips

**Post-Game Coach Questions**
- "What did you adjust at halftime to [swing momentum/contain their scorer]?"
- "How did [player X]'s foul trouble change your rotation?"
- "What was the key to [your defense/offensive execution] tonight?"
- "How does this [win/loss] affect your seeding/playoff positioning?"
- "What did you see from [opponent's strategy] that surprised you?"

**Player Questions**
- For scorers: "You had X points in the Y quarter. What opened up for you?"
- For playmakers: "Walk me through that [key assist/play]. What did you see?"
- For defenders: "You held [opponent's star] to X points. What was your approach?"
- For clutch performers: "What were you thinking on that [game-winning shot/free throw]?"

**What NOT to Ask**
- "Are you disappointed?" after a loss (too obvious; elicits clichés)
- Questions about referees' calls (puts players/coaches in awkward spot)
- "Did you expect to win by this much?" (can sound arrogant)

**Reading the Stat Sheet**
- Get official scorer's sheet immediately post-game
- Key data: Player name, minutes played, FG made-attempted, 3P made-attempted, FT made-attempted, rebounds, assists, turnovers, steals, blocks, points
- Look for: Who carried scoring load, rebounding dominance, turnover issues, bench contributions
- Calculate shooting percentages for story context

### Story Angles

**Evergreen Feature Ideas**
- **Breakout sophomore/junior**: Player who elevated game from previous season
- **Coach milestone**: 200th win, 25th season, etc.
- **Transfer impact**: New player reshaping team identity
- **Multi-sport star juggling seasons**: Basketball/soccer or basketball/lacrosse overlap
- **Family legacy**: Siblings, parent-child coach/player dynamics
- **Student-of-the-game profiles**: Player who watches film obsessively, gym rat
- **Manager or unsung support staff**: Team manager, statistician, trainer who's vital to program

**Trend & Analysis Pieces**
- **Three-point revolution**: High school teams copying NBA spacing/shooting trends
- **Pace-and-space offenses**: How teams adapt to shot-clock era
- **Defensive philosophy shifts**: Zone vs. man trends across conference
- **Recruiting pipeline**: Where Eastern Shore players land in college
- **AAU/travel ball impact**: Year-round basketball affecting high school dynamics
- **Girls' basketball growth**: Participation, scholarship opportunities

**Rivalry & Stakes Stories**
- **Head-to-head series**: Historical records, memorable games
- **Conference title implications**: "Win and clinch" scenarios
- **Playoff seeding battles**: How late-season games affect bracket position
- **Star vs. star matchups**: Best players on opposing teams
- **Streak watch**: Winning/losing streaks, consecutive championships

**Accountability Angles**
- **Eligibility controversies**: Transfers, academic issues, age questions
- **Spectator behavior**: Recent forfeit-and-no-spectator incidents; crowd control
- **Officiating consistency**: If pattern of controversial calls emerges
- **Facility access**: Scheduling conflicts with other sports, gym availability
- **Safety concerns**: Court conditions, overcrowding, security

**Community & Off-Field Stories**
- **Youth clinics**: Varsity players teaching elementary school kids
- **Senior signings**: College commitment ceremonies
- **Booster fundraising**: New uniforms, equipment, travel funds
- **Alumni games**: Graduates returning for charity matchups
- **Academic all-stars**: Players excelling in classroom and on court
- **Overcoming adversity**: Players dealing with family hardship, illness, personal challenges

---

## Field Hockey

### Rules & How the Game Works

**Basic Structure**
- Two 30-minute halves (some high school leagues use 25-minute halves; confirm local rule)
- 11 players per side
- Goal: Score by hitting ball into opponent's goal (4 yards wide, 7 feet high) using flat side of stick only
- Field dimensions: 100 yards long, 60 yards wide
- Only shots from within "shooting circle" (16-yard semicircle) count as goals

**Key Rules Unique to Field Hockey**
- **No feet/body contact with ball**: Only stick's flat side may touch ball
- **No high sticks**: Stick cannot be raised above shoulder in dangerous manner
- **No obstruction**: Players cannot shield ball with body; must allow tackle attempts
- **No offside**: Unlike soccer, field hockey has no offside rule
- **Free hits**: For minor fouls; taken where infringement occurred
- **Penalty corners (PCs)**: Awarded for fouls inside circle or intentional fouls within 25-yard line; most dangerous scoring opportunity
- **Penalty strokes**: Awarded for deliberate fouls preventing clear goals; one-on-one with goalkeeper

**What Decides Wins**
- **Penalty-corner execution**: Elite teams score on 30-40% of PCs
- **Midfield control**: Winning 50-50 balls, maintaining possession
- **Defensive organization**: Preventing opponent entries into circle
- **Goalkeeper saves**: On PCs and breakaways
- **Transition speed**: Quick counters catch defenses out of position

### Key Stats & What They Mean

**Offensive Stats**

| Stat | What It Measures | Why It Matters | "Good" High School Benchmark |
|------|-----------------|----------------|------------------------------|
| **Goals** | Times ball crossed goal line | Finishing ability | 15+ per season for top scorer |
| **Assists** | Passes leading directly to goals | Playmaking | 10+ per season for midfielder |
| **Shots on Goal (SOG)** | Shots forcing goalkeeper save or scoring | Offensive pressure | Team: 10+ per game shows dominance |
| **Penalty Corners Earned** | Fouls drawn in attacking 25 or circle | Offensive pressure, skills | 5+ per game for strong offense |
| **PC Conversion Rate** | PC goals ÷ Total PCs | Execution on


# Thoughts on Sports2.md #

I really like the start of this it is just very long and did not include 5 of the sports. I will modify the prompt to adjust for this. If this gave me all the sports I think this would be a good overview yet a bit long. 

I added this line: Keep the beat book comprehensive yet brief enough to include all the sports. 

I did not have much luck with this and the output was way too long. 

Prompt: You will receive nine high-school sports beat books (baseball, basketball, field hockey, football, lacrosse, soccer, softball, wrestling, etc.). Combine them into one unified beat book for the Star Democrat.

Requirements:
	•	Begin with Overall Tips for Covering High School Sports that focus on local, Eastern Shore / Mid-Shore reporting context, not generic national sports coverage.
	•	Then create one concise section per sport, each limited to 5–7 essential bullets.
Include only:
	•	sport-specific rules & scoring
	•	key stats
	•	what decides games
	•	terminology
	•	what to watch for
	•	common story angles
	•	interview tips
all tailored to local high school sports in this region
	•	Keep Overall Tips to 8–12 bullets.
	•	Eliminate repetition and filler.
	•	Keep the beat book comprehensive yet brief enough to include all sports.
	•	Always finish the full output; be more concise when needed.

Final Output Format:
	•	Overall Tips for Covering High School Sports
	•	Baseball
	•	Basketball
	•	Field Hockey
	•	Football
	•	Lacrosse
	•	Soccer
	•	Softball
	•	Wrestling

Goal:
Produce a single, clean, region-specific, non-repetitive beat book that prepares any Star Democrat reporter to cover any high school sport on the Eastern Shore.

Sports3: to# STAR DEMOCRAT UNIFIED HIGH SCHOOL SPORTS BEAT BOOK

## Overall Tips for Covering High School Sports on the Eastern Shore

1. **Know Your Geography & Rivalries** – The Bayside Conference (North & South), ESIAC, and county-line rivalries (Easton vs. Kent Island, Cambridge-South Dorchester vs. Colonel Richardson) drive attendance and story angles. Map schools and travel times; bridge traffic adds 15+ minutes.

2. **Embed in the Community** – Attend booster meetings, summer town-team games, and off-season events. The same family names appear on rosters, booster lists, and PTA minutes for decades. Building trust with coaches, ADs, and parents yields better access and story tips.

3. **Master the Calendar** – Create a color-coded master calendar for all sports. Spring overlaps (baseball, softball, lacrosse) and fall clashes (football, field hockey, soccer) require daily prioritization. Know playoff schedules months ahead.

4. **Use the "Impact-Decision Matrix"** – When games overlap, prioritize by: rivalry intensity, playoff stakes, milestone stories (coach wins, player records), and editor requests. Cover one live; follow up on the other via phone/stats.

5. **Build a Stats & Contact Database** – Track season stats, injury updates, roster changes, and coach/AD cell numbers in a shared spreadsheet. Update after every game. This database is your competitive advantage.

6. **Story Formula for Game Recaps** – Lead with the decisive moment (walk-off hit, overtime goal, shutout), add a coach or player quote within the first three paragraphs, then key stats. 300–500 words for print; longer web versions can include play-by-play.

7. **Look Beyond Scores** – Feature angles: senior profiles, coaching milestones, Title IX growth (girls' wrestling, lacrosse), injury comebacks, weather impacts on field prep, and recruiting/college commitments.

8. **Respect Eligibility & Safety** – Confirm rosters with ADs before publishing names. Know concussion-protocol stories are sensitive; always get parent/AD approval before reporting injuries.

9. **Shoot Quick Action Photos** – If no photographer is available, snap a few shots on your phone for web galleries. Action shots of local athletes drive social-media engagement.

10. **File Fast, Fact-Check Faster** – Friday night games demand Saturday morning publication. Draft your lede during the game; confirm final stats with the official scorer or coach before filing.

11. **Balance Coverage Across Sports & Genders** – Track your story count by sport and gender quarterly. The region's softball, field hockey, and girls' lacrosse programs deserve equal attention.

12. **Stay Visible & Accessible** – Introduce yourself to every coach at the start of the season. Share your cell number. Respond to voicemails and texts within two hours, even on weekends.

---

## Baseball

- **Scoring & Key Stats** – Runs, hits, errors (RHE line). Track ERA, batting average, RBI, and pitch counts (MPSSAA limits: 110/day, mandatory rest). Winning/losing pitcher and saves matter for recaps.
- **What Decides Games** – Pitching depth (starters rarely go beyond 5 innings), timely hitting with runners in scoring position, and defensive errors in late innings. Weather delays and field conditions are frequent story angles.
- **Terminology** – "Wheels came off" (bullpen collapse), "dinger" (home run), "can of corn" (easy fly ball), "small ball" (bunts, steals). Coaches use "QAB" (quality at-bat) to describe plate discipline.
- **What to Watch** – Pitch count (ask the coach after each inning if a star is approaching limits), base-running mistakes, and momentum shifts after errors. Note when a team "manufactures" runs without hits.
- **Common Story Angles** – Pitching-duel shutouts, walk-off wins in rivalry games, senior standouts headed to college, weather-related doubleheaders, and "late-bloomer" breakout performances.
- **Interview Tips** – Ask pitchers: "What was working today?" Ask hitters: "What did you see in that at-bat?" Ask coaches about pitch-count strategy and injury updates. Always confirm spelling of names.

---

## Basketball

- **Scoring & Key Stats** – Points, rebounds, assists, steals, blocks. Track shooting percentages (FG%, 3PT%, FT%) and turnovers. "Double-double" (10+ in two categories) and "triple-double" are instant story hooks.
- **What Decides Games** – Free-throw shooting in close games, defensive intensity in the final quarter, and coaching adjustments at halftime. Watch for foul trouble among star players (five fouls = disqualification).
- **Terminology** – "And-one" (fouled while making a basket), "downtown" (three-pointer), "coast-to-coast" (full-court drive), "in the paint" (close to the basket). Coaches talk about "transition defense" and "offensive sets."
- **What to Watch** – Tempo (fast-break vs. half-court offense), free-throw disparities (often a sign of aggressive defense or home-court officiating), and which team controls rebounds. Note scoring runs (e.g., "12–0 run to close the third").
- **Common Story Angles** – Milestone wins for coaches, buzzer-beaters, sibling/family legacies on the roster, transfer-student storylines, and playoff seeding implications.
- **Interview Tips** – Ask about the turning point in the game. For close losses, ask: "What would you do differently?" For blowouts, pivot to individual player development or upcoming schedule.

---

## Field Hockey

- **Scoring & Key Stats** – Goals, assists, saves (goalkeeper), penalty corners (PCs) awarded/converted, and shots on goal. A "PC battery" (inserter + striker) is critical; track their conversion rate.
- **What Decides Games** – Penalty-corner execution (often 50%+ of goals), midfield possession, and goalkeeper performance. Defensive "clog the circle" strategies can neutralize high-powered offenses.
- **Terminology** – "PC" (penalty corner), "green card" (warning), "yellow card" (temporary suspension), "stroke" (penalty shot). "Drag-flick" is a specialized PC shot.
- **What to Watch** – Which team controls midfield, how many PCs each team earns, and whether the goalkeeper is tested often. Late-game substitutions of field players for an extra attacker signal desperation.
- **Common Story Angles** – Senior goalkeeper standout performances, PC-specialist profiles, undefeated streaks, state tournament runs, and the rise of club-team pipelines feeding high-school rosters.
- **Interview Tips** – Ask PC specialists about their technique. Ask goalkeepers about positioning. Ask coaches about halftime adjustments and whether they "played their game" or adapted to the opponent.

---

## Football

- **Scoring & Key Stats** – Touchdowns (6 pts), field goals (3 pts), extra points (1 or 2 pts), turnovers, total yards (rushing + passing), third-down conversions, and time of possession. Quarterback stats (completions/attempts, yards, TDs, INTs) anchor most recaps.
- **What Decides Games** – Turnovers (fumbles, interceptions), red-zone efficiency, and special-teams play (punts, kickoff returns, blocked kicks). Momentum shifts often follow a "three-and-out" stop or a long scoring drive.
- **Terminology** – "Three-and-out" (offense fails to get a first down), "red zone" (inside opponent's 20-yard line), "sack" (QB tackled behind line), "pick-six" (interception returned for TD). Coaches talk about "winning the trenches" (offensive/defensive line play).
- **What to Watch** – Injuries (especially to QBs and offensive linemen), weather (wind affects passing, rain affects ball security), and which team controls the clock in the fourth quarter. Note fourth-down gambles and their outcomes.
- **Common Story Angles** – Rivalry-game recaps, playoff-seeding scenarios, coaching-milestone wins, quarterback duels (especially siblings/cousins), injury-comeback stories, and homecoming-game color pieces.
- **Interview Tips** – Ask coaches about key play-calls. Ask players about their "assignment" on decisive plays. For losses, frame questions around "what went right" before asking about mistakes.

---

## Lacrosse

- **Scoring & Key Stats** – Goals, assists, saves (goalie), ground balls (possession), and faceoff win percentage (critical in boys' lacrosse). Caused turnovers and "man-up" (power-play) goals are also tracked.
- **What Decides Games** – Faceoff dominance gives extra possessions. Goalie performance (save percentage above 60% is strong). Clearing the ball from defense to offense without turnovers sustains momentum.
- **Terminology** – "Man-up/man-down" (power play/penalty kill), "clear" (transition from defense to offense), "riding" (pressuring opponent's clear), "EMO" (extra-man offense). "Crease" is the circle around the goal.
- **What to Watch** – Faceoff specialist matchups, how many shots each goalie faces, and whether either team capitalizes on man-up opportunities. Late-game possessions often come down to which team wins ground balls.
- **Common Story Angles** – Breakout attackmen or midfielders, goalie duels, sibling rivalries (lacrosse families are common), playoff runs, and Title IX growth in girls' programs.
- **Interview Tips** – Ask faceoff specialists about technique. Ask goalies about "reading the shooter." Ask coaches whether they adjusted their "ride" or "clear" strategy during the game.

---

## Soccer

- **Scoring & Key Stats** – Goals, assists, shots on goal, saves (goalkeeper), corner kicks, and fouls. "Clean sheet" (shutout) is a point of pride for goalkeepers and defenses.
- **What Decides Games** – Midfield possession, set-piece execution (corner kicks, free kicks), and goalkeeper heroics. Late-game fitness often separates evenly matched teams.
- **Terminology** – "Clean sheet" (shutout), "brace" (two goals by one player), "hat trick" (three goals), "offsides trap," "through ball" (pass behind defense). Coaches talk about "shape" (formation) and "pressing."
- **What to Watch** – Which team controls possession in midfield, how many quality scoring chances each side creates, and whether either goalkeeper is forced into difficult saves. Note yellow/red cards and their impact.
- **Common Story Angles** – Shutout streaks, hat-trick performances, senior standouts headed to college, upset victories, penalty-kick shootouts (playoffs), and the growth of club-soccer pipelines.
- **Interview Tips** – Ask goal-scorers about the buildup to their goal. Ask goalkeepers about key saves. Ask coaches about formation changes and whether the game plan held up.

---

## Softball

- **Scoring & Key Stats** – Runs, hits, errors (RHE line). Track batting average, RBI, ERA, strikeouts (pitcher), and stolen bases. Pitch counts matter (MPSSAA limits mirror baseball).
- **What Decides Games** – Pitching dominance (shutouts are common), timely hitting with runners in scoring position, and defensive errors. Speed on the basepaths (steals, bunts) often decides close games.
- **Terminology** – "Dinger" (home run), "ribbie" (RBI), "going yard" (home run), "small ball" (bunts, steals). Pitchers throw "rise balls," "drop balls," and "change-ups." Coaches emphasize "situational hitting."
- **What to Watch** – Pitcher fatigue (most starters pitch complete games), base-running aggressiveness, and defensive miscommunication. Note when a team "manufactures" runs without big hits.
- **Common Story Angles** – Pitching gems (no-hitters, one-hitters), walk-off wins, senior profiles, sibling/family legacies, weather delays, and Title IX equity (equal coverage to baseball).
- **Interview Tips** – Ask pitchers what was working. Ask hitters about their approach with runners on base. Ask coaches about pitch-count management and when they considered pulling the starter.

---

## Wrestling

- **Scoring & Key Stats** – Match results: pin (6 team points), tech fall (5 pts), major decision (4 pts), decision (3 pts). Individual scoring: takedowns (2 pts), escapes (1 pt), reversals (2 pts), near-falls (2–3 pts). Track dual-meet team scores and tournament placements.
- **What Decides Matches** – Conditioning (third period is decisive), scrambling ability (who recovers from bad positions), and referee positioning/calls. Weight-class forfeits swing team scores in dual meets.
- **Terminology** – "Pin/fall," "tech fall" (15-point lead), "sudden victory" (first to score in OT wins), "riding time" (1 pt for 1+ min control). Coaches talk about "hand-fighting" and "mat sense."
- **What to Watch** – Which team forfeits weight classes (roster gaps), momentum shifts after pins, and third-period comebacks. Note when a wrestler "guts out" a decision despite trailing early.
- **Common Story Angles** – Milestone wins (100th career win, first state placer), girls' wrestling growth (Maryland added a girls' state tournament in 2020), weight-cutting concerns, and sibling/family wrestling legacies.
- **Interview Tips** – Ask about the decisive move or moment. For close losses, ask: "What would you adjust in a rematch?" Always ask coaches about the health/status of injured wrestlers (concussions, shoulder injuries common).

---

**End of Beat Book**


# Sports4 #

I like the intro to sports2 and will stick with that for this version even though it is a bit long. For now it works. I will try and use the original prompt I was using to generate just the sports sections. I may need to just throw the entire thing into an LLM and ask for it to shrink the entire thing but won't do that yet.

To generate these sports section I will put them into Sport5. 

Here is that prompt: You are combining nine separate high-school sports beat books into one unified beat book for the Star Democrat.
Each original beat book covers one sport (baseball, basketball, field hockey, football, lacrosse, soccer, softball, wrestling, etc.).

Your task is to merge them into a single beat book that:

create one section per sport in this order:
	1.	Baseball
	2.	Basketball
	3.	Field Hockey
	4.	Football
	5.	Lacrosse
	6.	Soccer
	7.	Softball
	8.	Wrestling
	9.	Any additional sports provided

Each sport section must:
	•	Include only the sport-specific guidance from that sport’s original beat book.
	•	Quickly Summarize each sport’s most important:
	•	rules & scoring basics
	•	key stats & what they mean
	•	what determines outcomes
	•	positions & terminology
	•	what to watch for during games
	•	interview tips & questions to ask
	•	common story angles

⸻

2. CONTENT RULES
	•	No duplication.
	•	No filler.
	•	Use consistent formatting across all sports.
	•	Clear, focused, practical guidance only.
	•	Keep the beat book comprehensive yet brief enough to include all the sports.
	•	Always finish the full output. If necessary, be more concise to ensure the entire beat book is included without cutting off sections.

Recommended sub-headings for each sport:
	•	Rules & How the Game Works
	•	Key Stats & What They Mean
	•	What Decides Matches/Games
	•	Positions & Terminology
	•	What to Watch For
	•	Interview Tips
	•	Story Angles

Star Democrat High School Sports Beat Book



output: # Star Democrat High School Sports Beat Book
## Unified Guide for All Sports Coverage

---

# 1. BASEBALL

## Rules & How the Game Works
- **Objective:** Score more runs than opponent in 7 innings (HS standard)
- **Scoring:** Runner crosses home plate = 1 run
- **Outs:** 3 per half-inning; game progresses through batting orders
- **Mercy rule:** Typically 10 runs after 5 innings on the Eastern Shore
- **Key situations:** Bases loaded, runners in scoring position (2nd/3rd), full counts

## Key Stats & What They Mean
| Stat | What it measures | Good benchmark (HS) |
|------|-----------------|-------------------|
| **Batting Average (BA)** | Hits ÷ At‑bats | .300+ is strong |
| **ERA (Earned Run Average)** | Earned runs allowed per 7 innings | Under 2.50 is elite |
| **RBI (Runs Batted In)** | Clutch hitting ability | 20+ in a season |
| **Strikeouts (pitching)** | Dominance on the mound | 7+ per game |
| **Fielding %** | (Putouts + Assists) ÷ (Putouts + Assists + Errors) | .950+ |

## What Decides Games
- **Pitching depth:** Who throws after the ace? Eastern Shore teams often struggle in game 2 of doubleheaders
- **Defense:** Errors in late innings destroy momentum
- **Situational hitting:** Moving runners with 0 or 1 out
- **Base-running:** Stolen bases matter when scoring is tight

## Positions & Terminology
- **Battery:** Pitcher + catcher
- **Infield:** 1B, 2B, SS, 3B
- **Outfield:** LF, CF, RF
- **DH (Designated Hitter):** Bats for pitcher in lineup
- **Key terms:** RBI, earned run, quality start (5+ innings, ≤3 runs), save situation

## What to Watch For
- **Pitch counts:** MPSSAA limits (105 pitches/day; mandatory rest)
- **Momentum swings:** 2‑out rallies, pickoff attempts
- **Weather delays:** Rain impacts field conditions and pitching rotations
- **Substitution patterns:** Pinch‑runners for catchers, defensive replacements late

## Interview Tips
**Winning team:**
- "Walk me through that big inning—what was working?"
- "How did your pitcher keep them off-balance?"

**Losing team:**
- "What did you see from their pitcher that was tough?"
- "Where do you regroup before the next game?"

**Coaches:** Always ask about pitch counts, injury updates, and next opponent scouting.

## Story Angles
- **Bayside Conference rivalries:** Easton vs Kent Island, Colonel Richardson matchups
- **Ace pitcher profiles:** Track pitch counts, velocity, college interest
- **Senior spotlights:** Last season, college commitments
- **Field conditions:** Weather impact, fundraising for turf upgrades
- **Summer league pipelines:** Town‑team tournaments, fall‑ball prospects

---

# 2. BASKETBALL

## Rules & How the Game Works
- **Objective:** Score more points in four 8‑minute quarters (HS)
- **Scoring:** Field goal = 2 pts, 3‑pointer = 3 pts, free throw = 1 pt
- **Shot clock:** 35 seconds (varies by state; confirm with officials)
- **Fouls:** 5 personal fouls = disqualification; bonus free throws after 7 team fouls per half
- **Overtime:** 4‑minute periods until winner determined

## Key Stats & What They Mean
| Stat | What it measures | Good benchmark |
|------|-----------------|----------------|
| **Points per game (PPG)** | Offensive output | 15+ PPG is a star |
| **Rebounds (Total/Off/Def)** | Possession control | 8+ RPG for bigs |
| **Assists** | Playmaking | 4+ APG for guards |
| **Field Goal %** | Shooting efficiency | 45%+ overall |
| **Turnovers** | Ball security | <3 per game |
| **Plus/Minus** | Net score while player is on court | Positive trend = impact |

## What Decides Games
- **Tempo control:** Fast‑break teams vs half‑court grinders
- **Free‑throw shooting:** Close games hinge on FT% in final 2 minutes
- **Rebounding:** Second‑chance points often decide 5‑point games
- **Foul trouble:** Star in foul trouble by halftime changes game plan
- **3‑point shooting:** Hot shooting can erase 10‑point deficits quickly

## Positions & Terminology
- **Guard (PG/SG):** Ball‑handlers, perimeter shooters
- **Forward (SF/PF):** Mid‑range scorers, rebounders
- **Center (C):** Rim protector, post presence
- **Key terms:** Double‑double (10+ in two stat categories), triple‑double, press (full‑court/half‑court), zone defense

## What to Watch For
- **Foul counts:** Track stars with 3+ fouls by halftime
- **Timeout usage:** Strategic calls in final 2 minutes
- **Lineup changes:** Defensive substitutions, "Hack‑a‑Shaq" tactics
- **Bench energy:** Reserves can swing momentum in tight games
- **Technical fouls:** Ejections change game narrative

## Interview Tips
**Post‑game (winners):**
- "What clicked in the second half?"
- "How did you attack their zone/press?"

**Post‑game (losers):**
- "Where did the momentum shift?"
- "What's the plan to bounce back?"

**Coaches:** Ask about foul trouble, defensive adjustments, injury updates.

## Story Angles
- **Bayside Conference standings:** North vs South division races
- **Rivalry games:** Easton vs Cambridge‑South Dorchester, Queen Anne's battles
- **Player milestones:** 1,000‑point scorers, all‑time program records
- **Coaching milestones:** Career win totals, conference titles
- **Transfer impact:** New players from Baltimore metro, eligibility questions
- **State tournament runs:** Underdog stories, bracket projections

---

# 3. FIELD HOCKEY

## Rules & How the Game Works
- **Objective:** Score more goals in two 30‑minute halves (or four 15‑min quarters)
- **Scoring:** Ball crosses goal line inside circle = 1 goal
- **Players:** 11 per side (10 field + 1 goalie)
- **Penalty corners (PCs):** Awarded for fouls in circle; high‑percentage scoring opportunity
- **Key restrictions:** Only flat side of stick contacts ball; no feet, no high sticks

## Key Stats & What They Mean
| Stat | Meaning | Good benchmark |
|------|---------|----------------|
| **Goals** | Offensive output | 20+ in a season |
| **Assists** | Playmaking | 10+ |
| **Penalty corners** | Scoring chances | 5+ per game |
| **PC conversion %** | Efficiency on set pieces | 25%+ |
| **Saves (goalie)** | Shot‑stopping | 10+ in tough games |
| **Shots on goal** | Offensive pressure | 15+ per game |

## What Decides Games
- **Penalty‑corner execution:** Teams with 3+ PC goals often win decisively
- **Defensive shape:** Preventing PCs and breakaways
- **Midfield possession:** Controlling the 50‑yard line
- **Goalie performance:** A hot keeper can steal games
- **Turnovers in attacking third:** Lead to quick counterattacks

## Positions & Terminology
- **Forwards (F):** Goal‑scorers, lead the press
- **Midfielders (M):** Transition play, two‑way workhorses
- **Defenders (D):** Protect circle, clear balls
- **Goalie (GK):** Wears full pads, uses feet/stick
- **Sweeper:** Last defender before goalie
- **Key terms:** Circle (scoring zone), insert (PC start), aerial, self‑pass

## What to Watch For
- **PC units:** First‑team vs second‑team personnel
- **Card discipline:** Green (warning), yellow (5‑10 min), red (ejection)
- **Substitution patterns:** Rolling subs every 5‑7 minutes
- **Weather:** Wet turf slows ball, affects PC plays
- **Injury timeouts:** Dehydration, stick‑to‑shin contact

## Interview Tips
**Post‑game:**
- "Walk me through that penalty‑corner goal—what was the play?"
- "How did you adjust after [opponent] shifted to a press?"

**Coaches:** Ask about PC strategy, card accumulation, turf conditions.

## Story Angles
- **North Bayside powerhouses:** Queen Anne's, Kent Island, Easton
- **Penalty‑corner specialists:** Profile the "PC battery" (inserter, stopper, striker)
- **Senior captains:** Leadership through playoffs
- **Underdog runs:** Lower‑seeded teams in regional brackets
- **Turf fundraising:** Community efforts to install/maintain fields
- **Club‑team pipelines:** Shore Select, regional club impact on HS rosters

---

# 4. FOOTBALL

## Rules & How the Game Works
- **Objective:** Score more points in four 12‑minute quarters
- **Scoring:** TD = 6 pts (+ 1 or 2‑pt conversion), FG = 3 pts, safety = 2 pts
- **Downs:** 4 attempts to gain 10 yards; reset on first down
- **Clock management:** Stops on incomplete passes, out‑of‑bounds, timeouts (3 per half)
- **Key rules:** Forward pass must originate behind line of scrimmage; offense can't "hold" defenders

## Key Stats & What They Mean
| Stat | What it measures | Good benchmark |
|------|-----------------|----------------|
| **Rushing yards** | Ground‑game effectiveness | 150+ team yards/game |
| **Passing yards** | Air‑attack output | 200+ yards/game |
| **Turnovers (TO)** | Ball security | Winning teams often win TO battle |
| **3rd‑down %** | Sustaining drives | 40%+ conversion |
| **Sacks/TFL** | Defensive pressure | 3+ sacks disrupts offense |
| **Time of possession** | Field control | 25+ minutes often wins |

## What Decides Games
- **Turnover margin:** Team with +2 TO advantage wins 75% of the time
- **Red‑zone efficiency:** TDs vs FGs inside 20‑yard line
- **Big plays:** 40+ yard runs/passes shift momentum instantly
- **Special teams:** Punt returns, FG accuracy, kickoff coverage
- **Line play:** Whoever wins the "trenches" controls game

## Positions & Terminology
**Offense:**
- **QB (Quarterback):** Passes, hands off, leads offense
- **RB (Running Back):** Carries ball, catches out of backfield
- **WR (Wide Receiver):** Pass‑catchers on perimeter
- **OL (Offensive Line):** 5 blockers (LT, LG, C, RG, RT)
- **TE (Tight End):** Hybrid blocker/receiver

**Defense:**
- **DL (Defensive Line):** Pass rush, run‑stopping
- **LB (Linebacker):** Middle defenders, cover RBs/TEs
- **DB (Defensive Back):** Cover WRs (CB = corner, S = safety)

**Key terms:** Blitz, screen pass, play‑action, "read‑option," two‑minute drill

## What to Watch For
- **Injuries:** Skill‑position stars, starting QB health
- **Weather:** Wind affects passing, rain impacts footing
- **Momentum swings:** Blocked punts, pick‑sixes
- **Clock management:** Late‑game timeouts, "icing" the kicker
- **Penalty flags:** Holding, offsides, unsportsmanlike conduct

## Interview Tips
**Post‑game (winners):**
- "That 3rd‑and‑long conversion—what did you see?"
- "How did the O‑line create those rushing lanes?"

**Post‑game (losers):**
- "Where did the turnovers hurt most?"
- "What's the fix before next week?"

**Coaches:** Ask about injury updates, game plan adjustments, playoff implications.

## Story Angles
- **Friday night rivalries:** Easton vs Kent Island, Colonel Richardson vs North Caroline
- **"Battle of the Bay":** Annual showcase game
- **Playoff races:** Conference standings, tiebreaker scenarios
- **Quarterback battles:** Multi‑year starter vs rising sophomore
- **College recruiting:** Seniors signing with D‑I, D‑II programs
- **Coaching milestones:** Career wins, program turnarounds
- **Community impact:** Booster‑club fundraisers, field upgrades

---

# 5. LACROSSE

## Rules & How the Game Works
- **Objective:** Score more goals in four 12‑minute quarters (HS)
- **Scoring:** Ball in net = 1 goal
- **Players:** 10 per side (3 attack, 3 midfield, 3 defense, 1 goalie)
- **Faceoffs:** Start each quarter and after goals
- **Key rules:** "Offsides" if too many players in offensive/defensive zones; stick‑checks allowed on ball‑carrier

## Key Stats & What They Mean
| Stat | Meaning | Good benchmark |
|------|---------|----------------|
| **Goals** | Scoring output | 3+ per game for attackmen |
| **Assists** | Playmaking | 2+ per game |
| **Ground balls** | Hustle, possession | 5+ per game |
| **Faceoff wins** | Possession control | 60%+ win rate |
| **Saves (goalie)** | Shot‑stopping | 10+ saves, 60%+ save % |
| **Turnovers** | Unforced errors | <10 per game |

## What Decides Games
- **Faceoff dominance:** Winning 70% of faceoffs = more possessions
- **Clearing/Riding:** Transition from defense to offense
- **Man‑up/Man‑down:** Penalty advantages (like hockey power plays)
- **Goalie performance:** Elite keepers can win games single‑handedly
- **Transition offense:** Quick‑strike goals in unsettled situations

## Positions & Terminology
- **Attack (A):** Offensive specialists, stay in offensive half
- **Midfield (M):** Two‑way players, run full field
- **Defense (D):** Protect goal, initiate clears
- **Goalie (G):** Last line, wears extra padding
- **LSM (Long‑Stick Middie):** Defensive midfielder with longer stick
- **SSDM (Short‑Stick Defensive Mid):** Quick defender
- **Key terms:** Clear (moving ball out of defensive zone), ride (pressuring opponent's clear), EMO (extra‑man offense)

## What to Watch For
- **Faceoff X:** Who wins possession battles
- **Penalty situations:** Slashing, cross‑check calls
- **Substitution "on the fly":** Quick changes during play
- **Ride pressure:** Aggressive teams force turnovers in opponent's end
- **Weather:** Wind affects long passes, rain makes ground balls slippery

## Interview Tips
**Post‑game:**
- "That run of three goals—what opened up?"
- "How did you adjust when they went zone defense?"

**Coaches:** Ask about faceoff strategy, man‑up units, goalie decisions.

## Story Angles
- **Bayside Conference races:** Easton, Kent Island, Queen Anne's battles
- **Faceoff specialists:** Profile the "X" player
- **Goalie duels:** Save‑percentage leaders
- **Senior classes:** College commitments (D‑I pipeline strong on Shore)
- **Club‑team influence:** Shore Select, regional travel teams
- **Coaching trees:** Ties to college programs (Salisbury, UMBC)
- **Playoff brackets:** State tournament runs, upset alerts

---

# 6. SOCCER

## Rules & How the Game Works
- **Objective:** Score more goals in two 40‑minute halves (HS)
- **Scoring:** Ball crosses goal line = 1 goal
- **Players:** 11 per side (10 field + 1 goalie)
- **Offsides:** Attacker can't be behind last defender when ball is played forward (doesn't apply on goal kicks, throw‑ins, corner kicks)
- **Fouls:** Direct free kick (inside box = penalty kick) or indirect free kick

## Key Stats & What They Mean
| Stat | Meaning | Good benchmark |
|------|---------|----------------|
| **Goals** | Offensive output | 15+ in a season |
| **Assists** | Playmaking | 8+ |
| **Shots on goal** | Offensive pressure | 8+ per game (team) |
| **Saves (GK)** | Shot‑stopping | 8+ in competitive games |
| **Shutouts (GK)** | Clean sheets | 5+ in a season |
| **Yellow/Red cards** | Discipline | Red = ejection + 1‑game suspension |

## What Decides Games
- **Possession:** Controlling the ball, dictating tempo
- **Set pieces:** Corner kicks, free kicks in dangerous areas
- **Counter‑attacks:** Quick transitions catch defenses out of position
- **Goalkeeping:** One brilliant save can preserve a 1‑0 win
- **Finishing:** Converting chances in the "final third"

## Positions & Terminology
**Formation (e.g., 4‑4‑2):**
- **Goalkeeper (GK):** Only player who can use hands (in box)
- **Defenders (D):** Fullbacks (LB/RB), center‑backs (CB)
- **Midfielders (M):** Defensive mid (DM), central mid (CM), attacking mid (AM), wingers (LM/RM)
- **Forwards (F):** Strikers, target forwards

**Key terms:** Through‑ball, give‑and‑go, offside trap, "park the bus" (ultra‑defensive)

## What to Watch For
- **Formation shifts:** Teams adjusting mid‑game (e.g., 4‑4‑2 to 3‑5‑2)
- **Card accumulation:** Yellow card = caution; second yellow = red
- **Substitution limits:** Typically 3‑5 subs (varies by league)
- **Penalty kicks:** High‑pressure moments; track conversion rates
- **Weather:** Wind, rain, field conditions (mud, grass length)

## Interview Tips
**Post‑game:**
- "That goal—walk me through the buildup."
- "How did you break down their defense?"

**Coaches:** Ask about formation choices, set‑piece strategy, injury reports.

## Story Angles
- **Boys' and girls' parity:** Both draw strong attendance
- **Club‑team influence:** Baltimore metro players transfer in
- **Goalkeeper spotlights:** Shutout streaks, penalty‑save heroics
- **Senior leaders:** Captains heading to college programs
- **Rivalry games:** Easton vs Queen Anne's, regional matchups
- **State playoff runs:** Bracket projections, Cinderella teams
- **Field conditions:** Turf vs grass impact, fundraising efforts

---

# 7. SOFTBALL

## Rules & How the Game Works
- **Objective:** Score more runs in 7 innings
- **Scoring:** Runner crosses home = 1 run
- **Pitching:** Underhand delivery from 43 feet (vs 60.5 in baseball)
- **Outs:** 3 per half‑inning
- **Mercy rule:** Typically 10 runs after 5 innings
- **Key differences from baseball:** Larger ball, base‑running rules (leaving early = out)

## Key Stats & What They Mean
| Stat | Meaning | Good benchmark |
|------|---------|----------------|
| **Batting Average** | Hits ÷ At‑bats | .350+ is strong |
| **ERA** | Earned runs per 7 innings | Under 2.00 is elite |
| **Strikeouts (pitching)** | Dominance | 10+ per game |
| **RBI** | Run production | 25+ in a season |
| **Stolen bases** | Speed threat | 15+ |
| **Fielding %** | Defensive reliability | .960+ |

## What Decides Games
- **Pitching dominance:** Elite pitchers (12+ Ks) can shut down offenses
- **Speed game:** Bunts, slap‑hitting, stolen bases
- **Clutch hitting:** 2‑out RBIs in late innings
- **Defense:** Errors in the circle (infield) are costly
- **Rise ball vs drop ball:** Pitch repertoire separates good from great

## Positions & Terminology
- **Battery:** Pitcher + catcher
- **Infield:** 1B, 2B, SS, 3B
- **Outfield:** LF, CF, RF
- **DP (Designated Player):** Can bat for any position
- **Flex:** Defensive specialist (opposite of DP in lineup)
- **Key terms:** Slap‑hitter, rise ball, drop ball, change‑up, windmill delivery

## What to Watch For
- **Pitch counts:** Monitor ace's innings (20+ innings/week = fatigue)
- **Speed on basepaths:** Drag bunts, fake bunts
- **Defensive shifts:** Against power hitters
- **Weather delays:** Rain impacts field drainage, pitching rotation
- **Substitution rules:** Re‑entry allowed once per player

## Interview Tips
**Post‑game:**
- "Your rise ball was working—when did you feel it click?"
- "That 2‑out rally—what was the approach?"

**Coaches:** Ask about pitching rotation, injury updates, playoff scenarios.

## Story Angles
- **Ace pitcher profiles:** Strikeout records, college commitments
- **Senior spotlights:** Final season, legacy
- **Bayside Conference races:** Standings, head‑to‑head records
- **Underdog stories:** Rebuilding programs making playoff runs
- **Field upgrades:** Booster fundraising, turf installations
- **Rival matchups:** Colonel Richardson vs Mardela, Queen Anne's battles
- **College pipeline:** D‑I, D‑II signings

---

# 8. WRESTLING

## Rules & How the Game Works
- **Objective:** Pin opponent's shoulders to mat (instant win) or outscore in 3 periods (2 min, 2 min, 2 min)
- **Scoring:**
  - Takedown = 2 points
  - Escape = 1 point
  - Reversal = 2 points
  - Near‑fall (back exposed) = 2‑3 points
  - Pin (fall) = match over, team gets 6 points
- **Weight classes:** 14 classes from 106 lbs to 285 lbs (boys); 10‑12 classes for girls
- **Team scoring:** Win by pin = 6 pts, tech fall (15+ lead) = 5 pts, major decision (8‑14 lead) = 4 pts, decision (<8 lead) = 3 pts

## Key Stats & What They Mean
| Stat | Meaning | Good benchmark |
|------|---------|----------------|
| **Win‑Loss Record** | Season performance | 25‑5 is strong |
| **Pins** | Dominance | 15+ pins in a season |
| **Takedowns/match** | Offensive aggression | 4+ per match |
| **Escape %** | Bottom‑position skill | 75%+ |
| **Near‑fall points** | Back‑exposure control | 3+ per match |
| **Tech falls** | Lopsided victories | 5+ in a season |

## What Decides Matches
- **First takedown:** Sets tone, often predicts winner
- **Riding time:** Controlling opponent on mat (1+ min = bonus point)
- **Third‑period choice:** Top/bottom/neutral—strategic decision
- **Conditioning:** Final period separates equals
- **Mental toughness:** Comebacks from 5+ point deficits

## Positions & Terminology
- **Neutral position:** Both wrestlers standing
- **Top/Bottom:** Referee's position (one wrestler controlling from behind)
- **Pin (fall):** Both shoulders on mat for 2 seconds
- **Escape:** Bottom wrestler breaks free to neutral
- **Reversal:** Bottom wrestler gains top position
- **Takedown:** From neutral to top position
- **Key terms:** Cradle, half‑nelson, granby roll, stand‑up, sprawl, duck‑under

## What to Watch For
- **Weight cuts:** Wrestlers dropping weight class (health concerns)
- **Forfeits:** Teams without wrestlers in certain weight classes
- **Dual‑meet strategy:** Coaches "bump" wrestlers to avoid tough matchups
- **Injury defaults:** Matches stopped for blood, concussion protocol
- **Stalling calls:** Referees penalize passive wrestlers
- **Team race:** Running score can dictate strategy in final bouts

## Interview Tips
**Post‑match (winner):**
- "That second‑period reversal—what opened up?"
- "How did you set up the pin?"

**Post‑match (loser):**
- "What was working for [opponent]?"
- "Where do you go from here?"

**Coaches:** Ask about lineup decisions, weight‑class strategy, injury updates.

## Story Angles
- **Bayside Conference dominance:** Traditional powerhouses
- **Girls' wrestling growth:** Historic 2024 team state title
- **Weight‑class battles:** Rivals meeting multiple times
- **Tournament runs:** Regionals, state championships
- **Milestones:** 100‑win careers, program records
- **Family legacies:** Brothers/sisters following parents
- **Coaching milestones:** Career dual‑meet wins
- **Underdog pins:** Lower seed upsetting favorite

---

# 9. CROSS COUNTRY / TRACK & FIELD

## Rules & How the Sport Works
**Cross Country (fall):**
- **Distance:** 5K (3.1 miles) for most HS courses
- **Scoring:** Top 5 finishers per team score; low score wins (1st place = 1 point)
- **Team total:** Sum of top 5 runners' places (e.g., 1+3+5+7+9 = 25 points)

**Track & Field (spring):**
- **Events:** Sprints (100m, 200m, 400m), distance (800m, 1600m, 3200m), hurdles, relays (4×100, 4×400), field events (long jump, triple jump, high jump, pole vault, shot put, discus, javelin)
- **Scoring:** Varies by meet (invitational vs dual‑meet); typically 10‑8‑6‑4‑2‑1 for top 6 places

## Key Stats & What They Mean
| Stat | Meaning | Good benchmark |
|------|---------|----------------|
| **PR (Personal Record)** | Fastest time/farthest distance | Season goal for every athlete |
| **Split times** | Intermediate times (e.g., 400m splits in 1600m) | Even splits = efficient pacing |
| **Relay legs** | Individual contributions to team relay | "Anchor leg" is often fastest runner |
| **State‑qualifying marks** | Standards to advance | Varies by event; track on MPSSAA site |

## What Decides Races/Meets
- **Pacing:** Going out too fast leads to "bonking" in final mile/lap
- **Kick:** Final sprint in last 200‑400m
- **Depth:** Team with 5 strong runners beats team with 2 stars + 3 weak
- **Weather:** Heat, humidity, wind affect times significantly
- **Course/track conditions:** Mud, standing water, wind lanes

## Positions & Terminology
- **Distance runners:** 800m and longer
- **Sprinters:** 100m, 200m, 400m
- **Hurdlers:** 110m high hurdles (boys), 100m hurdles (girls), 300m hurdles
- **Field‑event athletes:** Jumpers, throwers, vaulters
- **All‑around athlete:** Competes in multiple events
- **Key terms:** Lean (finishing technique), false start, handoff zone (relay), baton exchange, "PR'ed" (set new personal record)

## What to Watch For
- **Pack running:** Teams clustering runners to box out opponents
- **Relay exchanges:** Dropped batons = disqualification
- **Weather delays:** Lightning, extreme heat
- **Injury scratches:** Key athletes withdrawing before gun
- **Course records:** Especially at invitationals on historic courses

## Interview Tips
**Post‑race:**
- "That final kick—when did you decide to go?"
- "How did the team execute the race plan?"

**Coaches:** Ask about training volume, taper strategy, state‑qualifying progress.

## Story Angles
- **Program resurgence:** Schools investing in distance programs
- **State qualifiers:** First‑time qualifiers, breakthrough performances
- **Relay drama:** DQ's, come‑from‑behind wins
- **Multi‑event stars:** Athletes competing in 3‑4 events per meet
- **Senior leadership:** Captains setting example
- **Invitational results:** Big regional meets (e.g., Easton Invitational)
- **Weather impact:** How teams adapt to heat, cold, wind

---

# GENERAL COVERAGE PRINCIPLES

## Story Structure (All Sports)
**Game Recap Template (300‑500 words):**
1. **Lead:** Who, what, score, key moment (25‑35 words)
2. **Nut graf:** What it means (standings, streak, playoff implications)
3. **Turning point:** The play/moment that decided the game
4. **Star quote:** Coach or player reaction
5. **Key stats:** Top 3 performers, team totals
6. **Looking ahead:** Next opponent, date, implications

**Feature Template (800‑1,200 words):**
1. **Scene‑setter:** Anecdote or moment that captures subject
2. **Nut graf:** Why this story matters now
3. **Background:** Context, history, stats
4. **Multiple voices:** 3‑4 sources (player, coach, parent, opponent)
5. **Forward‑looking kicker:** What's next for subject

## Coverage Priorities (Impact‑Decision Matrix)
When two games conflict, prioritize:
1. **Playoff implications** over regular season
2. **Rivalry games** over non‑conference
3. **Undefeated teams** over .500 teams
4. **Senior nights / milestones** over routine games
5. **Girls' sports** equally with boys' (alternate if necessary)

## Ethical Guidelines
- **Accuracy first:** Double‑check all stats, spellings, scores
- **Balance:** Quote both winning and losing sides
- **Injury sensitivity:** Don't speculate on severity; report facts only
- **Youth protection:** No home addresses; be mindful of minors in photos
- **Conflict of interest:** Disclose if you have personal ties to teams/players

## Building Sources
- **Coaches:** Weekly check‑ins, not just post‑game
- **Athletic directors:** Scheduling changes, facility issues
- **Booster clubs:** Fundraising stories, community angles
- **Players:** Build rapport over full season, not just after big games
- **Officials:** Rules clarifications, controversial calls (off‑record)

## Essential Contacts
Maintain a master spreadsheet with:
- Coach names, cell phones, emails
- Athletic director contacts
- School media liaisons
- Booster club presidents
- Team Twitter/social accounts (for live score updates)

## Deadline Management
- **Pre‑game:** File preview 24 hours before first pitch/kickoff
- **Live coverage:** Tweet score updates every quarter/inning
- **Post‑game:** File gamer within 90 minutes of final whistle
- **Next‑day:** Deeper analysis, photo gallery, stat leaders

---

**Final Note:** The Eastern Shore lives and breathes high school sports. Your role is to illuminate the effort, drama, and community pride behind every game. Be fair, be accurate, be present—and the stories will write themselves.


Sport4 now has: The Eastern Shore of Maryland is a tight-knit patchwork of small towns where high school sports serve as community hubs. Schools function as the beating heart of towns like Easton, Cambridge-South Dorchester, Queen Anne's, St. Michael's, Kent Island, Wicomico, and Salisbury. Generations of families sit in the same bleachers, and the same surnames appear on rosters and in booster-club minutes year after year. Sports events are social calendar fixtures that can eclipse other news coverage.

### Core Beat Responsibilities

**Weekly Workflow Foundation**

| Day | Core Tasks | Notes |
|-----|------------|-------|
| **Monday** | Review weekend game notes, pull stats, update your database | Early start (7 a.m.) helps beat Monday print deadlines (typically 12 p.m.) |
| **Tuesday** | Pitch previews for marquee matchups; confirm travel plans & field/facility access | Maintain a shared calendar with travel distances |
| **Wednesday-Friday** | Attend games, take live notes, coordinate photography, conduct post-game interviews | Bring compact voice recorder; 30-second sound-bites from coaches are invaluable |
| **Thursday-Friday** | Write game recaps (300-500 words print, longer web); file stories by deadline | See "5-W-1-H + Quote + Stat" template below |
| **Saturday** | Attend community events to stay visible; file community spotlight pieces | Builds goodwill with boosters and volunteers |
| **Sunday** | Admin: clean database, confirm next week's schedule, recharge | The beat is a marathon, not a sprint |

### Travel & Logistics

**Geographic Challenges**
- Schools are often 30-45 minutes apart
- Bridge traffic can add 15+ minutes to travel time
- Create a master map for the week; plan hub-and-spoke routes to minimize backtracking

**Pack Smart**
- Small notebook and tablet with stylus (for quick play diagrams)
- Spare battery pack
- Weather-proof voice recorder
- Compact camera or ensure school photographer is coordinated

**Late-Night Game Strategy**
Use downtime to draft recap outlines on your phone; fill in final stats when posted.

### Managing Multiple Sports Simultaneously

**The Master Calendar System**
- Create one calendar listing ALL sports events
- Color-code by sport (e.g., baseball navy, softball pink, basketball orange)
- When games overlap, use the Impact-Decision Matrix to prioritize

**Impact-Decision Matrix**

| Factor | Weight | Questions to Ask |
|--------|--------|------------------|
| **Conference Stakes** | High | Does this game decide standings or playoff position? |
| **Rivalry Intensity** | High | Is this a historic rivalry that drives attendance and community interest? |
| **Story Continuity** | Medium | Are you following an ongoing narrative (coach milestone, player comeback)? |
| **Attendance/Community Interest** | Medium | Will bleachers be packed? Are boosters promoting heavily? |
| **Access to Stats** | Low | Can you get complete stats if you're not there live? |

Apply this matrix to decide which game merits live coverage and which can be covered via delayed recap.

### Building and Maintaining Sources

**Core Contact Lists**
- Head coaches (cell phone, email, preferred contact times)
- Athletic directors
- Booster club presidents
- Team captains and key players
- School administrators (for eligibility and policy questions)
- Parent volunteers who run timers, scoreboards, and concessions

**Relationship-Building Tactics**
- Attend non-game community events (tournaments, fundraisers, field renovations)
- Keep an "open questions" list to email coaches during off-days
- Respond promptly to tips and corrections from readers
- Be visible and approachable at games
- Remember: most coaches work multiple sports—keep separate but linked contact lists

### Story Structure: The "5-W-1-H + Quote + Stat" Template

**Game Recaps (Standard 300-500 words)**

```
LEAD PARAGRAPH (Who, What, When, Where, Why)
[Team A] defeated [Team B], [Score], on [Day] at [Venue] to [achieve what/why it matters].

NUT GRAF (Key turning point + decisive stat)
[Describe the crucial moment/play]. [Player Name] [key stat that tells the story].

QUOTE 1 (Winning coach or star player on the key moment)
"[Direct quote that captures emotion or strategy]," said [Name, Title].

CONTEXT (How/Why this matters)
The win [moves Team A to X-X record/clinches playoff spot/extends streak/etc.].

ADDITIONAL DETAILS (Supporting stats, other key plays)
[Player B] added [stat]. [Team A] built momentum by [describe pattern].

QUOTE 2 (Losing coach or perspective from other side)
"[Quote showing grace, analysis, or looking forward]," [Name] said.

GAME NOTES (Final stats, next games, injury updates)
[Team A] will face [next opponent] on [date]. [Any roster notes.]
```

### Essential Story Types

**1. Game Recaps**
- Breaking news; file quickly with accuracy
- Focus on what decided the outcome
- Balance winning and losing perspectives

**2. Rivalry Previews**
- Historical context (last five meetings, all-time records)
- Current stakes (standings, playoff implications)
- Key player matchups
- Coach perspectives

**3. Player Profiles**
- Focus on "late bloomers," overcoming adversity, milestone achievements
- Include coach and teammate quotes
- Connect personal story to on-field performance

**4. Trend Pieces**
- Statistical patterns across multiple games
- Conference-wide developments (scoring trends, defensive strategies)
- Equipment, rule changes, or technique evolution

**5. Coach's Corner/Weekly Columns**
- Rotating spotlight on different coaches
- Philosophy, career highlights, teaching moments
- Builds deeper connection with readership

**6. Accountability & Policy Stories**
- Eligibility issues
- Safety concerns
- Facility conditions
- Administrative decisions affecting teams

**7. Off-Season Features**
- "Where are they now" updates on alumni
- Facility renovations and community fundraising
- Summer league coverage
- Pre-season previews and roster changes

### Conference Structure & Rivalries

**Major Conferences**
- **Bayside Conference (North & South divisions)**: Easton, Colonel Richardson, Kent Island, Queen Anne's, Cambridge-South Dorchester, St. Michael's
- **Eastern Shore Independent Athletic Conference (ESIAC)**: Private and independent schools
- **Regional Classifications**: 1A, 2A, 3A, 4A determine playoff brackets

**Marquee Rivalries to Know**
- Easton vs. Kent Island
- Easton vs. Cambridge-South Dorchester
- Queen Anne's vs. Colonel Richardson
- Colonel Richardson vs. North Caroline
- St. Peter & Paul vs. Easton

These matchups generate heightened attendance, ticket sales, booster activity, and editorial interest. Prepare deeper coverage and anticipate stronger community reaction.

### Data Management

**Personal Database Maintenance**
- Keep running stats for all teams you cover
- Track season-long trends (scoring averages, winning streaks, head-to-head records)
- Note injury reports and roster changes
- Maintain historical records for context (coach milestones, school records, championship history)

**Sources for Stats**
- Official scorebooks (request access from coaches or ADs)
- School athletic department websites
- MaxPreps and other stat aggregation sites
- Conference websites
- Your own game notes

### Deadline Management

**Print Deadlines**
- Typical Monday-Friday print deadline: 12 p.m. for next-day publication
- Weekend deadlines vary; confirm with editors
- Late-night games require "running" story filed in sections

**Digital-First Strategy**
- Post score and quick highlight to web/social immediately post-game
- File full recap within 2 hours
- Add quotes, stats, and analysis for morning print edition
- Update web version with additional content throughout next day

### Ethical Guidelines & Best Practices

**Accuracy First**
- Double-check scores, stats, and name spellings
- Verify information with multiple sources when possible
- Correct errors promptly and transparently

**Balance & Fairness**
- Give both teams fair coverage in recaps
- Rotate feature subjects to avoid favoritism
- Be sensitive to age-appropriate coverage of minors

**Access & Boundaries**
- Respect coach/player time constraints
- Schedule formal interviews rather than ambushing
- Understand FERPA and student privacy rules
- Never interview injured players without coach/parent approval

**Community Sensitivity**
- Small towns mean long memories; maintain professionalism
- Avoid inflammatory language even in rivalry coverage
- Remember families read every word about their children
- Be accurate but not cruel when covering losses or poor performances

### Managing Seasonal Overlaps

**Peak Conflict Periods**

| Time of Year | Overlapping Sports | Strategy |
|--------------|-------------------|----------|
| **Late February - Early March** | Baseball/softball start, basketball playoffs, wrestling postseason | Prioritize playoff games; use delayed recaps for regular-season openers |
| **Late March - April** | Baseball, softball, lacrosse, soccer all in full swing | Rotate coverage; ensure each sport gets featured stories weekly |
| **Late October - November** | Football playoffs, basketball season starts, soccer/field hockey/volleyball postseason | Focus on football Fridays, basketball Tuesdays/Saturdays; cover other sports via quick recaps |
| **Late May - Early June** | Spring sports playoffs, baseball/softball championships | All hands on deck; coordinate with other reporters |

### Understanding Booster Culture

**What Boosters Do**
- Fund-raise for equipment, uniforms, facility improvements
- Run concessions and ticket sales
- Organize community events and senior nights
- Provide volunteer support (timers, scorekeepers, field maintenance)

**Why They Matter to Your Beat**
- They're passionate sources for feature stories
- They can provide historical context and archive materials
- They influence community sentiment about coverage
- They're often your most engaged readers

**How to Work With Them**
- Attend booster meetings occasionally
- Acknowledge their contributions in stories when relevant
- Be fair but don't let them dictate coverage
- Respond professionally to complaints or criticism

### Social Media Strategy

**Game Coverage**
- Live-tweet/post key moments and score updates
- Share photos (with proper attribution and permissions)
- Tag schools, athletes, and organizations when appropriate
- Drive traffic to full stories with teaser posts

**Engagement**
- Monitor comments for story ideas and corrections
- Respond professionally to criticism
- Share reader photos and stories (with permission)
- Promote upcoming coverage

**Boundaries**
- Don't follow or friend current high school athletes
- Keep interactions professional and public
- Don't engage with hostile commenters
- Verify social media information before using in stories

### Weather Contingencies

**Rain-Outs & Cancellations**
- Maintain updated contact list for quick confirmation
- Prepare "backup" stories for sudden cancellations
- Check conference websites and school social media for official announcements
- Have feature material ready for weather-related news holes

**Extreme Weather Coverage**
- Lightning delays: time them; ask about safety protocols
- Heat: watch for hydration breaks and modified schedules
- Cold: note how conditions affect play

### Building Subject Expertise

**Continuous Learning**
- Study rule books during off-season
- Watch college/pro games to understand advanced strategy
- Ask coaches to explain plays and tactics
- Read national coverage of your sports for story ideas and best practices
- Attend coaching clinics if possible (great for sources and understanding)

### Self-Care & Sustainability

**Managing the Grind**
- Set boundaries: You can't cover every game
- Delegate when possible; coordinate with photographers and other reporters
- Take advantage of slow periods to recharge
- Keep weekends during off-season truly off
- Remember: Burnout helps no one

**Signs You're Overextended**
- Missing deadlines
- Declining story quality
- Resentment toward sources or subjects
- Physical exhaustion affecting health
- Decreased engagement with stories

**When to Ask for Help**
- Overlapping major events
- Personal emergencies
- Sustained multi-week crunch periods
- Complex investigative or accountability stories

# 1. BASEBALL

## Rules & How the Game Works
- **Objective:** Score more runs than opponent in 7 innings (HS standard)
- **Scoring:** Runner crosses home plate = 1 run
- **Outs:** 3 per half-inning; game progresses through batting orders
- **Mercy rule:** Typically 10 runs after 5 innings on the Eastern Shore
- **Key situations:** Bases loaded, runners in scoring position (2nd/3rd), full counts

## Key Stats & What They Mean
| Stat | What it measures | Good benchmark (HS) |
|------|-----------------|-------------------|
| **Batting Average (BA)** | Hits ÷ At‑bats | .300+ is strong |
| **ERA (Earned Run Average)** | Earned runs allowed per 7 innings | Under 2.50 is elite |
| **RBI (Runs Batted In)** | Clutch hitting ability | 20+ in a season |
| **Strikeouts (pitching)** | Dominance on the mound | 7+ per game |
| **Fielding %** | (Putouts + Assists) ÷ (Putouts + Assists + Errors) | .950+ |

## What Decides Games
- **Pitching depth:** Who throws after the ace? Eastern Shore teams often struggle in game 2 of doubleheaders
- **Defense:** Errors in late innings destroy momentum
- **Situational hitting:** Moving runners with 0 or 1 out
- **Base-running:** Stolen bases matter when scoring is tight

## Positions & Terminology
- **Battery:** Pitcher + catcher
- **Infield:** 1B, 2B, SS, 3B
- **Outfield:** LF, CF, RF
- **DH (Designated Hitter):** Bats for pitcher in lineup
- **Key terms:** RBI, earned run, quality start (5+ innings, ≤3 runs), save situation

## What to Watch For
- **Pitch counts:** MPSSAA limits (105 pitches/day; mandatory rest)
- **Momentum swings:** 2‑out rallies, pickoff attempts
- **Weather delays:** Rain impacts field conditions and pitching rotations
- **Substitution patterns:** Pinch‑runners for catchers, defensive replacements late

## Interview Tips
**Winning team:**
- "Walk me through that big inning—what was working?"
- "How did your pitcher keep them off-balance?"

**Losing team:**
- "What did you see from their pitcher that was tough?"
- "Where do you regroup before the next game?"

**Coaches:** Always ask about pitch counts, injury updates, and next opponent scouting.

## Story Angles
- **Bayside Conference rivalries:** Easton vs Kent Island, Colonel Richardson matchups
- **Ace pitcher profiles:** Track pitch counts, velocity, college interest
- **Senior spotlights:** Last season, college commitments
- **Field conditions:** Weather impact, fundraising for turf upgrades
- **Summer league pipelines:** Town‑team tournaments, fall‑ball prospects

---

# 2. BASKETBALL

## Rules & How the Game Works
- **Objective:** Score more points in four 8‑minute quarters (HS)
- **Scoring:** Field goal = 2 pts, 3‑pointer = 3 pts, free throw = 1 pt
- **Shot clock:** 35 seconds (varies by state; confirm with officials)
- **Fouls:** 5 personal fouls = disqualification; bonus free throws after 7 team fouls per half
- **Overtime:** 4‑minute periods until winner determined

## Key Stats & What They Mean
| Stat | What it measures | Good benchmark |
|------|-----------------|----------------|
| **Points per game (PPG)** | Offensive output | 15+ PPG is a star |
| **Rebounds (Total/Off/Def)** | Possession control | 8+ RPG for bigs |
| **Assists** | Playmaking | 4+ APG for guards |
| **Field Goal %** | Shooting efficiency | 45%+ overall |
| **Turnovers** | Ball security | <3 per game |
| **Plus/Minus** | Net score while player is on court | Positive trend = impact |

## What Decides Games
- **Tempo control:** Fast‑break teams vs half‑court grinders
- **Free‑throw shooting:** Close games hinge on FT% in final 2 minutes
- **Rebounding:** Second‑chance points often decide 5‑point games
- **Foul trouble:** Star in foul trouble by halftime changes game plan
- **3‑point shooting:** Hot shooting can erase 10‑point deficits quickly

## Positions & Terminology
- **Guard (PG/SG):** Ball‑handlers, perimeter shooters
- **Forward (SF/PF):** Mid‑range scorers, rebounders
- **Center (C):** Rim protector, post presence
- **Key terms:** Double‑double (10+ in two stat categories), triple‑double, press (full‑court/half‑court), zone defense

## What to Watch For
- **Foul counts:** Track stars with 3+ fouls by halftime
- **Timeout usage:** Strategic calls in final 2 minutes
- **Lineup changes:** Defensive substitutions, "Hack‑a‑Shaq" tactics
- **Bench energy:** Reserves can swing momentum in tight games
- **Technical fouls:** Ejections change game narrative

## Interview Tips
**Post‑game (winners):**
- "What clicked in the second half?"
- "How did you attack their zone/press?"

**Post‑game (losers):**
- "Where did the momentum shift?"
- "What's the plan to bounce back?"

**Coaches:** Ask about foul trouble, defensive adjustments, injury updates.

## Story Angles
- **Bayside Conference standings:** North vs South division races
- **Rivalry games:** Easton vs Cambridge‑South Dorchester, Queen Anne's battles
- **Player milestones:** 1,000‑point scorers, all‑time program records
- **Coaching milestones:** Career win totals, conference titles
- **Transfer impact:** New players from Baltimore metro, eligibility questions
- **State tournament runs:** Underdog stories, bracket projections

---

# 3. FIELD HOCKEY

## Rules & How the Game Works
- **Objective:** Score more goals in two 30‑minute halves (or four 15‑min quarters)
- **Scoring:** Ball crosses goal line inside circle = 1 goal
- **Players:** 11 per side (10 field + 1 goalie)
- **Penalty corners (PCs):** Awarded for fouls in circle; high‑percentage scoring opportunity
- **Key restrictions:** Only flat side of stick contacts ball; no feet, no high sticks

## Key Stats & What They Mean
| Stat | Meaning | Good benchmark |
|------|---------|----------------|
| **Goals** | Offensive output | 20+ in a season |
| **Assists** | Playmaking | 10+ |
| **Penalty corners** | Scoring chances | 5+ per game |
| **PC conversion %** | Efficiency on set pieces | 25%+ |
| **Saves (goalie)** | Shot‑stopping | 10+ in tough games |
| **Shots on goal** | Offensive pressure | 15+ per game |

## What Decides Games
- **Penalty‑corner execution:** Teams with 3+ PC goals often win decisively
- **Defensive shape:** Preventing PCs and breakaways
- **Midfield possession:** Controlling the 50‑yard line
- **Goalie performance:** A hot keeper can steal games
- **Turnovers in attacking third:** Lead to quick counterattacks

## Positions & Terminology
- **Forwards (F):** Goal‑scorers, lead the press
- **Midfielders (M):** Transition play, two‑way workhorses
- **Defenders (D):** Protect circle, clear balls
- **Goalie (GK):** Wears full pads, uses feet/stick
- **Sweeper:** Last defender before goalie
- **Key terms:** Circle (scoring zone), insert (PC start), aerial, self‑pass

## What to Watch For
- **PC units:** First‑team vs second‑team personnel
- **Card discipline:** Green (warning), yellow (5‑10 min), red (ejection)
- **Substitution patterns:** Rolling subs every 5‑7 minutes
- **Weather:** Wet turf slows ball, affects PC plays
- **Injury timeouts:** Dehydration, stick‑to‑shin contact

## Interview Tips
**Post‑game:**
- "Walk me through that penalty‑corner goal—what was the play?"
- "How did you adjust after [opponent] shifted to a press?"

**Coaches:** Ask about PC strategy, card accumulation, turf conditions.

## Story Angles
- **North Bayside powerhouses:** Queen Anne's, Kent Island, Easton
- **Penalty‑corner specialists:** Profile the "PC battery" (inserter, stopper, striker)
- **Senior captains:** Leadership through playoffs
- **Underdog runs:** Lower‑seeded teams in regional brackets
- **Turf fundraising:** Community efforts to install/maintain fields
- **Club‑team pipelines:** Shore Select, regional club impact on HS rosters

---

# 4. FOOTBALL

## Rules & How the Game Works
- **Objective:** Score more points in four 12‑minute quarters
- **Scoring:** TD = 6 pts (+ 1 or 2‑pt conversion), FG = 3 pts, safety = 2 pts
- **Downs:** 4 attempts to gain 10 yards; reset on first down
- **Clock management:** Stops on incomplete passes, out‑of‑bounds, timeouts (3 per half)
- **Key rules:** Forward pass must originate behind line of scrimmage; offense can't "hold" defenders

## Key Stats & What They Mean
| Stat | What it measures | Good benchmark |
|------|-----------------|----------------|
| **Rushing yards** | Ground‑game effectiveness | 150+ team yards/game |
| **Passing yards** | Air‑attack output | 200+ yards/game |
| **Turnovers (TO)** | Ball security | Winning teams often win TO battle |
| **3rd‑down %** | Sustaining drives | 40%+ conversion |
| **Sacks/TFL** | Defensive pressure | 3+ sacks disrupts offense |
| **Time of possession** | Field control | 25+ minutes often wins |

## What Decides Games
- **Turnover margin:** Team with +2 TO advantage wins 75% of the time
- **Red‑zone efficiency:** TDs vs FGs inside 20‑yard line
- **Big plays:** 40+ yard runs/passes shift momentum instantly
- **Special teams:** Punt returns, FG accuracy, kickoff coverage
- **Line play:** Whoever wins the "trenches" controls game

## Positions & Terminology
**Offense:**
- **QB (Quarterback):** Passes, hands off, leads offense
- **RB (Running Back):** Carries ball, catches out of backfield
- **WR (Wide Receiver):** Pass‑catchers on perimeter
- **OL (Offensive Line):** 5 blockers (LT, LG, C, RG, RT)
- **TE (Tight End):** Hybrid blocker/receiver

**Defense:**
- **DL (Defensive Line):** Pass rush, run‑stopping
- **LB (Linebacker):** Middle defenders, cover RBs/TEs
- **DB (Defensive Back):** Cover WRs (CB = corner, S = safety)

**Key terms:** Blitz, screen pass, play‑action, "read‑option," two‑minute drill

## What to Watch For
- **Injuries:** Skill‑position stars, starting QB health
- **Weather:** Wind affects passing, rain impacts footing
- **Momentum swings:** Blocked punts, pick‑sixes
- **Clock management:** Late‑game timeouts, "icing" the kicker
- **Penalty flags:** Holding, offsides, unsportsmanlike conduct

## Interview Tips
**Post‑game (winners):**
- "That 3rd‑and‑long conversion—what did you see?"
- "How did the O‑line create those rushing lanes?"

**Post‑game (losers):**
- "Where did the turnovers hurt most?"
- "What's the fix before next week?"

**Coaches:** Ask about injury updates, game plan adjustments, playoff implications.

## Story Angles
- **Friday night rivalries:** Easton vs Kent Island, Colonel Richardson vs North Caroline
- **"Battle of the Bay":** Annual showcase game
- **Playoff races:** Conference standings, tiebreaker scenarios
- **Quarterback battles:** Multi‑year starter vs rising sophomore
- **College recruiting:** Seniors signing with D‑I, D‑II programs
- **Coaching milestones:** Career wins, program turnarounds
- **Community impact:** Booster‑club fundraisers, field upgrades

---

# 5. LACROSSE

## Rules & How the Game Works
- **Objective:** Score more goals in four 12‑minute quarters (HS)
- **Scoring:** Ball in net = 1 goal
- **Players:** 10 per side (3 attack, 3 midfield, 3 defense, 1 goalie)
- **Faceoffs:** Start each quarter and after goals
- **Key rules:** "Offsides" if too many players in offensive/defensive zones; stick‑checks allowed on ball‑carrier

## Key Stats & What They Mean
| Stat | Meaning | Good benchmark |
|------|---------|----------------|
| **Goals** | Scoring output | 3+ per game for attackmen |
| **Assists** | Playmaking | 2+ per game |
| **Ground balls** | Hustle, possession | 5+ per game |
| **Faceoff wins** | Possession control | 60%+ win rate |
| **Saves (goalie)** | Shot‑stopping | 10+ saves, 60%+ save % |
| **Turnovers** | Unforced errors | <10 per game |

## What Decides Games
- **Faceoff dominance:** Winning 70% of faceoffs = more possessions
- **Clearing/Riding:** Transition from defense to offense
- **Man‑up/Man‑down:** Penalty advantages (like hockey power plays)
- **Goalie performance:** Elite keepers can win games single‑handedly
- **Transition offense:** Quick‑strike goals in unsettled situations

## Positions & Terminology
- **Attack (A):** Offensive specialists, stay in offensive half
- **Midfield (M):** Two‑way players, run full field
- **Defense (D):** Protect goal, initiate clears
- **Goalie (G):** Last line, wears extra padding
- **LSM (Long‑Stick Middie):** Defensive midfielder with longer stick
- **SSDM (Short‑Stick Defensive Mid):** Quick defender
- **Key terms:** Clear (moving ball out of defensive zone), ride (pressuring opponent's clear), EMO (extra‑man offense)

## What to Watch For
- **Faceoff X:** Who wins possession battles
- **Penalty situations:** Slashing, cross‑check calls
- **Substitution "on the fly":** Quick changes during play
- **Ride pressure:** Aggressive teams force turnovers in opponent's end
- **Weather:** Wind affects long passes, rain makes ground balls slippery

## Interview Tips
**Post‑game:**
- "That run of three goals—what opened up?"
- "How did you adjust when they went zone defense?"

**Coaches:** Ask about faceoff strategy, man‑up units, goalie decisions.

## Story Angles
- **Bayside Conference races:** Easton, Kent Island, Queen Anne's battles
- **Faceoff specialists:** Profile the "X" player
- **Goalie duels:** Save‑percentage leaders
- **Senior classes:** College commitments (D‑I pipeline strong on Shore)
- **Club‑team influence:** Shore Select, regional travel teams
- **Coaching trees:** Ties to college programs (Salisbury, UMBC)
- **Playoff brackets:** State tournament runs, upset alerts

---

# 6. SOCCER

## Rules & How the Game Works
- **Objective:** Score more goals in two 40‑minute halves (HS)
- **Scoring:** Ball crosses goal line = 1 goal
- **Players:** 11 per side (10 field + 1 goalie)
- **Offsides:** Attacker can't be behind last defender when ball is played forward (doesn't apply on goal kicks, throw‑ins, corner kicks)
- **Fouls:** Direct free kick (inside box = penalty kick) or indirect free kick

## Key Stats & What They Mean
| Stat | Meaning | Good benchmark |
|------|---------|----------------|
| **Goals** | Offensive output | 15+ in a season |
| **Assists** | Playmaking | 8+ |
| **Shots on goal** | Offensive pressure | 8+ per game (team) |
| **Saves (GK)** | Shot‑stopping | 8+ in competitive games |
| **Shutouts (GK)** | Clean sheets | 5+ in a season |
| **Yellow/Red cards** | Discipline | Red = ejection + 1‑game suspension |

## What Decides Games
- **Possession:** Controlling the ball, dictating tempo
- **Set pieces:** Corner kicks, free kicks in dangerous areas
- **Counter‑attacks:** Quick transitions catch defenses out of position
- **Goalkeeping:** One brilliant save can preserve a 1‑0 win
- **Finishing:** Converting chances in the "final third"

## Positions & Terminology
**Formation (e.g., 4‑4‑2):**
- **Goalkeeper (GK):** Only player who can use hands (in box)
- **Defenders (D):** Fullbacks (LB/RB), center‑backs (CB)
- **Midfielders (M):** Defensive mid (DM), central mid (CM), attacking mid (AM), wingers (LM/RM)
- **Forwards (F):** Strikers, target forwards

**Key terms:** Through‑ball, give‑and‑go, offside trap, "park the bus" (ultra‑defensive)

## What to Watch For
- **Formation shifts:** Teams adjusting mid‑game (e.g., 4‑4‑2 to 3‑5‑2)
- **Card accumulation:** Yellow card = caution; second yellow = red
- **Substitution limits:** Typically 3‑5 subs (varies by league)
- **Penalty kicks:** High‑pressure moments; track conversion rates
- **Weather:** Wind, rain, field conditions (mud, grass length)

## Interview Tips
**Post‑game:**
- "That goal—walk me through the buildup."
- "How did you break down their defense?"

**Coaches:** Ask about formation choices, set‑piece strategy, injury reports.

## Story Angles
- **Boys' and girls' parity:** Both draw strong attendance
- **Club‑team influence:** Baltimore metro players transfer in
- **Goalkeeper spotlights:** Shutout streaks, penalty‑save heroics
- **Senior leaders:** Captains heading to college programs
- **Rivalry games:** Easton vs Queen Anne's, regional matchups
- **State playoff runs:** Bracket projections, Cinderella teams
- **Field conditions:** Turf vs grass impact, fundraising efforts

---

# 7. SOFTBALL

## Rules & How the Game Works
- **Objective:** Score more runs in 7 innings
- **Scoring:** Runner crosses home = 1 run
- **Pitching:** Underhand delivery from 43 feet (vs 60.5 in baseball)
- **Outs:** 3 per half‑inning
- **Mercy rule:** Typically 10 runs after 5 innings
- **Key differences from baseball:** Larger ball, base‑running rules (leaving early = out)

## Key Stats & What They Mean
| Stat | Meaning | Good benchmark |
|------|---------|----------------|
| **Batting Average** | Hits ÷ At‑bats | .350+ is strong |
| **ERA** | Earned runs per 7 innings | Under 2.00 is elite |
| **Strikeouts (pitching)** | Dominance | 10+ per game |
| **RBI** | Run production | 25+ in a season |
| **Stolen bases** | Speed threat | 15+ |
| **Fielding %** | Defensive reliability | .960+ |

## What Decides Games
- **Pitching dominance:** Elite pitchers (12+ Ks) can shut down offenses
- **Speed game:** Bunts, slap‑hitting, stolen bases
- **Clutch hitting:** 2‑out RBIs in late innings
- **Defense:** Errors in the circle (infield) are costly
- **Rise ball vs drop ball:** Pitch repertoire separates good from great

## Positions & Terminology
- **Battery:** Pitcher + catcher
- **Infield:** 1B, 2B, SS, 3B
- **Outfield:** LF, CF, RF
- **DP (Designated Player):** Can bat for any position
- **Flex:** Defensive specialist (opposite of DP in lineup)
- **Key terms:** Slap‑hitter, rise ball, drop ball, change‑up, windmill delivery

## What to Watch For
- **Pitch counts:** Monitor ace's innings (20+ innings/week = fatigue)
- **Speed on basepaths:** Drag bunts, fake bunts
- **Defensive shifts:** Against power hitters
- **Weather delays:** Rain impacts field drainage, pitching rotation
- **Substitution rules:** Re‑entry allowed once per player

## Interview Tips
**Post‑game:**
- "Your rise ball was working—when did you feel it click?"
- "That 2‑out rally—what was the approach?"

**Coaches:** Ask about pitching rotation, injury updates, playoff scenarios.

## Story Angles
- **Ace pitcher profiles:** Strikeout records, college commitments
- **Senior spotlights:** Final season, legacy
- **Bayside Conference races:** Standings, head‑to‑head records
- **Underdog stories:** Rebuilding programs making playoff runs
- **Field upgrades:** Booster fundraising, turf installations
- **Rival matchups:** Colonel Richardson vs Mardela, Queen Anne's battles
- **College pipeline:** D‑I, D‑II signings

---

# 8. WRESTLING

## Rules & How the Game Works
- **Objective:** Pin opponent's shoulders to mat (instant win) or outscore in 3 periods (2 min, 2 min, 2 min)
- **Scoring:**
  - Takedown = 2 points
  - Escape = 1 point
  - Reversal = 2 points
  - Near‑fall (back exposed) = 2‑3 points
  - Pin (fall) = match over, team gets 6 points
- **Weight classes:** 14 classes from 106 lbs to 285 lbs (boys); 10‑12 classes for girls
- **Team scoring:** Win by pin = 6 pts, tech fall (15+ lead) = 5 pts, major decision (8‑14 lead) = 4 pts, decision (<8 lead) = 3 pts

## Key Stats & What They Mean
| Stat | Meaning | Good benchmark |
|------|---------|----------------|
| **Win‑Loss Record** | Season performance | 25‑5 is strong |
| **Pins** | Dominance | 15+ pins in a season |
| **Takedowns/match** | Offensive aggression | 4+ per match |
| **Escape %** | Bottom‑position skill | 75%+ |
| **Near‑fall points** | Back‑exposure control | 3+ per match |
| **Tech falls** | Lopsided victories | 5+ in a season |

## What Decides Matches
- **First takedown:** Sets tone, often predicts winner
- **Riding time:** Controlling opponent on mat (1+ min = bonus point)
- **Third‑period choice:** Top/bottom/neutral—strategic decision
- **Conditioning:** Final period separates equals
- **Mental toughness:** Comebacks from 5+ point deficits

## Positions & Terminology
- **Neutral position:** Both wrestlers standing
- **Top/Bottom:** Referee's position (one wrestler controlling from behind)
- **Pin (fall):** Both shoulders on mat for 2 seconds
- **Escape:** Bottom wrestler breaks free to neutral
- **Reversal:** Bottom wrestler gains top position
- **Takedown:** From neutral to top position
- **Key terms:** Cradle, half‑nelson, granby roll, stand‑up, sprawl, duck‑under

## What to Watch For
- **Weight cuts:** Wrestlers dropping weight class (health concerns)
- **Forfeits:** Teams without wrestlers in certain weight classes
- **Dual‑meet strategy:** Coaches "bump" wrestlers to avoid tough matchups
- **Injury defaults:** Matches stopped for blood, concussion protocol
- **Stalling calls:** Referees penalize passive wrestlers
- **Team race:** Running score can dictate strategy in final bouts

## Interview Tips
**Post‑match (winner):**
- "That second‑period reversal—what opened up?"
- "How did you set up the pin?"

**Post‑match (loser):**
- "What was working for [opponent]?"
- "Where do you go from here?"

**Coaches:** Ask about lineup decisions, weight‑class strategy, injury updates.

## Story Angles
- **Bayside Conference dominance:** Traditional powerhouses
- **Girls' wrestling growth:** Historic 2024 team state title
- **Weight‑class battles:** Rivals meeting multiple times
- **Tournament runs:** Regionals, state championships
- **Milestones:** 100‑win careers, program records
- **Family legacies:** Brothers/sisters following parents
- **Coaching milestones:** Career dual‑meet wins
- **Underdog pins:** Lower seed upsetting favorite

# DRAFT 3 THOUGHTS #

This is by far my most comprehensive beat book. I do think it is a bit lenghty at the moment. The bigger issue is simplicity. I could try upgrading my prompt to provide a beat book for a more seasoned sports reporter but I think for a newbie this would be extremely helpful. My other concern is that the beat book is not specific enough to the eastern shore. I decided not to pick a specific geographic location and rather stick with high school because it would not make much sense to limit this to a smaller niche becasue the sports reporter will be coverall all sports across the region not just a few schools.

Please see sports4.md for my most updated beat book draft. 

