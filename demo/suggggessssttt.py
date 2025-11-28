from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://www.yatra.com/")
driver.maximize_window()
time.sleep(5)

# Close popup if appears
try:
    driver.find_element(By.XPATH, "//img[contains(@src,'close')]").click()
except:
    pass

time.sleep(2)
driver.execute_script("window.scrollBy(0,300);")
time.sleep(2)

# Open calendar
driver.find_element(By.XPATH, "//div[@class='css-w7k25o']").click()
time.sleep(2)


# -------------------------
# 🔹 YOUR DYNAMIC DATE
# -------------------------
day = 20
month = "March"
year = 2026
# -------------------------

# Function for suffix
def suffix(d):
    if d in [1, 21, 31]: return "st"
    if d in [2, 22]: return "nd"
    if d in [3, 23]: return "rd"
    return "th"

suf = suffix(day)

# Build dynamic aria-label value
dynamic_date = f"Choose {month} {day}{suf}, {year}"

# Dynamic XPath (like tutorial)
xpath = f"//div[contains(@aria-label,'{dynamic_date}')]"

print("Using:", xpath)

# Click the date
driver.find_element(By.XPATH, xpath).click()

time.sleep(3)
driver.quit()
