# Sentence breaker
# 23 March 2024

# Get the sentence
sentence = input("Enter a sentence:\n")

# Lower the whole sentence and append a whitespace at the end
sentence = sentence.lower() + " "


# Print the first word
whitespace_position = sentence.find(" ")
print("The word list: ", sentence[:whitespace_position], sep="", end="")
sentence = sentence[whitespace_position+1:]
whitespace_position = sentence.find(" ")

# Iterate the spaces continously chopping the sentence and printing 
# all characters till the next space
while whitespace_position != -1:
	whitespace_position = sentence.find(" ")
	print(", " + sentence[:whitespace_position], sep="", end="")	
	sentence = sentence[whitespace_position+1:]
	whitespace_position = sentence.find(" ")

print(".", end="")