import Fichero
import Front
import Scrapping


def Main():
    Front.ventana.mainloop()
    Fichero.readFichToArray()
    Scrapping.doScrappingWeb()

#     REVISAR LOS PUTOS FUTUROS PORQUE LA FUNCIÓN DE EJECUTAR NECESITA DE ELLOS
# PORQUE HASTA QUE NO SE EJECUTE...


if __name__ == '__main__':
    Main()