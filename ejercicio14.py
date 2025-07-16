#Ejercicio 14: Serie Fibonacci
#•	Generación de la serie de Fibonacci usando dos variables (a, b).
#•	Uso del bucle for.
num=int(input("Número de términos: "))
a, b=0, 1
for _ in range(num):
    print(a)
    a, b=b, a + b
