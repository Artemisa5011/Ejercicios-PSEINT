#Ejercicio 3: Menú con match-case
#•	Introduce el uso de match (nuevo en Python 3.10+) como una alternativa a múltiples if-elif.
#•	Cada case representa una opción del usuario.

seleccion=int(input("Selecciona la opción entre 1 al 3: "))
match seleccion:
    case 1:
        print("seleccionastes opción 1")
    case 2:
        print("seleccionastes opción 2")
    case 3:
        print("seleccionastes opción 3")
    case _:
        print("selección incorrecta, !Intentalo nuevamente¡")

