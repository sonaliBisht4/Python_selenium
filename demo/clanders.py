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

driver.find_element(By.XPATH,"//div[@class='css-w7k25o']").click()
time.sleep(3)

#driver.find_element(By.CSS_SELECTOR,"div[aria-label='Choose Saturday, November 22nd, 2025'] span[aria-label='MAHA SHIVARATHIRI']").click()
driver.find_element(By.XPATH,"//div[@class='MuiBox-root css-89knyc']//div[@aria-label='Choose Tuesday, March 17th, 2026']//span[@aria-label='MAHA SHIVARATHIRI']").click()
time.sleep(5)

driver.quit()