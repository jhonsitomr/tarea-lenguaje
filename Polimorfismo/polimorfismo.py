class Empleado:
    def trabajar(self):
        return "Trabajando..."

class Desarrollador(Empleado):
    def trabajar(self):
        return "Escribiendo código."

class Diseñador(Empleado):
    def trabajar(self):
        return "Creando diseño gráfico."

class Gerente(Empleado):
    def trabajar(self):
        return "Gestionando el equipo."

def mostrar_trabajo(empleados):
    for empleado in empleados:
        print(empleado.trabajar())

# Crear objetos de las clases derivadas
desarrollador = Desarrollador()
diseñador = Diseñador()
gerente = Gerente()

# Crear una lista de empleados
empleados = [desarrollador, diseñador, gerente]

# Mostrar el trabajo de cada empleado
mostrar_trabajo(empleados)