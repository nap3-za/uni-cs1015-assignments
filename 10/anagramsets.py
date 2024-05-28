# Anagram Sets Generator
# 04 May 2024


print("***** Anagram Set Search *****")


lexicon_file = open("EnglishWords.txt", "r")
lexicon = lexicon_file.readlines()
lexicon_file.close()


def is_anagram(word_1, word_2):
	"""Checks if the two given words are anagrams & returns a boolean value"""

	if len(word_1) == 0 and len(word_2) == 0:
		return True

	letter = word_1[0]

	word_1 = word_1.replace(letter, "")
	word_2 = word_2.replace(letter, "")
	
	if len(word_1) == len(word_2): # Check length after letter replacement
		return is_anagram(word_1, word_2) # Repeat if equal

	return False


def check_anagrams(i, text):
	anagrams = []
	read_words = False
	
	# I is the index after "START", to save time
	while i < len(lexicon):
		line = lexicon[i].strip().lower()

		if len(line) == len(text) and line != text:  # Must be of same size and indifferent
			if is_anagram(text, line):  # Add to anagrams if it is one
				anagrams.append(line)
				lexicon[i] = " "  # Nullify the anagram from the lexicon

		i += 1

	if len(anagrams) == 0:
		return None
	else:
		return anagrams


def check_anagram_sets(word_size, output_file_name):
	output_file = open(output_file_name, "w")
	anagram_sets = []

	read_words = False
	start_index = 0
	i = 0

	while i < len(lexicon):

		word = lexicon[i].strip().lower()  # Standardize lettercase

		if read_words:
			if len(word) == word_size:
				
				# If it has anagrams add them to the set of anagrams
				# ordered
				word_anagrams = check_anagrams(start_index, word)
				if word_anagrams != None and len(word_anagrams) > 0:
					word_anagrams.append(word)
					word_anagrams.sort()
					anagram_sets.append(word_anagrams)

		elif word == "start":  # Flag read_words
			read_words = True
			start_index = i+1

		i += 1

	# If there are sets of anagrams add them to the output file
	# ordered
	if len(anagram_sets) > 0:
		anagram_sets.sort()
		for anagram in anagram_sets:
			print(anagram, file=output_file)

	output_file.close()

word_length = eval(input("Enter a word length:\n"))
print("Searching...")
output_file_name = input("Enter a file name:\n")
print("Writing results...")


check_anagram_sets(word_length, output_file_name)


