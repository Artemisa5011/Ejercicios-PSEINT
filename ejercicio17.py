#Ejercicio 17: Año bisiesto
#•	Condición compuesta usando operadores lógicos and, or.
#•	Lógica de calendario para saber si el año es bisiesto.

año = int(input("Ingresa el año: "))
if (año % 4==0 and año%100 != 0) or (año % 400 == 0):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")

