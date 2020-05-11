#!../bin/python

"""005_list_overlap.py

Python learning project from
http://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

Take two lists, say for example these two:

    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements 
that are common between the lists (without duplicates). Make sure your program
works on two lists of different sizes.

Extras:

1. Randomly generate two lists to test this
2. Write this in one line of Python

"""

# Primary exercise ========
# make a couple of lists
list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
results = []

# iterate over one list
for i in list_a:
    # check to see if the current list item is in the other list
    if (list_b.count(i) > 0):
    # if it is in the other list, then check if it is already in our results
        if (results.count(i) == 0):
            # if not in results, then add to results
            results.append(i)

# print the results
print(f'The lists overlap on the following items: {results}')

