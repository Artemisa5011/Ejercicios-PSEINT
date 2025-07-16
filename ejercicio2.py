#Ejercicio 2: Mayor de dos números
num1=float(input("ingresa el primer número: "))
num2=float(input("ingresa el secundo número: "))
if num1>num2:
    print(f"El número mayor es: {num1}")
elif num2>num1:
    print(f"El número mayor es: {num2}")
else:
    print("Los dos numeros son iguales")