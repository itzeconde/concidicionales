#################################################################################
# Programa que pida dos números e indique Cuál es el mayor
# Si los dos son iguales que muestre el mensaje "Son iguales"
#################################################################################
num1 = input("Ingresa el número 1: ")
num1 = int(num1)
num2 = input("Ingresa el número 2: ")
num2 = int(num2)

if num1 > num2:
    print("El número mayor es el número", num1)
elif num2 > num1:
    print("El número mayor es el número", num2)
else:
    print("Los números son iguales")