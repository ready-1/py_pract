#!../bin/python

"""009_guessing_game_one.py

A Python learning project from 
http://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

Generate a random number between 1 and 9 (including 1 and 9). Ask the user 
to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. (Hint: remember to use the user input lessons from the 
very first exercise)

Extras:

1. Keep the game going until the user types “exit”
2. Keep track of how many guesses the user has taken, and when the game ends, 
    print this out.

"""

import random

# define the boundaries
upper_bound = 100
lower_bound = 1
# generate a random number
rand_num = random.randint(lower_bound, upper_bound)
print(rand_num)
