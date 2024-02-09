# In this we will see the use of one of the various modules availabe

"""
import random  # the modules r introduced using impport keyword

coin = random.choice(["Heads", "Tails"])
print(coin)
"""

# Now we see another method to import things that is using from keyword
"""
from random import choice

coin = choice(["Heads", "Tails"])
print(coin)
"""

# as the name suggests randint produces random integer


"""
import random

number = random.randint(1, 10)
print(number)
"""


# Now we r going to use shuffle which as name suggests shuffles things

"""
import random

Cards = ["Jack", "King", "Queen"]
random.shuffle(Cards)
# As the output printed is in the form of list we can convert it into single element using for loop
for card in Cards:
    print(card)

"""

# Now another example ussing statistics module
"""
import statistics

print(statistics.mean([100, 90]))
"""


# Now we r going to see the use of sys.argv which returns whatever logged in the terminal window

"""
import sys

try:
    print("Hello,", sys.argv[1])
except IndexError:
    print("No arguments were entered")
"""
"""
#  A python program to print the use of cowsay

import cowsay
import sys

cowsay.trex("hello,")
"""


# Now using request module for API requests

"""
import requests
import json

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=25&term=5%20seconds%20of%20summer"
)
# print(response.json())   here we r seeing the raw JSON script of the API
# now we r going to see using the json package


# print(json.dumps(response.json(), indent=2))

# n Now we r going to see how to iterate over things  like of the entire term list from the API
o = response.json()
for result in o["results"]:
    print(result["trackName"])
"""

# Now we are going to look at the creating ur own custom module and using it
from impfile import hello

User_Name = input("Enter Your Name:")
hello(User_Name)
