from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

food = input("Pls Enter fooditem: ")
time.sleep(2)
driver  = webdriver.Chrome()
driver.maximize_window()

try: 
    # swiggyfirstpage
    driver.get('https://www.swiggy.com/')
    print("Swiggy first page: " + driver.current_url)
    url  = driver.current_url
    print(url)
    time.sleep(3)
    #enter location
    e = driver.find_element("xpath",'.//*[@id="location"]')
    e.send_keys("Kothrud")
    time.sleep(3)
    #select location 
    driver.find_element("xpath",'.//*[@id="root"]/div[1]/div[1]/div/div[1]/div[1]/div/div[2]/div/div[2]/button[1]').click()
    # driver.find_element(By.LINK_TEXT,"Kothrud, Pune, Maharashtra, India").click() #bytext
    # byxpath driver.find_element("xpath",'.//*[@id="root"]/div[1]/div[1]/div/div[1]/div[1]/div/div[2]/div/div[2]/button[1]/span[2]').click()
    time.sleep(3)
    #clickonsearch 
    driver.find_element("xpath",'.//*[@id="root"]/div[1]/header/div/div/ul/li[5]/div/a').click()
    time.sleep(4)
    search_textbox =  driver.find_element("xpath",'.//*[@id="root"]/div[1]/div/div[1]/div/form/div/div[1]/input')
    search_textbox.send_keys(food)
    url_two = driver.current_url
    print(url_two)
    time.sleep(2) 
    driver.get('https://www.swiggy.com/search?query=McDonald%27s')
    url_3 = driver.current_url
    print(url_3)
    time.sleep(2)
    driver.find_element("xpath",'.//*[@id="root"]/div[1]/div/div[2]/div/div/div[3]/div[1]/div/a/div[2]').click()
    url_4 = driver.current_url
    print(url_4)
    time.sleep(3)
    #select burger
    driver.find_element("xpath",'.//*[@id="cid-Recommended"]/div[1]/div/div[1]/div[1]/div/div[2]/div[2]/div').click()
    time.sleep(2)
    #addburger to cart
    driver.find_element("xpath",'.//*[@id="modal-placeholder"]/div/div/div[2]/div/div[3]/div[2]').click()
    time.sleep(2)
    #view cart
    driver.find_element("xpath",'.//*[@id="view-cart-btn"]/span/span[2]').click()
    time.sleep(2)
    url_5 = driver.current_url
    print(url_5)
    element = driver.find_element("xpath",'.//*[@id="root"]/div[1]/div/div/div[2]/div/div[2]/div[2]').text
    print("Amount in INR to pay on SWIGGY: "+element)
    driver.quit()
except NoSuchElementException:
    print("exception occured")
    driver.get('https://www.swiggy.com/')
    print(driver.current_url)
    driver.quit
