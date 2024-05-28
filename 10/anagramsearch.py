# Anagram Finder
# 04 May 2024

print("***** Anagram Finder *****")


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


def check_anagrams(text, text_file):
    anagrams = []
    read_words = False
    
    for line in text_file:
        line = line.strip().lower()  # Standardize lettercase

        if read_words:  # Start line has been passed
            if len(line) == len(word) and line != text:  # Must be of same size and indifferent
                if is_anagram(text, line):  # Add to anagrams if it is one
                    anagrams.append(line)

        elif line == "start":  # Flag read_words
            read_words = True

    if len(anagrams) == 0:
        print(f"Sorry, anagrams of '{word}' could not be found.")
    else:
        print(anagrams)


try:
    lexicon = open("EnglishWords.txt", "r")
    word = input("Enter a word:\n").lower().strip()

    check_anagrams(word, lexicon)
    lexicon.close()
except Exception:
    print("Sorry, could not find file 'EnglishWords.txt'.")
