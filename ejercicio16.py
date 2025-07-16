#Ejercicio 16: Contador de vocales
#•	Recorre una cadena con for.
#•	Usa el operador in para verificar si un carácter es vocal.
frase= input("Ingresa una frase: ")
vocales=("aeiouAEIOU")
contador=0

for letra in frase:
    if letra in vocales:
        contador+= 1

print(f"La cantidad de vocales es: {contador}" )
