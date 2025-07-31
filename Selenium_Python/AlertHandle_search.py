#Validate Logo-is present
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:/Users/enthr/Desktop/Drivers/chromedriver.exe")
#pass the referce variable of Service Class in Chrome()
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.implicitly_wait(5)

#click on search button without sending any text in search field
driver.find_element(By.CSS_SELECTOR,".button-1.search-box-button").click()
alert=driver.switch_to.alert
alert.accept()
