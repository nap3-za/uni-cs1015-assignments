# GPS Coordinate Checker
# Date: 29 February 2024

# Get the input
latitude_degrees = int(input("Enter first number:\n"))
latitude_minutes = int(input("Enter second number:\n"))
latitude_seconds = int(input("Enter third number:\n"))
longitude_degrees = int(input("Enter fourth number:\n"))
longitude_minutes = int(input("Enter fifth number:\n"))
longitude_seconds = int(input("Enter sixth number:\n"))

# Initialize a flag for the validity of the coordinates
is_gp_coordinates = False
# Evaluate the input
if latitude_degrees in range(-90, 91) and longitude_degrees in range(-180, 181):
	if latitude_minutes in range(0, 60) and longitude_minutes in range(0, 60):
		if latitude_seconds in range(0, 60) and longitude_seconds in range(0, 60):
			is_gp_coordinates = True

if is_gp_coordinates:
	print("WOW! Looks like geographic coordinates!")
else:
	print("Hmmm ... looks like 6 random numbers.")

