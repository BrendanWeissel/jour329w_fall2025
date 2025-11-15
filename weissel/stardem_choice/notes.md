Star-Democrat Choice Assignment 11/14/25

From my last attempt I modified the data so that I have 240 stories (20 from each month) created by CoPilot with even weight to each month depending on how many stories are from that month. I suspect this will give me a better sense of the yearround coverage from the Stardemocrat. 

I also simplified my schema to incldue the title of those included in the stories, I removed the venue metadata due to the incosistency.

Prompt: uv run python add_entities.py --model groq/meta-llama/llama-4-maverick-17b-128e-instruct --input Sports.highschool.2024.240.json

Name of file: stories_with_entities5.json

For some reason the LLM did a bad job filitering the 240 stories and included way too many professional sports stories, I will fix that for my next attempt. The LLM also removed the metadata piece that wrote a blurb about who the target audience was for each story. 

I wonder if there are not 240 stories only on high school so it added in professional ones to hit the 240 mark...I doubt it but it could be. Probably bad filtering by CoPilot

Specifically looking at the high school stories llama did a great job completing all aspects of the requested metadata. 

Next steps: remake the data section and run again. 

Attempt 2: I requested that CoPilot assist me in making a .json file of all the high school stories from 2024 that remove and roundup articles that only have results and also remove the college and professional stories. 

My hope is to get a comprehnsive review of a year in coverage from the stardemocrat to see how they format their sports coverage over a year and what sports they focus most on. 

I also added back the "who is this story targeted to" metadata. Llama worked well for me and my classmates so I used it again.

What I asked CoPilot: here are steps you need to do 
1. Take sports.json and remove every story not from 2024
2. remove everystory that is not specificaly about high school sprots coverage 
3. remove every story that is simply a roundup story with no reporting
4. tell me how many stories are in the .json

Propmt: uv run python add_entities.py --model groq/meta-llama/llama-4-maverick-17b-128e-instruct --input sports2024highschool.json

Other than the fact that this took about 2 hours to run I was very pleased with the results. 

Here are my takeaways/findings





Attempt 3: 

I was happy with these results metadata wise but wanted to clean it up a bit by removing all the TV Listings from the data and the few remaining professional sports stories.

It took some time working with CoPilot to do this as it removed too many stories first but i got it to finally work. 

Prompt: uv run python add_entities.py --model groq/meta-llama/llama-4-maverick-17b-128e-instruct --input sports2024highschool4.json

Overall analysis:

Changes: remove TV listings from the data