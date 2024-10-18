from abc import ABC, abstractmethod

class Empleado(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass

    @abstractmethod
    def mostrar_info(self):
        pass

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salario_mensual):
        self.nombre = nombre
        self.salario_mensual = salario_mensual

    def calcular_salario(self):
        return self.salario_mensual

    def mostrar_info(self):
        print(f"Empleado de tiempo completo: {self.nombre}")
        print(f"Salario mensual: ${self.calcular_salario()}")

class EmpleadoMedioTiempo(Empleado):
    def __init__(self, nombre, horas_trabajadas, pago_por_hora):
        self.nombre = nombre
        self.horas_trabajadas = horas_trabajadas
        self.pago_por_hora = pago_por_hora

    def calcular_salario(self):
        return self.horas_trabajadas * self.pago_por_hora

    def mostrar_info(self):
        print(f"Empleado de medio tiempo: {self.nombre}")
        print(f"Salario: ${self.calcular_salario()}")

# Crear objetos de las clases derivadas
empleado_tiempo_completo = EmpleadoTiempoCompleto("Juan Pérez", 3000)
empleado_medio_tiempo = EmpleadoMedioTiempo("Ana García", 80, 15)

# Mostrar la información de los empleados
empleado_tiempo_completo.mostrar_info()
print()
empleado_medio_tiempo.mostrar_info()