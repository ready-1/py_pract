#!../bin/python

"""011_check_primality_functions.py

Ask the user for a number and determine whether the number is prime or not. 
(For those who have forgotten, a prime number is a number that has 
no divisors.). You can (and should!) use your answer to Exercise 4 to help 
you. Take this opportunity to practice using functions, described below.

"""

print('Hello World! This is 011_check_primality_functions.py')

import math

def is_prime(val):
    start = 2
    stop = math.floor(math.sqrt(val)) + 1
    for i in range(start, stop):
        if (val%i == 0):
            return False
    return True

# get a number from the user
val = int(input('\nEnter an integer greater than 1: '))

# check for primality
is_a_prime = is_prime(val)

# make the output string
result = f'Your value {val} is '
result += '' if is_a_prime else 'not '
result += 'prime.\n'

#display the results
print(result)




