import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.worldometers.info/geography/flags-of-the-world/")
driver.maximize_window()
time.sleep(4)

#driver.execute_script("window.scrollBy(0,500)")
#time.sleep(2)
#driver.execute_script("window.scrollBy(500,700)")
#time.sleep(2)
#driver.execute_script("window.scrollBy(0,200)")


#flag = driver.find_element(By.XPATH, "//a[@href='/img/flags/in-flag.gif']")
#driver.execute_script("arguments[0].scrollIntoView();", flag)

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)

driver.quit()

