from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup chrome driver
driver = webdriver.Chrome() 
driver.maximize_window()
	

# Navigate to the url
# driver.get('https://www.swiggy.com/city/pune')

# # Find input text field
# input_text_fname1 = driver.find_element("xpath",'.//*[@id="__next"]/main/div[1]/div/div/div[3]/div/button')
# input_text_fname1.click()
# # Take a screenshot before entering a value
# # driver.save_screenshot("screenshot-1.png")
# # element = driver.find_element("xpath",'.//*[@id="__next"]/main/div[1]/div/div/div[3]/div/div')
# # Enter a value in the input text field 
# element1 = driver.find_element("xpath",'.//*[@id="__next"]/main/div[1]/div/div/div[3]/div/div/div/input')
# element1.send_keys("Ram")
# time.sleep(5)
# # Take a screenshot after entering a value
# driver.save_screenshot("screenshot-2.png")
driver.get('https://www.swiggy.com/') #back to home page
url = driver.current_url
print(url)#first page
e = driver.find_element("xpath",'.//*[@id="location"]')
e.send_keys("Pune")#enter location
time.sleep(3)
#select location
driver.find_element("xpath",'.//*[@id="root"]/div[1]/div[1]/div/div[1]/div[1]/div/div[2]/div/div[2]/button[1]/span[2]').click()
time.sleep(5)
url_third = driver.current_url
print(url_third)

# find mcdonalds
driver.find_element(By.PARTIAL_LINK_TEXT,"McDonald's").click()
url_two = driver.current_url
print(url_two)
time.sleep(3)
#select burger
driver.find_element("xpath",'.//*[@id="cid-Recommended"]/div[1]/div/div[1]/div[1]/div/div[2]/div[2]/div/div[2]').click()

#adding item to cart
driver.find_element("xpath",'.//*[@id="modal-placeholder"]/div/div/div[2]/div/div[3]/div[2]').click()
time.sleep(10)

#view cart
driver.find_element("xpath",'.//*[@id="view-cart-btn"]/span').click()
url_checkout = driver.current_url
print(url_checkout)
time.sleep(5)

#checkoutpage

total_amount = driver.find_element("xpath",'.//*[@id="root"]/div[1]/div/div/div[2]/div/div[2]/div[2]').text
print(total_amount)
# Close the driver
driver.quit()

