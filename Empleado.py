
class Empleado:
    def init(self, identificacion, nombre, cargo, salario):
        self.identificacion = identificacion
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        self.faltas = []
        self.bonos = []

    def registrar_falta(self, fecha):
        """Registra una falta para un empleado"""
        self.faltas.append(fecha)

    def registrar_bono(self, fecha, valor, concepto):
        """Registra un bono extra-legal para un empleado"""
        self.bonos.append({"fecha": fecha, "valor": valor, "concepto": concepto})

    def calcular_nomina(self):
        """Calcula la nómina mensual del empleado"""
        salario_base = self.salario

        # Descuentos
        descuento_pension = salario_base * 0.045
        descuento_salud = salario_base * 0.04

        # Auxilio de transporte si el salario es menor a dos salarios mínimos (2 SMMLV = 2.000.000)
        auxilio_transporte = 140606 if self.salario < 2000000 else 0

        # Deducción por inasistencias
        dias_laborables = 30
        valor_dia = salario_base / dias_laborables
        deduccion_faltas = len(self.faltas) * valor_dia

        # Total de bonos
        total_bonos = sum(bono["valor"] for bono in self.bonos)

        # Nómina final
        nomina_final = salario_base - descuento_pension - descuento_salud - deduccion_faltas + auxilio_transporte + total_bonos

        return {
            "salario_base": salario_base,
            "descuento_pension": descuento_pension,
            "descuento_salud": descuento_salud,
            "deduccion_faltas": deduccion_faltas,
            "auxilio_transporte": auxilio_transporte,
            "total_bonos": total_bonos,
            "nomina_final": nomina_final
        }
