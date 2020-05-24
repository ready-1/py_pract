#!../bin/python

"""014_list_remove_duplicates.py

This is a Python learning project from:
http://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html

Write a program (function!) that takes a list and returns a new list that 
contains all the elements of the first list minus all the duplicates.

Extras:

    1. Write two different functions to do this - one using a loop and 
    constructing a list, and another using sets.

    2. Go back and do Exercise 5 using sets, and write the solution for 
    that in a different function.


"""

print('Hello World! This is 014_list_remove_duplicates.py\n')

# ask the user for a list of values and split it into a list.
def get_user_list():
    raw_vals = input('Enter a series of values separated by spaces: ')
    return raw_vals.split()

# use a for loop to find the duplicates
def de_duplicator(raw_list):
    result = []
    for i in raw_list:
        if not i in result:
            result.append(i)
    return result



# using a for loop
print('Remove duplicates using a for loop:')
print(de_duplicator(get_user_list()))




