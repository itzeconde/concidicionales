# ################################################################################
# Escribe un programa que pida un nombre de usuario y una contraseña 
# y si se ha introducido "pepe" y "asdasd" se indica "Has entrado al sistema", 
# sino se da un error.
# ################################################################################

usuario=input("Ingresa un nombre de usuario: ")
contraseña=input("Ingresa una contraseña: ")


if usuario == "pepe" and contraseña == "asdasd":
    print("Has entrado al sistema")
else:
    print("Error no se ha logrado acceder al sistema")
