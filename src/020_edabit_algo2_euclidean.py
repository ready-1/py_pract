#!../bin/python

"""020_edabit_algo2_euclidean.py

This is a Python learning project from:
https://edabit.com/challenge/2SPQuzZTskcBpXpv4

Algorithms II: The Euclidean Algorithm
Welcome to part two of the collection for Computer Science Algorithms. This 
challenge will deal further with writing recursive functions by covering the 
Euclidean Algorithm. The "Euclidean Algorithm" is a method for finding the 
greatest common divisor (GCD) of two numbers. It was originally described 
by the Greek mathematician Euclid.

"""

print('Hello World! This is 020_edabit_algo2_euclidean.py\n')


def euclidean(a, b):
    # Ensure that "a" >= "b". If "a" < "b", swap them.
    if (a < b):
        a, b = b, a
    # Find the remainder. Divide "a" by "b" and set "r" as the remainder.
    r = a%b
    # Is "r" zero? If so terminate the function and return "b" (the second number).
    if r == 0:
        return b
    # Set "a" = "b" and "b" = "r" and start the algorithm over again.
    return euclidean(b, r)
    

# get two numbers
n1 = int(input('Enter a positive integer (n1): '))
n2 = int(input('Enter a positive integer (n2): '))

# call the recursive function
gcd = euclidean(n1, n2)
# display the results
print(f'The Greatest Common Divisor of {n1} & {n2} is {gcd}\n')

