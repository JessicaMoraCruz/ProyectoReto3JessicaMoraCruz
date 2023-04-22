import tkinter as tk

class inventarioInstrumentos:
    def __init__(self, ventana):
        # Configuración de la ventana principal
        self.ventana = ventana
        self.ventana.title("Inventario de instrumentos")

        # Etiquetas para los campos de entrada
        tk.Label(self.ventana, text="Instrumento: ").grid(row=0, column=0)
        tk.Label(self.ventana, text="Familia: ").grid(row=1, column=0)
        tk.Label(self.ventana, text="Cantidad: ").grid(row=2, column=0)

        # Campos de entrada
        self.producto = tk.Entry(self.ventana)
        self.producto.grid(row=0, column=1)
        self.familia = tk.Entry(self.ventana)
        self.familia.grid(row=1, column=1)
        self.cantidad = tk.Entry(self.ventana)
        self.cantidad.grid(row=2, column=1)

        # Botones para agregar y eliminar elementos del inventario
        tk.Button(self.ventana, text="Agregar", command=self.agregar).grid(row=3, column=0)
        tk.Button(self.ventana, text="Eliminar", command=self.eliminar).grid(row=3, column=1)

        # Lista para mostrar el inventario
        self.lista = tk.Listbox(self.ventana)
        self.lista.grid(row=4, columnspan=2)

    def agregar(self):
        # Agregar el producto y la cantidad a la lista
        self.lista.insert(tk.END, f"{self.producto.get()} - {self.familia.get()} - {self.cantidad.get()}")

        # Limpiar los campos una vez que se agreguen a la lista
        self.producto.delete(0, tk.END)
        self.familia.delete(0, tk.END)
        self.cantidad.delete(0, tk.END)

    def eliminar(self):
        # Eliminar el elemento seleccionado de la lista
        seleccion = self.lista.curselection()
        if seleccion:
            self.lista.delete(seleccion)


# Crear la ventana principal y el inventario
ventana = tk.Tk()
inventarioInstrumentos = inventarioInstrumentos(ventana)



# Iniciar el bucle de eventos
ventana.mainloop()

def llamar_interfaz():
    mi_interfaz = inventarioInstrumentos()
    mi_interfaz.abrir.interfaz()
