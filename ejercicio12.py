#Ejercicio 12: Verificar número primo
#•	Uso de bandera booleana (es_primo = True).
#•	Lógica matemática para determinar si un número tiene divisores distintos de 1 y sí mismo.
#•	Optimización con la raíz cuadrada.

import math

numero = int(input("Ingresa un número entero mayor que 1: "))
# Inicializamos la bandera como True
es_primo = True
# Validar que el número sea mayor que 1
if numero <= 1:
    es_primo = False
else:
    # Solo necesitamos verificar hasta la raíz cuadrada del número
    limite = int(math.sqrt(numero)) + 1
    for i in range(2, limite):
        if numero % i == 0:
            es_primo = False
            break
if es_primo:
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
