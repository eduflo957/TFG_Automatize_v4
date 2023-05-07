import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def doScrappingWeb(columna, stringClasePom):
    driver = webdriver.Chrome()

    for enlace in columna:
        driver.get(enlace)
        driver.maximize_window()
        wait = WebDriverWait(driver, 3)
        button = wait.until(EC.presence_of_element_located((By.XPATH, stringClasePom)))
        time.sleep(2)
        button.click()
        time.sleep(2)


    driver.quit()
