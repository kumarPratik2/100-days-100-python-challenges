#defines a function to check palindrome
def check(x):
    y = x[::-1] #inverses the string
    if x == y:
        print(f'{x} is a palindrome.')
    else:
        print(f'{x} is not a palindrome.')

#starts continuation loop so whenver its true it will restart the whole loop
c = True
while c == True:

#asks user for input
    s = input('Enter a word or number you want to check: ').lower()
    check(s)

    print('Do you want to check another? If yes type "y" or "n" for no.')
    a = input('Your answer: ').lower()

    if a == 'y' or a == 'yes':
        c = True
    elif a == 'n' or a == 'no':
        c = False
    else:
        c = False
        print('You entered invalid response.')