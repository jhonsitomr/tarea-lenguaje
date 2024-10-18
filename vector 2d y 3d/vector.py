import math

class Norma:
    def calcular_norma(self, *args):
        raise NotImplementedError("Subclases deben implementar este método")

class Vector2D(Norma):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calcular_norma(self):
        return math.sqrt(self.x**2 + self.y**2)

class Vector3D(Norma):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def calcular_norma(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

# Ejemplo de uso:
vector2d = Vector2D(3, 4)
norma2d = vector2d.calcular_norma()
print("Norma del vector 2D:", norma2d)  # Output: Norma del vector 2D: 5.0

vector3d = Vector3D(1, 2, 2)
norma3d = vector3d.calcular_norma()
print("Norma del vector 3D:", norma3d)  # Output: Norma del vector 3D: 3.0