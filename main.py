from gestion import GestionNomina

def mostrar_menu():
    print("\n////Menú Gestión de Nómina////")
    print("1. Agregar empleado")
    print("2. Registrar falta")
    print("3. Registrar bono")
    print("4. Calcular nómina")
    print("5. Guardar datos")
    print("6. Cargar datos")
    print("7. Salir")

def main():
    sistema = GestionNomina()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            identificacion = input("Identificación: ")
            nombre = input("Nombre: ")
            cargo = input("Cargo: ")
            salario = float(input("Salario: "))
            sistema.agregar_empleado(identificacion, nombre, cargo, salario)
            print(f"Empleado {nombre} agregado.")

        elif opcion == "2":
            identificacion = input("Identificación del empleado: ")
            fecha = input("Fecha de la falta (YYYY-MM-DD): ")
            print(sistema.registrar_falta(identificacion, fecha))

        elif opcion == "3":
            identificacion = input("Identificación del empleado: ")
            fecha = input("Fecha del bono (YYYY-MM-DD): ")
            valor = float(input("Valor del bono: "))
            concepto = input("Concepto del bono: ")
            print(sistema.registrar_bono(identificacion, fecha, valor, concepto))

        elif opcion == "4":
            identificacion = input("Identificación del empleado: ")
            nomina = sistema.calcular_nomina(identificacion)
            if isinstance(nomina, dict):
                print(f"\n--- Nómina de {identificacion} ---")
                for clave, valor in nomina.items():
                    print(f"{clave.capitalize()}: {valor}")
            else:
                print(nomina)
        elif opcion == "5":
          archivo = input("Nombre del archivo para guardar (con extensión .json): ")
          sistema.guardardatos(archivo)
          print("Datos guardados correctamente.")
        
        
        elif opcion == "6":
          
          archivo = input("Nombre del archivo para cargar (con extensión .json): ")
          sistema.cargardatos(archivo)
          print("Datos cargados correctamente.")

        elif opcion == "7":
          sistema.mostratDatos()  
        print("Datos mostrados correctamente.")
        
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida, intente de nuevo.")

if __name__ == "__main":
    main()
