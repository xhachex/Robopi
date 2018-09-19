from gpiozero import Robot, DistanceSensor, LED
from time import sleep

# Variables:
# Motors
RobotLeftPlus = 4
RobotLeftMinus = 14
RobotRightPlus = 17
RobotRightMinus = 18
RobotFullSpeed = 1

# Sensor
DistanceECHO = 23
DistanceTRIG = 24
DistanceMAX = 1
#DistanceTHRESHOLD = 0.2

# LEDs

# GPIOzero def:
robot = Robot(left(RobotLeftPlus, RobotLeftMinus), right(RobotRightPlus, RobotRightMinus))
sensor = DistanceSensor(DistanceECHO, DistanceTRIG, max_distance = DistanceMAX)

# Funciones:

# Selecciona camino a seguir
def chose_path():
    robot.stop()
    print("Eligiendo camino...")
    robot.left()
    sleep(1)
    DistanceLeft = sensor.distance
    print("Izquierda: ", DistanceLeft, " cm")
    robot.right()
    sleep(2)
    DistanceRight = sensor.distance
    print("Derecha: ", DistanceRight, " cm")
    robot.stop()
    if DistanceLeft > DistanceRight:
        print("Elegir izquierda")
        robot.left()
        sleep(2)
        robot.stop()
    else:
        print("Elegir derecha")

# Mainloop:
try:
    while True:
        DistanceFront = sensor.distance
        print(DistanceFront," cm")

        if DistanceFront < 10:
            chose_path()
        else:
            print ("Forward")
            robot.forward(RobotFullSpeed)
        sleep(0.5)

except KeyboardInterrupt:
    robot.stop()
    print("C'ya")
    pass
