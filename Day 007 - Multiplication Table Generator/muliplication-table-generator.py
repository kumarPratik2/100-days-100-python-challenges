
#define a function to print table of the given number
def table(n):
    for i in range(1,11):
        m = n*i
        print(f'{a}x{i}={m}')

#takes input from user
a = int(input('Enter the number: '))
table(a)