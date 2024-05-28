# Palindromic Primes
# 27 April 2024

import sys
sys.setrecursionlimit (30000)


def is_prime(counter, number):
	if counter > round(number/2) or number <= 3: # If counter is above midpoint
		return True
	elif number % counter == 0: # If at any point number is divisible by counter, terminate
		return False
	else:
		return is_prime(counter+1, number)


def is_palindrome(text):
    text_size = len(text)

    if text_size <= 1: # Base case if size is 1 or 0
        return True

    if text[0] == text[text_size-1]: # Check if the ends are the same
        return is_palindrome(text[1:text_size-1]) # Recursively chop the ends
    else:
        return False


def palindromic_primes(counter, end):
	if counter > end: # If the counter exceed the end terminate
		return

	# Check if the current number is a palindrome and a prime
	elif is_palindrome(str(counter)) and is_prime(2, counter):
		print("\n", counter, sep="", end="")

	palindromic_primes(counter+1, end) # Increment the counter till end+1 to trigger base case
	return


# Get input from the user
start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:", end="")
palindromic_primes(start, end) # Invoke the 'recursive' while loop


