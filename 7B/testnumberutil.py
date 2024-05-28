# Number to Word program tester
# 07 April 2024

"""
>>> import numberutil
>>> numberutil.aswords(0)
'zero'
>>> numberutil.aswords(15)
'fifteen'
>>> numberutil.aswords(27)
'twenty seven'
>>> numberutil.aswords(50)
'fifty'
>>> numberutil.aswords(300)
'three hundred'
>>> numberutil.aswords(115)
'one hundred and fifteen'
>>> numberutil.aswords(127)
'one hundred and twenty seven'
>>> numberutil.aswords(150)
'one hundred and fifty'

"""
import doctest
doctest.testmod(verbose=True)