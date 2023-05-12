from urllib.parse import urlparse

import pandas as pd


def readFichToArray(filePath):
    doc = pd.read_excel(filePath, header=None)

    dimension = doc.shape
    tamFilas = dimension[0]
    print(f"tamFilas: ", tamFilas)

    # Acceder a la primera fila
    columna = doc.iloc[:, 0]

    arrayEnlaces = []

    for x in columna:
        arrayEnlaces.append(x)

    return arrayEnlaces


def readFichFindDominio(filePath):
    doc = pd.read_excel(filePath, header=None)

    dimension = doc.shape
    tamFilas = dimension[0]
    print(f"tamFilas: ", tamFilas)

    # Acceder a la primera fila
    columna = doc.iloc[:, 0]

    enlaceInicial = columna[0]
    dominioInicial = urlparse(enlaceInicial)
    dominioAccesible = dominioInicial.scheme + "://" + dominioInicial.netloc + "/"
    print(dominioAccesible)

    return dominioAccesible
