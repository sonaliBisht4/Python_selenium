import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://demoqa.com/alerts")
driver.maximize_window()
time.sleep(2)

driver.execute_script("window.scrollBy(0, 200);")
time.sleep(2)

driver.find_element(By.XPATH, "//*[@id='alertButton']").click()
time.sleep(1)

driver.switch_to.alert.accept()

driver.find_element(By.XPATH, "//*[@id='confirmButton']").click()
time.sleep(1)
driver.switch_to.alert.dismiss()
time.sleep(3)


driver.quit()