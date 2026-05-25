#task checks if user has accepted only y/n
task = True
while task == True:

#takes hieght and weight as variables from user
    h = (input('Enter height in meters: '))
    w = input('Enter weight in kg: ')

    #checks if the inputs are valid or not
    try:
        h = float(h)
        w = float(w)
    except ValueError:
        print('Enter valid information.')
        continue

#makes sure that height is not zero
    if h <= 0:    
        print('Height can neither be 0 nor negative.')
        continue

    BMI = w/(h**2)

    if BMI <= 18.4:
        print(f'Your BMI is : {BMI:.2f} and you are underweight')
    elif  18.5 <= BMI <= 24.9:
        print(f'Your BMI is : {BMI:.2f} and you are healthy')
    elif 25 <= BMI <= 29.9:
        print(f'Your BMI is : {BMI:.2f} and you are overweight')
    elif BMI >= 30:
        print(f'Your BMI is : {BMI:.2f} and you are obese')

#makes sure user has only chosen y or n or loop will restart and ask for valid input
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