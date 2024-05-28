# Calendar printer
# 03 April 2024


import math


def day_of_week(day, month, year):
    # Your code here

    if month == 1 or month == 2:
        month += + 12
        year -= 1

    raw_day_of_week = (day + math.floor((13*(month+1))/5) + year + math.floor(year/4) - math.floor(year/100) + math.floor(year/400)) % 7
    day_of_week = ((raw_day_of_week + 5) % 7) + 1

    return day_of_week


def is_leap(year):
    # Your code here
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    return False



def month_num(month_name):
    # Your code here
    month_name = month_name.lower()

    if month_name == "january":
        return 1
    elif month_name == "february":
        return 2
    elif month_name == "march":
        return 3
    elif month_name == "april":
        return 4
    elif month_name == "may":
        return 5
    elif month_name == "june":
        return 6
    elif month_name == "july":
        return 7
    elif month_name == "august":
        return 8
    elif month_name == "september":
        return 9
    elif month_name == "october":
        return 10
    elif month_name == "november":
        return 11
    elif month_name == "december":
        return 12

def num_days_in(month_num, year):
    # Your code here
    if (month_num <= 7 and month_num % 2 == 1) or (month_num >= 8 and month_num % 2 == 0):
        return 31
    elif month_num != 2:
        return 30
    else:
        if is_leap(year):
            return 29
        else:
            return 28


def num_weeks(month_num, year):
    # Your code here
    day_of_first_week = day_of_week(1, month_num, year)

    if month_num == 2 and not is_leap(year) and day_of_first_week == 1:
        return 4
    else:
        number_of_days = num_days_in(month_num, year)

        # Special cases when there are 6 weeks
        if ((number_of_days >= 30) and (day_of_first_week == 7)) or ((number_of_days == 31) and (day_of_first_week == 6)):
            return 6
        return 5

def format_day(day):
    """Handles the trailing space of single digit days"""
    if day <= 9:
        return " {}".format(day)
    else:
        return str(day)

def week(week_num, start_day, days_in_month):
    # Your code here
    week = ""

    if week_num == 1: # Handle the trailling spacing for first weeks
        if start_day != 1:
            week = "   " + ("   " * (start_day-2))
        week += " 1"
       
        for i in range(2, ((7-start_day)+2)):
            week += "  {}".format(i)
    else:
        # Determine the first day on the Nth week and append it to the output string
        week_start_day = (8-start_day) + (7*(week_num-2)) + 1
        week = str(format_day(week_start_day))


        day_of_week = week_start_day+1
        # Iterate over the remaining days and append them to the output string
        while (day_of_week <= week_start_day+6) and (day_of_week <= days_in_month):
            week += " {}".format(format_day(day_of_week))
            day_of_week += 1

    return week


def get_calendar(month, year):
    """Returns a formatted multiline string representation of the calendar"""

    month_number = month_num(month)
    days_in_month = num_days_in(month_number, year)
    start_day = day_of_week(1, month_number, year)

    
    calendar = month.lower().title() + "\nMo Tu We Th Fr Sa Su"
    # Iterate for n number of weeks appending each week to the output
    for week_number in range(1, num_weeks(month_number, year)+1):
        calendar += "\n" + week(week_number, start_day, days_in_month)

    return calendar


def main():
    # Your code here
    month = input("Enter month:\n")
    year = int(input("Enter year:\n"))

    print(get_calendar(month, year))


if __name__=='__main__':
    main()