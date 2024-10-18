from abc import ABC, abstractmethod

class Navegable(ABC):
    @abstractmethod
    def navegar(self):
        pass

class Volador(ABC):
    @abstractmethod
    def volar(self):
        pass

class Hidroavion(Navegable, Volador):
    def navegar(self):
        return "El hidroavión está navegando."

    def volar(self):
        return "El hidroavión está volando."

# Crear un objeto Hidroavion
hidroavion = Hidroavion()

# Utilizar los métodos
print(hidroavion.navegar())  # Output: El hidroavión está navegando.
print(hidroavion.volar())    # Output: El hidroavión está volando.