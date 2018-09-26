import serial
from time import sleep

arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
sleep(3)

print("Starting!")

#comando = input('Introducir un')

def func_medir():
    arduino.write(b'M')
    print("sending...")
    if(arduino.in_waiting > 0):
        line = arduino.readline().decode('ascii')
    print(line)

try:
    while True:
        print(func_medir())
        sleep(10)


except KeyboardInterrupt:
    arduino.close() #Finalizamos la comunicacion
    print("C'ya")
    pass



