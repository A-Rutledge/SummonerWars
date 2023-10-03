# SummonerWars
Database building and parsing data from Summoner Wars Online matches
-----------------------------------------------------------------------------------------------------------------
The goal of this project is to create a database that I can use to store and analyze game data from Summoner Wars Online matches. Using the replay links, I will use web scraping to extract the data for the game log, and then use a data parser to extract the key details. The end result will be 3 dataframes holding different details that can be joined and analyzed.

Attack Dataframe hold all attacking details:
Turn Number,Player,Attacking Card,Card Targeted,Damage

Movement Dataframe will hold all movement details:
Turn Number,Player,Card,Forced

Magic Dataframe will track how much magic is built each turn
Turn,Player,Number of cards discarded to build magic

I foresee some issues with the parser for the build magic phase. I can't just scrape for the word "discard" because cards like Border Archer exist that let you discard to attack again.
