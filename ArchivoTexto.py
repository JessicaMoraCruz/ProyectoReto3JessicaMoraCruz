def realizar_Archivo_Texto(nombre_archivo, texto):
    ## Se abre el archivo en modo a (append) para agregar contenido al final
    with open(nombre_archivo, "a") as archivo:
        ## con write escribe la linea de texto y salto de linea al final
        archivo.write(texto + "\n")