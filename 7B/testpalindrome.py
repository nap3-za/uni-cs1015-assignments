# Palindrome program tester
# 07 April 2024

"""
>>> import palindrome
>>> palindrome.is_palindrome('')
True
>>> palindrome.is_palindrome('h')
True
>>> palindrome.is_palindrome('Am')
False
>>> palindrome.is_palindrome('AA')
True
>>> palindrome.is_palindrome('AmoA') 
False

"""
import doctest
doctest.testmod(verbose=True)