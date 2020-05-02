#!../bin/python

"""003_less_than_ten.py

Python learning project from
http://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements of the list that are 
less than 5.

Extras:

1. Instead of printing the elements one by one, make a new list that has all 
the elements less than 5 from this list in it and print out this new list.
2. Write this in one line of Python.
3. Ask the user for a number and return a list that contains only elements 
from the original list a that are smaller than that number given by the user.

"""

#the original list
list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Intial spec
#print all the elements less than 5
print('As individual items:')
for e in list_1:
    if e < 5:
        print(f'{e} is less than 5')

# Extra 1
# make a new empty list
list_2 = []
# loop through list_1 and add vals greateer than 5 to the new list
for e in list_1:
    if e < 5:
        list_2.append(e)
# print the result
print(f'The values less than 5: {list_2}')