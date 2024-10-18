class Transformador:
    def transformar(self, datos):
        raise NotImplementedError("Subclases deben implementar este método")

class Sumador(Transformador):
    def transformar(self, datos):
        return sum(datos)

class Multiplicador(Transformador):
    def transformar(self, datos, factor=1):
        return [x * factor for x in datos]

# Ejemplo de uso:
sumador = Sumador()
resultado_suma = sumador.transformar([1, 2, 3, 4])
print("Suma:", resultado_suma)  # Output: Suma: 10

multiplicador = Multiplicador()
resultado_multiplicacion = multiplicador.transformar([1, 2, 3], 2)
print("Multiplicación:", resultado_multiplicacion)  # Output: Multiplicación: [2, 4, 6]