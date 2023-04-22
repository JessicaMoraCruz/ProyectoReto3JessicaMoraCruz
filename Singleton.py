class Singleton:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self):
        if not self.__initialized:
            self.__initialized = True
            # Inicializar la instancia aquí
def llamar_Singleton():
    # Ejemplo de uso con la Banda
    BandaMunicipalDeAcosta = Singleton()
    BMA = Singleton()
    ## Esto debería dar como resultado Verdadero
    print("Es lo mismo la instancia Banda Municipal de Acosta a instancia BMA")
    print(BandaMunicipalDeAcosta == BMA)

