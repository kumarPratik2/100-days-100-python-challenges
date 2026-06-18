#imports random module
import random

#defines an empty list to store the rolls
roll = []

#defines all possible rolls from a dice
dice = '1', '2', '3', '4', '5', '6'

#ask user to input how many dice they want to roll
n = int(input('Enter how many dices you want to roll: '))

#here '_' runs loop as normal variable but without using the counter
for _ in range(1,n+1):
    a = random.choice(dice)
    roll.append(a)
    
print(roll)
