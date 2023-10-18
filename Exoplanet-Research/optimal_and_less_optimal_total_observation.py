def get_minutes(hh_mm):
    """Convert HH:MM format to total minutes."""
    hours, minutes = map(int, hh_mm.split(':'))
    return hours * 60 + minutes

def format_time(minutes):
    """Convert total minutes to HH:MM format."""
    hours = minutes // 60
    minutes %= 60
    return f"{hours:02}:{minutes:02}"

def main():
    while True:
        # Ask for expected transit duration
        transit_duration_str = input("Enter the expected transit time in HH:MM format: ")

        # Convert the HH:MM string to total minutes
        transit_duration_minutes = get_minutes(transit_duration_str)

        # Calculate the Optimal and Less Optimal cases
        optimal_minutes = transit_duration_minutes * 3
        less_optimal_minutes = transit_duration_minutes * 2

        outside_transit_optimal = transit_duration_minutes  # 1x of transit duration
        outside_transit_less_optimal = transit_duration_minutes // 2  # 0.5x of transit duration

        # Print the results
        print("\n\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print(f"\nOptimal Total Observation Window\n(HH:MM): {format_time(optimal_minutes)}")
        print(f"\n[Before Transit Time {format_time(outside_transit_optimal)}]\n[Transit Duration {transit_duration_str}]\n[After Transit Time {format_time(outside_transit_optimal)}]")

        print("\n\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print(f"\nLess Optimal Total Observation Window\n(HH:MM): {format_time(less_optimal_minutes)}")
        print(f"\n[Before Transit Time {format_time(outside_transit_less_optimal)}]\n[Transit Duration {transit_duration_str}]\n[After Transit Time {format_time(outside_transit_less_optimal)}]")

        # Ask the user if they want to run the program again
        retry = input("\n\n\nWould you like to run the program again?\n(y/yes or hit Enter to end) ").strip().lower()
        if retry not in ['y', 'yes']:
            break

if __name__ == "__main__":
    main()
