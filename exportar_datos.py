def exportar_datos(archivo_texto, inventario_portatil, inventario_tableta, vector_ingenieros, vector_disenadores):
    with open(archivo_texto, 'w') as file:
        for computador in inventario_portatil:
            file.write(f'computador,{computador.serial},{computador.marca},{computador.tamaño},{computador.precio},{computador.sistema_operativo},{computador.procesador}\n')
        
        for tableta in inventario_tableta:
            file.write(f'tableta,{tableta.serial},{tableta.marca},{tableta.tamaño},{tableta.precio},{tableta.almacenamiento},{tableta.peso}\n')

        for ingeniero in vector_ingenieros:
            file.write(f'ingeniero,{ingeniero.cedula},{ingeniero.nombre},{ingeniero.apellido},{ingeniero.telefono},{ingeniero.semestre},{ingeniero.promedio},{ingeniero.serial}\n')
        
        for disenador in vector_disenadores:
            file.write(f'disenador,{disenador.cedula},{disenador.nombre},{disenador.apellido},{disenador.telefono},{disenador.modalidad},{disenador.asignaturas},{disenador.serial}\n')
