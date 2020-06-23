""" The dice rolling simulator will imitate the experience of rolling a dice. It will generate a random number and the user can play again and again to get a number from the dice until the user decides to quit the program."""

import random

print("Press any integer to Play Again or \"0\" to Quit")
val=input()

while val != 0:
 print(random.randrange(1, 6))
 print("Press any integer to Play Again or \"0\" to Quit")
 val=input()
