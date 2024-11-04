from prestamo_equipo import PrestamoEquipo
from estudiante_ingenieria import EstudianteIngenieria
from estudiante_diseno import EstudianteDiseno
from computador_portatil import ComputadorPortatil
from tableta_grafica import TabletaGrafica
from importar_datos import importar_datos
from exportar_datos import exportar_datos

def main():
    prestamo_equipo = PrestamoEquipo()  # Instancia de la clase de gestión de préstamos
    prestamo_equipo.inicializar_inventario()  # Inicializa el inventario con equipos predeterminados

    while True:
        # Menú principal para seleccionar acciones
        print("\nMenú Principal")
        print("1. Estudiantes de Ingeniería")
        print("2. Estudiantes de Diseño")
        print("3. Imprimir Inventario Total")
        print("4. Importar datos ")
        print("5. Exportar Datos")
        print("6. Agregar Nuevo Computador")
        print("7. Agregar Nueva Tableta")
        print("8. Salir")        
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            # Menú para gestionar estudiantes de ingeniería
            print("\nEstudiantes de Ingeniería")
            print("1.1 Registrar préstamo de equipo")
            print("1.2 Modificar préstamo de equipo")
            print("1.3 Devolución de equipo")
            print("1.4 Buscar equipo")
            print("1.5 Volver al menú principal")
            opcion_ingenieria = input("Seleccione una opción: ")

            if opcion_ingenieria == '1.1':
                # Mostrar equipos disponibles
                prestamo_equipo.mostrar_equipos_disponibles()
                # Registrar préstamo de un computador
                cedula = int(input("\n Ingrese cédula: "))
                nombre = str(input("Ingrese nombre: "))
                apellido = str(input("Ingrese apellido: "))
                telefono = int(input("Ingrese teléfono: "))
                semestre = int(input("Ingrese semestre: "))
                promedio = float(input("Ingrese promedio acumulado: "))
                serial = input("Ingrese serial del computador (ejemplo : MLX123): ")
                # Crea una instancia del estudiante
                estudiante = EstudianteIngenieria(cedula, nombre, apellido, telefono, semestre, promedio, serial)
                # Solicita el serial del computador
                computador_serial = input("Confirme e ingrese serial equipo: ")
                # Registra el préstamo
                prestamo_equipo.registrar_prestamo(estudiante, computador_serial)

            elif opcion_ingenieria == '1.2':
            # Modificar préstamo de un computador
                cedula = int(input("Ingrese cédula del estudiante: "))
                print("Ingrese nuevos datos del computador:")
                serial = input("Ingrese nuevo serial del computador: ")
                marca = input("Ingrese nueva marca del computador: ")
                tamaño = float(input("Ingrese nuevo tamaño en pulgadas: "))
                precio = float(input("Ingrese nuevo precio: "))
                print("Seleccione nuevo sistema operativo:")
                print("1. Windows 7")
                print("2. Windows 10")
                print("3. Windows 11")
                so = input("Seleccione una opción: ")
                sistema_operativo = { '1': 'Windows 7', '2': 'Windows 10', '3': 'Windows 11' }[so]
                print("Seleccione nuevo procesador:")
                print("1. AMD Ryzen")
                print("2. Intel® Core™ i5")
                proc = input("Seleccione una opción: ")
                procesador = { '1': 'AMD Ryzen', '2': 'Intel® Core™ i5' }[proc]

                # Crea una nueva instancia del computador
                nuevo_computador = ComputadorPortatil(serial, marca, tamaño, precio, sistema_operativo, procesador)
                # Modifica el préstamo existente
                prestamo_equipo.modificar_prestamo_ingenieria(cedula, nuevo_computador)

            elif opcion_ingenieria == '1.3':
                # Registrar la devolución de un computador
                cedula = int(input("Ingrese cédula del estudiante: "))
                prestamo_equipo.devolucion_equipo_ingenieria(cedula)

            elif opcion_ingenieria == '1.4':
                # Buscar equipo asociado a un estudiante
                cedula = int(input("Ingrese cédula del estudiante: "))
                equipo = prestamo_equipo.buscar_equipo(cedula)
                if equipo:
                    print(f"Equipo encontrado: {equipo.serial}")
                else:
                    print("No se encontró ningún equipo.")

            elif opcion_ingenieria == '1.5':
                # Regresar al menú principal
                continue
            else :
                print("Opcion no valida , selecciona una opcion entre 1 y 1.5 ")

        elif opcion == '2':
            # Menú para gestionar estudiantes de diseño
            print("\n Estudiantes de Diseño")
            print("2.1 Registrar préstamo de equipo")
            print("2.2 Modificar préstamo de equipo")
            print("2.3 Devolución de equipo")
            print("2.4 Buscar equipo")
            print("2.5 Volver al menú principal")
            opcion_diseno = input("Seleccione una opción: ")

            if opcion_diseno == '2.1':
                 # Mostrar equipos disponibles
                prestamo_equipo.mostrar_equipos_disponibles()
                # Registrar préstamo de una tableta
                cedula = int(input("\n Ingrese cédula: "))
                nombre = str(input("Ingrese nombre: "))
                apellido = str(input("Ingrese apellido: "))
                telefono = int(input("Ingrese teléfono: "))
                modalidad = input("Ingrese modalidad (virtual/presencial): ")
                asignaturas = int(input("Ingrese cantidad de asignaturas que está viendo: "))
                serial = input("Ingrese serial de la tableta (ejemplo : TBL123): ")
                # Verifica si la tableta está disponible antes de crear el objeto
                if serial not in [tableta.serial for tableta in prestamo_equipo.inventario_tableta]:
                    print("Error: La tableta no está disponible para préstamo.")
                    continue  # Vuelve al menú
                marca = input("Ingrese marca de la tableta: ")
                tamaño = float(input("Ingrese tamaño en pulgadas: "))
                precio = float(input("Ingrese precio: "))
                peso = float(input("Ingrese peso en kg: "))
                print("Seleccione almacenamiento:")
                print("1. 256 GB")
                print("2. 512 GB")
                print("3. 1 TB")
                almacenamiento = { '1': '256 GB', '2': '512 GB', '3': '1 TB' }[input("Seleccione una opción: ")]

                # Crea una instancia del estudiante y de la tableta
                estudiante = EstudianteDiseno(cedula, nombre, apellido, telefono, modalidad, asignaturas, serial)
                tableta = TabletaGrafica(serial, marca, tamaño, precio, almacenamiento, peso)
                # Registra el préstamo
                prestamo_equipo.registrar_prestamo_diseno(estudiante, tableta.serial)

            elif opcion_diseno == '2.2':
                # Modificar préstamo de una tableta
                cedula = int(input("Ingrese cédula del estudiante: "))
                print("Ingrese nuevos datos de la tableta:")
                serial = input("Ingrese nuevo serial de la tableta: ")
                marca = input("Ingrese nueva marca de la tableta: ")
                tamaño = float(input("Ingrese nuevo tamaño en pulgadas: "))
                precio = float(input("Ingrese nuevo precio: "))
                peso = float(input("Ingrese nuevo peso en kg: "))
                print("Seleccione nuevo almacenamiento:")
                print("1. 256 GB")
                print("2. 512 GB")
                print("3. 1 TB")
                almacenamiento = { '1': '256 GB', '2': '512 GB', '3': '1 TB' }[input("Seleccione una opción: ")]

                # Crea una nueva instancia de la tableta
                nueva_tableta = TabletaGrafica(serial, marca, tamaño, precio, almacenamiento, peso)
                # Modifica el préstamo existente
                prestamo_equipo.modificar_prestamo_diseno(cedula, nueva_tableta)

            elif opcion_diseno == '2.3':
                # Registrar la devolución de una tableta
                cedula = int(input("Ingrese cédula del estudiante: "))
                prestamo_equipo.devolucion_equipo_diseno(cedula)

            elif opcion_diseno == '2.4':
                # Buscar equipo asociado a un estudiante
                cedula = int(input("Ingrese cédula del estudiante: "))
                equipo = prestamo_equipo.buscar_equipo(cedula)
                if equipo:
                    print(f"Equipo encontrado: {equipo.serial}")
                else:
                    print("No se encontró ningún equipo.")

            elif opcion_diseno == '2.5':
                # Regresar al menú principal
                continue
            else :
                print("Opcion no valida , selecciona una opcion entre 2 y 2.5 ")

        elif opcion == '3':
            # Imprimir el inventario total de equipos
            prestamo_equipo.imprimir_inventario()
        elif opcion == '4':
            archivo_texto = input("Ingrese el nombre del archivo de texto para importar datos: ")
            # Importar datos
            importar_datos(archivo_texto, prestamo_equipo.inventario_portatil, 
                           prestamo_equipo.inventario_tableta, 
                           prestamo_equipo.vector_ingenieros, 
                           prestamo_equipo.vector_disenadores)
            print("Datos importados exitosamente.")
        elif opcion == '5':
            archivo_texto = input("Ingrese el nombre del archivo de texto para exportar datos: ")
            # Exportar datos
            exportar_datos(archivo_texto, prestamo_equipo.inventario_portatil, 
                           prestamo_equipo.inventario_tableta, 
                           prestamo_equipo.vector_ingenieros, 
                           prestamo_equipo.vector_disenadores)
            print("Datos exportados exitosamente.")
        
        elif opcion == '6':
            # Agregar nuevo computador
            serial = input("Ingrese serial del computador: ")
            marca = input("Ingrese marca del computador: ")
            tamaño = float(input("Ingrese tamaño en pulgadas: "))
            precio = input("Ingrese precio: ")
            print("Seleccione sistema operativo:")
            print("1. Windows 7")
            print("2. Windows 10")
            print("3. Windows 11")
            so = input("Seleccione una opción: ")
            sistema_operativo = { '1': 'Windows 7', '2': 'Windows 10', '3': 'Windows 11' }[so]
            print("Seleccione procesador:")
            print("1. AMD Ryzen")
            print("2. Intel® Core™ i5")
            proc = input("Seleccione una opción: ")
            procesador = { '1': 'AMD Ryzen', '2': 'Intel® Core™ i5' }[proc]

            # Llama al método para agregar el computador
            prestamo_equipo.agregar_computador(serial, marca, tamaño, precio, sistema_operativo, procesador)

        elif opcion == '7':
            # Agregar nueva tableta
            serial = input("Ingrese serial de la tableta: ")
            marca = input("Ingrese marca de la tableta: ")
            tamaño = float(input("Ingrese tamaño en pulgadas: "))
            precio = input("Ingrese precio: ")
            peso = float(input("Ingrese peso en kg: "))
            print("Seleccione almacenamiento:")
            print("1. 256 GB")
            print("2. 512 GB")
            print("3. 1 TB")
            almacenamiento = { '1': '256 GB', '2': '512 GB', '3': '1 TB' }[input("Seleccione una opción: ")]

            # Llama al método para agregar la tableta
            prestamo_equipo.agregar_tableta(serial, marca, tamaño, precio, almacenamiento, peso)

        elif opcion == '8':
            # Salir del programa
            print("Saliendo del programa.")
            break
        else:
         print("Opción no válida, por favor intente de nuevo.")
if __name__ == "__main__":
    # Ejecuta la función principal al iniciar el programa
    main()

