import random
number = '1234567890' #creates pool of characters needed for password
characters = '!@#$%&?'
alphabets = 'QqWwEeRrTtYyUuIiOoPpAaSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm'

password ='' #defines an empty string to hold password characters

ch = number + characters + alphabets #combines all characters pool into one

n = int(input('Enter the strength of your password: '))#asks user for length of password

for i in range(n):
    i=random.choice(ch) #random.choice selects one character each time the loop runs
    pw += i #add the randomly selected character in password string and saves it
print(pw)