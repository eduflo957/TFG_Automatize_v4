import pandas as pd


def readFichToArray(rutaCompleta):

    doc = pd.read_excel(rutaCompleta, header=None)

    dimension = doc.shape
    tamFilas = dimension[0]
    print(f"tamFilas: ", tamFilas)

    # Acceder a la primera fila
    columna = doc.iloc[:, 0]

    arrayEnlaces = []

    for x in columna:
        arrayEnlaces.append(x)

    return arrayEnlaces
