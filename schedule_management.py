from datetime import datetime
from data_management import load_data, save_data

# View collection schedule -python main.py --view-schedule

def view_schedule():
    data = load_data()
    
    if not data['collection_schedule']:
        print("No collection schedules available.")
        return

    print(f"{'Bin ID':<10} {'Location':<20} {'Status':<10} {'Request Time':<20}")
    print("-" * 60)
    
    for schedule in data['collection_schedule']:
        print(f"{schedule['bin_id']:<10} {schedule['location']:<20} {schedule['status']:<10} {schedule['request_time']:<20}")
    
    print("-" * 60)
    print(f"Total requests: {len(data['collection_schedule'])}")

# Update collection status - python main.py --update-status 1 Completed

def update_schedule(bin_id, status):
    data = load_data()
    for schedule in data['collection_schedule']:
        if schedule['bin_id'] == bin_id:
            schedule['status'] = status
            save_data(data)
            print(f"Bin {bin_id} collection status updated to {status}.")
            return
    print(f"Collection for bin {bin_id} not found.")
