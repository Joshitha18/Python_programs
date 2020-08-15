"""A program which randomly chooses a number to guess and then the user will have a 20 chances to guess the number correctly. In each wrong attempt, the computer will give a hint that the number is greater or smaller than the one you have guessed."""

import random

x=random.randrange(1, 1000)

print("Guess the number")
chance=1
val=input()

while val != x and chance<=20:
 if val>x:
  print("less than "+str(val))
  val=input()
  chance+=1
  
 elif val<x:
  print("Greater than "+str(val))  
  val=input()
  chance+=1  
 else:
  print("Guessed Correctly")
  break
  
else:
 if chance>20:
  print("Exceeded number of chances") 
