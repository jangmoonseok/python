import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


URL = "http://127.0.0.1:5000/emp"
driver = webdriver.Chrome(executable_path='chromedriver')
driver.get(url = URL)
driver.implicitly_wait(time_to_wait=5)

table = driver.find_element(By.CSS_SELECTOR, "table")
names = table.find_elements(By.CSS_SELECTOR, "td:nth-child(2)")
addrs = table.find_elements(By.CSS_SELECTOR, "td:nth-child(4)")
for i in names:
    print("이름:{}".format(i.text))
    
for i in addrs:
    print("주소:{}".format(i.text))