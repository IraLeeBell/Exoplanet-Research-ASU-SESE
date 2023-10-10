from datetime import datetime, timedelta

def calculate_observing_window(start_time_str, end_time_str, transit_duration_str):
    # Parse times from input
    start_time = datetime.strptime(start_time_str, "%H:%M")
    end_time = datetime.strptime(end_time_str, "%H:%M")
    transit_hours, transit_minutes = map(int, transit_duration_str.split(":"))
    
    # If the end time is before the start time, it's assumed to be the next day
    if end_time < start_time:
        end_time += timedelta(days=1)
    
    # Calculate total observing duration
    total_duration = end_time - start_time
    total_hours, remainder = divmod(total_duration.seconds, 3600)
    total_minutes = remainder // 60
    
    # Calculate midpoint of the observing window
    midpoint = start_time + total_duration / 2
    
    # Calculate start and end times of the exoplanet transit
    half_transit_duration = timedelta(hours=transit_hours, minutes=transit_minutes) / 2
    transit_start = midpoint - half_transit_duration
    transit_end = midpoint + half_transit_duration
    
    return {
        'total_observing_duration': f"{total_hours} hours {total_minutes} minutes",
        'transit_start': transit_start.strftime("%H:%M"),
        'transit_end': transit_end.strftime("%H:%M")
    }

start_time_str = input("Enter the recommended observing start time (HH:MM): ")
end_time_str = input("Enter the recommended observing end time (HH:MM): ")
transit_duration_str = input("Enter the transit duration (HH:MM): ")

results = calculate_observing_window(start_time_str, end_time_str, transit_duration_str)

print(f"\nTotal observing duration: {results['total_observing_duration']}")
print(f"Exoplanet transit start time: {results['transit_start']}")
print(f"Exoplanet transit end time: {results['transit_end']}")
