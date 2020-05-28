#!../bin/python

"""019_edabit_algo1_recursion_1.py

This is a Python learning project from:
https://edabit.com/challenge/x6McEkHer8A3Hke2q

Algorithms I: Introduction to Recursion
Welcome to the beginning of this collection on Computer Science Algorithms. 
Admittedly there are other challenges on Edabit that deal with recursion and 
algorithmic processes, but these particular challenges are designed to give 
examples and to educate users on the topics being covered.

"""

print('Hello World! This is 019_edabit_algo1_recursion_1.py\n')

# challenge 1
# Factorial
def factorial(num):
    # set a target for the base case
    targetNumber = 0
    # test for the base case
    if (num == targetNumber):
        # if we are done, return 1 so that the last operation in the 
        # recursion will be num = 1 * 1
        return 1
    else:
        # do the recursion
        return num * factorial(num-1)

# get an number from the user
n = int(input('Enter an integer to factorialize: '))
# show the factorial of n
print(f'challenge 1 - factorial of {n}: {factorial(n)}\n')

# challenge 2 


