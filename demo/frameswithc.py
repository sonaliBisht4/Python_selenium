from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://demoqa.com/frames")

driver.maximize_window()
time.sleep(2)

driver.switch_to.frame("frame1")
text1 = driver.find_element(By.ID, "sampleHeading").text
print("Frame 1 Text:", text1)
time.sleep(2)

driver.switch_to.default_content()
time.sleep(2)

driver.switch_to.frame("frame2")
text2 = driver.find_element(By.ID, "sampleHeading").text
print("Frame 2 Text:", text2)
time.sleep(2)

driver.switch_to.default_content()
time.sleep(2)

driver.quit()