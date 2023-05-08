import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def doScrappingWeb(columna, busquedaXpath, botonSiNo, busquedaXpathPopup, dominio):
    botonSiNo = True
    driver = webdriver.Chrome()

    if botonSiNo == True:
        driver.get(dominio)
        driver.maximize_window()
        wait = WebDriverWait(driver, 3)
        buttonPopUp = wait.until(EC.presence_of_element_located((By.XPATH, busquedaXpathPopup)))

    time.sleep(5)

    for enlace in columna:
        driver.get(enlace)
        driver.maximize_window()
        wait = WebDriverWait(driver, 3)
        button = wait.until(EC.presence_of_element_located((By.XPATH, busquedaXpath)))
        time.sleep(2)
        button.click()
        time.sleep(2)

    driver.quit()
