from gpiozero import Motor
from time import sleep

left_wheel = Motor(forward=14, backward=15)
right_wheel = Motor(forward=24, backward=23)


def stop():
    left_wheel.stop()
    right_wheel.stop()
    
def forward(speed,time):
    left_wheel.forward(speed)
    right_wheel.forward(speed)
    sleep(time)
    stop()

def backward(speed,time):
    left_wheel.backward(speed)
    right_wheel.backward(speed)
    sleep(time)
    stop()

def left_open(speed):
    left_wheel.stop()
    right_wheel.forward(speed)

def left(speed, time):
    left_wheel.backward(speed)
    right_wheel.forward(speed)
    sleep(time)
    stop()

def right_open(speed):
    right_wheel.stop()
    left_wheel.forward(speed)

def right(speed, time):
    right_wheel.backward(speed)
    left_wheel.forward(speed)
    sleep(time)
    stop()

