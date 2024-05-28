# Perfect number checker
# Date: 29 February 2024


number = int(input("Enter a number:\n")) # Get the number from the user
summation = 0 # Initialize the summation of divisors to 0

print("The proper divisors of", number, "are:")
for i in range(1, number): # Loop through all numbers till the input number
	if number % i == 0: # Check if the counter is a perfect divisor
		summation += i # Increase the sum by the counter if the above holds
		print(i, end=" ") # Output the divisor

# Check if the number provided is a perfect number
# and output the result
if summation == number: 
	print("\n")
	print(number, "is a perfect number.")
else:
	print("\n")
	print(number, "is not a perfect number.")
