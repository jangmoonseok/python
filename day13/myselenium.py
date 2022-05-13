import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


URL = "http://127.0.0.1:5000/emp"
driver = webdriver.Chrome(executable_path='chromedriver')
driver.get(url = URL)

tbody = driver.find_element(By.CSS_SELECTOR, "table > tbody")
trs = tbody.find_elements(By.CSS_SELECTOR, "tr")

for tr in trs:
    name = tr.find_elements(By.CSS_SELECTOR, "td")[1].text 
    addr = tr.find_elements(By.CSS_SELECTOR, "td")[3].text 
    print(name, "\t", addr)