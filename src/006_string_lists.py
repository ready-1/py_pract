#!../bin/python

"""006_string_lists.py

Python learning project from
https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

Ask the user for a string and print out whether this string is a palindrome 
or not. (A palindrome is a string that reads the same forwards and backwards.)

"""

# init some vars
reversed_string = ''

# ask the user for a string
user_string = input('Enter a string: ')

# create a reversed string
for c in user_string:
    reversed_string = c + reversed_string

# compare the two strings

# display the results