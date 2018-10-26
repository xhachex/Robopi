import pigpio
from time import sleep

pi = pigpio.pi()

def yep():
    print("Yeai")
    for x in range(3):
        pi.set_servo_pulsewidth(3, 1000)
        sleep(.3)
        pi.set_servo_pulsewidth(3, 2000)
        sleep(.3)            

def nop():
    print("No no")
    for x in range(3):
        pi.set_servo_pulsewidth(2, 1000)
        sleep(.3)
        pi.set_servo_pulsewidth(2, 2000)
        sleep(.3)
