#imports datetime and time modules for using their operations
import datetime
import time

#asks user to print the time they want alarm to notify in HH:MM:SS format
alarm = input('Enter the time you want the alarm to ring(in 24 hour format): ')

#runs a while loop to run until the condition is true
while True:
    now = datetime.datetime.now() #calls current time using datetime module's operation
    now = now.strftime("%H:%M:%S") # cnverts time in general format
    print(now) #prints system time each second till loop runs
    time.sleep(1)

    if alarm == now:
        print(f'Its {now}')
        break