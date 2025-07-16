# Algoritmo para calcular el salario de un trabajador

# Solicitar datos al usuario
nom = input("Ingrese el nombre del trabajador: ")

# Validar y convertir horas trabajadas
while True:
    try:
        H_laboradas = float(input("Ingrese la cantidad de horas trabajadas: "))
        if H_laboradas < 0:
            print("Las horas trabajadas no pueden ser negativas.")
        else:
            break
    except ValueError:
        print("Por favor ingrese un número válido.")

# Validar y convertir valor por hora
while True:
    try:
        v_hora = float(input("Ingrese el valor por hora trabajada: "))
        if v_hora < 0:
            print("El valor por hora no puede ser negativo.")
        else:
            break
    except ValueError:
        print("Por favor ingrese un número válido.")

# Calcular el salario total
sal_total = H_laboradas * v_hora

# Mostrar el resultado
print(f"\nResumen del salario de {nom}:")
print(f"Horas trabajadas: {H_laboradas}")
print(f"Valor por hora: ${v_hora:.2f}")
print(f"Salario total: ${sal_total:.2f}")
