class EstudianteDiseno:
    def __init__(self, cedula, nombre, apellido, telefono, modalidad, asignaturas, serial):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.modalidad = modalidad
        self.asignaturas = asignaturas
        self.serial = serial
        self.prestamo = None  # Almacena el equipo en préstamo
