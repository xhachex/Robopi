#import os
 
def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	#os.system('cls') # NOTA para windows tienes que cambiar clear por cls
	print ("Selecciona una opción")
	print ("\t1 - primera opción")
	print ("\t2 - segunda opción")
	print ("\t3 - tercera opción")
	print ("\t9 - salir")
 
def end():
    print("C'ya")
    

while True:
	# Mostramos el menu
	menu()
 
	# solicituamos una opción al usuario
	opcionMenu = input("inserta un numero valor >> ")
 
	if opcionMenu=="1":
		print ("")
		input("Has pulsado la opción 1...\npulsa una tecla para continuar")
	elif opcionMenu=="2":
		print ("")
		input("Has pulsado la opción 2...\npulsa una tecla para continuar")
	elif opcionMenu=="3":
		print ("")
		input("Has pulsado la opción 3...\npulsa una tecla para continuar")
	elif opcionMenu=="9":
		end()
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
