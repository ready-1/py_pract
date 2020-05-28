#!../bin/python

import random

"""018_cows_bulls.py

This is a Python learning project from:
http://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html

Create a program that will play the “cows and bulls” game with the user. 
The game works like this:

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. 
For every digit that the user guessed correctly in the correct place, they 
have a “cow”. For every digit the user guessed correctly in the wrong place 
is a “bull.” Every time the user makes a guess, tell them how many “cows” 
and “bulls” they have. Once the user guesses the correct number, the game 
is over. Keep track of the number of guesses the user makes throughout the 
game and tell the user at the end.

Say the number generated by the computer is 1038. An example interaction 
could look like this:

  Welcome to the Cows and Bulls Game! 
  Enter a number: 
  >>> 1234
  2 cows, 0 bulls
  >>> 1256
  1 cow, 1 bull

"""

print('Hello World! This is 018_cows_bulls.py\n')

guesses = 0

# generate a 4-digit integer
pig = ''
for i in range(0,4):
    pig += str(random.randint(0,9))

while True:
    cows = 0
    bulls = 0
    guesses += 1
    usr_str = input('Enter a four digit number: ')
    for i in range(0,4):
        if usr_str[i] == pig[i]:
            cows += 1
        else:
            bulls += 1
    print(f'guesses: {guesses}')
    if cows == 4:
        print(f'{cows} cows!  You win!!')
        break
    else:
        print(f'cows: {cows}  bulls: {bulls}\n')


