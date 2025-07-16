#Ejercicio 10: Contar positivos y negativos
#•	Uso de contadores separados para clasificar los números como positivos o negativos.
#•	for de 5 repeticiones.

cont_posi= 0
con_nega= 0  
for i in range(5): 
    num = int(input("Ingresa un número: ")) 
    if num > 0:
        cont_posi += 1
    elif num < 0:
        con_nega += 1
print(f"Positivos: {cont_posi}, Negativos: {con_nega}")
