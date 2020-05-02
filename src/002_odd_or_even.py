#!../bin/python


"""002_odd_or_even.py

Python learning project from
http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

Ask the user for a number. Depending on whether the number is even or odd, 
print out an appropriate message to the user. Hint: how does an even / odd 
number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one 
number to divide by (check). If check divides evenly into num, tell that to 
the user. If not, print a different appropriate message.
"""

def is_even(num):
    # determine if odd or even
    return 'even' if (num % 2 == 0) else 'odd'

def is_divisible(num1, num2):
    #check if the numbver is divisible by 4
    return '' if (num1 % num2 == 0) else 'not '

def get_a_number():
    # ask the user for a number
    return int(input('Enter a number: '))

num = get_a_number()

# display the result
print(f'{num} is an {is_even(num)} number and is {is_divisible(num, 4)}divisible by 4.')

# ask for two numbers
num1 = get_a_number()
num2 = get_a_number()

# display result
print(f'{num1} is {is_divisible(num1, num2)}divisble by {num2}.')
