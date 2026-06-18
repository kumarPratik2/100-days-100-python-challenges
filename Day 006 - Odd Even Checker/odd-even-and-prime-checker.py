#defines function 
def check(a):
    #checks is number is 2
    if a == 2:
        print(f'{a} is both even and prime')

#checks if the number is any other even number except 2
    elif a> 2 and a%2 == 0:
        print(f'{a} is even and not prime')
    
    #checks if the number is odd
    elif a%2 ==1:
        #checks if number is prime
        f =[]
        for i in range(1,a+1):
            n = a%i
            if n == 0:
                f.append(i)
        if len(f) == 2:
         print(f'{a} is odd and prime')
        else:
            print(f'{a} is odd but not prime')
    
x = int(input('Enter a number: '))
check(x)