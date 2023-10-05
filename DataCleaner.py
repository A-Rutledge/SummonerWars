#This code checks the log for attacks that deal no damage. It adds the text saying the card received 0 damage so the parser can work on all cases.

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
                preprocessed_log.append(line)  # Append the "rolls" line first
                preprocessed_log.append(f"{current_card_name} received 0 damage")  # Append the "takes 0 damage" line
                skip_next_line = True
    
    if not skip_next_line:
        preprocessed_log.append(line)
    
    index += 1
    skip_next_line = False  # Reset the flag so it doesn't skip next time

# Join the preprocessed log data back into a single string
preprocessed_log_data = '\n'.join(preprocessed_log)
