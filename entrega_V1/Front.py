import tkinter
import Fichero
import Scrapping

rutaCompleta = ""

ventana = tkinter.Tk()
ventana.geometry("600x500")

# TEXTO Y CAJA DE RUTA DOCUMENTO
etiqueta = tkinter.Label(ventana, text="Ruta de tu documento Excel")
etiqueta.pack()
cajaRutaEnlaces = tkinter.Entry(ventana)
cajaRutaEnlaces.pack()
# cajaRutaEnlaces.place(x="300", y="100")

# TEXTO Y CAJA DE NOMBRE DOCUMENTO
etiqueta = tkinter.Label(ventana, text="Nombre de tu documento Excel")
etiqueta.pack()
cajaNombreDocumento = tkinter.Entry(ventana)
cajaNombreDocumento.pack()

# TEXTO Y CAJA DE NOMBRE CLASE
etiqueta = tkinter.Label(ventana, text="Nombre de la clase del POM")
etiqueta.pack()
cajaClasePom = tkinter.Entry(ventana)
cajaClasePom.pack()


# RECOLECCIÓN DE DATOS
def inputRutaDocumento():
    return cajaRutaEnlaces.get()


def inputNombreDocumento():
    return cajaNombreDocumento.get()


def inputClasePom():
    return cajaClasePom.get()


def guardarInfo():
    global rutaCompleta
    rutaCompleta = inputRutaDocumento() + "/" + inputNombreDocumento()
    # TEXTO Y CAJA DE TODA LA INFORMACIÓN
    etiqueta = tkinter.Label(ventana, text="La ruta completa es: " + rutaCompleta + "\nEl DOM introducido es :" + inputClasePom())
    etiqueta.pack()


# BOTON GUARDAR INFORMACIÓN
botonInfo = tkinter.Button(ventana, text="Introducir información", command=guardarInfo)
botonInfo.pack()


def ejecutar():
    global rutaCompleta
    Scrapping.doScrappingWeb(
        Fichero.readFichToArray(rutaCompleta))


# BOTON EJECUTAR
botonEjecutar = tkinter.Button(ventana, text="Ejecutar programa", command=ejecutar)
botonEjecutar.pack()
