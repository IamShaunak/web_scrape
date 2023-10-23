from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#SWIGGY WITH PRECISE LOCATION#
driver = webdriver.Chrome()
driver.maximize_window()
# driver.get('https://www.swiggy.com/restaurants-near-me')
driver.get('https://www.swiggy.com/city/pune')

url_one = driver.current_url
print(url_one)

# driver.find_element(By.PARTIAL_LINK_TEXT,"Domino's Pizza").click()
# url_second = driver.current_url
# print(url_second)
# 
# driver.find_element(By.TAG_NAME,"The Good Bowl").click()
# 
driver.find_element(By.PARTIAL_LINK_TEXT,"McDonald's").click()
url_third = driver.current_url
print(url_third)
#adding items to cart
driver.find_element("xpath",'./html/body/div[2]/div/div[2]/div[3]').click() 


# location = driver.find_element(By.ID,"overlay-sidebar-root")
# location.click()
# location.send_keys("Pune")
url_two = driver.current_url
print(url_two)
time.sleep(5)

# driver.get('https://www.swiggy.com/city/pune') #back to home page
# element2 = driver.find_element(By.PARTIAL_LINK_TEXT,'.//*[@id="__next"]/main/div[5]/div/div[1]/div[2]/div[2]/div/div[3]/div/a/div/div[2]/div[1]/div')
# print(element2.text())
# element2.click()

# url_this = driver.current_url
# print(url_this)
# # element = driver.find_element_by_xpath('//*[@id="cid-Recommended"]/div[1]/div/div[1]/div[1]/div/div[2]/div[2]/div/div[1]').click()
# # element.click()
# # driver.find_element_by_xpath(By.XPATH,"Add*[@id="cid-Recommended"").click()
# # driver.find_element(By.LINK_TEXT,"+").click()
time.sleep(5)
driver.quit()
#SWIGGY WITHOUT PRECISE LOCATION#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('https://www.swiggy.com/city/pune')
# driver.find_element(By.PARTIAL_LINK_TEXT,"Domino's Pizza").click()
# url_second = driver.current_url
# print(url_second)

# driver.get('https://www.swiggy.com/city/pune') #back to home page

# driver.find_element(By.PARTIAL_LINK_TEXT,"McDonald's").click()
# url_five = driver.current_url
# print(url_five)
# driver.quit()


