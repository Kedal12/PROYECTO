from estudiante_ingenieria import EstudianteIngenieria
from estudiante_diseno import EstudianteDiseno
from tableta_grafica import TabletaGrafica
from computador_portatil import ComputadorPortatil

class PrestamoEquipo:
    def __init__(self):
        self.vector_ingenieros = []  # Lista para almacenar estudiantes de ingeniería
        self.vector_disenadores = []  # Lista para almacenar estudiantes de diseño
        self.inventario_portatil = []  # Inventario de computadores portátiles
        self.inventario_tableta = []  # Inventario de tabletas gráficas
        self.prestamos = {}  # Inicializa un diccionario para registrar préstamos

    def inicializar_inventario(self):
        # Inicializa el inventario con algunos equipos predeterminados
        self.inventario_portatil.append(ComputadorPortatil("MLX123", "HP", 15.6, 800, "Windows 10", "Intel® Core™ i5"))
        self.inventario_portatil.append(ComputadorPortatil("LMX321", "Dell", 14.0, 750, "Windows 11", "AMD Ryzen"))
        self.inventario_tableta.append(TabletaGrafica("TBL123", "Wacom", 13.3, 400, "512 GB", 1.2))
        self.inventario_tableta.append(TabletaGrafica("LTB321", "Huion", 12.0, 350, "256 GB", 1.0))
    
    def agregar_computador(self, serial, marca, tamaño, precio, sistema_operativo, procesador):
        nuevo_computador = ComputadorPortatil(serial, marca, tamaño, precio, sistema_operativo, procesador)
        self.inventario_portatil.append(nuevo_computador)
        print(f"Computador {serial} agregado exitosamente al inventario.")

    def agregar_tableta(self, serial, marca, tamaño, precio, almacenamiento, peso):
        nueva_tableta = TabletaGrafica(serial, marca, tamaño, precio, almacenamiento, peso)
        self.inventario_tableta.append(nueva_tableta)
        print(f"Tableta {serial} agregada exitosamente al inventario.")
    
    def imprimir_inventario(self):
        print("Inventario de Computadores:")
        for computador in self.inventario_portatil:
            print(f"Serial: {computador.serial}, Marca: {computador.marca}, Precio: {computador.precio}")

        print("\nInventario de Tabletas:")
        for tableta in self.inventario_tableta:
            print(f"Serial: {tableta.serial}, Marca: {tableta.marca}, Precio: {tableta.precio}")

    def registrar_prestamo(self, estudiante, computador_serial):
        # Verifica si el estudiante ya tiene un préstamo
        if estudiante.cedula in self.prestamos:
            print("Error: El estudiante ya tiene un equipo registrado.")
            return
        # Busca el computador en el inventario
        for computador in self.inventario_portatil:
            if computador.serial == computador_serial:
                self.prestamos[estudiante.cedula] = computador  # Registra el préstamo
                self.vector_ingenieros.append(estudiante)  # Agrega el estudiante al registro
                self.inventario_portatil.remove(computador)  # Elimina el computador del inventario
                print("Préstamo de computador registrado con éxito.")
                return
        print("Error: Computador no encontrado en el inventario.")

    def registrar_prestamo_diseno(self, estudiante, tableta_serial):
        # Verifica si el estudiante ya tiene un préstamo
        if estudiante.cedula in self.prestamos:
            print("Error: El estudiante ya tiene un equipo registrado.")
            return
        # Busca la tableta en el inventario
        for tableta in self.inventario_tableta:
            if tableta.serial == tableta_serial:
                self.prestamos[estudiante.cedula] = tableta  # Registra el préstamo
                self.vector_disenadores.append(estudiante)  # Agrega el estudiante al registro
                self.inventario_tableta.remove(tableta)  # Elimina la tableta del inventario
                print("Préstamo de tableta registrado con éxito.")
                return
        print("Error: Tableta no encontrada en el inventario.")

    def modificar_prestamo_ingenieria(self, cedula, nuevo_computador):
        if cedula in self.prestamos:
            self.prestamos[cedula] = nuevo_computador
            print("Préstamo de computador modificado con éxito.")
        else:
            print("Error: No se encontró ningún préstamo registrado para esta cédula.")

    def modificar_prestamo_diseno(self, cedula, nueva_tableta):
        if cedula in self.prestamos:
            self.prestamos[cedula] = nueva_tableta
            print("Préstamo de tableta modificado con éxito.")
        else:
            print("Error: No se encontró ningún préstamo registrado para esta cédula.")

    def buscar_equipo(self, cedula):
        # Busca un equipo en los préstamos usando la cédula
        if cedula in self.prestamos:
            return self.prestamos[cedula]
        else:
            print("No se encontró ningún equipo asociado a esta cédula.")
            return None

    def devolucion_equipo_ingenieria(self, cedula):
        # Verifica si el estudiante de ingeniería tiene un equipo en préstamo
        if cedula in self.prestamos:
            equipo_devuelto = self.prestamos.pop(cedula)
            self.inventario_portatil.append(equipo_devuelto)  # Agrega el computador al inventario
            print(f"El equipo con serial {equipo_devuelto.serial} ha sido devuelto y añadido al inventario.")
        else:
            print("No se encontró un equipo en préstamo para este estudiante de ingeniería.")

    def devolucion_equipo_diseno(self, cedula):
        # Verifica si el estudiante de diseño tiene una tableta en préstamo
        if cedula in self.prestamos:
            equipo_devuelto = self.prestamos.pop(cedula)
            self.inventario_tableta.append(equipo_devuelto)  # Agrega la tableta al inventario
            print(f"La tableta gráfica con serial {equipo_devuelto.serial} ha sido devuelta y añadida al inventario.")
        else:
            print("No se encontró una tableta en préstamo para este estudiante de diseño.")

    def mostrar_equipos_disponibles(self):
        print("Equipos disponibles para préstamo:")
        if not self.inventario_portatil and not self.inventario_tableta:
            print("No hay equipos disponibles.")
            return

        print("\nComputadores disponibles:")
        for computador in self.inventario_portatil:
            print(f"Serial: {computador.serial}, Marca: {computador.marca},Tamaño en pulgadas : {computador.tamaño}, Precio: {computador.precio}")

        print("\nTabletas disponibles:")
        for tableta in self.inventario_tableta:
            print(f"Serial: {tableta.serial}, Marca: {tableta.marca},Tamaño en pulgas : {tableta.tamaño}, Precio: {tableta.precio}, Almacenamiento : {tableta.almacenamiento},Peso : {tableta.peso}")       
