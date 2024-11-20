#################################################################################
#Escribe un programa que pida un número entero entre uno y doce e imprima el 
#número de días que tiene el mes correspondiente.
# Si introducimos otro número nos da un error.
#################################################################################

mes=input("Ingresa un mes en numero entero del 1 al 12:")
mes=int(mes)

if mes ==1:
    print("El mes es enero y tiene 31 dias")
    
elif mes ==2:
        print("El mes es febrero y tiene 28 dias o 29 si es bisiesto ")
        
elif mes ==3:
        print("El mes es marzo y tiene 31 dias")
        
elif mes ==4:
        print("El mes es abril y tiene 30 dias")
        
elif mes ==5:
        print("El mes es mayo y tiene 31 dias")
        
elif mes ==6:
        print("El mes es junio y tiene 30 dias")
    
elif mes ==7:
        print("El mes es julio y tiene 31 dias")
    
elif mes ==8:
        print("El mes es Agosto y tiene 31 dias")
        
elif mes ==9:
        print("El mes es septiembre y tiene 30 dias")
    
elif mes ==10:
        print("El mes es octubre y tiene 31 dias")
    
elif mes ==11:
        print("El mes es noviembre y tiene 30 dias")
        
elif mes ==12:
        print("El mes es diciembre y tiene 31 dias")

else:
    print("Error ningun mes corresponde al numero",mes)