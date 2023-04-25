import pandas as pd

def readFichToArray(rutaCarpeta, nomArchivo):
    rutaCompleta = rutaCarpeta + "/" + nomArchivo
    rutaCompletaToPythonFormat = rutaCompleta.replace("/", "\\")

    doc = pd.read_excel(rutaCompletaToPythonFormat, header=None)

    dimension = doc.shape
    tamFilas = dimension[0]
    print(f"tamFilas: ", tamFilas)

    # Acceder a la primera fila
    columna = doc.iloc[:, 0]

    return columna