from selenium import webdriver
import time 
from selenium.common.exceptions import NoSuchElementException

location = input("Delivery Location: ")
time.sleep(2)
fooditem = input("Enter fooditem:\n ")
search_link = 'https://www.swiggy.com/search?query='+fooditem
driver = webdriver.Chrome()

try:
    # taking differernt locations
    website = 'https://www.swiggy.com/'
    driver.get(website)
    time.sleep(2)
    e = driver.find_element("xpath",'.//*[@id="location"]')
    e.send_keys(location)
    time.sleep(2)
    driver.find_element("xpath",'.//*[@id="root"]/div[1]/div[1]/div/div[1]/div[1]/div/div[2]/div/div[2]/button[1]').click()
    time.sleep(2)
    url = driver.current_url
    print(url)
    #clickonsearch 
    driver.find_element("xpath",'.//*[@id="root"]/div[1]/header/div/div/ul/li[5]/div/a').click()
    time.sleep(4)
    search_textbox =  driver.find_element("xpath",'.//*[@id="root"]/div[1]/div/div[1]/div/form/div/div[1]/input')
    search_textbox.send_keys(fooditem)
    driver.get(search_link)
    url_two = driver.current_url
    print(url_two)
    time.sleep(2)   
    driver.quit()
except NoSuchElementException: 
    print("exception occured")
    driver.get('https://www.swiggy.com/')
    time.sleep(3)