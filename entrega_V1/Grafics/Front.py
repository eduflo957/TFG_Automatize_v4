import tkinter as tk

from entrega_V1.Logics import Fichero
from entrega_V1.Logics import Scrapping

# VARIABLES GLOBALES
rutaCompleta = ""

# VENTANA PRINCIPAL
ventana = tk.Tk()
ventana.geometry("600x500")

# IMAGEN LOGO
# imagenLogo = tk.PhotoImage(file="C:\\Users\\Edu guapo\\Desktop\\TFG_Automatize3\\entrega_V1\\Resources\\automatize_logo.png")
# label_imagen = tk.Label(ventana, image=imagenLogo)
# label_imagen.config(width=500, height=500)
# label_imagen.pack()

# TEXTO Y CAJA DE RUTA DOCUMENTO
etiquetaRutaEnlaces = tk.Label(ventana, text="Ruta de tu documento Excel: ")
etiquetaRutaEnlaces.pack()
etiquetaRutaEnlaces.place(x="100", y="100")
cajaRutaEnlaces = tk.Entry(ventana)
cajaRutaEnlaces.pack()
cajaRutaEnlaces.place(x="300", y="100", width="200")

# TEXTO Y CAJA DE NOMBRE DOCUMENTO
etiquetaNombreDocumento = tk.Label(ventana, text="Nombre de tu documento Excel: ")
etiquetaNombreDocumento.pack()
etiquetaNombreDocumento.place(x="100", y="150")
cajaNombreDocumento = tk.Entry(ventana)
cajaNombreDocumento.pack()
cajaNombreDocumento.place(x="300", y="150", width="200")

# TEXTO Y CAJA DE NOMBRE CLASE
etiquetaClasePom = tk.Label(ventana, text="Nombre de la clase del POM: ")
etiquetaClasePom.pack()
etiquetaClasePom.place(x="100", y="200")
cajaClasePom = tk.Entry(ventana)
cajaClasePom.pack()
cajaClasePom.place(x="300", y="200", width="200")


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
    etiquetaRutaCompleta = tk.Label(ventana, text= "La ruta completa es: " + rutaCompleta + "\nEl DOM introducido es :" + inputClasePom() +
                                         "\n\nAVISO: Si la ruta es correcta, ejecuta el programa, en caso contrario,"
                                         "\nvuelve a introducir la información")
    etiquetaRutaCompleta.pack()
    etiquetaRutaCompleta.place(relx=0.5, rely=0.5, anchor="center", y="90")

    # Cuando se pulse introducir información se mostrará el botón de guardar información
    # BOTON EJECUTAR
    botonEjecutar = tk.Button(ventana, text="Ejecutar programa", command=ejecutar)
    botonEjecutar.pack()
    botonEjecutar.place(relx=0.5, rely=0.5, anchor="center", y="170")



# BOTON GUARDAR INFORMACIÓN
botonInfo = tk.Button(ventana, text="Introducir información", command=guardarInfo)
botonInfo.pack()
botonInfo.place(relx=0.5, rely=0.5, anchor="center", y="30")







