from computador_portatil import ComputadorPortatil
from tableta_grafica import TabletaGrafica
from estudiante_ingenieria import EstudianteIngenieria
from estudiante_diseno import EstudianteDiseno

def importar_datos(archivo_texto, inventario_portatil, inventario_tableta, vector_ingenieros, vector_disenadores):
    try:
        # creamos una verificacion para que no se dupliquen ingenenieros ni deiseñadores
        cedulas_ingenieros_existentes = {estudiante.cedula for estudiante in vector_ingenieros}
        cedulas_disenadores_existentes = {estudiante.cedula for estudiante in vector_disenadores}

        with open(archivo_texto, 'r') as file:
            for line in file:
                datos = line.strip().split(',')
                tipo = datos[0].strip()

                if tipo == 'computador':
                    serial, marca, tamaño, precio, so, procesador = datos[1:]
                    if any(equipo.serial == serial for equipo in inventario_portatil):
                        print(f"El computador con serial {serial} ya existe. No se añadirá.")
                        continue
                    equipo = ComputadorPortatil(serial, marca, float(tamaño), float(precio), so, procesador)
                    inventario_portatil.append(equipo)

                elif tipo == 'tableta':
                    serial, marca, tamaño, precio, almacenamiento, peso = datos[1:]
                    if any(equipo.serial == serial for equipo in inventario_tableta):
                        print(f"La tableta con serial {serial} ya existe. No se añadirá.")
                        continue
                    equipo = TabletaGrafica(serial, marca, float(tamaño), float(precio), almacenamiento, float(peso))
                    inventario_tableta.append(equipo)

                elif tipo == 'ingeniero':
                    cedula, nombre, apellido, telefono, semestre, promedio, serial = datos[1:]
                    if cedula in cedulas_ingenieros_existentes:
                        print(f"El ingeniero con cédula {cedula} ya existe. No se añadirá.")
                        continue
                    estudiante = EstudianteIngenieria(cedula, nombre, apellido, int(telefono), int(semestre), float(promedio), serial)
                    vector_ingenieros.append(estudiante)
                    cedulas_ingenieros_existentes.add(cedula)

                elif tipo == 'disenador':
                    cedula, nombre, apellido, telefono, modalidad, asignaturas, serial = datos[1:]
                    if cedula in cedulas_disenadores_existentes:
                        print(f"El diseñador con cédula {cedula} ya existe. No se añadirá.")
                        continue
                    estudiante = EstudianteDiseno(cedula, nombre, apellido, int(telefono), modalidad, int(asignaturas), serial)
                    vector_disenadores.append(estudiante)
                    cedulas_disenadores_existentes.add(cedula)

    except FileNotFoundError:
        print(f"El archivo '{archivo_texto}' no se encontró.")
    except Exception as e:
        print(f"Se produjo un error al importar datos: {e}")

    print("Importación completa.")
    print(f"Total computadores: {len(inventario_portatil)}")
    print(f"Total tabletas: {len(inventario_tableta)}")
    print(f"Total ingenieros: {len(vector_ingenieros)}")
    print(f"Total diseñadores: {len(vector_disenadores)}")



