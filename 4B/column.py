# 7th Number Printer
# 10 March 2024

# Getting the starting number from the user
start_number = eval(input("Enter a number between -6 and 2:\n"))


# Check if it's within the range -6 and 2
if start_number > -6 and start_number < 2:
	for number in range(start_number, start_number+42, 7):
		if number >= 0 and number <= 9:
			print(" " + str(number))
		else:
			print(number)
else:
	print("Invalid input! The value of 'n' should be between -6 and 2.")
