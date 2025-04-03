""" 
Work time tracking program in Python that allows users to enter start and end times, then calculates the total hours worked.

No extra dependencies required, but for CSV handling, pandas makes it easier:

-- pip install pandas -- 

Features:
1. Supports multiple work periods per day
2. Detects & logs overtime if total work exceeds 8 hours
3. Generates weekly & monthly reports from saved work logs
4. Logs data in both CSV (spreadsheet-friendly) & JSON (structured format)
5. Improved user experience with menus & data validation

"""

import datetime
import csv
import os
import json

# Constants
LOG_CSV = "work_log.csv"
LOG_JSON = "work_log.json"
STANDARD_WORK_HOURS = 8  # Standard daily work limit

# Load existing work logs
def load_work_log():
    if os.path.exists(LOG_JSON):
        with open(LOG_JSON, "r") as file:
            return json.load(file)
    return {}

# Save work log to JSON file
def save_work_log(log_data):
    with open(LOG_JSON, "w") as file:
        json.dump(log_data, file, indent=4)

# Convert user input to a datetime object
def parse_time(time_str):
    formats = ["%H:%M", "%I:%M %p"]
    for fmt in formats:
        try:
            return datetime.datetime.strptime(time_str, fmt)
        except ValueError:
            continue
    raise ValueError("Invalid time format! Use HH:MM or HH:MM AM/PM.")

# Calculate total work duration
def calculate_total_time(work_periods, break_time=0):
    total_minutes = sum([(end - start).total_seconds() / 60 for start, end in work_periods]) - break_time
    hours, minutes = divmod(int(total_minutes), 60)
    overtime = max(0, total_minutes - STANDARD_WORK_HOURS * 60)
    return hours, minutes, overtime

# Log work session in CSV
def log_to_csv(date, work_periods, break_time, total_hours, total_minutes, overtime, day_of_week, day_of_month):
    file_exists = os.path.exists(LOG_CSV)
    with open(LOG_CSV, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Date", "Day of Week", "Day of Month", "Work Periods", "Break Time (min)", "Total Hours", "Total Minutes", "Overtime (min)"])
        
        # Format work periods to human-readable strings
        formatted_work_periods = [f"{start.strftime('%H:%M')} - {end.strftime('%H:%M')}" for start, end in work_periods]
        
        writer.writerow([date, day_of_week, day_of_month, str(formatted_work_periods), break_time, total_hours, total_minutes, overtime])

# Main function to track work time
def work_time_tracker():
    print("\n🔹 Work Time Tracker (Supports Multiple Sessions per Day) 🔹")
    
    date = datetime.date.today().strftime("%Y-%m-%d")
    day_of_week = datetime.datetime.today().strftime('%A')  # Get the day of the week (e.g., Monday, Tuesday)
    day_of_month = datetime.datetime.today().day  # Get the day of the month (1, 2, ..., 31)
    work_periods = []

    while True:
        start_time_str = input("Enter start time (HH:MM or HH:MM AM/PM) [or 'done' to finish]: ").strip()
        if start_time_str.lower() == "done":
            break
        
        end_time_str = input("Enter end time (HH:MM or HH:MM AM/PM): ").strip()
        
        try:
            start_time = parse_time(start_time_str)
            end_time = parse_time(end_time_str)

            if end_time <= start_time:
                print("❌ Error: End time must be later than start time!\n")
                continue

            work_periods.append((start_time, end_time))
            print(f"✅ Work session from {start_time_str} to {end_time_str} recorded.\n")

        except ValueError:
            print("❌ Invalid time format! Please use HH:MM or HH:MM AM/PM.\n")

    break_time = int(input("Enter total break time in minutes (0 if none): ").strip())

    # Calculate total time worked
    total_hours, total_minutes, overtime = calculate_total_time(work_periods, break_time)

    print(f"\n🔹 Total Work Time: {total_hours} hours, {total_minutes} minutes")
    if overtime > 0:
        print(f"⚡ Overtime: {overtime} minutes")

    # Save data
    log_to_csv(date, work_periods, break_time, total_hours, total_minutes, overtime, day_of_week, day_of_month)

    work_log = load_work_log()
    work_log[date] = {"sessions": [f"{s.strftime('%H:%M')} - {e.strftime('%H:%M')}" for s, e in work_periods], 
                      "break_time": break_time, 
                      "total_hours": total_hours, 
                      "total_minutes": total_minutes, 
                      "overtime": overtime,
                      "day_of_week": day_of_week,
                      "day_of_month": day_of_month}

    save_work_log(work_log)
    print(f"📂 Work session logged in '{LOG_CSV}' and '{LOG_JSON}'.\n")

# Generate a weekly or monthly report
def generate_report():
    log_data = load_work_log()
    
    if not log_data:
        print("❌ No work sessions found!\n")
        return

    print("\n🔹 Report Options: 1 - Weekly, 2 - Monthly")
    option = input("Choose (1/2): ").strip()

    today = datetime.date.today()
    total_minutes = 0

    for date, details in log_data.items():
        session_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        
        if option == "1" and (today - session_date).days <= 7:
            total_minutes += (details["total_hours"] * 60) + details["total_minutes"]
        elif option == "2" and session_date.month == today.month:
            total_minutes += (details["total_hours"] * 60) + details["total_minutes"]

    hours, minutes = divmod(total_minutes, 60)
    print(f"\n📊 Total Work Time: {hours} hours, {minutes} minutes\n")

# Main menu
def main():
    while True:
        print("\n🔹 Work Time Tracker Menu 🔹")
        print("1️⃣ Log Work Session")
        print("2️⃣ Generate Weekly/Monthly Report")
        print("3️⃣ Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            work_time_tracker()
        elif choice == "2":
            generate_report()
        elif choice == "3":
            print("👋 Exiting Work Time Tracker. Have a productive day!\n")
            break
        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

""" 

How to Use?
1 Log Work Session - Enter start & end times, multiple sessions allowed
2 Automatic Overtime Calculation - Detects overtime beyond 8 hours
3 Break Time Handling - Enter total break minutes
4 Generate Reports - See total work time for the past week or month
5 Exit Program - Quit safely while preserving logs

"""