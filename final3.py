# Crear un vector de 9 posiciones y llenarlo con números desde teclado
vector = []

print("Ingrese 9 números para llenar el vector:")

# Llenar el vector
for i in range(9):
    while True:
        try:
            num = int(input(f"Ingrese el número #{i + 1}: "))
            vector.append(num)
            break  # Salir del bucle si el número es válido
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número entero.")

# Mostrar el vector
print("\nVector con los números ingresados:")
print(vector)
