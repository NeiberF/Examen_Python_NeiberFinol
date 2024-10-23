import json
from Empleado import Empleado

class GestionNomina:
    def init(self):
        self.empleados = []

    def agregar_empleado(self, identificacion, nombre, cargo, salario):
        """Agrega un nuevo empleado al sistema"""
        empleado = Empleado(identificacion, nombre, cargo, salario)
        self.empleados.append(empleado)

    def buscar_empleado(self, identificacion):
        """Busca un empleado por su identificación"""
        for empleado in self.empleados:
            if empleado.identificacion == identificacion:
                return empleado
        return None

    def registrar_falta(self, identificacion, fecha):
        """Registra una falta para un empleado específico"""
        empleado = self.buscar_empleado(identificacion)
        if empleado:
            empleado.registrar_falta(fecha)
            return f"Falta registrada para {empleado.nombre}"
        else:
            return "Empleado no encontrado"
def registrar_bono(self, identificacion, fecha, valor, concepto):
        """Registra un bono para un empleado específico"""
        empleado = self.buscar_empleado(identificacion)
        if empleado:
            empleado.registrar_bono(fecha, valor, concepto)
            return f"Bono registrado para {empleado.nombre}"
        else:
            return "Empleado no encontrado"

def calcular_nomina(self, identificacion):
        """Calcula la nómina de un empleado específico"""
        empleado = self.buscar_empleado(identificacion)
        if empleado:
            return empleado.calcular_nomina()
        else:
            return "Empleado no encontrado"

def guardar_datos(self, archivo):
        """Guarda la información de los empleados en un archivo JSON"""
        data = [{
            "identificacion": emp.identificacion,
            "nombre": emp.nombre,
            "cargo": emp.cargo,
            "salario": emp.salario,
            "faltas": emp.faltas,
            "bonos": emp.bonos
        } for emp in self.empleados]
        with open(archivo, 'w') as f:
            json.dump(data, f, indent=4)

def cargar_datos(self, archivo):
        """Carga la información de los empleados desde un archivo JSON"""
        with open(archivo, 'r') as f:
            data = json.load(f)
            for emp_data in data:
                empleado = Empleado(
                    emp_data['identificacion'],
                    emp_data['nombre'],
                    emp_data['cargo'],
                    emp_data['salario']
                )
                empleado.faltas = emp_data['faltas']
                empleado.bonos = emp_data['bonos']
                self.empleados.append(empleado)