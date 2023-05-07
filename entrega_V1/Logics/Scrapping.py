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
        wait = WebDriverWait(driver, 5)
        # urlOld = driver.current_url
        button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, stringClasePom)))
        time.sleep(3)
        button.click()
        time.sleep(3)
        # urlNew = driver.current_url


    driver.quit()
