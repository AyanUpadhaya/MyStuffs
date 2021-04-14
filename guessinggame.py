#lets import random lib
 
import random
 
#generate a random number for computer
 
computer=random.randint(1,20)
 
guess=0
 
while guess!=computer:
         print("Guess a number between 1 to 20")
         guess=int(input())
 
         if guess<computer:
                  print("Too low")
         if guess>computer:
                  print("Too high")
         if guess==computer:
                  print("You Guessed it right")
