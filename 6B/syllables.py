# Given a word, calculate how many syllables it contains.
# 03 April 2024

def is_vowel(letter):
    """Check if letter is a vowel and return True or False"""
    if letter.lower() in "aeiouy":
        return True
    else:
        return False

def next_vowel(word, index):
    """Return the next vowel after index in word"""
    vowels = "aeiouy"

    # Inspect every letter for a vowel in word starting from index
    for letter_position in range(index, len(word)):
        if word[letter_position].lower() in vowels:
            return letter_position

    return -1

def count_syllables(word):
    count = 0
    # Your code here.
    if len(word) == 1:
        count = 1 # The min syllable count is 1 independent of the letter
    else:
        vowel_position = next_vowel(word, 0)

        while vowel_position != -1: # While there are vowels
            next_vowel_position = next_vowel(word, vowel_position+1)

            # If the next vowel is not the next letter increment count
            if next_vowel_position - vowel_position != 1: 
                count += 1

            # Shift the vowel position
            vowel_position = next_vowel_position

        # If 'e' is the last letter without a trailing vowel and NOT the only vowel reduce count
        if (word[len(word)-1] == "e" and not word[len(word)-2] in "aeiouy") and count != 1:
            count -= 1

    return count

def prefix(count):
    """Return the appropriate prefix according to the count"""
    if count > 1:
        return "s"
    return ""

def main():
    word = input('Enter a word (or \'q\' to quit):\n')
    # Your code here.

    while word != "q":
        syllable_count = count_syllables(word)
        # Format the output
        print("The word '{}' has {} syllable{}.".format(word, syllable_count, prefix(syllable_count)) + "\n")

        # Prompt the user
        word = input('Enter a word (or \'q\' to quit):\n')

# Do not modify.
if __name__ == '__main__':
    main()

