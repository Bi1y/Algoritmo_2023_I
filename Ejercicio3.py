import math

# calcule el área de un círculo
# Constantes Pi = 3.14
# Variables Radio, area = real
Pi = 3.14
radio = 0.0
area = 0.0

# Imprimir "Introduce el radio: "
print("Introduce el radio: ")

# Leer radio
radio = float(input())
area = radio * radio * Pi
# Imprimir "El área del círculo es:", area
print("El área del círculo es:", area)
# Fin