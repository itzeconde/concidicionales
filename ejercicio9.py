#################################################################################
#Programa que pida tres números y los muestre ordenados (de mayor a menor);
#################################################################################

num1 = input("Ingrese el primer número: ")
num1=int(num1)

num2 =input("Ingrese el segundo número: ")
num2=int(num2)

num3 = input("Ingrese el tercer número: ")
num3=int(num3)

if (num1>num2 and num2>num3):
    print("",num1,"-",num2,"-",num3)
    
elif(num2>num1 and num1>num3):
    print("",num2,"-",num1,"-",num3)
    
elif(num3>num1 and num1>num2):
    print("",num3,"-",num1,"-",num2)
    
elif(num3>num2 and num2>num1):
    print("",num3,"-",num2,"-",num1)
    
elif(num1>num3 and num3>num2):
    print("",num1,"-",num3,"-",num2)
    
elif(num2>num3 and num3>num1):
    print("",num2,"-",num3,"-",num1) 

else:
    print("son numeros iguales")
