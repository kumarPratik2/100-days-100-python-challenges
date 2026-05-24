def add(a,b):
    print(f'Sum of given numbers is: {a+b}')

def sub(a,b):
    print(f'Difference of given numbers is: {a-b}')

def mul(a,b):
    print(f'Product of given numbers is: {a*b}')

def div(a,b):
    print(f'Divison of given numbers is: {a/b}')


a = input('Enter first nmber: ')
b = input('Enter second number: ')

a,b = float(a), float(b)

    

task = True
            
while task == True:


    print('"add" for Addition, "sub" for Substraction, "mul" for Multiplication, "div" for Divison')
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
                
