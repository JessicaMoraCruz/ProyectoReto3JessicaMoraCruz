import ArchivoTexto
## Se utiliza el patrón singleton para la clase registroEstudiantes
class RegistroEstudiantes:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self):
        if not self.__initialized:
            self.__initialized = True
            self.listaEstudiantes = []
            self.manejador_archivos = ArchivoTexto.ManejadorArchivosEstudiantes("nuevo_archivo.txt")


    def registrarEstudiante(self):
        print("Registro de Estudiantes\n")
        cedula = int(input("Ingrese el numero de cedula: "))
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        instrumento = input("Ingrese el instrumento: ")
        edad = int(input("Ingrese su edad: "))
        objEstudiante = Estudiantes(cedula, nombre, apellido, instrumento, edad)
        self.manejador_archivos.escribir_Archivo_Texto(str(cedula) + '-' + str(nombre) + '-' + str(apellido) + '-' + str(instrumento) + '-' + str(edad))
        self.listaEstudiantes.append(objEstudiante)

    def listadoEstudiantes(self):
        print("Lista de Estudiantes\n")
        for objEstudiante in self.listaEstudiantes:
            objEstudiante.imprimirDatos()


    def buscarEstudiante(self):
        print("Buscar Estudiante\n")
        cedula = int(input("Ingrese el numero de cedula a buscar: "))
        for objEstudiante in self.listaEstudiantes:
            if cedula == objEstudiante.cedula:
                objEstudiante.imprimirDatos()


    def modificarDatos(self):
        print("Modificar Instrumento\n")
        cedula = int(input("Ingrese el numero de cedula a buscar: "))
        for objEstudiante in self.listaEstudiantes:
            if cedula == objEstudiante.cedula:
                instrumento = input("Ingrese nuevo instrumento: ")
                objEstudiante.editarDatos(instrumento)
                objEstudiante.imprimirDatos()
                recepcionMensaje = objEstudiante.incluirEvento(instrumento)
                objEstudiante.historial.append(recepcionMensaje)
                self.manejador_archivos.modificar_Archivo_Texto(cedula, instrumento)


    def consultarHistorial(self):
        print("Consulta de Historial\n")
        cedula = int(input("Ingrese el numero de cedula a buscar: "))
        for objEstudiante in self.listaEstudiantes:
            if cedula == objEstudiante.cedula:
                for recepcionMensaje in objEstudiante.historial:
                    print("Evento: {}".format(recepcionMensaje))

# Se define la clase Integrante junto con sus parametros y 5 metodos donde se solicita datos y se realizan calculos
class Estudiantes:
    def __init__(self, _cedula, _nombre, _apellido, _instrumento, _edad):
        self.cedula = _cedula
        self.nombre = _nombre
        self.apellido = _apellido
        self.instrumento = _instrumento
        self.edad = _edad
        self.historial = []
        # Se utiliza la funcion format para indicar el orden de impresion junto con la ayuda de las {} llaves
    def imprimirDatos(self):
        print("Informacion estudiante: {} {} {} {} {}".format(self.cedula, self.nombre, self.apellido, self.instrumento, self.edad))
    # Se solicitan datos de las mensualidades
    def editarDatos(self, _instrumento):
        self.instrumento = _instrumento
        print("Registro Exitoso!")
    # Se utiliza la funcion format para indicar el orden de impresion, junto con la ayuda de las {} llaves
    def incluirEvento(self, _instrumento):
        return ("modificacion: Instrumento: {}".format(_instrumento))

    def entregaHistorial(self):
        print("No. Cedula: {} - {} {} {}".format(self.cedula, self.nombre, self.apellido, self.instrumento))

    # Lo siguiente corresponde a las opciones de menu, que se encontraria en el main. Esto se mostrara en consola

