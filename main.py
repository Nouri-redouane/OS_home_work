import os
import time
from hideProcess import hideProcess
from createProcess import createProcess
from showProcess import showProcess

if __name__ == "__main__": 
    # create an empty folder in home folder
    os.system("mkdir /home/empty")
    username = os.getlogin()
    
    #install pyinstaller
    os.system("pip install -U pyinstaller")

    PID_APP = os.getpid()
    print("Main PID: ", PID_APP)

    # Take some time before hiding the process
    print('Pause 5 seconds before hiding main process ...')
    time.sleep(5)

    # Hide Main App Process
    hideProcess(PID_APP, username)

    # Create a process "sleep"
    PID_PROCESS=createProcess(cmd=['sleep', '10'])
    print("PID_PROCESS: ", PID_PROCESS)

    # Take some time before hiding the process
    print('Pause 20 seconds before hiding subprocess ...')
    time.sleep(20)

    # Hide "sleep" Process
    hideProcess(PID_PROCESS, username)

    # Show Main App Process
    print('You can see the main process now')
    showProcess(PID_APP)

    # Pause 10 seconds ...
    print('Pause 20 seconds before showing subprocess ...')
    time.sleep(20)

    # Show "sleep" Process
    print('You can see the subprocess now')
    showProcess(PID_PROCESS)
