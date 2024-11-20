#################################################################################
# Juego Piedra Papel y Tijera
# Programa que lea las opciones de 2 jugadores, y muestra el resultado
# Empate, gana jugador 1 o gana jugador 2
# Si introducimos una opción que no coindica con piedra, papel o tijera
# Diga que opción Incorrecta
#################################################################################
print("Bienvenido al juego de piedra papel y tijera")

jugador1 = input("Jugador 1: elige piedra, papel o tijera: ")
jugador2 = input("Jugador 2: elige piedra, papel o tijera: ")

if jugador1 == "piedra" and jugador2 == "tijera":
    print("Gana Jugador 1.")
    
elif jugador1 == "papel" and jugador2 == "piedra":
    print("Gana Jugador 1.")
    
elif jugador1 == "tijera" and jugador2 == "papel":
    print("Gana Jugador 1.")
    
elif jugador1 == jugador2:
    print("Empate.")
    
elif jugador2 == "piedra" and jugador1 == "tijera":
    print("Gana Jugador 2.")
    
elif jugador2 == "papel" and jugador1 == "piedra":
    print("Gana Jugador 2.")
    
elif jugador2 == "tijera" and jugador1 == "papel":
    print("Gana Jugador 2.")
    
else:
    print("No es una opcion valida")