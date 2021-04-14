#lets import random lib
#generate a random number for computer
import random
import time

print("Enter your name:")
name=input()
print("Nice to meet you "+name)

print("Computer:I have choosed a number between 1 to 20.")
total_chance=3
chance=0
computer=random.randint(1,20) 
guess=0
time.sleep(3)
 
while guess!=computer and chance!=total_chance:
         print("Take a guess:")
         guess=int(input())
 
         if guess<computer:
                  print("Too low")
         if guess>computer:
                  print("Too high")
         if guess==computer:
                  print("You Guessed it right")

         chance=chance+1
         if chance==total_chance:
             print("Sorry you loose!")
         else:
             print("Left chances: "+str(total_chance-chance))
