from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys

import time
import selenium.webdriver.common.action_chains

class Teste:

    def __init__(self):
        driver = webdriver.Chrome(executable_path='chromedriver.exe')

        driver.get("https://www.terra.com.br")
        driver.switch_to_window(driver.window_handles[0])
        driver.implicitly_wait(3)

        driver.execute_script("window.open('https://www.google.com.br','new window')")
        driver.switch_to_window(driver.window_handles[1])
        driver.implicitly_wait(3)

        driver.execute_script("window.close()")
        driver.implicitly_wait(3)

        driver.switch_to_window(driver.window_handles[0])
        driver.implicitly_wait(3)

        driver.quit

teste = Teste()