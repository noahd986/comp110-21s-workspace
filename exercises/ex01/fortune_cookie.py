"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730336970"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")
draw: int = int(randint(1, 100))

if draw < 25:
    print("Nothing is impossible to a willing heart.")
else:
    if draw < 50:
        print("Don't worry about money. The best things in life are free.")
    else:
        if draw < 75:
            print("All things are difficult before they become easy.")
        else:
            print("A ship in harbor is safe, but that's not why ships are built.")

print("Now, go spread positive vibes!")