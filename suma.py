print("--- Calculadora de Promedio ---")

# 1. Asignación de las 10 notas a variables
#    Usamos float para representar valores con decimales.

estudiante1 = nota1 = 8.0
estudiante2 = nota2 = 6.0
estudiante3 = nota3 = 9.5
estudiante4 = nota4 = 7.0
estudiante5 = nota5 = 5.5
estudiante6 = nota6 = 10.0
estudiante7 = nota7 = 8.5
estudiante8 = nota8 = 6.5
estudiante9 = nota9 = 7.5
estudiante10 = nota10 = 9.0

# ----------------------------------------------------
# 1B. Mostrar el detalle de las notas (como solicitaste)
# ----------------------------------------------------
print("\n--- Detalle de Notas Registradas ---")
print(f"Estudiante 1 (nota1): {nota1:.2f}")
print(f"Estudiante 2 (nota2): {nota2:.2f}")
print(f"Estudiante 3 (nota3): {nota3:.2f}")
print(f"Estudiante 4 (nota4): {nota4:.2f}")
print(f"Estudiante 5 (nota5): {nota5:.2f}")
print(f"Estudiante 6 (nota6): {nota6:.2f}")
print(f"Estudiante 7 (nota7): {nota7:.2f}")
print(f"Estudiante 8 (nota8): {nota8:.2f}")
print(f"Estudiante 9 (nota9): {nota9:.2f}")
print(f"Estudiante 10 (nota10): {nota10:.2f}")
print("------------------------------------")


# 2. Calcular la SUMA de todas las notas
suma_total = nota1 + nota2 + nota3 + nota4 + nota5 + nota6 + nota7 + nota8 + nota9 + nota10

# 3. Calcular el PROMEDIO
promedio = suma_total / 10

# 4. Mostrar el resultado final
print("\n--- Resultado Final ---")
print(f"La Suma Total de las 10 notas es: {suma_total:.2f}")
print(f"El **Promedio** general es: **{promedio:.2f}**")
print("-----------------------")
