# Game of Cards: Strategy Unveiled Through Data Analysis

![SW_Screen](https://github.com/A-Rutledge/SummonerWars/assets/33138919/66d4eb84-2f34-453a-a219-54928dc48373)

## Important Note:
This is a work in progress as I continue to build it out. I am challenging myself to take part in Hacktober 2023 and commit to at least 1 significant git commit a day. My goal is to have the base functionality fully working by Oct. 10 and fully refined and automated by October 30th (We'll get into why I chose those specific dates later).

## Why This Project?
This project combines my two biggest passions; board games and data. Summoner Wars(First Edition) was one of my first board game purchases when I got into the hobby over a decade ago. Summoner Wars(Second Edition) came out in 2021, making some significant improvements over it's original version, and has steadily been releasing new factions every couple of months. Between work, 2 kids (8 and 1), and just adulting in general, my free time is much more limited than it used to be. How can I possibly keep up and stay competitive when there are so many unique factions and matchups to learn in this card battling game of tactics? Well, I don't know, but I'm hoping my 5 years of Data Engineering experience might provide a solution. I'm using this project to learn new skills, show off my current ones, and maybe, just maybe, find a way to gain an edge when I do get the chance to play a game of Summoner Wars.

## Why should you read?
I will be utilizing Python and it's various libraries (MatplotLib, Pandas, RegEx, etc.) to try to gain as much information as I can from the game logs of matches between the game's top players. I will be trying to find a definitive answer for which cards get played the most, which cards deal the most damage, which cards are targed the most often, what does the average damage per turn look like, and many more questions. I will be building out the dataset through web scraping, processing the game logs into a format we can work with, transforming and analyzing the data with Pandas and Matplotlib, storing the data in a SQL Database, and possibly even building a Tableau Dashboard to be able to see the information at a faction level. It's a big task, but one I am excited about, and I hope that passion will be enough to keep this interesting to read. So join me, fellow board gamers and data nerds, as we dive deep into the world of fantasy and magic.

## Game in Progress
![GameExample](https://github.com/A-Rutledge/SummonerWars/assets/33138919/9783e426-f1dd-4dc3-b763-8de8c7c59e32)


## How the game works
To give some context for the dataset, I have to talk a bit about how the game works. Feel free to skip this section if you just want to see the analysis and come back to it later if you want to try to see why I chose to analyze the metrics I did. 

Each player controls a Summoner and several types of units. The goal of the game is to defeat the opponents Summoner. As soon as one of the two Summoners is defeated, the game ends and the player that landed the killing blow is declared the victor. Simple enough right? Like with any good board game, the depth lies in the limitations. On each of your turns, you can Summon as many units as you are able to, play Event Cards giving your units a big boost or limiting your opponents options, build new gates if you have the card in your hand, move up to 3 units up to 2 spaces each, attack with up to 3 units (eiither melee attacks or range attacks depending on the card), and then discard cards to gain more magic you can use to summon cards. With only 5 cards in hand on most of your turns, it becomes a constant puzzle as you try to find the right balance between keeping pressure on your oppenent, keeping enough magic in reserve to build a defense quickly should you need it, and positioning your units just right to maximize offense and defense. The different factions in the game are very asymmetrical and allow you to "break" the rules in various ways. Some let you move further, some provide extra attacks, some give you extra places you can summon units from, and another even lets you bring units back from the dead at the cost of your Summoner's health. You'll notice in the picture that the game log tracks every action that is done. You can see every card that is summoned, every move that is made, every attack that is rolled, and the damage that is dealt. It is this game log we will be scraping and using for our analysis.

## Dataset Details
Great, we know loosely how the game works, we know where we're getting the data from, and now, it's time to dive into code. To extract the data from the log, for now I am pulling up the game I want to analyze, inspecting the page, going into the console, and then manually using document.querySelector to select the log data. We then loop through the log, extracting all the text and storing it in an array, and then write it out to a .csv file. From there we load the file with Python, clean it to fit our needs, parse the specific data we are looking for using Regex (attacks, moves, discards, etc.), and then write it into a dataframe using Pandas. 

![attack df example](https://github.com/A-Rutledge/SummonerWars/assets/33138919/afb702ec-5b6f-4b71-a3f0-8731184ea399)

For now I am manually running the code for each individual game while I get all of the processes sorted out. Once I have all the data I need, I start working on automating it to take in a list of game links, automatically process all the information, write it to an S3 bucket, and then I can bulk process it through SQL or Tableau to see larger trends.

## Analysis
Thanks for reading this far. For now all I have made is the dataframe holding attacks from a single game so not much can be gleaned from it yet. Once I get few dozen games in, I can start seeing some more trends. For now though, I have been looking at data round by round to see when the winning player took the lead, how much more damage they did than their opponent, which cards were used the most, the average damage per card, and which cards were targeted the most. From a single game level, this data should be very interesting to see what had the biggest impact in each game and could lead to some exciting findings.

I will work on getting this all displayed in a better way moving forward, but for now I want to have it documented where I am in the process and how it's coming together so far. Here are some screen shots of the various calculations used and the results.

### The Winning Player:
I foresee this being helpful as more and more games start populating. It will help determine if 1st or 2nd player win more often (first player advantage) and will help me ensure I corellate the findings properly. It is possible the player that does the most damage does not win if they left their Summoner open for one big lethal attack from their opponent. The last attack in the game will always be the attack that destroys the Summoner, so it is very straightforward to get.

![image](https://github.com/A-Rutledge/SummonerWars/assets/33138919/d0016cb4-6c54-48c4-83cd-fcd10d637c78)


### Total Damage over the course of the game by each player:
This one is the most fun and I got an actual plot working with it.
![image](https://github.com/A-Rutledge/SummonerWars/assets/33138919/f452e5c6-78a8-47e0-b127-302f5423bc40)


### Number of Attacks per Card
This gives some useful insight into which cards are used the most often. In my games it may help determine which pose the biggest threat and should be focused on first.

![image](https://github.com/A-Rutledge/SummonerWars/assets/33138919/57788791-b2c6-4e13-b9c4-9e0142d48d2b)


### Most Targeted Cards
In the same vein as the last one, this shows which cards the high ranking players thought were the biggest threat. My expectation early on is to always see the Summoners as some of the most targeted cards because that is the win condition and will always be a priority.

![image](https://github.com/A-Rutledge/SummonerWars/assets/33138919/c09b1f45-87c1-42d2-898f-3137a7287924)


### Average Damage per Card
This may help show which cards consistently do the most damage.

![image](https://github.com/A-Rutledge/SummonerWars/assets/33138919/cb5bf82e-39ab-4973-a46c-7f83c0c32f68)


### Attack breakdown by Round
Trying to see the breakdown of attacks per round. As you can only attack with 3 units each round, I wanted to see how well they capitalized on that. As stated earlier, certain factions allow you to break that 3 attack max rule, which is why you will see Player 2 gets 5 attacks in a single round in this game.

![image](https://github.com/A-Rutledge/SummonerWars/assets/33138919/adc296fa-c8ed-4ee1-881f-3e280c7bb956)

### Number of Rounds Where at Least 3 Attacks Were Made
This is the same metric, just in a different view. I am experimenting to see what works best and to see what I can plot in the future given more data points.

![image](https://github.com/A-Rutledge/SummonerWars/assets/33138919/aae8408c-004c-4d44-a612-82a2ef10d527)

### Summary View of Attacks Made and Damage Done
This view shows how big of an impact using your limited attacks with the wrong cards matters. Yes, the dice can play a factor in this, but any significant differences should lead to further analysis.

![image](https://github.com/A-Rutledge/SummonerWars/assets/33138919/0190df93-fa5d-41d9-991e-3a3fa190814a)

I find this particular game fascinating as both players ended with the same number of attacks made, but player 2 had a whopping 10 damage extra. What makes that even better is one of their attacks did 0 damage so they really managed to fully capitalize on their best cards.

## What's next?
10/05
That's all I have so far. I need to narrow down the metrics I want to focus on and spend some time building out the charts for them, but for now I need to finish the core parts of this. I will build out the dataframes to track movement next, followed by events played, magic built, and cards summoned. Once the core is fully built out, I can start pulling in more and more games to see how things start stacking up.

10/06
We made tons of progress today as we head into the weekend. I will have this knocked out in no time! Once I figured out how I was going to extract all the data I need, it was really just reusing the same logic and tweaking the RegEx to get all the different categories I wanted to track. I still need to work out the new select statements now that all of the details are in one big dataframe, but I did manage to get this really fun view out of it:

![image](https://github.com/A-Rutledge/SummonerWars/assets/33138919/a3614798-a85e-460f-8851-b83590609783)

Looking at details like this game by game would be great, so I need to deep dive into Pandas over the weekend and see how to properly group this data. I can tell already I am not doing things as efficiently as I can in Pandas. I have given each game a unique id that we can use to reference them (it's based on the name of the csv file, so that will need work in the future so it's not just game (8).csv and so on. I am interested to learn how powerful grouping is and if I can group by the game ID and then further group/aggregate to see stats like this for all the games at once. Although the big test I will be doing is validating the other games that I pulled to ensure that none of the other Factions create edge cases I didn't account for when designing the parser. I know for a fact my event tracker does not track all of the interactions events cause, but events in Summoner Wars are so powerful and so varied from faction to faction that I may just have to settle for "good enough".

I am ahead of schedule for my goal of getting the core system working by the 10th. There is a tournment starting that I want to track the stats for and I think it will be really interesting. By the end of the month I will aim to automate the log extraction process and get the dashboard created, but for the upcoming week, I think I will be focusing on refining my Pandas skills to get the most value out of the data as possible.

10/07:
Lots of QA testing today. Spent a lot of time combing through the game logs looking for any inaccuracies now that I have brought in many different factions. Each faction being able to break the rules in different ways is proving to be a challenge. Spent some time reading through pandas documentation and building out more metrics I can capture from the data. Still working on a way to get it all graphed.

10/08:

Added logic for tracking the number of cards destroyed. It's working in most cases, but Obsidian Dwarves are causing an issue with the "Wild Swing" ability. It does multiple instances of damage so it is not properly capturing the "was destroyed" text with the current logic. I can change it to just append player based off what round it is, but have not made that change yet.

10/09:

Changed logic for how the attack parser worked. Tundra Orcs and Obsidian Dwarves were causing issues with damage tracking. This led to doing damage,destroy, and build magic all in 1 check. IMPORTANT NOTE: This tracks every instance of damage, including damage to self and own cards. This is leading to larger numbers then seen on sw-zone.com for cards destroyed and damage values, but I feel it is a more accurate reflection of what the card does on average.

The tournament starts tomorrow and will take at least 3 days before the majority of the games are finished. In that time, I can get as many stats tracked through the dataframe as I can think of and publish it to s3 buckets and a database. I am planning on using BigQuery as the free trial is more generous than Snowflake. After that will be the Tableau Dashboard to put the final level of polish on it. 

And as a preview of what's to come, here is 16 games broken down into aggregates: 

![image](https://github.com/A-Rutledge/SummonerWars/assets/33138919/1893af00-d631-408e-bcdb-758d97a72eb0)

I will need to append which Player won each game, but am trying to find a solution for that. In 95% of the cases, it is the player that attacked last, but there are a few occasions where the game ended due to a timeout which would incorrectly flag the wrong winner. 

10/10:
Did not have as much time to work on this today as I would have liked. I was able to get all previous calculations done on an individual game to scale properly across the dozens of games I am planning on bringing in. Here are some of the cool ones so far:

Top Average Damage:

![image](https://github.com/A-Rutledge/SummonerWars/assets/33138919/d8438fd1-e573-4c57-a171-d205f41f7fd2)


Most Targeted:

![image](https://github.com/A-Rutledge/SummonerWars/assets/33138919/399a9908-d2fa-416e-b9ed-af9b89bb8cf2)


Most Attacks made:

![image](https://github.com/A-Rutledge/SummonerWars/assets/33138919/e28cec29-86d0-470d-8cac-374b4585e14b)


Here I wanted to highlight the issue of determining who won each game. This may be best handled in Tableau, but I am considering a dictionary and if the Summoner's name is in the "Target" column in the last row of the game, that means that faction loses:

![image](https://github.com/A-Rutledge/SummonerWars/assets/33138919/07497911-2972-4481-bc48-451105bcecc7)

Tomorrow I will be moving this to an s3 bucket and a database so I am not expecting to see many more graphs. Maybe just an average hit rate or something similar. Once I have the final view completed, I can get feedback from the game community and see what changes can be made.

10/11:

Spent the day getting the s3 buckets and database setup. Nothing to report on that yet as I still have quite a bit of work left with it. Also spent some time getting my personal website started. I did go ahead and try to implement faction tracking. It's still in the early stages, but here it is displaying the losing faction.

![image](https://github.com/A-Rutledge/SummonerWars/assets/33138919/01f16644-2350-44e7-90f1-a602c67b89c4)


10/12 Update:
BigQuery database is almost done. I am having some trouble getting jupyter to run the jobs due to not being able to install the dependencies (pyarrow). Darn you GRPCIO constantly failing to build wheels or something. Troubleshooting that has taken the better part of the day unfortunately. I did however, manage to get all the factions tagged properly. I used the movement data to get a unique list of cards, and then compared that list against the summoners and assigned factions. For all factions, the owner of the faction is the faction is the only one that is able to "move" the summoner. Opponents can "force" it, but not "move" it. I used this to create the full list and it is working as intended. I will keep a close eye on if it breaks once I load in significantly more games.

![image](https://github.com/A-Rutledge/SummonerWars/assets/33138919/6299c247-a67c-476a-a656-556da22b41e4)

![image](https://github.com/A-Rutledge/SummonerWars/assets/33138919/84673c99-e545-48fd-bc01-5f9580ae9ab9)

I don't think I will end up doing the join at this stage. I will probably keep the list of gameid,playerid,and faction as a separate table that can be referenced with smaller datasets as opposed to just smacking it on the whole thing where it will serve little purpose besides convenience.

![image](https://github.com/A-Rutledge/SummonerWars/assets/33138919/bbbba48d-2d61-422d-b9ce-2615ab076d3b)

10/13 update:

The core functionality is officially finished! I have it doing everything I want and even have the Tableau Dashboard built out. The BigQuery issue was just me passing in one of the parameters incorrectly because the error code was saying it was caused by something else. 

![image](https://github.com/A-Rutledge/SummonerWars/assets/33138919/5ed754af-9623-4e29-9131-21a3780a8639)

Here it is working and query-able. I had to change plans anyways though, as the free version of Tableau is not able to be connected to BigQuery like it is in the full version. I ended up exporting the dataframes as .xlsx files and importing them that way. It works just fine and with only 15 games of records, it has no issues being slow. For the ongoing tournament, 90% of the games are finished and I'm already looking at pulling in 84 games so that will be the real test. Here is the link to the Tableau Dashboard: https://public.tableau.com/views/SummonerWarsGameDataAnalysis/GameAnalysis?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link

![image](https://github.com/A-Rutledge/SummonerWars/assets/33138919/103f5381-30aa-4b56-ab2e-2a86afb48fed)




