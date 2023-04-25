import pandas as pd
import time
import tkinter

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():

    doc = pd.read_excel("C:/Users/Edu guapo/Desktop/carpetaFicheros/TFG_pruebas_enlaces3.xls", header=None)

    dimension = doc.shape
    tamFilas = dimension[0]
    print(f"tamFilas: ", tamFilas)

    # Acceder a la primera fila
    columna = doc.iloc[:, 0]

    # Mostrar enlaces
    for x in columna:
        print(x)

    driver = webdriver.Chrome()

    for enlace in columna:
        driver.get(enlace)
        driver.maximize_window()
        wait = WebDriverWait(driver, 5)
        button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'barre')))
        time.sleep(3)
        button.click()
        time.sleep(3)

    driver.quit()

############################################################ VENTANA #########################################
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

def allInfo():
    return (inputRutaDocumento()+ "/" +inputNombreDocumento())
    #print("La ruta es: " + inputRutaDocumento() + inputNombreDocumento() + "El POM es: " + inputClasePom())

# BOTON EMPEZAR
botonInfo = tkinter.Button(ventana, text = "Introducir información", command=allInfo)
botonInfo.pack()

botonEjecutar = tkinter.Button(ventana, text = "Ejecutar programa", command=allInfo)
botonEjecutar.pack()





if __name__ == '__main__':
    ventana.mainloop()
    main()
