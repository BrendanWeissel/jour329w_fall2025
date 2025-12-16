The Beat Book 12/15/25

I back tracked to the stories to attempt to make one final beat book very specifically focused on High School Football coverager by the Stardemocrat. The issue I see happening is there not being enough stories for there to be enough info. However I am sticking to the football focus so I can have time to fact check the material to ensure the final beat book has possible usage. 

Code: cat prompt_sport.txt source_stories_highschool_football.json | uv run llm -m groq/openai/gpt-oss-120b > HSfootball.md

I stored each prompt in prompt_sports.txt (added numbers to the end based on attempt number) and result in HSfootball.md (same story w the numbers)

Attempt 1: Way too long and just all that helpful. Large focus on player names that will graduate. 

Attempt 2: While doing in real time fact checking I see that the LLM is getting tripped up on schools that are mentioned but not actually in the usual FOV for the star-dem. 

Attempt 3: I adjusted the script to look for just school in the bayside confrence. I also asked to LLM to comment on play style but due to the lack of coverage of every game this led to so much hallucination so I removed it:

Attempt 4: With the removal of play style the LLM still included information on some schools 

Attempt 5: The school specific recap is solid. I combined the attempt 4 close as it provided more story ideas and journalistis tips for my attempt 6 and will fact check 

## Attempt 6/football beat book overiew. 

 This beat book is not perfect. The LLM got confused on similar named schools and mixed up their records. The big issue is that not every game played had a story about it in the star-dem. So the focus of this is obviously the 2024 season as that is when the stories we had were from. Knowing that I focused on making a prompt that could be used with the newer stories that I could give to the star-dem and then provide and accurate output. 

 With that being said the issue is that, for example if a team plays 10 games but their final story was on the 8th game the LLM may list their record at the time of the 8th game as 6-2 but when you fact check you see that the record was really 6-4. Adding in all the results from these teams via a website like MaxPreps (which is how I looked at all these scores to fact check) would be a great way to have an LLM generate story ideas and have all the info. 

I realized over the course of this class that I think "quick fact sheet" might be a more accurate name for what we are generating than a beat book. 

 The beat book idea is abitiious as it assumed we can know the ins and outs of the jobs just by reading the stories. In my experience this led to the LLM generating BS that it was not worth asking the LLM to add that info. 

 I also think for the set of stories I was given on high school football coverage the quaility of stories was too poor to get additional meaningful info on some of these schools other than results. The player stats are helpful and something I would tell the reporter to use an LLM to do but is so unnescary for me to inclued as the info is all outdated. 

 This prompt could be replicated for the other sports I looked into but I worried about not having enough information. 

## Final thoughts ##

 I recognize this is not the strongest beat book I have submitted in this course in terms of content overview and scope. With that being said I am confident it is the most accurate and my final prompt can be reused to make accurate beat books. 

 I renamed the beatbook HSfootballfinal.