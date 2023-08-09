#creado una clase Cola que tiene métodos para encolar elementos (encolar()) y 
# desencolar elementos (desencolar()). También tiene un método esta_vacia() para 
# verificar si la cola está vacía. Estamos utilizando una lista de Python como base
# para implementar la cola. La cola sigue la estructura FIFO (primero en entrar, primero en salir).
class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, elemento):
        self.items.append(elemento)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            return None

# Crear una instancia de la cola
cola = Cola()

# Encolar elementos
cola.encolar("Manzana")
cola.encolar("Banana")
cola.encolar("Naranja")

# Desencolar elementos
print(cola.desencolar())  # "Manzana"
print(cola.desencolar())  # "Banana"
print(cola.desencolar())  # "Naranja"
print(cola.desencolar())  # None, la cola está vacía