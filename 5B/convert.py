# 24H time to 12H time format
# 23 March 2024

# Get 24h the time
time_24 = input("Enter the date and time (yyyy-mm-dd hh:mm):\n")



# Check if the time is past 12 or not and
# append the appropriate conversions and comments 
if int(time_24[-5:-3]) > 12:
	time_12 = str(int(time_24[-5:-3])-12) + time_24[-3:] + " pm "
elif int(time_24[-5:-3]) == 12:
	time_12 = "12" + time_24[-3:] + " pm "
elif int(time_24[-5:-3]) == 0:
	time_12 = "12" + time_24[-3:] + " am "
else:
	time_12 = str(int(time_24[-5:-3])) + time_24[-3:] + " am "

# Extract the day as a string and append the integer
day = time_24[8:10]
time_12 += "on the " + str(int(day))

# Add the prefix according to the digit of the day 
prefix = "th"
if day[0] != "1" and day[1] == "1":
	prefix = "st"
elif day[1] == "2":
	prefix = "nd"
elif day[1] == "3":
	prefix = "rd"

time_12 += prefix + " of "

# Check the month and append the word form 
month_int = int(time_24[5:7])
month_str = ""
if month_int == 1:
	month_str = "January "
elif month_int == 2:
	month_str = "February "
elif month_int == 3:
	month_str = "March "
elif month_int == 4:
	month_str = "April "
elif month_int == 5:
	month_str = "May "
elif month_int == 6:
	month_str = "June "
elif month_int == 7:
	month_str = "July "
elif month_int == 8:
	month_str = "August "
elif month_int == 9:
	month_str = "September "
elif month_int == 10:
	month_str = "October "
elif month_int == 11:
	month_str = "November "
else:
	month_str = "December "

# Append the last two digits of the year
time_12 += month_str + "'" + str(time_24[2:4])

# Output the result
print(time_12)
