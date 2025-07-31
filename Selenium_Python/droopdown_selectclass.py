#Validate Search box is working....
import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:/Users/enthr/Desktop/Drivers/chromedriver.exe")
#pass the referce variable of Service Class in Chrome()
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.implicitly_wait(5)
#workflow: got to books>using dropdown>get all item having add to cart btn>click and add to cart
#click on books tab
driver.find_element(By.XPATH,"//ul[@class='top-menu']//a[normalize-space()='Books']").click()

#Method to select_dropdwon_item
def select_dropdwon_item(element,visible_text):
    drop_down = Select(element)
    drop_down.select_by_visible_text(visible_text)

#perform dropdown
#sort_by:
sort_by=driver.find_element(By.ID,"products-orderby")
#calling method
select_dropdwon_item(sort_by,"Name: A to Z")

#display:
display_dropdown=driver.find_element(By.ID,"products-pagesize")
#calling method
select_dropdwon_item(display_dropdown,"8")
#view as: products-viewmode
view_dropdown=driver.find_element(By.ID,"products-viewmode")
#calling method
select_dropdwon_item(view_dropdown,"List")

#add product by clicking on add to cart
#empty list
addedItems=[]
items_with_addtocart=driver.find_elements(By.XPATH,"//div[@class='item-box']//input[@class='button-2 product-box-add-to-cart-button']")
for item in items_with_addtocart:
    item.click()
    addedItems.append("item")
    print("added item to cart")

print(addedItems)