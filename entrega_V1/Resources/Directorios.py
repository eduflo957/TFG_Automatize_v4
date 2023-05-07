import os


def rutaRepositorio():
    #Cuando hagas la versión 4, tienes que modificar esto, para que coja el nombre del repositorio, quitando 2 puntos,
    # el join lo único que hace es subir de nivel.
    # recuerda que con os.path tienes muchos métodos
    dirName = os.path.abspath(os.path.join(__file__, "../../../"))
    return dirName
