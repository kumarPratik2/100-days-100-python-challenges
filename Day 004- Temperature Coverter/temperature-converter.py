#defining function that will convert celius to farhenheit
def Celsius(far):
    cel =5*(far - 32)/9
    print(cel)

#defining function that will convert farenheit to celsius
def Fahrenheit(Cel):
    Far = (Cel * 9/5) +32
    print(Far)

#asking user to input is their function is in celsius or farhenheit
x = input('Type "C" if your temperature is in Celisius or "F" if its in Fahrenheit: ')

#converting to celsius
if x.capitalize() == 'F':
    t = float(input('Enter temperature in Fahrenheit: '))
    Celsius(t)

#converting to fahrenheit
if x.capitalize() == 'C':
    t = float(input('Enter temperature in Celsius: '))
    Fahrenheit(t)