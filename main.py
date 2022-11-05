import os
import time
from hideProcess import hideProcess
from createProcess import createProcess
from showProcess import showProcess

if __name__ == "__main__":
    # create an empty folder in home folder
    username = os.getlogin()
    os.system("mkdir /home/{}/empty".format(username))

    # install pyinstaller
    os.system("pip install -U pyinstaller")

    MAIN_PROCESS_PID = os.getpid()
    print("MAINPROCESS PID: ", MAIN_PROCESS_PID)

    SUB_PROCESS_PID = createProcess(cmd=['sleep', '10'])
    print("SUBPROCESS PID: ", SUB_PROCESS_PID)
    # Hide Main App Process
    hideProcess(MAIN_PROCESS_PID, username)
    hideProcess(SUB_PROCESS_PID, username)
    current_time = time.time()
    while 1:
        # print counter in seconds
        print("Counter: ", int(time.time()%current_time), end="\r")

    # Take some time before hiding the process
    #print('Pause 5 seconds before hiding main process ...')
    # time.sleep(5)
#
    # Create a process "sleep"
#
    # Take some time before hiding the process
    #print('Pause 20 seconds before hiding subprocess ...')
    # time.sleep(20)
#
    # Hide "sleep" Process
    #hideProcess(SUB_PROCESS_PID, username)
#
    # Show Main App Process
    #print('You can see the main process now')
    # showProcess(MAIN_PROCESS_PID)

    # Pause 10 seconds ...
    print('Pause 20 seconds before showing subprocess ...')
    time.sleep(20)

    # Show "sleep" Process
    print('You can see the subprocess now')
    showProcess(SUB_PROCESS_PID)
