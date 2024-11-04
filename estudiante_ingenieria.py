class EstudianteIngenieria:
    def __init__(self, cedula, nombre, apellido, telefono, semestre, promedio, serial):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.semestre = semestre
        self.promedio = promedio
        self.serial = serial
        self.prestamo = None  # Almacena el equipo en préstamo
