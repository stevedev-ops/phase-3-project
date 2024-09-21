import argparse
from bin_operations import view_bins, add_bin, simulate_bin_fill, request_pickup
from schedule_management import view_schedule, update_schedule
from route_optimization import calculate_optimal_route


def main():
    parser = argparse.ArgumentParser(description="Smart Waste Management System CLI")

    parser.add_argument('--view-bins', action='store_true', help="View all bins and their status.")
    parser.add_argument('--add-bin', nargs=2, metavar=('location', 'capacity'), help="Add a new bin.")
    parser.add_argument('--simulate-fill', type=int, help="Simulate bin fill level by bin ID.")
    parser.add_argument('--request-pickup', action='store_true', help="Request pickup for full bins.")
    parser.add_argument('--view-schedule', action='store_true', help="View collection schedule.")
    parser.add_argument('--update-status', nargs=2, metavar=('bin_id', 'status'), help="Update collection status for a bin.")
    parser.add_argument('--calculate-route', action='store_true', help="Calculate the optimal collection route.")

    args = parser.parse_args()

    if args.view_bins:
        view_bins()
    elif args.add_bin:
        add_bin(args.add_bin[0], int(args.add_bin[1]))
    elif args.simulate_fill:
        simulate_bin_fill(args.simulate_fill)
    elif args.request_pickup:
        request_pickup()
    elif args.view_schedule:
        view_schedule()
    elif args.update_status:
        update_schedule(int(args.update_status[0]), args.update_status[1])
    elif args.calculate_route:
        calculate_optimal_route()
    else:
        print("Invalid command. Use --help for available options.")

if __name__ == "__main__":
    main()
