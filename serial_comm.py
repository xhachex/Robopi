import serial
from time import sleep



ser = serial.Serial('COM3', baudrate = 9600, timeout = 1)
sleep(3)

def getValues():
  ser.write(b'g')
  arduinoData = ser.readline().decode('ascii')
  return arduinoData


while(1):
  userInput = input('Get data poing?')
  
  if userInput == 'y':
    print(getValues())
 

  
