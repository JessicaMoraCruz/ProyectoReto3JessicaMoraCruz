import tkinter as tk


## Se hace un llamado de la funcion y se incluye un archivo de texto de la reñesa de la banda
from ArchivoTexto import realizar_Archivo_Texto

realizar_Archivo_Texto("nuevo_archivo.txt", "La banda tiene historia desde el anio 2008, donde se han obtenido premios!")


def main():
    while True:
        print("1. Abrir la interfaz gráfica")
        print("2. Abrir la interfaz gráfica")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            from InterfazInventario import llamar_interfaz
            llamar_interfaz()
        if opcion == "2":
            from MenuInterfaz import Calcular_promedio
            Calcular_promedio()
        elif opcion == "3":
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
