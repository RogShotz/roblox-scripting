import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
#from selenium.webdriver.firefox.service import Service
#from selenium.webdriver.firefox.options import Options


def kill_by_process_name_shell(name):
    os.system("taskkill /f /im " + name)


load_dotenv()

# create webdriver object
# driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\geckodriver-v0.31.0-win64\geckodriver.exe')
options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.roblox.com/games/9551640993/JULY-4th-Mining-Simulator-2")
driver.add_cookie({"name": ".ROBLOSECURITY", "value": os.getenv("COOKIE")})
driver.refresh()
driver.implicitly_wait(0.5)
agreement = driver.find_element(By.XPATH, "//*[@id='user-agreements-checker-modal']/div/div/div[3]/div[2]/button")
agreement.click()

while True:
    # get element
    element = driver.find_element(By.XPATH, "//*[@id='game-details-play-button-container']/button")
    element.click()
    time.sleep(30)
    # print complete element
    print(element)
    kill_by_process_name_shell("RobloxPlayerBeta.exe")
