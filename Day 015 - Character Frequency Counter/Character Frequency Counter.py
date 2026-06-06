# asks for a string on which we  will operate and uses .lower() so all characters are in lower
inp = input('Enter the string: ').lower()

#defines empty dictionary
d = {}

# builds a frequency dictionary where each character is stored as a key and its number of occurrences is stored as the value
def frequency(x):
    for i in inp:
        count = inp.count(i)
        d.update({i:count})
    print(f'{x} has appeared {d[x]} time(s) is this string.')

#starts continuation loop for frequency counter so everytime its true it will ask user to input chracter to check
cont = True
while cont == True:

    char = input('Enter the character whose frequency you want to check: ').lower()
    if char in inp:
        frequency(char)
    else:
        print('Character is not present in string.')
    
#starts continuation loop for users response so it will always be true if user enters invalid response and ask until user inputs valid response
    res = True
    while res == True:
        print('Do you want to check anoter character? If yes type "y" or "n" if not.')
        a = input('Enter your choice: ').lower()
        if a == 'y' or a == 'yes':
            cont = True
            res = False
        elif a == 'n' or a == 'no':
            cont = False
            res = False
            print('Thank You')
        else:
            print('Enter valid response')
            res = True