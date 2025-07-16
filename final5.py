# ciclo for

# Solicitar el número al usuario
num = int(input("Ingrese un número para ver su tabla de multiplicar: "))

# Usar el ciclo for para mostrar la tabla del 1 al 10
print(f"\nTabla de multiplicar del {num}:\n")

for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")