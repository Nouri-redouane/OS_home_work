import os


def showProcess(PID):
    # unmount the empty folder
    os.system('sudo umount /proc/{}'.format(PID))
