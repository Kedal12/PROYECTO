from computador_portatil import ComputadorPortatil
from tableta_grafica import TabletaGrafica
from estudiante_ingenieria import EstudianteIngenieria
from estudiante_diseno import EstudianteDiseno

def importar_datos(archivo_texto, inventario_portatil, inventario_tableta, vector_ingenieros, vector_disenadores):
    try:
        # Crear conjuntos de identificadores únicos existentes como cadenas
        cedulas_ingenieros_existentes = {str(estudiante.cedula) for estudiante in vector_ingenieros}
        cedulas_disenadores_existentes = {str(estudiante.cedula) for estudiante in vector_disenadores}

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
                    cedula = str(cedula)  # Asegurarse de que la cédula sea una cadena
                    if cedula in cedulas_ingenieros_existentes:
                        print(f"El ingeniero con cédula {cedula} ya existe. No se añadirá.")
                        continue
                    print(f"Antes de añadir: {[(eng.cedula, eng.nombre) for eng in vector_ingenieros]}")
                    estudiante = EstudianteIngenieria(cedula, nombre, apellido, int(telefono), int(semestre), float(promedio), serial)
                    vector_ingenieros.append(estudiante)
                    cedulas_ingenieros_existentes.add(cedula)
                    print(f"Después de añadir: {[(eng.cedula, eng.nombre) for eng in vector_ingenieros]}")

                elif tipo == 'disenador':
                    cedula, nombre, apellido, telefono, modalidad, asignaturas, serial = datos[1:]
                    cedula = str(cedula)  # Asegurarse de que la cédula sea una cadena
                    if cedula in cedulas_disenadores_existentes:
                        print(f"El diseñador con cédula {cedula} ya existe. No se añadirá.")
                        continue
                    print(f"Antes de añadir: {[(des.cedula, des.nombre) for des in vector_disenadores]}")
                    estudiante = EstudianteDiseno(cedula, nombre, apellido, int(telefono), modalidad, int(asignaturas), serial)
                    vector_disenadores.append(estudiante)
                    cedulas_disenadores_existentes.add(cedula)
                    print(f"Después de añadir: {[(des.cedula, des.nombre) for des in vector_disenadores]}")

    except FileNotFoundError:
        print(f"El archivo '{archivo_texto}' no se encontró.")
    except Exception as e:
        print(f"Se produjo un error al importar datos: {e}")

    print("Importación completa.")
    print(f"Total computadores: {len(inventario_portatil)}")
    print(f"Total tabletas: {len(inventario_tableta)}")
    print(f"Total ingenieros: {len(vector_ingenieros)}")
    print(f"Total diseñadores: {len(vector_disenadores)}")

