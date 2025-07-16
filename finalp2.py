# Crear matriz 3x3 y llenarla con vocales ingresadas desde teclado
matriz = []
total_elementos = 9
contador = 0

print("Ingrese 9 vocales (a, e, i, o, u) para llenar una matriz 3x3:")
# Llenar la matriz
while contador < total_elementos:
    vocal = input(f"Ingrese la vocal #{contador + 1}: ").lower()
    
    if vocal in ['a', 'e', 'i', 'o', 'u'] and len(vocal) == 1:
        # Agregar a la matriz
        if contador % 3 == 0:
            matriz.append([vocal])  # Nueva fila
        else:
            matriz[-1].append(vocal)  # Añadir a la última fila
        contador += 1
    else:
        print("Entrada inválida. Solo se permiten las vocales: a, e, i, o, u.")

# Mostrar la matriz
print("\nMatriz 3x3 con las vocales ingresadas:")
for fila in matriz:
    print(fila)
