import json
import pandas
# Read and clean the lines from the file
with open("FriendListIDS.txt", "r") as f:
    lines = f.readlines()

cleaned_lines = []
for line in lines:
    if 'u' in line:
        index = line.index('u')  # Find the index of the first 'u'
        cleaned_lines.append(line[index:].strip())  # Slice the line from the 'u' onward and strip whitespace

def add_user_friends_to_json(user_id, friends_list, json_file):
    try:
        # Read the existing JSON data
        with open(json_file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        # If the file does not exist, start with an empty list
        data = []

    # Check if the user already exists in the data
    user_exists = False
    for entry in data:
        if entry['user_id'] == user_id:
            user_exists = True
            break

    if not user_exists:
        # Add the new user and their friends
        data.append({
            "user_id": user_id,
            "friends": [friend for friend in friends_list if friend]
        })

        # Write the updated data back to the JSON file
        with open(json_file, 'w') as f:
            json.dump(data, f, indent=4)

# Check the first cleaned line for verification
print(cleaned_lines[0])

# Add user friends to JSON
add_user_friends_to_json("test", cleaned_lines, "FriendListIDS.json")
