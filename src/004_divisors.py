#!../bin/python

"""004_divisors.py

Python learning project from
http://www.practicepython.org/exercise/2014/02/26/04-divisors.html

Create a program that asks the user for a number and then prints out a list 
of all the divisors of that number. (If you don’t know what a divisor is, it 
is a number that divides evenly into another number. For example, 13 is a 
divisor of 26 because 26 / 13 has no remainder.)

"""

# get a number from the user
num = int(input("\nEnter a number: "))

results = [] # the list of divisors

# loop over the range of numbers from 1 to num + 1
# we don't want to divide by zero and we want to account
# for num/num = 1
for i in range(1, num + 1):
    #test if i is a divisor
    if (num % i == 0):
        # if yes, then add it to the list
        results.append(i)


print(f'\nYou entered {num} and it\'s dividors are {results}.\n\n')
