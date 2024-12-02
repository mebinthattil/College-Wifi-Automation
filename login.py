from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from setup import user_data_read


#chromedriver for particular platform
try:
    driver_name = user_data_read()["driver_name"]
    username = user_data_read()["username"]
    password = user_data_read()["password"]
    driver = webdriver.Chrome(service=Service(f'./Drivers/{driver_name}' ))
except:
    print("Your chrome driver was not found")

#trying authentication
try:
    driver.get("http://172.16.1.1:8090/")
    time.sleep(0.5)
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.ID, "loginbutton").click()
    time.sleep(0.5)
finally:
    # Close the browser
    driver.quit()