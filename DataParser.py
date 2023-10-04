import re
import pandas as pd


# Split the log into individual actions
actions = re.split(r"Beginning of turn \d+\.", log_data)

# Initialize lists to store parsed data
player_ids = []
card_names = []
targets = []
total_damages = []

#There is a bug here. rolls:\n(.+?)\n captures everything after rolls:\n which in the case of our log file, will incorrectly capture attacks that do 0 damage. I tried to account for it with the if statement, but it is not working properly
#Sample log data:
#Player 2 is attacking with Border Archer, targeting Enigma Sage.
#Player 2 rolls:
#Player 2 is attacking with Border Archer, targeting Enigma Sage.
#Player 2 rolls:
#Enigma Sage received 1 damage.

#The first attack incorrectly parses due do capturing "Player 2 is attacking with Border Archer, targeting Enigma Sage" as the line where the damage comes from and extracts the 2. I will have to spend more time on working this out.

# Define a regex pattern to extract relevant information from each action
pattern = r"Player (\d+) is attacking with (.+?), targeting (.+?)\.\nPlayer \d+ rolls:\n(.+?)\n"

# Initialize variables to store attack and damage data
current_round = 0
current_player = None
current_card = None
current_target = None
attacks = []

# Iterate through actions and parse relevant data
for action in actions:
    if action.strip():
        if action.startswith("Beginning of turn"):
            current_round += 1
        else:
            matches = re.finditer(pattern, action)
            for match in matches:
                player_id, card_name, target, rolls = match.groups()
                # Extract numeric attack values from the rolls
                damage_values = [int(roll.strip()) for roll in re.findall(r'\d+', rolls)]
                if "damage" not in rolls.lower():
                    # Handle the case of 0 damage attack
                    attacks.append({
                        "Round": current_round,
                        "PlayerID": int(player_id),
                        "CardName": card_name.strip(),
                        "Target": target.strip(),
                        "Attack": 1,
                        "DamageValue": 0
                    })
                for damage in damage_values:
                    attack = 1  # Set attack to 1 for all attacks except the 0 damage attack
                    attacks.append({
                        "Round": current_round,
                        "PlayerID": int(player_id),
                        "CardName": card_name.strip(),
                        "Target": target.strip(),
                        "Attack": attack,
                        "DamageValue": damage
                    })

# Convert parsed data to a DataFrame for analysis
df = pd.DataFrame(attacks)
