
import os
## Se hace un llamado de la funcion y se incluye un archivo de texto de la reñesa de la banda
from ArchivoTexto import realizar_Archivo_Texto
from RegistroEstudiantes import registrarEstudiante, listadoEstudiantes,buscarEstudiante, modificarDatos, consultarHistorial
realizar_Archivo_Texto("nuevo_archivo.txt", "La banda tiene historia desde el anio 2008, donde se han obtenido premios!")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def main():
    print("____________________________________________________________________________")
    print("                       Bienvenido estimado usuario")
    print("____________________________________________________________________________")
    print("")

    print("A continuacion se muestran los nombres de las personas autorizadas a llenar lo que se le solicita")
    print("Jose", "Julio", "Axel", "Jessica", "Ernesto")
    # Aquí se está utilizando una tupla de nombres que no va a variar mientras se ejecuta
    profesores_encargados = ["Jose", "Julio", "Axel", "Jessica", "Ernesto"]

    nombres = {"Juan": 25, "María": 30, "Pedro": 40}
    print(nombres["María"])  # Output: 30
    nombre = input("Estimado profesor por favor ingrese su nombre: ")
    if nombre in profesores_encargados:
        print("Usted está autorizado a editar, ya que se encuentra en la siguiente lista:")

    while True:
        clear()
        print("Por favor elija una de las siguientes opciones:");
        print("1.- Ingresar datos de estudiantes")
        print("2.- Mostrar datos de integrante")
        print("3.- Buscar Integrante")
        print("4.- Modificar Instrumento")
        print("5.- Consultar Instrumento Modificado")
        print("6.- Realizar inventario de instrumentos")
        print("7.- Calcular promedios de notas")
        print("8.- Imprimir historial de banda")
        print("9.- Eliminar el historial de la banda")
        print("10.- Salir\n")

        opcion = int(input("Opcion: "))

        if opcion == 1:
            registrarEstudiante()
        elif opcion == 2:
            listadoEstudiantes()
        elif opcion == 3:
            buscarEstudiante()
        elif opcion == 4:
            modificarDatos()
        elif opcion == 5:
            consultarHistorial()
        elif opcion == 6:
            from InterfazInventario import llamar_interfaz
            llamar_interfaz()
        elif opcion == 7:
            from InterfazPromedio import Calcular_promedio
            Calcular_promedio()
        elif opcion == 8:
            # Abre el archivo de texto en modo lectura
            archivo = open("nuevo_archivo.txt", "r")

            # Lee el contenido del archivo y lo almacena en una variable
            contenido = archivo.read()

            # Imprime el contenido del archivo en pantalla
            print(contenido)

            # Cierra el archivo
            archivo.close()
        elif opcion == 9:
            # Nombre del archivo que deseas eliminar
            nuevo_archivo = "archivo.txt"

            # Eliminar el archivo
            os.remove(nuevo_archivo)
        elif opcion == 10:
            break
        # Pregunta si se desea volver al menu
        i = input("\nDesea volver al menu principal (s/n). Si elige NO se le mostrara informacion de instrumentos BMA")
        if i == 'n' or i == 'N':
            break

if __name__ == "__main__":
    main()
    from PatronAbstractFactory import InformacionVentaInstrumentos, programa_aleatorio
    programa = InformacionVentaInstrumentos(programa_aleatorio)
    for i in range(5):
        programa.informacion_De_instrumentos_BMA()

