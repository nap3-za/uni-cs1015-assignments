# Animal type identifier quiz
# Date: 29 February 2024


print("Welcome to the Biology Expert")
print("-----------------------------")
print("Answer the following questions by selecting from among the options.")

# Get the skeleton type and initialize the type of animal to nothing.
skeleton_type = input("The skeleton is (internal/external)?\n")
animal_type = ""

# Only test for cases which require futher information and proceed to
# Ask for that information
if skeleton_type == "internal":
	fertelisation_location = input("The fertilisation of eggs occurs (within the body/outside the body)?\n")
	if fertelisation_location == "within the body":
		offspring_production = input("Young are produced by (waterproof eggs/live birth)?\n")
		if offspring_production == "waterproof eggs":
			animal_outer_cover = input("The skin is covered by (scales/feathers)?\n")
			if animal_outer_cover == "scales":
				animal_type = "Reptile"

			# No need to test for the other case as no error in input is expected thus 
			# an else case is suffiient
			else:
				animal_type = "Bird"
		else:
			animal_type = "Mammal"
	else:
		habitat = input("It lives (in water/near water)?\n")
		if habitat == "in water":
			animal_type = "Fish"
		else:
			animal_type = "Amphibian"
else:
	animal_type = "Arthropod"

print("Type of animal:", animal_type)
