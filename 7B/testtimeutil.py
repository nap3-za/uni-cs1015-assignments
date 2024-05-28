# Time-text Checker program tester
# 07 April 2024

"""
>>> import timeutil
>>> timeutil.validate(':124 p.m.')
False
>>> timeutil.validate('012:40 p.m.')
False
>>> timeutil.validate('07:40 p.m.')
False
>>> timeutil.validate('5:40 p.p.')
False
>>> timeutil.validate('1:310 p.m.')
False
>>> timeutil.validate('5:40 p.m.')
True

"""
import doctest
doctest.testmod(verbose=True)