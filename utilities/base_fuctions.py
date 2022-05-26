"""
 Contains all the common and reusable functions
"""
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from utilities import config


def invoke_driver_service():
    if config.DRIVER_TYPE == "Chrome":
        driver_location = config.DRIVER_PATH + config.CHROME_DRIVER
        serv_obj = Service(driver_location)
        driver = webdriver.Chrome(service=serv_obj)
    else:
        driver_location = config.DRIVER_PATH + config.FIREFOX_DRIVER
        serv_obj = Service(driver_location)
        driver = webdriver.firefox(service=serv_obj)
    return driver


def launch_url(url):
    driver = invoke_driver_service()
    driver.get(url)
    driver.maximize_window()


launch_url(config.APP_URL)
