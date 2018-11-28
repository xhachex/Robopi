from gpiozero import Motor
from time import sleep

left_wheel = Motor(forward=4, backward=14)
right_wheel = Motor(forward=23, backward=24)


def fullstop:
	left_wheel.stop()
	right_wheel.stop()
	
def forward(speed):
	left_wheel.forward(speed)
	right_wheel.forward(speed)

def backward(speed):
	left_wheel.backward(speed)
	right_wheel.backward(speed)

def left_open(speed):
	left_wheel.stop()
	right_wheel.forward(speed)

def left_closed(speed)
	left_wheel
