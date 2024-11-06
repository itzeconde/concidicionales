# Crea un programa que pida al usuario dos números y muestre su división 
# si el segundo no es cero, o un mensaje de aviso en caso contrario.
#################################################################################

num1 = input("Ingresa el primer número: ")
num1=int(num1)
num2 = input("Ingresa el segundo número: ")
num2=int(num2)

if num2 != 0:
    division = num1 / num2
    print("El resultado de la división es:", division)
else:
    print(" No se puede dividir entre cero.")