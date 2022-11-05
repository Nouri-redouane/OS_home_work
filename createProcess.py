from subprocess import Popen


def createProcess(cmd):
    # create a subprocess and get its PID
    command = Popen(cmd)
    PID = command.pid

    return PID
