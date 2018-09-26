from time import sleep

x = "Hola"
try:
    for i in range (0, 10):
        print(x)
        sleep(1)
except:
    print("An exception ocurred")
else:
    print("Nothing went wrongs")
finally:
    print("FINI")
