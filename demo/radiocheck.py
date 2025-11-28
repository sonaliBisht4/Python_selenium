import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
time.sleep(2)

# Scroll down
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(2)

# Check if Female radio button is selected
radio_input = driver.find_element(By.ID, "gender-radio-2")
print("Before click:", radio_input.is_selected())


radio_input = driver.find_element(By.XPATH, "//label[@for='gender-radio-2']")
print("Before click:", radio_input.click())
# Click on the label instead of input


# Verify again
print("After click:", radio_input.is_selected())

driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-1']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-2']").click()
time.sleep(2)

state_dropdown = driver.find_element(By.ID, "state")
driver.execute_script("arguments[0].scrollIntoView();", state_dropdown)
state_dropdown.click()
time.sleep(1)

state_option = driver.find_element(By.XPATH, "//div[contains(text(),'NCR')]")
state_option.click()
time.sleep(1)


driver.quit()
