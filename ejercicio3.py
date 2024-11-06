#################################################################################
# Escribe un programa que lea un número e indique si es par o impar.
#################################################################################

num=input("Ingresa un numero")
num=int(num)

if num % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")