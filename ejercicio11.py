#################################################################################
#La política de cobro de una compañía telefónica es: cuando se realiza una 
#llamada, el cobro es por el tiempo que ésta dura, de tal forma que los primeros 
#cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos,
#los siguientes dos minutos, 70 céntimos, y a partir del décimo minuto, 50 céntimos.
#Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno
#de mañana, 15 %, y en turno de tarde, 10 %. 
#Realice un programa para determinar cuánto debe pagar por cada concepto 
#una persona que realiza una llamada.
#################################################################################

print("bienvenido")
tiempo= input("Ingrese la duración de la llamada en minutos: ")
tiempo=int(tiempo)

dia = input("En que dia realizaste la llamada es decir de lunes a domingo: ").strip().lower()


turno= input("Momento del dia en que la realizaste? (M/T): ").strip().upper()



if tiempo <= 5:
    costo= tiempo * 1  

elif tiempo<= 8:
    costo = 5 * 1 + (tiempo- 5) * 0.8 

elif tiempo <= 10:
    costo = 5 * 1 + 3 * 0.8 + (tiempo- 8) * 0.7 
    costo= 5 * 1 + 3 * 0.8 + 2 * 0.7 + (tiempo - 10) * 0.5 

if dia == "domingo":
    impuesto = costo * 0.03  
elif turno == "M":
    impuesto = costo * 0.15  
else:
    impuesto = costo* 0.10 


total = costo + impuesto

print(f"Costo de la llamada (sin impuestos): {costo:.2f} euros")
print(f"llamada con inpuesto: {impuesto:.2f} euros")
print(f"El total de tu llamada es: {total:.2f} euros")
print("Gracias")
