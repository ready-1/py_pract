#!../bin/python

"""008_rps.py

This is a Python learning project from 
https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays 
(using input), compare them, print out a message of congratulations to the 
winner, and ask if the players want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock

"""

print('Hello World! This is 008_rps.py')

player_1 = ''
player_2 = ''

def score_game(player_1, player_2):
    winner = 'Player 2 wins!'
    # rock beats scissors
    if player_1 == 'r' and player_2 == 's':
        winner == 'Player 1 wins!'
    # scissors beats paper
    if player_1 == 's' and player_2 =='p':
        winner == 'Player 1 wins!'
    # paper beats rock
    if player_1 == 'p' and player_2 == 'r':
        winner == 'Player 1 wins!'
    # its a tie!
    if player_1 == player_2:
        winner = 'It\'s a tie!'
    return winner

def get_input(player):
    #prompt player for input
    print(' r for rock\n p for paper\n s for scissors')
    return input(f'Player {player} - Enter your play: ')

while True:
    print('=' * 40)
    # instructions to quit
    print(f'<Ctrl-c> to exit\n')
    # get user input
    player_1 = get_input(1)
    player_2 = get_input(2)
    # print the result
    print(f'\n{">" * 10} {score_game(player_1, player_2)} {"<" * 10}')
    print(f'\nPress <Enter> for another game...')
