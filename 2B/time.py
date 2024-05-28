# Time validity checker
# Date: 22 February 2024

hours = int(input("Enter the hours:\n"))
minutes = int(input("Enter the minutes:\n"))
seconds = int(input("Enter the seconds:\n"))

if hours >= 0 and hours <= 23:
	if minutes >= 0 and minutes <= 59:
		if seconds >= 0 and seconds <= 59:
			print("Your time is valid.")
		
		else:
			print("Your time is invalid.")
	else:
		print("Your time is invalid.")
else:
	print("Your time is invalid.")

