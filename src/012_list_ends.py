#!../bin/python

"""012_list_ends.py


http://www.practicepython.org/exercise/2014/04/25/12-list-ends.html

Write a program that takes a list of numbers (for example, 
a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last 
elements of the given list. For practice, write this code inside a function.

"""

print('Hello World! This is 012_list_ends.py\n')

# our list of values
list_a = [5, 10, 15, 20, 25]
print(f'Our original list is {list_a}')
# a new list containing the first and last items from list_a
list_b = []



# using index values
# get the ffirst item
list_b.append(list_a[0])
#get the last item
list_b.append(list_a[-1])
# display the results
print(f'Using index values, the first and last values are {list_b}')

print('Done.')



