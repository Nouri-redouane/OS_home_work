import os
import re
import time
from showProcess import showProcess


def getMountedProcesses():
    # get list of mounted processes from /proc/mounts
    command = os.popen("cat /proc/mounts")

    # get the output of the command
    output = command.read()

    # split the output into lines
    lines = output.splitlines()

    # create a list to store the mounted processes
    mountedProcesses = []

    # loop through the lines
    for line in lines:
        # split the line into columns
        columns = line.split()

        # 5 digits or more regex to match the process id
        fiveDigitsOrMore = re.compile(r'/proc/\d{5,}')

        # check if the line is a mounted process => the 1st column contains with /proc/id
        if re.match(fiveDigitsOrMore, columns[1]):
            # get the process id
            PID = columns[1].split('/')[2]

            # add the process id to the list
            mountedProcesses.append(PID)

    return mountedProcesses


bar = [

    " [========  ]",
    " [ ======== ]",
    " [  ========]",
    " [   =======]",
    " [    ======]",
    " [     =====]",
    " [      ====]",
    " [       ===]",
    " [        ==]",
    " [         =]",
    " [          ]",
    " [         =]",
    " [        ==]",
    " [       ===]",
    " [      ====]",
    " [     =====]",
    " [    ======]",
    " [   =======]",
    " [  ========]",
    " [ ======== ]",
    " [========  ]",
    " [=======   ]",
    " [======    ]",
    " [=====     ]",
    " [====      ]",
    " [===       ]",
    " [==        ]",
    " [=         ]",
    " [          ]",
    " [=         ]",
    " [==        ]",
    " [===       ]",
    " [====      ]",
    " [=====     ]",
    " [======    ]",
    " [=======   ]",
]
i = 0
current_time = time.time()

while True:

    # get the list of mounted processes
    mountedProcesses = getMountedProcesses()

    # check the number of mounted processes
    nbProcs = len(mountedProcesses)
    if nbProcs > 0:

        # loop through the mounted processes and print them with all the related information about theme with the help of ps
        for PID in mountedProcesses:
            print(PID)

            # unmount the empty folder to show the process informations
            showProcess(PID)

            command = os.popen(
                "ps -p {} -o user,start,time,pid,ppid,cmd".format(PID))
            output = command.read()

            print(output)

    else:
        print("Searching mounted processes  " +
              bar[i % len(bar)]+"  (time: "+str(int(time.time() % current_time))+"s)", end="\r")
        time.sleep(.2)
        i += 1
