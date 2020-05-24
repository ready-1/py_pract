#!../bin/python

"""015_reverse_word_order.py

This is a Python learning project from:
http://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

Write a program (using functions!) that asks the user for a long string 
containing multiple words. Print back to the user the same string, except 
with the words in backwards order. For example, say I type the string:

  My name is Michele

Then I would see the string:

  Michele is name My

shown back to me.

"""

# whoami?
print('Hello World! This is 015_reverse_word_order.py\n')

# condense the prompt into a function call for code formatting.
def get_inp():
    return input('Enter a string of words seperated by spaces: ')

# from the inside out:
# 1. get_inp() ask for a string of words
# 2. get_inp().splt() returns a list of words split on whitespace
# 3. reversed(get_inp().splt()) returns a reversed version of the list
# 4. " ".join(reversed(get_inp().splt())) puts it all back together.
# Neat.  Tidy.  All in one line. (Except for the prompt.)
print(f'The reversed string: {" ".join(reversed(get_inp().split()))}')



# breathing room
print()

