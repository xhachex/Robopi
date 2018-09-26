from time import sleep

try:
    while True:
        print("Funcionando")
        sleep(1)
        
except KeyboardInterrupt:
    print("Interrumpido")
    pass
