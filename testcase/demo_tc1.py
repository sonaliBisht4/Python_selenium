from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
driver.get("https://www.yatra.com/")
driver.maximize_window()
wait = WebDriverWait(driver, 20)
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

driver.find_element(By.XPATH, "//p[@title='Mumbai']").click()
time.sleep(3)

driver.find_element(By.XPATH, "//div[@class='MuiFormControl-root MuiTextField-root css-49nu37']").send_keys("New Delhi")
time.sleep(3)

driver.find_element(By.XPATH,"//body/div[@id='__next']/div[@class='MuiBox-root css-1cezz5w']/div[@class='MuiBox-root css-1h9nmm8']/div[@class='MuiBox-root css-1jea2if']/div[@class='MuiBox-root css-n9rhs2']/div[@class='MuiBox-root css-1xaekgw']/div[@class='MuiBox-root css-1az9q6q']/div[@class='MuiBox-root css-92q1lr']/div[@class='MuiBox-root css-0']/div[@class='MuiBox-root css-t8k0vn']/div[@class='MuiBox-root css-offmes']/div[@class='MuiStack-root css-1187icl']/div[@class='MuiBox-root css-b3ziwv']/div[@class='MuiBox-root css-134xwrj']/ul/div[1]/li[1]/div[1]/div[1]").click()
time.sleep(3)

driver.find_element(By.XPATH,"//input[contains(@type,'checkbox')]").click()
time.sleep(3)

driver.find_element(By.XPATH,"//button[normalize-space()='Search']").click()
time.sleep(40)


# COUNT NUMBER OF FLIGHTS

flight_cards = driver.find_elements(By.CSS_SELECTOR, "span[aria-label='Non Stop']")

print("Total 0-stop flights found:", len(flight_cards))

for i, flight in enumerate(flight_cards, start=1):
    print(f"Flight {i}:")
    print(flight.text)
    print("--------------------------------")

driver.quit()
