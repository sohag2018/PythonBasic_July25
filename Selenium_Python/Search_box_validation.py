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

#after checking loginlink enaled clcking on it

login_link=driver.find_element(By.XPATH,"//a[@class='ico-login']")
if login_link.is_enabled():
    login_link.click()

#put the credentials then click on login_btn #dummypass123@gmail.com   DummyPass123
#userid
userid=driver.find_element(By.ID,"Email")
userid.clear()
userid.send_keys("dummypass123@gmail.com")
#Pass
password=driver.find_element(By.ID,"Password")
password.clear()
password.send_keys("DummyPass123")
#clicking on login_btn
driver.find_element(By.CSS_SELECTOR,".button-1.login-button").click()
time.sleep(5)
exp_prof_txt="dummypass123@gmail.com"
act_prof_text=driver.find_element(By.XPATH,"//a[normalize-space()='dummypass123@gmail.com']").text
print(exp_prof_txt,"-",act_prof_text)
if exp_prof_txt==act_prof_text:
    print("Pass")
    assert True
else:
    print("Fail")
    assert False

driver.quit()#session of the drivr instance is killing


