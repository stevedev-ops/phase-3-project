import random
from data_management import load_data, save_data
from datetime import datetime

# Simulate bin fill level - python main.py --simulate-fill 1

def simulate_bin_fill(bin_id):
    data = load_data()
    for bin in data['bins']:
        if bin['id'] == bin_id:
            new_fill = int(input(f"Enter new fill level for bin {bin_id} (current: {bin['current_fill']}%): "))
            if 0 <= new_fill <= bin['capacity']:
                bin['current_fill'] = new_fill
                save_data(data)
                print(f"Bin {bin_id} at {bin['location']} is now {bin['current_fill']}% full.")
            else:
                print(f"Error: Fill level must be between 0 and {bin['capacity']}%.")
            return
    print(f"Bin with ID {bin_id} not found.")

# View all bins - python main.py --view-bins

def view_bins():
    data = load_data()
    for bin in data['bins']:
        print(f"Bin ID: {bin['id']}, Location: {bin['location']}, Fill Level: {bin['current_fill']}%, Capacity: {bin['capacity']}")

# Add a new bin python main.py --view-bins

def add_bin(location, capacity):
    data = load_data()
    new_id = max([bin['id'] for bin in data['bins']], default=0) + 1
    new_bin = {
        "id": new_id,
        "location": location,
        "capacity": capacity,
        "current_fill": 0
    }
    data['bins'].append(new_bin)
    save_data(data)
    print(f"New bin added at {location} with capacity {capacity}%.")

# Request pickup for full bins - python main.py --request-pickup

def request_pickup():
    data = load_data()
    for bin in data['bins']:
        if bin['current_fill'] >= 75:
            data['collection_schedule'].append({
                "bin_id": bin['id'],
                "location": bin['location'],
                "request_time": str(datetime.now()),
                "status": "Pending"
            })
            print(f"Pickup requested for bin {bin['id']} at {bin['location']}.")
    save_data(data)
