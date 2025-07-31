#----java
#WebDriverManager.chromedriver().setup();----
#System.setProperty(webdriver.chrome.driver,".exe path of driver")
#WebDriver driver=new ChromeDriver()
#----------------------------------------------------------------------

#importing required pkgs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#approach-1: selenium 3
service = Service(executable_path="C:/Users/enthr/Desktop/Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)

#approach-2: selenium 4
#pass the driver path in the constructor of Service
serv_obj=Service("C:/Users/enthr/Desktop/Drivers/chromedriver.exe")
#pass the referce variable of Service Class obj in Chrome()
driver=webdriver.Chrome(service=serv_obj)


#approach-3: if we keep deriver.exe file in the project:script folder then
driver = webdriver.Chrome()
