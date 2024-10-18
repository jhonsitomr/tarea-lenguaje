from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def arrancar(self):
        pass

    @abstractmethod
    def parar(self):
        pass

class Carro(Vehiculo):
    def arrancar(self):
        return "El carro está arrancando."

    def parar(self):
        return "El carro se ha detenido."

# Crear un objeto Carro
mi_carro = Carro()

# Utilizar los métodos
print(mi_carro.arrancar())  # Output: El carro está arrancando.
print(mi_carro.parar())     # Output: El carro se ha detenido.