import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/links")
time.sleep(1)

links = driver.find_elements(By.TAG_NAME, "a")

print("No of links present in site are : ", len(links))

for link in links:
    print (link.text)
driver.quit()

