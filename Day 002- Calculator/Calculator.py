#definig addition function
def add(a,b):
    print(f'Sum of given numbers is: {a+b}')

#definig subtraction function
def sub(a,b):
    print(f'Difference of given numbers is: {a-b}')

#definig multiplication function
def mul(a,b):
    print(f'Product of given numbers is: {a*b}')

#definig division function
def div(a,b):
    print(f'Division of given numbers is: {a/b}')

#taking inputs and storing them as float for calculations
a = input('Enter first number: ')
b = input('Enter second number: ')

a,b = float(a), float(b)

    
#task will check if user has given valid operation or not
task = True
            
while task == True:


    print('"add" for Addition, "sub" for Subtraction, "mul" for Multiplication, "div" for Division')
    x = input('Choose the function you want to perform: ')
    if x == 'add':
        add(a,b)
    elif x == 'sub':
        sub(a,b)
    elif x == 'mul':
        mul(a,b)
    elif x == 'div':
        if b==0:
            print(f'{a} cannot be divided by 0.')
        else: 
            div(a,b)
    else:
        print('Enter valid function: ')

#s will check if user has given valid input(y/n) or not
    s = False
    while s == False:
        z =input('Type "y" if you have another operation or "n" if not: ' )

        if z == 'y':
            task = True
            s = True
        elif z == 'n':
            task = False
            s = True
        else:
            print('Enter valid input: ')            
                
