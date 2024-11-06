#################################################################################
#Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.
#################################################################################
cadena = input("Introduce una letra: ")

if len(cadena) == 1 and cadena.isupper():
    print("Es una letra mayúscula.")
else:
    print("No es una letra mayúscula.")