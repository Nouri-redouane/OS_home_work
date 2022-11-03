from subprocess import Popen


def createProcess(cmd):
    # create a subprocess and get its PID
    command = Popen(cmd)
    PID = command.pid
    print("Subprocess PID: ", PID)

    return PID
