import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with open("TESTdata.json",'r') as json_file:
    test_data = json.load(json_file)
# Run login for each username/password in CSV
for data in test_data['users']:
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    time.sleep(2)

    # 🔹 Read username/password from CSV columns
    driver.find_element(By.ID, "user-name").send_keys(data["username"])
    driver.find_element(By.ID, "password").send_keys(data["password"])
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    # Optional: verify login
    if "inventory" in driver.current_url:
        print(f" Login successful for: {data['username']}")
    else:
        print(f" Login failed for: {data['username']}")

    driver.quit()
