#creado una clase Pila que tiene métodos para apilar elementos (apilar()) y desapilar elementos 
# (desapilar()). También tiene un método esta_vacia() para verificar si la pila está vacía. Estamos 
# utilizando una lista de Python como base para implementar la pila. La pila sigue la estructura LIFO 
# (último en entrar, primero en salir).
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

# Crear una instancia de la pila
pila = Pila()

# Apilar elementos
pila.apilar(10)
pila.apilar(20)
pila.apilar(30)

# Desapilar elementos
print(pila.desapilar())  # 30
print(pila.desapilar())  # 20
print(pila.desapilar())  # 10
print(pila.desapilar())  # None, la pila está vacía
