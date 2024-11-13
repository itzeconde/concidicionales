#################################################################################
#Realiza un programa que pida el día de la semana (del 1 al 7) y escriba 
#el día correspondiente. 
# Si introducimos otro número nos da un error.
#################################################################################

dia=input("Ingresa el dia de la semana del 1 al 7")
dia=int(dia)

if dia==1:
    print("El dia de la semana es lunes: ")
    
elif dia==2:
    print("El dia de la semana es martes: ")
    
elif dia==3:
    print("El dia de la semana es miercoles:")

elif dia==4:
    print("El dia de la semana es jueves:")
    
elif dia==5:
    print("El dia de la semana es viernes:")
    
elif dia==6:
    print("El dia de la semana es sabado:")
elif dia==7:
    print("El dia de la semana es domingo:")
else:
        print("Uyyy no, no es un dia de la semana :")