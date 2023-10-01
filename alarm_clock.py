# Function to validate and parse time input
def parse_time(time_str):
    try:
        hours, minutes = map(int, time_str.split(":"))
        if 0 <= hours < 24 and 0 <= minutes < 60:
            return hours, minutes
        else:
            raise ValueError
    except ValueError:
        print("Invalid time format. Please enter time in HH:MM format with hours between 0-23 and minutes between 0-59.")
        return None

# Get the current time
current_time_str = input("Enter the current time in HH:MM format (24-hour clock): ")
parsed_time = parse_time(current_time_str)

if parsed_time:
    current_hours, current_minutes = parsed_time

    # Get the number of hours to wait for the alarm
    try:
        hours_to_wait = int(input("Enter the number of hours to wait for the alarm: "))
        if hours_to_wait < 0:
            raise ValueError("Invalid number of hours. Hours should be non-negative.")

        # Calculate the time when the alarm goes off
        total_current_minutes = current_hours * 60 + current_minutes
        total_alarm_minutes = total_current_minutes + hours_to_wait * 60
        alarm_hours = (total_alarm_minutes // 60) % 24
        alarm_minutes = total_alarm_minutes % 60

        # Print the alarm time
        print(f"The alarm will go off at {alarm_hours:02d}:{alarm_minutes:02d}.")
        
    except ValueError as e:
        print(e)