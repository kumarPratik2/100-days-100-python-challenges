# Number Guessing Game
# Beginner Python Project
# User gets 5 attempts to guess the correct number

import random as rd 
c = rd.randint(1, 100)  
#Generates a random number which stays constant throughout the game

count = 0   
#declaring that guess count starts from zero

while count < 5: 
    #declaring how many times user can guess(5)
    u = input("Guess a number between 1 and 100: ")
    try:    
        #tries the value enterd by user
        ug = int(u)
    except ValueError:  #in case the user has input anything except numbers, next line will get printed
         print(f'Enter valid value as {u} is invalid')
         continue   
    #stops the counter from incresing in case of error
    
    count += 1  
    #count increases by 1 for every valid guess
    
    if c < ug:
            print(f"Your guess is high.")
            print(f'Guess count = {count}, You have {5 - count} guesses left.')
    
    elif c> ug:
            print(f"Your guess is low.")
            print(f'Guess count = {count}, You have {5 - count} guesses left.')
   
    else:
            print("You won as you guessed right.")
            break
    if count == 5:
                print(f'Game Over. The correct answe was {c}')  
                #Prints game over if the user has failed to guess the number in his limited number of guesses
