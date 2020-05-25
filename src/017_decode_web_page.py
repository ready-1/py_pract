#!../bin/python

"""017_decode_web_page.py

This is a Python learning project from:
http://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html

Use the BeautifulSoup and requests Python packages to print out a list of 
all the article titles on the New York Times homepage.

"""

# This one is a bit abbreviated.  Due to how complex the NYT homepage has
# become since this challenge was written, I decided to not spend the hours
# it would have taken to parse all the headlines buried in various CSS classes
# and concentrate more on the simple proof of concept that would have been
# expected in 2014.  In this exercise, I simply look for all the h2 tags
# and get the enclosed text.  This will scale to whatever amount of effort
# one is willing to put forth to grind through the details.  The plate and
# screws in my neck don't want to put forth that much effort today.  :-)

from bs4 import BeautifulSoup
import requests
import html5lib

print('\nHello World! This is 017_decode_web_page.py\n')

# get the NYT hompage and store it to a string
r = requests.get('https://www.nytimes.com/')

# parse the raw HTML and create a bs4 object from it.
soup = BeautifulSoup(r.text, features="html5lib")

# find all the h2 tags in the page and put them in a list
h2 = soup.find_all('h2')

# how many tags we found.
total = len(h2)
# our little counter
i = 0
# loop through the list and get the text.
for h in h2:
    # increment the counter
    i += 1 
    # extract the text
    text = BeautifulSoup(str(h), features="html5lib")
    # Show it to the user
    print(f'{i} of {total}: {h.get_text()}')

# display headroom
print()





