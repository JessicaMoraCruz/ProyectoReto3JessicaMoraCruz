listaEstudiantes=[]

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
def registrarEstudiante():
    print("Registro de Estudiantes\n")
    cedula = int(input("Ingrese el numero de cedula: "))
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    instrumento = input("Ingrese el instrumento: ")
    edad = int(input("Ingrese su edad: "))
    objEstudiante = Estudiantes(cedula, nombre, apellido, instrumento, edad)
    listaEstudiantes.append(objEstudiante)

def listadoEstudiantes():
    print("Lista de Estudiantes\n")
    for objEstudiante in listaEstudiantes:
        objEstudiante.imprimirDatos()


def buscarEstudiante():
    print("Buscar Estudiante\n")
    cedula = int(input("Ingrese el numero de cedula a buscar: "))
    for objEstudiante in listaEstudiantes:
        if cedula == objEstudiante.cedula:
            objEstudiante.imprimirDatos()


def modificarDatos():
    print("Modificar Instrumento\n")
    cedula = int(input("Ingrese el numero de cedula a buscar: "))
    for objEstudiante in listaEstudiantes:
        if cedula == objEstudiante.cedula:
            instrumento = input("Ingrese nuevo instrumento: ")
            objEstudiante.editarDatos(instrumento)
            objEstudiante.imprimirDatos()
            recepcionMensaje = objEstudiante.incluirEvento(instrumento)
            objEstudiante.historial.append(recepcionMensaje)


def consultarHistorial():
    print("Consulta de Historial\n")
    cedula = int(input("Ingrese el numero de cedula a buscar: "))
    for objEstudiante in listaEstudiantes:
        if cedula == objEstudiante.cedula:
            for recepcionMensaje in objEstudiante.historial:
                print("Evento: {}".format(recepcionMensaje))
