import os
import time as t
from datetime import datetime

def fun(time,op):

   cmd = {'shutdown':'/s','restart':'/r'}
   cmd = cmd.get(op)
   client_time=time.split(":")
   print(cmd)


   flag=1
   while flag:
            systime = datetime.now().strftime("%H:%M").split(":")
            if client_time[0]==systime[0] and client_time[1]==systime[1]:
                os.system(f"shutdown  {cmd} /t 1")
                flag=0
            else:
                print(f" {client_time[0]}:{client_time[1]} {systime[0]}:{systime[1]}")
            t.sleep(3)




keys = {'1':'shutdown','2':'restart'}

inkey = input(f"Choose the option\n1){keys['1']}\n2){keys['2']} \n").strip()

if inkey in keys:

    option=keys.get(inkey)

    time = input(f"Enter the time you wanna {inkey} 'ex: 23:32' : ").strip()
    fun(time,option)
else:
     print("Error occurred")


