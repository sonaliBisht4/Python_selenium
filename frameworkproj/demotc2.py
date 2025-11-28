import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.yatra.com/")

time.sleep(3)
popup_xpaths = [
        "(//*[name()='svg'][@class='h-6 w-6'])[2]",
        "//iframe[@id='webpush-onsite']",
        "//img[contains(@src,'close') or contains(@class,'close')]",
        "//*[@id='popup-close-button']"
    ]

for path in popup_xpaths:
     try:
            driver.find_element(By.XPATH, path).click()
     except:
            pass
# SCROLL FIX — correct JavaScript
driver.execute_script("window.scrollBy(0, 300);")

# FROM CITY
driver.find_element(By.XPATH,"//p[@title='New Delhi']").click()
from_box = driver.find_element(By.ID, "input-with-icon-adornment")
from_box.click()
from_box.send_keys("new ")
time.sleep(2)

search_results = driver.find_elements(By.XPATH, "//div[@class='MuiBox-root css-134xwrj']")
print(f"Number of autosuggestions found: {len(search_results)}")

for results in search_results:
    if "New York" in results.text:
        results.click()
        break

# TO CITY
driver.find_element(By.XPATH,"//p[normalize-space()='BOM, Chhatrapati Shivaji International']").click()
to_box = driver.find_element(By.ID, "input-with-icon-adornment")
to_box.click()
to_box.send_keys("new delhi")
time.sleep(2)

driver.find_element(By.XPATH, "//span[normalize-space()='New Delhi']").click()
time.sleep(2)

# DATE
driver.find_element(By.XPATH, "(//div[contains(@class,'css-13lub7m')])[1]").click()
time.sleep(1)

driver.find_element(By.XPATH,
                    "//div[@aria-label='Choose Tuesday, December 9th, 2025']"
                   ).click()

# SEARCH
driver.find_element(By.XPATH, "//button[normalize-space()='Search']").click()

time.sleep(40)

innerfrom = driver.find_element(By.XPATH, "(//input[@id='origin_0'])[1]")
innerfrom.click()

time.sleep(2)

innerfrom.clear()
innerfrom.send_keys("Beiji")

time.sleep(4)
innerfrom.send_keys(Keys.ENTER)

time.sleep(3)

innerto = driver.find_element(By.XPATH, "(//input[@id='destination_0'])[1]")
innerto.click()

time.sleep(2)

innerto.clear()
innerto.send_keys("Mumbai")

time.sleep(4)
innerto.send_keys(Keys.ENTER)
time.sleep(2)

driver.find_element(By.XPATH,"(//input[@id='flight_depart_date_0'])[2]").click()
time.sleep(3)

driver.find_element(By.XPATH, "//div[@title='Wednesday, December 24, 2025']//span[@class='full date-val'][normalize-space()='24']").click()
time.sleep(3)

driver.find_element(By.XPATH,"(//button[contains(@class,'fs-14 btn-submit cursor-pointer bold')])[2]").click()
time.sleep(5)


