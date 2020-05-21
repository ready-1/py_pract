#!../bin/python

"""010_list_overlap_comprehensions.py

Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements 
that are common between the lists (without duplicates). Make sure your 
program works on two lists of different sizes. Write this in one line of 
Python using at least one list comprehension. (Hint: Remember list 
comprehensions from Exercise 7).

The original formulation of this exercise said to write the solution using 
one line of Python, but a few readers pointed out that this was impossible 
to do without using sets that I had not yet discussed on the blog, so you can 
either choose to use the original directive and read about the set command in 
Python 3.3, or try to implement this on your own and use at least one list 
comprehension in the solution.

Extra:

Randomly generate two lists to test this

"""

# print('Hello World! This is 010_list_overlap_comprehensions.py')

import random


# Initial Spec
list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# use a list comprehension to find the common values
# then use set()to get the unique values
# then use list() to convert to a list for the correct output format
result = list(set([a for a in list_a for b in list_b if (a == b)]))

# show the initial lists
print(f'List A: {list_a}')
print(f'List B: {list_b}')

# show the common values
print(f'The common values are: {result}')

# Extra Credit
# parameters
max_length = 50 # the length of the lists
max_val = 10 # the maximum value to generate

# utility function to create random lists
# feed it a maximum length and maximum value and it spits out a list 
# of random values within the spec 
def make_list(length, val):
    new_list = []
    for i in range(0,random.randint(1,length)):
        new_list.append(random.randint(1, val))
    return new_list

# comparison code from above moved to a function
def compare_lists(list_a, list_b):
    return list(set([a for a in list_a for b in list_b if (a == b)]))

# create out two lists of random values and length
list_a = make_list(max_length, max_val)
list_b = make_list(max_length, max_val)

# display the results.
print('\nExtra Credit!\n')
print(f'List A: {list_a}')
print(f'List B: {list_b}')

# the actual list comparison happens inside the print statement since 
# there is no need to do anything else with the resulting list of common values
print(f'The common values are: {compare_lists(list_a, list_b)}\n')

