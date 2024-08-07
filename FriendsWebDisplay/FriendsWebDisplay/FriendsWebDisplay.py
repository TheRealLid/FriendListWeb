import json
import pandas

f = open('usr_76e2aa13-2cbf-4cc2-861f-b11246832faf.json')
data = json.load(f)
friends_list = data.get('friends', [])
print(friends_list)


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

