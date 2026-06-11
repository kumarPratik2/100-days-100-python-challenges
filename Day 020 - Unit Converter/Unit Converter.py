#defines functions for different conversions
def kmtomiles(km):
    miles = km * 0.621371
    print(f'{km} km is {miles:.2f} miles')

def milestokm(Miles):
    KM = Miles / 0.621371
    print(f'{Miles} miles is {KM:.2f} km')

def ftoc(f):
    c = (f - 32) * 5/9
    print(f'{f} F is {c:.2f} C')

def ctof(C):
    F = (C * 9/5) + 32
    print(f'{C} C is {F:.2f} F')

def kgtolb(kg):
    pounds = kg * 2.20462
    print(f'{kg} kg is {pounds:.2f} lbs')

def lbtokg(LB):
    KG = LB / 2.20462
    print(f'{LB} lbs is {KG:.2f} kg')

#starts a while loop that will repeat when conditions are true
while True:

    print('''Unit Converter
        1. kilometers to miles
        2. miles to Kilometers
        3. fahreheit to celsius
        4. celsius to fahrenheit
        5. kilgrams to pounds
        6. Kpounds to kilograms
        7. Exits
        ''')
    inp = int(input('Enter the of the number fucnction you want to perform: '))

    if inp == 1:
        value = float(input(('Enter the value you want to convert: ')))
        kmtomiles(value)
    elif inp == 2:
        value = float(input(('Enter the value you want to convert: ')))
        milestokm(value)
    elif inp == 3:
        value = float(input(('Enter the value you want to convert: ')))
        ftoc(value)
    elif inp == 4:
        value = float(input(('Enter the value you want to convert: ')))
        ctof(value)
    elif inp == 5:
        value = float(input(('Enter the value you want to convert: ')))
        kgtolb(value)
    elif inp == 6:
        value = float(input(('Enter the value you want to convert: ')))
        lbtokg(value)
    elif inp == 7:
        print('Thank You')
        break
        
    else:
        print('Enter valid option number')
        cont = True