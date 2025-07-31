#Initialize webdriver
#launch brower

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


#In python

serv_obj=Service("C:/Users/enthr/Desktop/Drivers/chromedriver.exe")
#pass the referce variable of Service Class in Chrome()
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://demowebshop.tricentis.com/")
exp_tile="Demo Web Shop"
act_title=driver.title
if exp_tile==act_title:
    print("Pass")
    assert True
else:
    print("Fail")
    assert False






