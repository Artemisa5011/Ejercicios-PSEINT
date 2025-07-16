#Ejercicio 20: Palíndromo
#•	Uso de indexación inversa ([::-1]) para comparar una cadena con su reverso.
#•	Comparación para determinar si es igual (palíndromo).
num=input("Ingresa un número: ")
if num==num[::-1]:
    print("El número es palíndromo")
else:
    print("El número no es palíndromo")

