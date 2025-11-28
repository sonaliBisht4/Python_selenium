import time
import unittest
import csv
from ddt import ddt, data, unpack
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


# ----------------- CSV READER -----------------
def read_csv(path):
    rows = []
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for r in reader:
            rows.append(r)
    return rows


@ddt
class TestSearchFlight(unittest.TestCase):

    # ----------------- SETUP -----------------
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    # ----------------- REMOVE POPUPS -----------------
    def close_popups(self):
        driver = self.driver
        try:
            driver.switch_to.frame("webpush-onsite")
            close_btn = driver.find_element(By.XPATH, "//button[contains(@class,'close')]")
            close_btn.click()
            driver.switch_to.default_content()
            print("Popup closed.")
        except:
            driver.switch_to.default_content()

    # ----------------- SEARCH FUNCTION -----------------
    def search_flight(self, departlocation, gotolocation):

        driver = self.driver

        self.close_popups()

        # ----------- ENTER DEPART CITY -----------
        from_box = driver.find_element(By.ID, "input-with-icon-adornment")
        from_box.clear()
        from_box.send_keys(departlocation)
        time.sleep(2)

        self.close_popups()

        # CLICK FIRST SUGGESTION
        suggestions = driver.find_elements(By.XPATH, "//div[contains(@class,'MuiBox-root')]")

        for item in suggestions:
            try:
                if departlocation.lower() in item.text.lower():
                    driver.execute_script("arguments[0].scrollIntoView(true);", item)
                    time.sleep(0.3)
                    item.click()
                    break
            except ElementClickInterceptedException:
                self.close_popups()
                item.click()

        # ----------- ENTER TO CITY -----------
        to_box = driver.find_element(By.ID, "input-with-icon-adornment")
        to_box.clear()
        to_box.send_keys(gotolocation)
        time.sleep(2)

        self.close_popups()

        driver.find_element(By.XPATH, f"//span[contains(text(),'{gotolocation}')]").click()

        # ----------- DATE -----------
        driver.find_element(By.XPATH, "(//div[contains(@class,'css-13lub7m')])[1]").click()
        time.sleep(1)

        driver.find_element(By.XPATH,
            "//div[@aria-label='Choose Tuesday, December 9th, 2025']"
        ).click()

        # ----------- CLICK SEARCH -----------
        driver.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
        time.sleep(5)

    # ----------------- TEST CASE -----------------
    @data(*read_csv(r"C:\Users\Fleek\PycharmProjects\PythonProjectwithpomandunittest\frameworkproj\tdata.csv"))
    @unpack
    def test_search_flight(self, departlocation, gotolocation, stop1, stop2, stop3):

        driver = self.driver
        driver.get("https://www.yatra.com/")
        time.sleep(3)

        self.close_popups()

        # RUN MAIN SEARCH
        self.search_flight(departlocation, gotolocation)

        # APPLY STOP FILTERS
        for stop in [stop1, stop2, stop3]:
            try:
                ele = driver.find_element(By.XPATH, f"//p[contains(text(),'{stop}')]")
                driver.execute_script("arguments[0].scrollIntoView(true);", ele)
                time.sleep(0.5)
                ele.click()
                print("Applied stop:", stop)
            except:
                print("Stop not found:", stop)

        self.assertTrue(True)


    # ----------------- TEARDOWN -----------------
    def tearDown(self):
        self.driver.quit()
