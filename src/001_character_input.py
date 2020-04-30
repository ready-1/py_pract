#!../bin/python

"""001_character_input.py

Python learning project from 
http://www.practicepython.org/exercise/2014/01/29/01-character-input.html

Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that 
they will turn 100 years old.

Extras:

1. Add on to the previous program by asking the user for another number 
and printing out that many copies of the previous message. (Hint: order
of operations exists in Python)
2. Print out that many copies of the previous message on separate lines. 
(Hint: the string "\n is the same as pressing the ENTER button)
"""
import datetime as dt


# Initial project spec ===============
# Ask the user for their name
name = input('Enter your name: ')
# Ask the user for their age
age = input('Enter your age: ')
# calculate the year they will turn 100 years old

# print the message
print(f'Your name is {name} and you are {age} years old.')