import tkinter as tk
from tkinter import filedialog

from entrega_V1.Logics import Fichero
from entrega_V1.Logics import Scrapping
from entrega_V1.Resources import Directorios

# VARIABLES GLOBALES
filePath = ""
clasePom = ""

# VENTANA PRINCIPAL
ventana = tk.Tk()
ventana.geometry("800x600")
ventana.configure(bg='#FFFFFF')

# IMAGEN LOGO
imagenLogo = tk.PhotoImage(
    file=Directorios.rutaRepositorio() + "\\entrega_V1\\Grafics\\automatize_logo_2.png")
cajaImagen = tk.Label(ventana, image=imagenLogo)
cajaImagen.pack()
cajaImagen.place(relx=0.5, rely=0.15, anchor="center")
cajaImagen.configure(bg='#FFFFFF')


# TEXTO Y CAJA DE NOMBRE DOCUMENTO
etiquetaNombreDocumento = tk.Label(ventana, text="Selecciona tu documento Excel: ")
etiquetaNombreDocumento.pack()
etiquetaNombreDocumento.place(x="100", y="200")
etiquetaNombreDocumento.configure(bg='#FFFFFF')

cajaNombreDocumento = tk.Entry(ventana)
cajaNombreDocumento.pack()
cajaNombreDocumento.place(x="300", y="200", width="300")

# BOTÓN EXAMINAR
def open_file():
    global filePath
    filePath = filedialog.askopenfilename()
    cajaNombreDocumento.insert(0, filePath)
    print(filePath)
botonExaminar = tk.Button(ventana, text="Examinar", command=open_file)
botonExaminar.pack()
botonExaminar.place(x="600", y="200", width="100")


# TEXTO Y CAJA DE NOMBRE CLASE
etiquetaClasePom = tk.Label(ventana, text="Ruta XPATH: ")
etiquetaClasePom.pack()
etiquetaClasePom.place(x="100", y="250")
etiquetaClasePom.configure(bg='#FFFFFF')
cajaClasePom = tk.Entry(ventana)
cajaClasePom.pack()
cajaClasePom.place(x="300", y="250", width="400")

def inputClasePom():
    return cajaClasePom.get()


def ejecutar():
    global filePath
    global clasePom
    clasePom = inputClasePom()
    print(clasePom)
    Scrapping.doScrappingWeb(
        Fichero.readFichToArray(filePath), clasePom)


# BOTON EJECUTAR
botonEjecutar = tk.Button(ventana, text="Ejecutar programa", command=ejecutar)
botonEjecutar.pack()
botonEjecutar.place(relx=0.5, rely=0.5, anchor="center", y="100")
botonEjecutar.configure(bg='#28df28')