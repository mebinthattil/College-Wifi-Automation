from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from setup import user_data_read
import sys, os

headless_mode = True

#chromedriver for particular platformz
try:
    if getattr(sys, 'selenium', False):
        driver_dir = os.path.join(sys._MEIPASS, 'Drivers')
    else:
        # Otherwise, use the source path
        driver_dir = os.path.join(os.path.dirname(__file__), 'Drivers')
    driver_name = user_data_read()["driver_name"]
    username = user_data_read()["username"]
    password = user_data_read()["password"]
    driver_path = os.path.join(driver_dir, driver_name)

    if headless_mode: #checking if it should run in headless browser or not
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(service=Service(driver_path), options= options)
    else:
        driver = webdriver.Chrome(service=Service(driver_path))

except:
    print("Your chrome driver was not found")

#trying authentication
try:
    driver.get("http://192.168.254.1:8090/httpclient.html")
    time.sleep(0.5)
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.ID, "loginbutton").click()
    time.sleep(0.5)
finally:
    # Close the browser
    driver.quit()
