#Initialize webdriver
#launch brower

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#WebDriverManager.chromedriver().setup();----
#System.setProperty(webdriver.chrome.driver,".exe path of driver")
#WebDriver driver=new ChromeDriver()----java

#In python

# #approach-2
# #if we keep deriver.exe file in the project then
# driver = webdriver.Chrome()
#approach-1 (selenium-4
#pass the driver path in the constructo of Service
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






