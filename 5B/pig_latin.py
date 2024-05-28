# English to Pig-latin
# 23 March 2024


# Get the normal text
english_text = input("Enter a sentence:\n")

# Lower the whole english_text and append a whitespace at the end
english_text = english_text.lower() + " "

pig_latin_sentence = "" # Initialize the output string
whitespace_position = 0 # Initialize the whitespace position

# Iterate the spaces continously chopping the english_text
while whitespace_position != -1:
	whitespace_position = english_text.find(" ")
	word = english_text[:whitespace_position]

	# Convert the current word to a pig latin word
	if word[0] in "aeiou":
		pig_latin_sentence += " " + word + "way"
	else:
		vowel_index = 0
		for i in range(len(word)): # Try to find a vowel
			if word[i] in "aeiou":
				vowel_index = i
				break

		# Format the word and add it to the output string
		if vowel_index > 0: # Vowel cannot be in index 0
			pig_latin_sentence += " " + word[vowel_index:] + "a" + word[:vowel_index] + "ay"
		else:
			pig_latin_sentence += " " + word[::-1] + "ay"

	english_text = english_text[whitespace_position+1:]
	whitespace_position = english_text.find(" ")

print(pig_latin_sentence[1:], end="") # Output the result