import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:/Users/enthr/Desktop/Drivers/chromedriver.exe")
#pass the referce variable of Service Class in Chrome()
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://ui.vision/demo/webtest/frames/")
driver.maximize_window()
driver.implicitly_wait(5)

#Frame 1
frame1=driver.find_element(By.XPATH,"//frame[@src='frame_1.html']")
driver.switch_to.frame(frame1)
driver.find_element(By.XPATH,"//input[@name='mytext1']").send_keys("Hello World")
#come back from frame1
driver.switch_to.default_content()
time.sleep(2)

#Frame 3
#webelement of frame3
frame3=driver.find_element(By.XPATH,"//frame[@src='frame_3.html']")
driver.switch_to.frame(frame3)#element
driver.find_element(By.XPATH,"//input[@name='mytext3']").send_keys("Hi")
#now inner Frame=iframe
#now we are in frame 3 and we have only 1 iframe so we can go index wise
driver.switch_to.frame(0)#index passing
#click on radio button
#//div[@id='i6']//div[@class='AB7Lab Id5V1']
driver.find_element(By.XPATH,"//div[@id='i9']//div[@class='AB7Lab Id5V1']").click()
time.sleep(3)
#finaly going back to parent
driver.switch_to.default_content()
driver.close()
