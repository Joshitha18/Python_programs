""" The dice rolling simulator will imitate the experience of rolling a dice. It will generate a random number and the user can play again and again to get a number from the dice until the user decides to quit the program."""

import random
import time

print("Press y to Play or n to Quit")
val=input().lower()

while val != 'n':
 print("Dice is rolling...")
 time.sleep(1)
 
 dice_1=random.randrange(1, 6)
 print("Dice 1 value: ",dice_1)
 dice_2=random.randrange(1, 6)
 print("Dice 2 value: ",dice_2)
 
 if dice_1 == dice_2:
  print("Congratulations! You got same values")
  
 print("Press y to Play Again or n to Quit")
 val=input().lower()

