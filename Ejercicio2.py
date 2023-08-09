# calcule el área de un triángulo recibiendo como entrada el valor de base y altura.
# Variables Altura, Base, Area.
altura = 0.0
base = 0.0
area = 0.0

# Imprimir "Introduce la base y la altura: "
print("Introduce la base y la altura: ")

# Leer base y altura
base = float(input("Base: "))
altura = float(input("Altura: "))

# Calcular el área
area = (base * altura) / 2

# Imprimir Area
print("El área del triángulo es:", area)

# Fin