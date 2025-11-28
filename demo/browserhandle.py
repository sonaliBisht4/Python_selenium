import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/browser-windows")
driver.maximize_window()

time.sleep(2)

driver.execute_script("window.scrollBy(0,200)")
driver.find_element(By.ID, "tabButton").click()
time.sleep(2)

print(driver.current_window_handle)
whandle = driver.window_handles
for handle in whandle:
       driver.switch_to.window(handle)
       print(driver.title)
       time.sleep(2)
if driver.title == "DEMOQA":
    driver.close()
time.sleep(4)

driver.quit()
