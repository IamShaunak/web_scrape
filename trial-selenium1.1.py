from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.swiggy.com/restaurants-near-me')
url_one = driver.current_url
print(url_one)

# //*[@id="__next"]/main/div[2]/div[4]/div/div[1]/div[2]/div[2]/div/div[1]/div/a/div/div[2]/div[1]/div
element = driver.find_element("xpath",'.//*[@id="__next"]/main/div[2]/div[4]/div/div[1]/div[2]/div[2]/div/div[1]/div/a/div/div[2]/div[1]/div')
element.click()
url_two = driver.current_url
print(url_two)

# driver.find_element("name", "q")
driver.quit()

# + xpath: 
#//*[@id="root"]/div[1]/div/div/div/div[2]/div[5]/div[1]/div[1]/div/div[1]/div/div/div/div[2] 