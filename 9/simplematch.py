# Simple match
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

    