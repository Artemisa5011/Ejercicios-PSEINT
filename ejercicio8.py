#Ejercicio 8: Adivina el número
#•	Condicional simple if-else.
#•	Comparación de valores para saber si el número ingresado coincide con el secreto.
num_secreto=88
adivina=int(input("Adivina el número (1-100): "))  
if num_secreto == adivina:
    print("BINGO!")
else:
    print("!FALLASTES¡. El número era:", adivina)
