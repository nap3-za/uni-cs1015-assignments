# 6x7 Grid Printer
# 10 March 2024

# Getting the starting number from the user
start_number = eval(input("Enter a number between -6 and 2:\n"))

# Check if it's within the range -6 and 2
if start_number > -6 and start_number < 2:
	number = start_number # A tracker for the current number

	for row in range(6):
		# Print the initial number without padding for the current row
		if number >= 0 and number <= 9:
			print(" " + str(number), end="")
		else:
			print(number, end="")

		# Print the rest of the numbers for the current row
		# incrementing by 1 
		for column in range(6):
			number += 1
			if number >= 0 and number <= 9:
				print("  " + str(number), end="")
			else:
				print(" " + str(number), end="")

		print() # Terminate the current row
		number += 1 # Increment the current number for the next row
		
else:
	print("Invalid input! The value of 'n' should be between -6 and 2.")
