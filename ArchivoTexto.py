class ManejadorArchivosEstudiantes:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    def escribir_Archivo_Texto(self, texto):
        ## con write escribe la linea de texto y salto de linea al final
        with open(self.nombre_archivo, "a") as archivo:
            archivo.write(texto + "\n")

    ## MODIFICAR cedula-nombre-apellido-instrumento-edad
    def modificar_Archivo_Texto(self, cedula, instrumento):
        with open(self.nombre_archivo, "r") as archivo:
            # se obtienen las lineas del archivo de texto
            archivo_texto = archivo.readlines()

        # Se recorre el archivo por linea
        for numero_linea in range(len(archivo_texto)):
            # line = una linea separada por guiones del archivo de texto
            informacion = archivo_texto[numero_linea].split('-')

            # se compara la información en la posición cero de la línea (cédula) con la cédula entrante a modificar
            if informacion[0] == str(cedula):
                # se sobreescribe el instrumento
                informacion[3] = instrumento
                # se une la información en el formato separado por guiones para generar la nueva linea
                archivo_texto[numero_linea] = '-'.join(informacion)

        with open(self.nombre_archivo, "w") as archivo:
            # se actualiza el archivo con la nueva linea
            archivo.writelines(archivo_texto)