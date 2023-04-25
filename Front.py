import tkinter

import Fichero
import Scrapping

ventana = tkinter.Tk()
ventana.geometry("600x500")

# CAJA DE RUTA DOCUMENTO
etiqueta = tkinter.Label(ventana, text="Ruta de tu documento Excel")
# pack es más o menos el CSS de TKINTER
etiqueta.pack()
cajaRutaEnlaces = tkinter.Entry(ventana)
cajaRutaEnlaces.pack()
def inputRutaDocumento():
    return cajaRutaEnlaces.get()

# CAJA DE NOMBRE DOCUMENTO
etiqueta = tkinter.Label(ventana, text="Nombre de tu documento Excel")
etiqueta.pack()
cajaNombreDocumento = tkinter.Entry(ventana)
cajaNombreDocumento.pack()
def inputNombreDocumento():
    return cajaNombreDocumento.get()


# CAJA DE NOMBRE CLASE
etiqueta = tkinter.Label(ventana, text="Nombre de la clase del POM")
# pack es más o menos el CSS de TKINTER
etiqueta.pack()
cajaClasePom = tkinter.Entry(ventana)
cajaClasePom.pack()
def inputClasePom():
    return cajaClasePom.get()

def guardarInfo():
    inputRutaDocumento()
    inputNombreDocumento()
    inputClasePom()

# BOTON EMPEZAR
botonInfo = tkinter.Button(ventana, text = "Introducir información", command=guardarInfo())
botonInfo.pack()

botonEjecutar = tkinter.Button(ventana, text = "Ejecutar programa", command=Scrapping.doScrappingWeb(Fichero.readFichToArray(inputRutaDocumento(), inputNombreDocumento())))
botonEjecutar.pack()

