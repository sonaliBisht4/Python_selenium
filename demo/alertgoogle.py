import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Full path to your CSV file
csv_file = r"C:\Users\Fleek\PycharmProjects\PythonProjectwithpomandunittest\csvdataa\testdata.csv"

test_data = []

# Read CSV file
with open(csv_file, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        test_data.append(row)

print("Test data loaded:", test_data)

# Run login for each username/password in CSV
for data in test_data:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)

    # Read username/password from CSV columns
    driver.find_element(By.ID, "user-name").send_keys(data["username"])
    driver.find_element(By.ID, "password").send_keys(data["password"])
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)


    driver.switch_to.alert.accept()

    # Optional: verify login
    if "inventory" in driver.current_url:
        print(f" Login successful for: {data['username']}")
    else:
        print(f" Login failed for: {data['username']}")

    driver.quit()
