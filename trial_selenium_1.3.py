from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver  = webdriver.Chrome()
driver.maximize_window()
# homepage
driver.get('https://www.swiggy.com/')
url = driver.current_url
print(url)#first page

#enter location
e = driver.find_element("xpath",'.//*[@id="location"]')
e.send_keys("Pune")
time.sleep(3)
#select location
driver.find_element("xpath",'.//*[@id="root"]/div[1]/div[1]/div/div[1]/div[1]/div/div[2]/div/div[2]/button[1]/span[2]').click()
time.sleep(3)

# find mcdonalds //*[@id="seo-core-layout"]/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div/a/div/div[2]/div[1]/div
driver.find_element("xpath",'.//*[@id="seo-core-layout"]/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div/a/div/div[2]/div[1]/div').click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"McDonald's").click()
url_two = driver.current_url
print(url_two)
time.sleep(3)
#select burger
# round 1                     
driver.find_element("xpath",'.//*[@id="cid-Recommended"]/div[1]/div/div[1]/div[1]/div/div[2]/div[2]/div/div[1]').click()
driver.find_element("xpath",'.//*[@id="modal-placeholder"]/div/div/div[2]/div/div[3]/div[2]').click()
time.sleep(5)

# driver.find_element("xpath",'.//*[@id="view-cart-btn"]/span').click()

# for fooditem in fooditems:
#     fooditem.click()
#     quantites.click()
#     carts.click()
    
# round2
# driver.find_element("xpath",'.//*[@id="cid-Recommended"]/div[1]/div/div[2]/div[1]/div/div[2]/div[2]/div').click()
driver.find_element("xpath",'.//*[@id="cid-Recommended"]/div[1]/div/div[3]/div[1]/div/div[2]/div[2]/div/div[1]').click()#ordering the same burger twice
# driver.find_element("xpath",'.//*[@id="modal-placeholder"]/div/div/div[2]/div/div[3]/div[2]').click()
driver.find_element("xpath",'.//*[@id="modal-placeholder"]/div/div/div[2]/div/div[3]/div[2]').click()
time.sleep(3)
# driver.find_element("xpath",'.//*[@id="modal-placeholder"]/div/div/div[2]/div/div[3]/div[2]').click()
time.sleep(3)
driver.find_element("xpath",'.//*[@id="view-cart-btn"]/span/span[1]').click()
time.sleep(5)

driver.quit()



