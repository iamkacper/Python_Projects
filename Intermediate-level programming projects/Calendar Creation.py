""" A script that generates a calendar for a specific month or year, allowing the user to view weekdays, working days, and holidays. """

import calendar

# Define public holidays (for Poland, can be modified for other countries)
HOLIDAYS = {
    "01-01": "New Year's Day",
    "05-01": "Labor Day",
    "05-03": "Constitution Day",
    "11-01": "All Saints' Day",
    "11-11": "Independence Day",
    "12-25": "Christmas Day",
    "12-26": "Second Christmas Day",
}

def print_calendar(year, month=None):
    """
    Generates and displays a calendar for the given year and month.
    If the month is not specified, it generates a full-year calendar.
    """
    if month:
        print(f"\nCalendar for {calendar.month_name[month]} {year}:\n")
        print_month_calendar(year, month)
    else:
        print(f"\nCalendar for the year {year}:\n")
        for m in range(1, 13):
            print_month_calendar(year, m)

def print_month_calendar(year, month):
    """
    Displays the calendar for a specific month, highlighting weekends and public holidays.
    """
    cal = calendar.monthcalendar(year, month)
    print(f"{calendar.month_name[month]} {year}")
    print("Mo  Tu  We  Th  Fr  Sa  Su")

    for week in cal:
        for day in week:
            if day == 0:
                print("    ", end="")  # Empty space for days outside the current month
            else:
                date_str = f"{month:02d}-{day:02d}"
                if date_str in HOLIDAYS:
                    print(f"{day:2d}*", end=" ")  # Mark holidays with "*"
                elif calendar.weekday(year, month, day) in [5, 6]:  
                    print(f"\033[91m{day:2d}\033[0m", end=" ")  # Color weekends in red
                else:
                    print(f"{day:2d} ", end=" ")
        print()  # New line for the next week

if __name__ == "__main__":
    year = int(input("Enter year: "))
    month_input = input("Enter month (1-12) or leave empty for full year: ")
    month = int(month_input) if month_input else None

    print_calendar(year, month)
