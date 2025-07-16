#Ejercicio 9: Sumar hasta que el usuario escriba 0
#•	Bucle while controlado por entrada del usuario.
#•	Acumulador que suma mientras no se ingrese 0.
contador=0
salida=0

num = int(input("Ingresa un número, si digitas CERO (0) vas a salir del programa): "))
while num != salida: 
    contador += num 
    num = int(input("Ingresa otro número, si digitas CERO (0) vas a salir del programa: "))

print(f"La suma de todos los numeros es: {contador}")

