import tkinter as tk
from tkinter import filedialog

from entrega_V1.Logics import Fichero
from entrega_V1.Logics import Scrapping
from entrega_V1.Resources import Directorios

# VARIABLES GLOBALES
filePath = ""
clasePom = ""
popUp = False

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


# TEXTO Y CAJA DE Xpath
etiquetaXpath = tk.Label(ventana, text="Búsqueda XPATH: ")
etiquetaXpath.pack()
etiquetaXpath.place(x="100", y="250")
etiquetaXpath.configure(bg='#FFFFFF')
cajaXpath = tk.Entry(ventana)
cajaXpath.pack()
cajaXpath.place(x="300", y="250", width="400")


# TEXTO Y CAJA POP UP
etiquetaPopupInicial = tk.Label(ventana, text="¿Aparece un pop up inicial?"
                                              "\n(Abre la ruta padre en un navegador de incógnito,\n"
                                              "si aparece un PopUp, escribe su búsqueda Xpath)", anchor="w")
etiquetaPopupInicial.pack()
etiquetaPopupInicial.place(x="100", y="300")
etiquetaPopupInicial.configure(bg='#FFFFFF')


# Funciones para los botones
def botonSi():
    popUp=True
    print("popUp: "+str(popUp))
    etiquetaXpathPopUp.place(x="100", y="360")
    cajaXpathPopUp.place(x="300", y="360", width="400")

def botonNo():
    popUp=False
    print("popUp: "+str(popUp))
    etiquetaXpathPopUp.place_forget()
    cajaXpathPopUp.place_forget()

# Crear la etiqueta y la caja de texto
etiquetaXpathPopUp = tk.Label(ventana, text="Búsqueda XPATH del PopUp: ")
etiquetaXpathPopUp.configure(bg='#FFFFFF')
etiquetaXpathPopUp.place(x="100", y="1000")
cajaXpathPopUp = tk.Entry(ventana)
cajaXpathPopUp.place(x="300", y="1000", width="400")


etiquetaXpathPopUp = tk.Label(ventana, text="Búsqueda XPATH del PopUp: ")
etiquetaXpathPopUp.configure(bg='#FFFFFF')
etiquetaXpathPopUp.place(x="100", y="1000")
cajaXpathPopUp = tk.Entry(ventana)
cajaXpathPopUp.place(x="300", y="1000", width="400")

# Crear los botones
boton_si = tk.Button(ventana, text="Sí", command=botonSi)
boton_no = tk.Button(ventana, text="No", command=botonNo)
boton_si.place(x="400", y="310", width="40")
boton_no.place(x="460", y="310", width="40")



def inputClasePom():
    return cajaXpath.get()

def inputXpathPopup():
    return cajaXpathPopUp.get()


def ejecutar():
    global filePath
    global clasePom
    clasePom = inputClasePom()
    infoXpathPopup = inputXpathPopup()
    print(clasePom)
    Scrapping.doScrappingWeb(
        Fichero.readFichToArray(filePath), clasePom, popUp, infoXpathPopup, Fichero.readFichFindDominio(filePath))


# BOTON EJECUTAR
botonEjecutar = tk.Button(ventana, text="Ejecutar programa", command=ejecutar)
botonEjecutar.pack()
botonEjecutar.place(relx=0.5, rely=0.5, anchor="center", y="170")
botonEjecutar.configure(bg='#28df28')