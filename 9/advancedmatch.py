# Advanced match
# 27 April 2024

def match(pattern, word):
    pattern_size = len(pattern)
    word_size = len(word)
    
    # '' & ''
    if pattern_size == 0 and word_size == 0: 
        return True
    # '' & '*' or '*' & ''
    elif (pattern_size == 0 and word_size > 0) or (word_size == 0 and pattern_size > 0):
        return False
    
    # ? Wildcard
    elif word[0] == pattern[0] or pattern[0] == "?":
        return match(pattern[1:], word[1:])

    # '*' Wild card special cases
    elif pattern[0] == "*":
        if pattern_size == 1: # The rest of the word matches if * is at the end of the pattern
            return True

        next_position = word.find(pattern[1])

        if next_position >= 0: # If the letter after * is in word, recurse
            return match(pattern[1:], word[next_position:])
        elif next_position == -1 and word_size > 1: # Else don't continue
            return False
        