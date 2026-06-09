#imports time module
import time

#asks user to input in seconds and stores in 't' variable 
t = int(input('Enter how many seconds you want to count: '))

#runs a loop until t becomes 0
while t > 0:

    #converts seconds to minutes
    m = t //60
    s = (t %60)
    t -= 1
    print(f'{m:02d}:{s:02d}')
    #.sleep(1) pauses the loop for 1 second every time the loop runs
    time.sleep(1)
print('Times up!')