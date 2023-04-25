import tkinter as tk
from tkinter import messagebox
## Se realiza interfaz para calcular promedios
def Calcular_promedio():
    n1 = float(txtN1.get())
    n2 = float(txtN2.get())
    n3 = float(txtN3.get())
    prom = (n1+n2+n3)/3
    if prom < 70:
        messagebox.showwarning("Resultado",f"El promedio es: {prom:.2f}\n Ha perdido la materia.")
    elif prom >= 70 and prom <=100:
        messagebox.showinfo("Resultado",f"El promedio es: {prom:.2f}\n Ha ganado la materia")

root = tk.Tk()
root.title("Calcular Promedio")
root.geometry("300x300")

Etiqueta1 = tk.Label(root, text= "Nombre de estudiante:")
txtNE = tk.Entry(root)

Etiqueta2 = tk.Label(root, text= "Nota 1:")
txtN1 = tk.Entry(root)

Etiqueta3 = tk.Label(root, text= "Nota 2:")
txtN2 = tk.Entry(root)

Etiqueta4 = tk.Label(root, text= "Nota 3:")
txtN3 = tk.Entry(root)

btn_calcular = tk.Button(root, text="Promedio", command = Calcular_promedio)

Etiqueta1.grid(row=0,column=0)
txtNE.grid(row=0, column=1)

Etiqueta2.grid(row=1,column=0)
txtN1.grid(row=1, column=1)

Etiqueta3.grid(row=2 , column=0)
txtN2.grid(row=2, column=1)

Etiqueta4.grid(row=3 , column=0)
txtN3.grid(row=3, column=1)

btn_calcular.grid(row=4, column=0, columnspan=2, pady=10)
root.mainloop()