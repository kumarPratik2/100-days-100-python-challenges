#defines function with x as parameter to calculate average
def result(x):
    aver = x/5
    return aver #stores average as aver vaiable
    
#defines  function with a as parameter to calculate grade
def grad(a):
    if a >=  90:  
        grade = 'A'

    elif 89>= a >=  80:  
        grade = 'B'

    elif 79 >= a >= 70:  
        grade = 'C'

    elif 69 >= a >= 60:  
        grade = 'D'

    elif a <= 59:  
        grade = 'E'
    return grade #stores grade as aver vaiable

 #declares countinuation variable 'cont' as true and runs while loop so loop will restart when cont is true
cont = True
while cont == True:

#prints ovening message and asks user for marks of each subject
    print('''Students marks calculator 
    Enter marks for each subject below:''')
    Mat = int(input('MATHS: '))
    Sci = int(input('SCIENCE: '))
    SSc = int(input('Social Science: '))
    Eng = int(input('ENGLISH: '))
    GK = int(input('GK: '))

#calculates sum of all subjects and passes through functions to get average and grade
    s = Mat+Sci+SSc+Eng+GK
    Aver = result(s)
    Grad = grad(Aver)

#prints complete result, "-----" is just for asthetics
    print(f'''Result
        Math          : {Mat}
        Science       : {Sci}
        Social Science: {SSc}
        English       : {Eng}
        GK            : {GK}
        ----------------------
        Average       : {Aver}
        Grade         : {Grad}
        ''')

#asks user if they want to check another result
    c = input('Do you want to check another resul(y/n): ').lower().strip()

#when user inputs yes(y), loop restarts
    if c == 'y':
        cont = True

#when user inputs no(n), loop stop
    elif c == 'n':
        cont = False
        print('Thank You')
