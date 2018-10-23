import sys, tty, termios, time

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def toggleLights():
    global lightStatus

    if(lightStatus == False):
        ligthStatus = True
    else:
        ligthStatus = False

lightSatus = False

while True:


    char = getch()

    if (char == "l"):
        print("Lights toggle")
        println(lightStatus)
        toggleLights()

    if(char == "x"):
        print("Program Ended")
        break
