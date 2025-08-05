import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:/Users/enthr/Desktop/Drivers/chromedriver.exe")
#pass the referce variable of Service Class in Chrome()
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://practice.expandtesting.com/dynamic-table")
driver.maximize_window()
driver.implicitly_wait(5)

# table rows
rows=driver.find_elements(By.XPATH,"//table[@class='table table-striped']/tbody/tr")
print(len(rows))#4
print(rows[1])
for r in range(0,len(rows)):
    if rows[r].text.__contains__("Chrome"):
        allcellvalue=rows[r].text.split() # [Chrome] [81.7] [] []
        for cv in allcellvalue:
            if cv.__contains__("%"):
                print (f"Chrome: {cv}")


