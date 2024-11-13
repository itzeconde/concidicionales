#################################################################################
#El director de una escuela está organizando un viaje de estudios, y requiere 
#determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de 
#viajes por el servicio. La forma de cobrar es la siguiente: 
#si son 100 alumnos o más, el costo por cada alumno es de 65 euros; 
#de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, 
#y si son menos de 30, el costo de la renta del autobús es de 4000 euros, 
#sin importar el número de alumnos. 
#Realice un programa que permita determinar el pago a la compañía de autobuses 
#y lo que debe pagar cada alumno por el viaje.
#################################################################################

print("Bienvenido")
alumnos = input("¿Cuántos alumnos viajarán? ")
alumnos=int(alumnos)

if alumnos >= 100:
    costo = 65 * alumnos
    print("El costo por alumno es de 65 euros")
    print("El costo total para la compañía es de", costo)

elif 50 <= alumnos <= 99:  # Condición de 50 a 99 alumnos
    costo2 = 70 * alumnos
    print("El costo por alumno es de 70 euros")
    print("El costo total para la compañía es de", costo2)
    
elif 30 <= alumnos <= 49:
    costo3 = 95 * alumnos
    print("El costo por alumno es de 95 euros")
    print("El costo total para la compañía es de", costo3)

else:
    costo4=4000*alumnos
    print("El costo por alumno es de 4000 euros")
    print("El costo total para la compañía es de", costo4)