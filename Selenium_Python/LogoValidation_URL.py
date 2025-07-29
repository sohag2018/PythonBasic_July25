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
#checking LOGO is present
isLogoAvailable=driver.find_element(By.XPATH,"//img[@alt='Tricentis Demo Web Shop']").is_displayed()
if isLogoAvailable:
    print("Pass")
    assert True
else:
    print("Fail")
    assert False

#validate login_link is enabled or not
is_loginlink_enabled=driver.find_element(By.XPATH,"//a[@class='ico-login']").is_enabled()
if is_loginlink_enabled==True:
    print("Pass")
    assert True
else:
    print("Fail")
    assert False

#is_selected or not----how to handle with radio button
#check radio button selected or not
ex_radion_btn=driver.find_element(By.CSS_SELECTOR,"#pollanswers-1")
if ex_radion_btn.is_selected()==True:
    print("already selected")
    assert False
else:
    ex_radion_btn.click()
    print("Pass:radio_btn has been selected")
    assert True





