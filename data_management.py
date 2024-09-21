import json

DB_FILE = 'db.json'

# Load the data from db.json
def load_data():
    with open(DB_FILE, 'r') as f:
        return json.load(f)

# Save the data to db.json
def save_data(data):
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=4)
