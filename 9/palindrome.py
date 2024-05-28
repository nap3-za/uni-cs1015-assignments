# Palindrome Tester
# 27 April 2024

def palindrome(text):
    text_size = len(text)

    if text_size <= 1: # Base case if size is 1 or 0
        return "Palindrome!"

    if text[0] == text[text_size-1]: # Check if the ends are the same
        return palindrome(text[1:text_size-1]) # Recursively chop the ends
    else:
        return "Not a palindrome!"

text = input("Enter a string:\n")
print(palindrome(text))
