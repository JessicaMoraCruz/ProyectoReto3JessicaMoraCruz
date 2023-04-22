import random


# Se utiliza el metodo Abstract Factory para que los usuarios visualicen informacion de venta de instrumentos.
class InformacionVentaInstrumentos:

    def __init__(self, BMA_instrumentos=None):
        """ Venta de instrumentos musicales """
        self.BMA_instrumentos = BMA_instrumentos
    def informacion_De_instrumentos_BMA(self):
        """Crea y muestra informacion usando el metodo: abstract factory"""
        programa = self.BMA_instrumentos()
        print("Necesita informacion sobre compra de instrumentos:  {} de la BMA?".format(programa))
        print("Su estado es  {} ".format(programa.estado()))
        print("Su precio sería {}".format(programa.precio()))
        print('\n')

class Nuevos:
    """ Clase instrumentos nuevos"""
    def estado(self):
        return "Completamente nuevo"
    def precio(self):
        return "350000 colones"
    def __str__(self):
        return "Nuevo"

class Usados_Bueno:
    """ Clase instrumentos usados buenos"""
    def estado(self):
        return "Bueno pero usado"
    def precio(self):
        return "150000 colones"
    def __str__(self):
        return "Usado pero bueno"

class Usado_Arreglar:
    """ Clase instrumentos para arreglar"""
    def estado(self):
        return "Para arreglar"
    def precio(self):
        return "25000 colones"
    def __str__(self):
        return "Para arreglar"

def programa_aleatorio():
    """ Se brinda informacion aleatoria para los usuarios"""
    return random.choice([Nuevos, Usados_Bueno, Usado_Arreglar])()
