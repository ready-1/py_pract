#!../bin/python

"""013_fibonacci.py

http://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html

Write a program that asks the user how many Fibonnaci numbers to generate 
and then generates them. Take this opportunity to think about how you can 
use functions. Make sure to ask the user to enter the number of numbers in 
the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of 
numbers where the next number in the sequence is the sum of the previous 
two numbers in the sequence. 

The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

"""

print('Hello World! This is 013_fibonacci.py\n')

# get input
length = int(input("Enter a length for the Fibonacci series: "))

# iterative solution
series = []

for i in range(length):
    if len(series) < 2:
        series.append(1)
    else:
        n1 = series[-1] # get the last value
        n2 = series[-2] # get the next to last value
        series.append(n1 + n2) # append the sum of the last two vlaues to the series

print(f'Fibonacci series created iteratiely: {series}')

# recursive solution
series = []

# the recursive function
def fib(n, a = 0, b = 1):
    # get access to the series list
    global series
    # take care of the first call
    if a == 0:
        series.append(1)
    #create the next fibonacci number
    c = a + b
    # add it to the series
    series.append(c)
    # checl to see if the series is complete
    # if it is, stop the recursion
    if len(series) == length:
        return
    # if it's not, calculate the next number via recursion
    else:
        return fib(n - 1, b, c )

# call the recursive function
fib(length)
# display the results
print(f'Fibonacci series created recursively: {series}')
print()


