#Ejercicio 15: Calcular promedio
#•	Uso de acumulador para suma.
#•	División para obtener el promedio: promedio = suma / cantidad.
cont_suma=0
cant = int(input("Ingresar la cantidad de números que necesitas: "))
for i in range(cant):
    num = float(input(f"Número {i}: "))
    cont_suma+= num
prome=cont_suma/cant
print(f"El promedio es: {prome}")


