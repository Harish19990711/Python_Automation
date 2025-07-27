from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def get_driver():
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver
