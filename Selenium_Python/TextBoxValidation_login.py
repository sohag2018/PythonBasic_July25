#Validate Search box is working....
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:/Users/enthr/Desktop/Drivers/chromedriver.exe")
#pass the referce variable of Service Class in Chrome()
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.implicitly_wait(5)

#find the searchbox webelement
search_item="Com"
if len(search_item)>2:
 driver.find_element(By.ID,"small-searchterms").send_keys(search_item,Keys.RETURN)
 time.sleep(2)
 print("Items found")
else:
    driver.find_element(By.ID, "small-searchterms").send_keys(search_item, Keys.RETURN)
    time.sleep(2)
    act_msg=driver.find_element(By.XPATH,"//strong[@class='warning']").text
    print(act_msg)
    if act_msg=="Search term minimum length is 3 characters":
        print("showing appropriate message")
