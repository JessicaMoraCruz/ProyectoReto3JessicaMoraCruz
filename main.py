import os

from RegistroEstudiantes import RegistroEstudiantes
## Para limpiar pantalla
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
## Metodo main
def main():
    ## Se da la bienvenida al usuario
    print("____________________________________________________________________________")
    print("                       Bienvenido estimado usuario")
    print("____________________________________________________________________________")
    print("")
    ## Se imprimen los nombres de los profesores autorizados
    print("A continuacion se muestran los nombres de las personas autorizadas a llenar lo que se le solicita")
    print("Jose", "Julio", "Axel", "Jessica", "Ernesto")
    # Aquí se está utilizando una tupla de nombres que no va a variar mientras se ejecuta
    profesores_encargados = ["Jose", "Julio", "Axel", "Jessica", "Ernesto"]

    ## Ejemplo de diccionario
    nombres = {"Jose": 25, "Julio": 30, "Axel": 40, "Jessica" : 50, "Ernesto" : 60}
    ## Se imprime el código del profesor Julio que representa su edad
    print(nombres["Julio"])  # Output: 30
    ## Se solicita que ingrese el nombre del profesor que está editando
    nombre = input("Estimado profesor por favor ingrese su nombre: ")
    if nombre in profesores_encargados:
        print("Usted está autorizado a editar, ya que se encuentra en la siguiente lista:")
    ## Ejemplo de singleton como si existieran dos registros
    registro_de_estudiantes_1 = RegistroEstudiantes()
    registro_de_estudiantes_2 = RegistroEstudiantes()
    ## Se realiza un while para repetir el menú cada vez que el usuario indica que si desea volver a ver el menpú
    while True:
        clear()
        ## Se imprimen las opciones del menú
        print("Por favor elija una de las siguientes opciones:");
        ## los primeros números representan el registro de estudiantes
        print("1.- Ingresar datos de estudiantes")
        print("2.- Mostrar datos de estudiantes")
        print("3.- Buscar estudiante")
        print("4.- Modificar Instrumento")
        print("5.- Consultar Instrumento Modificado")
        ## luego se realiza por medio de una interfaz el inventario de instrumentos
        print("6.- Realizar inventario de instrumentos")
        ## luego se realiza por medio de una interfaz el cálculo de promedios de estudiantes
        print("7.- Calcular promedios de notas de estudiante")
        ## Se imprime el historial de los datos de estudiantes ingresados en el archivo de texto
        print("8.- Imprimir historial de estudiantes")
        ## Se elimina el historia en el archivo de texto
        print("9.- Eliminar el historial de estudiantes")
        print("10.- Salir\n")

        opcion = int(input("Opcion: "))
        ## según la opción se hace un llamado de la funcion
        if opcion == 1:
            registro_de_estudiantes_1.registrarEstudiante()
        elif opcion == 2:
            registro_de_estudiantes_2.listadoEstudiantes()
        elif opcion == 3:
            registro_de_estudiantes_1.buscarEstudiante()
        elif opcion == 4:
            registro_de_estudiantes_1.modificarDatos()
        elif opcion == 5:
            registro_de_estudiantes_1.consultarHistorial()
        elif opcion == 6:
            try:
                from InterfazInventario import llamar_interfaz
                llamar_interfaz()
            except:
                print("")
        elif opcion == 7:
            ## se utilizan excepciones
            try:
                from InterfazPromedio import Calcular_promedio
                Calcular_promedio()
            except:
                print("")
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
            nuevo_archivo = "nuevo_archivo.txt"

            # Elimina la información del archivo
            with open(nuevo_archivo, 'w') as archivo:
                archivo.write('')

        elif opcion == 10:
            break
        # Pregunta si se desea volver al menu
        i = input("\nDesea volver al menu principal (s/n). Si elige NO se le mostrara informacion de instrumentos BMA\n")
        if i == 'n' or i == 'N':
            break

if __name__ == "__main__":
    main()
    ## Se hace un llamado de la información utilizada con el patrón abstract factory
    from PatronAbstractFactory import InformacionVentaInstrumentos, programa_aleatorio
    programa = InformacionVentaInstrumentos(programa_aleatorio)
    for i in range(5):
        programa.informacion_De_instrumentos_BMA()

