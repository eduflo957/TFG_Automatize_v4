import pandas as pd
import time

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


if __name__ == '__main__':
    main()
