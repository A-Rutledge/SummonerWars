import re
import pandas as pd
import csv
import os
import math

def clean_log_data(log_data):
    # Split the log data into lines
    lines = log_data.split('\n')

    # Initialize variables
    preprocessed_log = []
    current_card_name = None
    skip_next_line = False  # Flag to skip the next line when "rolls" is followed by another "Player" line

    # Iterate through the lines
    index = 0
    while index < len(lines):
        line = lines[index]
        if line.startswith("Player"):
            # Extract the card name when an attack is initiated
            if "is attacking with" in line:
                parts = line.split("is attacking with")
                current_card_name = parts[1].split(",")[0].strip()

            # Check if "rolls" is followed by another "Player" line (no damage done)
            elif "rolls:" in line:
                next_line_index = index + 1
                if next_line_index < len(lines) and lines[next_line_index].startswith("Player"):
                    if "damage" not in lines[next_line_index]:
                        if "rolls:" in lines[next_line_index]:
                            preprocessed_log.append(line)  # Append the "rolls" line first
                            del lines[next_line_index]
                            #preprocessed_log.append(f"{current_card_name} rerolled")  # Append the "takes 0 damage" line
                            skip_next_line = True
                        else:
                            preprocessed_log.append(line)  # Append the "rolls" line first
                            preprocessed_log.append(f"{current_card_name} received 0 damage")  # Append the "takes 0 damage" line
                            skip_next_line = True
                            
        if not skip_next_line:
            preprocessed_log.append(line)

        index += 1
        skip_next_line = False  # Reset the flag so it doesn't skip next time

    # Join the preprocessed log data back into a single string
    preprocessed_log_data = '\n'.join(preprocessed_log)
    
    return preprocessed_log_data

def parse_attack_data(preprocessed_log_data):
    # Split the log into individual actions
    actions = re.split(r"Beginning of turn \d+\.", preprocessed_log_data)
    # Initialize lists to store parsed data
    player_ids = []
    card_names = []
    targets = []
    total_damages = []

    # Define a regex pattern to extract relevant information from each action
    pattern = r"Player (\d+) is attacking with (.+?), targeting (.+?)\.\nPlayer \d+ rolls:\n([\s\S]*?)(?=Player \d is attacking|$)"
    #nPlayer 2 is attacking with Frost Mage, targeting Ember Guard.\nPlayer 2 rolls:\nEmber Guard received 4 damage.\nEmber Guard was destroyed.\nPlayer 2 discarded a card for magic.\nPlayer 2 discarded a card for magic.\nPlayer 2 discarded a card for magic.\n'

    # Initialize variables to store attack and damage data
    current_round = 0
    attacks = []

    # Iterate through actions and parse relevant data
    for action in actions:
        matches = re.finditer(pattern, action)
        for match in matches:
            player_id, card_name, target, rolls = match.groups()
            roll = rolls.split("\n")
            damage = 0
            destroyed = 0
            discarded = 0
            for r in roll:
                number_match = re.search(r'\d+', r)
                if number_match:
                    number = number_match.group()
                    damage += int(number)
                elif "destroyed" in r:
                    destroyed += 1
                elif "magic" in r:
                    discarded += 1
            attacks.append({
                "Round": current_round,
                "PlayerID": int(player_id),
                "CardName": card_name.strip(),
                "Target": target.strip(),
                "Attack": 1,
                "DamageValue": damage,
                "CardsDestroyed": destroyed,
                "MagicBuilt": discarded
            })
        current_round += 1

    # Convert parsed data to a DataFrame for analysis
    df = pd.DataFrame(attacks)
    return df

def parse_movement_data(preprocessed_log_data):
    # Split the log into individual actions
    actions = re.split(r"Beginning of turn \d+\.", preprocessed_log_data)
    # Initialize lists to store parsed data
    player_ids = []
    card_names = []
    targets = []
    total_damages = []

    # Define a regex pattern to extract relevant information from each action
    pattern = r"Player (\d+) (moved|forced) (.+?).\n"

    # Initialize variables to store attack and damage data
    current_round = 0
    movement = []

    # Iterate through actions and parse relevant data
    for action in actions:
        matches = re.finditer(pattern, action)
        for match in matches:
            player_id, moveType,card_name = match.groups()
            # Extract numeric attack values from the rolls
            movement.append({
            "Round": current_round,
            "PlayerID": int(player_id),
            "movementType": moveType,
            "CardName": card_name.strip()
            })
        current_round += 1

    # Convert parsed data to a DataFrame for analysis
    moveDF = pd.DataFrame(movement)
    return moveDF


def parse_summon_data(preprocessed_log_data):
    # Split the log into individual actions
    actions = re.split(r"Beginning of turn \d+\.", preprocessed_log_data)
    # Initialize lists to store parsed data
    player_ids = []
    card_names = []
    targets = []
    total_damages = []

    # Define a regex pattern to extract relevant information from each action
    pattern = r"Player (\d+) summoned (.+?).\n"

    # Initialize variables to store attack and damage data
    current_round = 0
    summons = []

    # Iterate through actions and parse relevant data
    for action in actions:
        matches = re.finditer(pattern, action)
        for match in matches:
            player_id,card_name = match.groups()
            # Extract numeric attack values from the rolls
            summons.append({
            "Round": current_round,
            "PlayerID": int(player_id),
            "summoned": 1,
            "CardName": card_name.strip()
            })
        current_round += 1

    # Convert parsed data to a DataFrame for analysis
    summonDF = pd.DataFrame(summons)
    return summonDF

def parse_event_data(preprocessed_log_data):
    # Split the log into individual actions
    actions = re.split(r"Beginning of turn \d+\.", preprocessed_log_data)
    # Initialize lists to store parsed data
    player_ids = []
    card_names = []
    targets = []
    total_damages = []

    # Define a regex pattern to extract relevant information from each action
    pattern = r"Player (\d+) played the event (.+?).\n"

    # Initialize variables to store attack and damage data
    current_round = 0
    events = []

    # Iterate through actions and parse relevant data
    for action in actions:
        matches = re.finditer(pattern, action)
        for match in matches:
            player_id,card_name = match.groups()
            # Extract numeric attack values from the rolls
            events.append({
            "Round": current_round,
            "PlayerID": int(player_id),
            "CardName": card_name.strip(),
            "Event": 1
            })
        current_round += 1

    # Convert parsed data to a DataFrame for analysis
    eventDF = pd.DataFrame(events)
    return eventDF


def parse_csv_file(file_path):
    # Load the CSV file into a DataFrame
    with open(file_path, 'r') as f:
        log_data = f.read()
    
    df = pd.DataFrame()

    
    # Perform data parsing using your parsing functions
    preprocessed_log_data = clean_log_data(log_data)
    attack_data = parse_attack_data(preprocessed_log_data)
    move_data = parse_movement_data(preprocessed_log_data)
    summon_data = parse_summon_data(preprocessed_log_data)
    event_data = parse_event_data(preprocessed_log_data)

    return attack_data, move_data, summon_data, event_data



def process_multiple_csv_files(directory):
    # Initialize a list to store the parsed data from all CSV files
    all_data = []

    # Loop through CSV files in the specified directory
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            file_path = os.path.join(directory, filename)
                        
            # Parse the CSV file and get the dataframes
            attack_data, move_data, summon_data, event_data = parse_csv_file(file_path)

            # Assign a unique ID to each game
            game_id = os.path.splitext(filename)[0]

            # Add the game ID to each dataframe
            attack_data['GameID'] = game_id
            move_data['GameID'] = game_id
            summon_data['GameID'] = game_id
            event_data['GameID'] = game_id

            # Append the dataframes to the list
            all_data.extend([attack_data, move_data, summon_data, event_data])

    # Concatenate all dataframes into a single dataframe
    combined_data = pd.concat(all_data, ignore_index=True)

    return combined_data




##df = pd.read_csv(file_path)
directory_path = 'C:/Users/Andrew/Downloads/SampleCSV/'
combined_data = process_multiple_csv_files(directory_path)
