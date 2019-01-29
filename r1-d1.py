#Import Python
import os, test, _thread

#Import modules
import move, face

from time import sleep
 
def menu():
    os.system('clear')
    print ("\t1 - primera opción")
    print ("\t2 - Face test")
    print ("\t3 - Motor test")
    print ("\t9 - Quit")
 
def end():
    face.clean()
    print("C'ya")
    

while True:
    # Mostramos el menu
    menu()
 
    # solicituamos una opción al usuario
    opcionMenu = input(">> ")
 
    if opcionMenu=="1":
        print ("")
        input("Nop.\n")
    elif opcionMenu=="2":
        print ("Look!")
        try:
            _thread.start_new_thread(face.resting,())
        except:
            print("Error.")
    elif opcionMenu=="3":
        print ("")
        print ("Motor test running...")
        try:
            _thread.start_new_thread(move.forward,(0.5,2,))
        except:
            print("Error")
    elif opcionMenu=="9":
        end()
        break
    else:
        print ("")
        input("Invalid choice...")

