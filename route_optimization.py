from data_management import load_data

# Calculate optimal collection route (simple example) - python main.py --calculate-route

def calculate_optimal_route():
    data = load_data()
    pending_bins = [schedule['bin_id'] for schedule in data['collection_schedule'] if schedule['status'] == 'Pending']
    if not pending_bins:
        print("No pending collections.")
        return
    route = sorted(pending_bins)
    print("Optimal route (by bin ID):", ' -> '.join(map(str, route)))
