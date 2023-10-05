# Split the log into individual actions
actions = re.split(r"Beginning of turn \d+\.", preprocessed_log_data)
# Initialize lists to store parsed data
player_ids = []
card_names = []
targets = []
total_damages = []

# Define a regex pattern to extract relevant information from each action
pattern = r"Player (\d+) is attacking with (.+?), targeting (.+?)\.\nPlayer \d+ rolls:\n(.+?)\n"

# Initialize variables to store attack and damage data
current_round = 0
attacks = []

# Iterate through actions and parse relevant data
for action in actions:
    matches = re.finditer(pattern, action)
    for match in matches:
        player_id, card_name, target, rolls = match.groups()
        # Extract numeric attack values from the rolls
        damage_values = [int(roll.strip()) for roll in re.findall(r'\d+', rolls)]
        for damage in damage_values:
            attacks.append({
                "Round": current_round,
                "PlayerID": int(player_id),
                "CardName": card_name.strip(),
                "Target": target.strip(),
                "Attack": 1,
                "DamageValue": damage
            })
    current_round += 1

# Convert parsed data to a DataFrame for analysis
df = pd.DataFrame(attacks)
