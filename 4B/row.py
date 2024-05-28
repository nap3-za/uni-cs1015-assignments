# Number sequence printer
# 10 March 2024

# Getting the starting number from the user
start_number = eval(input("Enter a number between -6 and 93:\n"))

# Check if it's within the range -6 and 93
if start_number > -6 and start_number < 93:
	# Print the initial number
	if start_number >= 0  and start_number <= 9:
		print(" ", start_number, sep="", end="")
	else:
		print(start_number, end="")

	# Loop for the next six numbers after start_number
	for number in range(start_number+1, start_number+7):
		# Add a leading whitespace
		if number >= 0 and number <= 9:
			print("  ", number, sep="", end="")
		else:
			print(" ", number, sep="", end="")

else:
	print("Invalid input! The value of 'n' should be between -6 and 93.")

