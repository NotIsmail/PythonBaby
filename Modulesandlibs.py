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
import sys

try:
    print("Hello,", sys.argv[1])
except IndexError:
    print("No arguments were entered")
