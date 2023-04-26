import tkinter as tk

from entrega_V1.Logics import Fichero
from entrega_V1.Logics import Scrapping

# VARIABLES GLOBALES
rutaCompleta = ""

# VENTANA PRINCIPAL
ventana = tk.Tk()
ventana.geometry("800x600")
ventana.configure(bg='#FFFFFF')

# IMAGEN LOGO
imagenLogo = tk.PhotoImage(
    file="C:\\Users\\Edu guapo\\Desktop\\TFG_Automatize3\\entrega_V1\\Grafics\\automatize_logo_2.png")
cajaImagen = tk.Label(ventana, image=imagenLogo)
cajaImagen.pack()
cajaImagen.place(relx=0.5, rely=0.15, anchor="center")
cajaImagen.configure(bg='#FFFFFF')

# TEXTO Y CAJA DE RUTA DOCUMENTO
etiquetaRutaEnlaces = tk.Label(ventana, text="Ruta de tu documento Excel: ")
etiquetaRutaEnlaces.pack()
etiquetaRutaEnlaces.place(x="100", y="150")
etiquetaRutaEnlaces.configure(bg='#FFFFFF')

cajaRutaEnlaces = tk.Entry(ventana)
cajaRutaEnlaces.pack(pady=10, padx=10)
cajaRutaEnlaces.place(x="300", y="150", width="400")

# TEXTO Y CAJA DE NOMBRE DOCUMENTO
etiquetaNombreDocumento = tk.Label(ventana, text="Nombre de tu documento Excel: ")
etiquetaNombreDocumento.pack()
etiquetaNombreDocumento.place(x="100", y="200")
etiquetaNombreDocumento.configure(bg='#FFFFFF')

cajaNombreDocumento = tk.Entry(ventana)
cajaNombreDocumento.pack()
cajaNombreDocumento.place(x="300", y="200", width="400")

# TEXTO Y CAJA DE NOMBRE CLASE
etiquetaClasePom = tk.Label(ventana, text="Nombre de la clase del POM: ")
etiquetaClasePom.pack()
etiquetaClasePom.place(x="100", y="250")
etiquetaClasePom.configure(bg='#FFFFFF')
cajaClasePom = tk.Entry(ventana)
cajaClasePom.pack()
cajaClasePom.place(x="300", y="250", width="400")


# RECOLECCIÓN DE DATOS
def inputRutaDocumento():
    return cajaRutaEnlaces.get()


def inputNombreDocumento():
    return cajaNombreDocumento.get()


def inputClasePom():
    return cajaClasePom.get()


def ejecutar():
    global rutaCompleta
    Scrapping.doScrappingWeb(
        Fichero.readFichToArray(rutaCompleta))


def guardarInfo():
    global rutaCompleta
    rutaCompleta = inputRutaDocumento() + "/" + inputNombreDocumento()
    # TEXTO Y CAJA DE TODA LA INFORMACIÓN
    etiquetaRutaCompleta = tk.Label(ventana,
                                    text="El programa se ejecutará con la siguiente información:\n"
                                    "Ruta completa: " + rutaCompleta + "\nEl DOM introducido es :" + inputClasePom() +
                                         "\n\nAVISO: Si la ruta es correcta, ejecuta el programa, en caso contrario,"
                                         "\nvuelve a introducir la información")
    etiquetaRutaCompleta.pack()
    etiquetaRutaCompleta.place(relx=0.5, rely=0.5, anchor="center", y="150")
    etiquetaRutaCompleta.configure(bg="#95FCA1")

    # Cuando se pulse introducir información se mostrará el botón de guardar información
    # BOTON EJECUTAR
    botonEjecutar = tk.Button(ventana, text="Ejecutar programa", command=ejecutar)
    botonEjecutar.pack()
    botonEjecutar.place(relx=0.5, rely=0.5, anchor="center", y="240")
    botonEjecutar.configure(bg='#28df28')
6

# BOTON GUARDAR INFORMACIÓN
botonInfo = tk.Button(ventana, text="Introducir información", command=guardarInfo)
botonInfo.pack()
botonInfo.place(relx=0.5, rely=0.5, anchor="center", y="60")
