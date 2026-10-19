"""
Day 15 - number guessing game in python
Author - Uma
Date - 19-10-2026
"""

import random

number = random.randint(1, 10)

guess = int(input("guess a number between 1 - 10 : "))

if guess == number:
    print("you guessed it")

else:
    print("Oops! the number was",number)