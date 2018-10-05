import os
import time

seconds = int(5)
minutes = int(0)
hours = int(1)

start = input('Enter "R" to start timer.')

while start.lower() == 'r':
    if seconds == 0:
        seconds = 59 
        minutes -= 1
    if minutes == 0:
        minutes = 59
        hours -= 1
    os.system('cls')
    seconds -= 1
    print(hours, ':', minutes, ':', seconds)
    time.sleep(1)