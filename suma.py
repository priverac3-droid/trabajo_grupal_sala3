print("--- Calculadora de Promedio ---")

# 1. Pedir las 10 notas y guardarlas en 10 variables diferentes
#    Usamos float() para asegurarnos de que se puedan ingresar decimales
nota1 = float(input("Ingresa la Nota 1: "))
nota2 = float(input("Ingresa la Nota 2: "))
nota3 = float(input("Ingresa la Nota 3: "))
nota4 = float(input("Ingresa la Nota 4: "))
nota5 = float(input("Ingresa la Nota 5: "))
nota6 = float(input("Ingresa la Nota 6: "))
nota7 = float(input("Ingresa la Nota 7: "))
nota8 = float(input("Ingresa la Nota 8: "))
nota9 = float(input("Ingresa la Nota 9: "))
nota10 = float(input("Ingresa la Nota 10: "))

# 2. Calcular la SUMA de todas las notas
#    Se suma cada una de las 10 variables
suma_total = nota1 + nota2 + nota3 + nota4 + nota5 + nota6 + nota7 + nota8 + nota9 + nota10

# 3. Calcular el PROMEDIO
#    El divisor es directamente 10, ya que sabemos que son 10 notas
promedio = suma_total / 10

# 4. Mostrar el resultado
print("\n--- Resultado ---")
print(f"La Suma Total es: {suma_total:.2f}")
print(f"El **Promedio** de las 10 notas es: **{promedio:.2f}**")
print("-----------------")
