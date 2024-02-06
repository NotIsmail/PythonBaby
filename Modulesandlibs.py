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

import random

Cards = ["Jack", "King", "Queen"]
random.shuffle(Cards)
print(Cards)
