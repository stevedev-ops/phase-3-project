
Smart Waste Management System
Welcome to the Smart Waste Management System! This command-line interface (CLI) tool helps you manage waste bins efficiently by allowing you to view bin statuses, simulate fill levels, add new bins, request pickups, and manage collection schedules.

Table of Contents
Installation
Usage
Features
Functions
Data Management
License
Installation
To use the Smart Waste Management System, clone the repository and ensure you have Python installed. You can run the following commands:

bash
Copy code
git clone <repository-url>
cd <repository-directory>
pip install -r requirements.txt
Make sure to create a db.json file to store bin data and collection schedules.

Usage
Run the program using the following command format:

bash
Copy code
python main.py [options]
Available Options
--view-bins: View all bins and their statuses.
--add-bin <location> <capacity>: Add a new bin at the specified location with a given capacity.
--simulate-fill <bin_id>: Simulate the fill level of a bin by its ID.
--request-pickup: Request pickup for bins that are full.
--view-schedule: View the collection schedule.
--update-status <bin_id> <status>: Update the collection status for a specific bin.
--calculate-route: Calculate the optimal route for bin pickups.
Features
View Bin Status: Check the current fill levels and capacities of all bins.
Add New Bins: Easily add new waste bins with specified locations and capacities.
Simulate Fill Levels: Update and simulate the fill levels of existing bins.
Request Pickups: Automatically request pickups for bins that are 75% full or more.
View and Update Collection Schedules: Manage collection requests and their statuses.
Calculate Pickup Routes: Determine the most efficient route for collecting waste.
Functions
1. simulate_bin_fill(bin_id)
Simulates the fill level of a specific bin by prompting the user for input.

2. view_bins()
Displays all bins along with their IDs, locations, current fill levels, and capacities.

3. add_bin(location, capacity)
Adds a new bin with the specified location and capacity.

4. request_pickup()
Requests pickups for bins that are 75% full or more and updates the collection schedule.

5. view_schedule()
Displays the current collection schedule, including bin IDs, locations, statuses, and request times.

6. update_schedule(bin_id, status)
Updates the status of a specific bin's collection request.

7. calculate_optimal_route()
Calculates and displays the optimal route for collecting bins based on their IDs.

Data Management
The system utilizes a JSON file (db.json) to store data related to bins and collection schedules. You can modify this file directly if needed, but it is recommended to use the provided functions for data integrity.

Load Data
python
Copy code
def load_data():
    with open(DB_FILE, 'r') as f:
        return json.load(f)
Save Data
python
Copy code
def save_data(data):
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=4)
License
This project is licensed under the MIT License. Feel free to modify and use the code as per your requirements!