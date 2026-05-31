#imports random module
import random 
 #defines the choices given
rps = 'rock', 'paper', 'scissor'
#asks user to input his choice
u = input('Enter your pick between "rock", "paper" and "scissor": ').lower()
#computer uses choice from random module to choose an option from given choices(rps)
c = random.choice(rps) 

print(f'Computer chose: {c}')

#defines the conditon where game can be drawn
if u == c: 
    print("Match Draw. Try again")

#defines conditions where user wins
elif( 
    (u == 'rock' and c =='scissor') or
    (u == 'paper' and c == 'rock') or 
    (u == 'scissor' and c == 'paper')
):
    print("User Won")

#defines conditions where computer wins
elif(
    (u == 'rock' and c == 'paper') or
    (u == 'paper' and c == 'scissor') or
    (u == 'scissor' and c == 'rock')
):
    print("Computer Won.")

#asks user to try again in case of invalid input
else:
    print('Enter valid input and Try again.')