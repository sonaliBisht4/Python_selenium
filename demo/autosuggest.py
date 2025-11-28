from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://www.yatra.com/")
driver.maximize_window()
time.sleep(5)

# Close popup if appears
try:
    big_close = driver.find_element(By.XPATH, "//img[contains(@src,'close') or contains(@class,'close')]")
    big_close.click()
    print("Closed main login popup.")
except:
    print("Main login popup not found.")
time.sleep(3)

# Scroll
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(3)

# Click From city
element = driver.find_element(By.XPATH, "//p[@title='New Delhi']")
element.click()
time.sleep(2)

# Type in the From input
driver.find_element(By.ID, "input-with-icon-adornment").send_keys("new")
time.sleep(3)

print("Clicked the From city box")

# Capture autosuggestions
search_results = driver.find_elements(By.XPATH, "// div[ @class ='MuiBox-root css-134xwrj']")

print("Number of autosuggestions found:", len(search_results))

for item in search_results:
    print(item.text)

for results in search_results:
    if   "New York"in results.text:
        print(results.text)
        results.click()
        time.sleep(3)
        break


time.sleep(3)
driver.quit()
print("Browser closed successfully")
