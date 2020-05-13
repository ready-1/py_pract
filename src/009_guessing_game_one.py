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

# I kind of went off the rails on this one, free-coding pretty much the 
# entire thing.  Not too much overall design, just a lot of fun.

import random

# define the boundaries
upper_bound = 9
lower_bound = 1
game_counter = 0 # how many games have been played
guess_counter = 0 # number of guesses for each round
guess_state = 'correct' # if this is 'correct' gen a new random num
rand_num = 0 # number to try to guess



play = True # this is the game state

def gen_random():
    # generate a random number
    return random.randint(lower_bound, upper_bound)

def check_guess(guess):
    global play
    try:
        if (int(guess) < rand_num):
            return 'too low'
        elif (int(guess) > rand_num):
            return 'too high'
        elif (int(guess) == rand_num):
            return 'correct'
    
    except:
        if (guess == 'exit'):
            play = False
            return 'exit'
        else:
            return '-1'

def new_game():
    global rand_num
    global game_counter
    global guess_counter
    rand_num = gen_random()
    game_counter += 1
    guess_counter = 0
    print('\nNew Game!')
    print(f'Enter "exit" to quit.\n')
    return

# start the first game
new_game()
while play:
    loop = True
    while (True):
        guess = input(f'Enter a guess between {lower_bound} and {upper_bound}: ')
        result = check_guess(guess)
        if (result != '-1'):
            break
        print('<< Invalid Input - Try Again >>')

    guess_counter += 1

    if (result == 'correct'):
        print(f'Tries: {guess_counter} - Your guess ({guess}) is {result}.')
        print('You Win!')
        print(f'Your stats: games played: {game_counter} guesses/game {guess_counter/game_counter}')
        new_game()
    elif (result == 'too high' or result == 'too low'):
        print(f'Tries: {guess_counter} - Your guess ({guess}) is {result}.')