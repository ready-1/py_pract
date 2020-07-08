"""
Password Cracking Demonstration

Author: Robert King

Date Revised: 02 Decmeber 2019

Attributions:
    Portions of the brute_force() function were found at
        https://stackoverflow.com/a/40269815
    The dictionary file is found at
        https://raw.githubusercontent.com/danielmiessler/SecLists/master/
            Passwords/xato-net-10-million-passwords-1000000.txt

This application demonstrates two approaches to cracking passwords:
    Brute Force - interating over every possible combination of characters
        until a solution is found.
    Dictionary - using a list of common passwords to find a match.

It also includes an automated brute force cracking routine for data generation.
The auto_crack() function takes a list of target password specificatoins and sends them
through the guess_password() function then records the results to a file for
later analysis.

Runtime Environment:
    Python 3.7.3

Dependencies:
    Python 3.7.3 modules:
        string
        itertools
        time
        datetime
    External Libraries:
        - None -
License
=============================================================================
pwd_cracker.py - A brute force and dictionary attack demonstration project.
Copyright (C) 2019  Abigail King & Robert King

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
=============================================================================
"""

import string, itertools, time
from datetime import datetime

# Dictionary file
file_name = "xato-net-10-million-passwords-1000000.txt"

dt = datetime # create the datetime object for timing

pool = "" # characterset to be used in brute force

# character sets to add to pool
lc = string.ascii_lowercase # a-z
uc = string.ascii_uppercase # A-Z
nums = string.digits # 0-9
punc = "!#$%&()*+-./:;<=>?@[]^_`{|}~" # no quotes

def make_test_set():
    """ Create a test set for auto_crack()

    Keyword Arguments:
    ------------------
    - None -
    Return:
    ------------------
    ts - a list of pwd/char_set pairs

    1. Append items onto ts

    """

    # create the pools
    luc = lc + uc
    lun = lc + uc + nums
    lunp = lc + uc + nums + punc
    lc_short = lc[0:-1] # missing last character of the original pool
    luc_short = luc[0:-1] # missing last character of the original pool
    lun_short = lun[0:-1] # missing last character of the original pool
    lunp_short = lunp[0:-1] # missing last character of the original pool

    # create the target list
    ts = []
    ts.append([4, lc_short])
    ts.append([4, lc])
    ts.append([4, luc_short])
    ts.append([4, luc])
    ts.append([4, lun_short])
    ts.append([4, lun])
    ts.append([4, lunp_short])
    ts.append([4, lunp])

    return ts

def auto_crack():
    """ Automated Brute Force Attack with data recording

    This function records its results to a file named "auto-results.csv".

    Keyword Arguments:
    ------------------
    - None -
    Return:
    ------------------
    - None -

    1. read an item from the list
    2. get target_length
    3. crack the password
    4. record results to a file
        - target
        - target_length
        - attempts required to crack
        - pool
        - start_time
        - end_time
        - elapsed_time
    """

    file_name = "auto-results.csv"

    # insert header info file
    csv = 'Target,Target Length,Attempts,Pool,Start Time,'
    csv += 'End Time,Elapsed Time, Pool Length\n'
    f = open(file_name, 'w')
    f.writelines(csv)
    f.close()

    # create something to test
    test_set = make_test_set()

    # loop through the list of targets
    for t in test_set:
        for i in range(1,t[0] + 1):
            # pause for clock seperation
            time.sleep(1)
            pool = t[1]
            target = pool[-1] * i

            # crack the password
            cracked = guess_password(target, pool)
            # return [guess, attempts, pool, start_time, end_time]

            elapsed_time = cracked[4] - cracked[3]
            elapsed = str(elapsed_time.seconds) + "." + str(elapsed_time.microseconds)

            # csv = '\"'
            # csv += cracked[0] + '\", ' # target
            # csv += str(len(cracked[0])) + ', ' # target length
            # csv += str(cracked[1]) + ', \"' # attempts
            # csv += str(cracked[2]) + '\", \"' # pool
            # csv += str(cracked[3]) + '\", \"' # start_time
            # csv += str(cracked[4]) + '\", \"' # end_time
            # csv += str(elapsed) + '\"' # elapsed_time
            # csv += '\n'

            csv = ""
            csv += cracked[0] + ',' # target
            csv += str(len(cracked[0])) + ',' # target length
            csv += str(cracked[1]) + ',' # attempts
            csv += str(cracked[2]) + ',' # pool
            csv += str(cracked[3]) + ',' # start_time
            csv += str(cracked[4]) + ',' # end_time
            csv += str(elapsed) + ','# elapsed_time
            csv += str(len(cracked[2])) # pool length
            csv += '\n'


            print(csv)
            # record the data
            f = open(file_name, 'a')
            f.writelines(csv)
            f.close()

    print("\nFinished with auto_crack()\n\n")


def dictionary(): # dictionary attack
    """ Dictionary Attack

    Keyword Arguments:
    ------------------
    - None -
    Return:
    ------------------
    - None -

    1. ask for a password
    2. initialize the guess counter
    3. open the dictionary file
    4. read each line of the file and compare it to the password
    5. if a match is found, stop guessing and tell the user
    6. if no match is found, close the file and tell the user
    """

    pwd = input("Enter a password to check: ")
    i = 0 # guess counter
    with open(file_name) as f:
        for l in f:
            guess = str.strip(l, '\n')
            i += 1
            if guess == pwd:
                print("\nYour password is " + guess)
                print("It was found in " + str(i) + " tries.")
                print("You should choose a better password.\n")
                f.close()
                return
    print("\nYour password was not found in the Dictionary.")
    print("I tried " + str(i) + " different passwords.\n")
    return

def add_to_pool(prompt_string, char_set, p):
    """ Add a set of characters to the pool variable

    Keyword Arguments:
    ------------------
    prompt_string - characters to insert into the prompt for each
        character set
    char_set - the character set variable to append to the Pool
    p - the pool to append to

    Return:
    ------------------
    - None -

    1. prompt the user to add the character char_set
    2. if yes to add:
    - concatenate the pool and the char_set
    - return the pool
    if no to add, return the pool with no additions
    """

    while True:
        answer = input("Does your password include " + prompt_string + "? [Y/n]")
        if str.lower(answer) == "y" or answer == "":
            p += char_set
            # probe(p, "pool")
            return p
        elif str.lower(answer) == "n":
            return p

def guess_password(target, pool):
    """ Brute force cracking algorithm

    Keyword Arguments:
    ------------------
    target - the password to cracked
    pool - the character set to use

    Returns:
    ------------------
    guess - the correct guess
    attempts - number of attempts required to  match
    pool - the character set used to crack
    start_time - time of first guess
    end_time - time of last guess

    1. initialize the attempts counter to 0
    2. record the start time
    3. set target_length to the length of the password to crack
    4. begin iterating through the guesses
    - increment the attempt counter
    - create the new guess
    - test if match
        if match, then record end_time and return results
    """

    attempts = 0
    start_time = dt.now()
    target_length = len(target)
    for guess in itertools.product(pool, repeat=target_length):
        guess = ''.join(guess)
        attempts += 1
        if guess == target:
            end_time = dt.now()
            return [guess, attempts, pool, start_time, end_time]

def brute_force():
    """ Brute force password cracker algorithm

    Keyword Arguments:
    ------------------
    - None -

    Return:
    ------------------
    - None -

    1. initialize the pool variable to an empty string
    2. prompt for password to crack
    3. create the character set to use
    4. call guess_password() and record results in cracked
    5. calculate elapsed_time
    6. display results
    """

    pool = ""
    #ask for password
    pwd = input("Enter password here: ")
    print("")
    #ask for complexity of password (number of lowercase, uppercase, digits, and punctuation)
    pool = add_to_pool("lowercase ASCII", lc, pool)
    pool = add_to_pool("uppercase ASCII", uc, pool)
    pool = add_to_pool("numbers", nums, pool)
    pool = add_to_pool("special characters", punc, pool)
    print("")
    #brute force part
    cracked = guess_password(pwd, pool)
    elapsed_time = cracked[4] - cracked[3]
    print("Password is: " + cracked[0])
    print("Attempts required: " + str(cracked[1]))
    print("Cracked in: " + str(elapsed_time))
    print("Charcter Pool: " + cracked[2])

def main():
    """ Main function for the password cracker application

    Keyword Arguments:
    ------------------
    - None -

    Return:
    ------------------
    System exit code (0 on normal exit)

    1. Start the main loop
    2. Prompt for user choice
    - "d" - call dictionary()
    - "b" - call brute_force()
    - "a" - automated cracking for data analysis <unprompted>
    - "q" - quit with exit code 0 (normal)
    """

    while True: # main loop
        choice = input("[D]ictionary, [B]rute force or [Q]uit: ")
        if choice == 'd' or choice == 'D':
            dictionary()
        if choice == 'b' or choice == 'B':
            brute_force()
        if choice == 'a' or choice == 'A':
            auto_crack()
        if choice == 'q' or choice == 'Q':
            print("\nGoodbye.\n")
            exit()


main() # call the main loop
