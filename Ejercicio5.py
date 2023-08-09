#  lea de entrada 3 números y que indique cual es el mayor de ellos.

# Variables a, b, c
print("Introduce los datos a comparar:")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
if a > b and a > c:
    print("El mayor es:", a)
elif b > a and b > c:
    print("El mayor es:", b)
else:
    print("El mayor es:", c)
# Fin