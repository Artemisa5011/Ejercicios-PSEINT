#Ejercicio 7: Factorial con while
#•	Uso de una estructura de repetición y un acumulador multiplicativo (*=).
#•	Lógica matemática del factorial: n! = n × (n−1) × ... × 1.

num = int(input("Ingresa un número para factorial: "))
fac = 1 
i = 1

while i <= num: 
    fac *= i 
    i += 1 
print(f"El factorial de {num} es {fac}")
