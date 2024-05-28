# Reference formatter
# 23 March 2024

# Get the unformatted reference from the user
raw_reference = input("Enter the reference:\n")

# Slice the reference till the first character after
# the closed bracket, lower and title it.
reference = raw_reference[0:raw_reference.find(")")+3].lower().title()

# Chop the original string to exclude the first coma
raw_reference = raw_reference[len(reference):]

# Lower the portion of the original after the first coma
reference += raw_reference[:raw_reference.find(",")].lower()
# Append the rest of the reference
reference += raw_reference[raw_reference.find(","):]

# Output the result
print(f"Reformatted reference:\n{reference}")
