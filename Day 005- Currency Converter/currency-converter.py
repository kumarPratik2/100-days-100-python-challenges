#define the function to convert dollar from rupee
def Dol(r):
    d = r/83
    print(f'USD {d:.2f}')

#define the function to convert rupee from dollar
def Rup(D):
    R = D*83
    print(f'{R:.2f} INR')

#asks user toinput it their currency is in dollar or rupee
cur = input('Enter "USD" id your currency is in USD or "INR" if its in INR: ')

#converts to rupee in case of dollar
if cur.upper() == 'USD':
    a = float(input('Enter amount: '))
    Rup(a)

#converts to dollar in case of rupee
elif cur.upper() == 'INR':
    a = float(input('Enter amount: '))
    Dol(a)