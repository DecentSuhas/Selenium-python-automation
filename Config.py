from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
serv_obj = Service("C:\seleniumWebDrivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("http://automationpractice.com/index.php")
