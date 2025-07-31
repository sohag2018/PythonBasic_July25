#Validate Search box is working....
import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:/Users/enthr/Desktop/Drivers/chromedriver.exe")
#pass the referce variable of Service Class in Chrome()
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.implicitly_wait(5)

#clicking on Computer head tab
comp_tab=driver.find_element(By.XPATH,"//ul[@class='top-menu']//a[normalize-space()='Computers']")
action=ActionChains(driver)
action.move_to_element(comp_tab).perform()
time.sleep(2)
driver.find_element(By.XPATH,"//ul[@class='top-menu']//a[normalize-space()='Desktops']").click()
#add 1st product to cart
driver.find_element(By.XPATH,"(//input[@value='Add to cart'])[1]").click()
time.sleep(2)
#click on add button
driver.find_element(By.XPATH,"//input[@id='add-to-cart-button-72']").click()
print("product added to cart")