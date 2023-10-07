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
