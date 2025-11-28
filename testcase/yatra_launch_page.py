import logging
import time
from selenium.webdriver.common.by import By
from testcase.util import Util
from testcase.basedriver import BaseDriver
from testcase.testsearch_flight import searchfile_resultpage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LaunchPage(BaseDriver):

    log = Util.custom_logger(logLevel=logging.WARNING)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # XPaths / Locators
        self.department_from_field = "//p[@title='New Delhi']"
        self.department_to_field = "//p[normalize-space()='BOM, Chhatrapati Shivaji International']"
        self.depart_fromfield = "input-with-icon-adornment"
        self.depart_tofield = "input-with-icon-adornment"
        self.depart_tolocation = "//span[normalize-space()='New Delhi']"
        self.calander = "(//div[contains(@class,'css-13lub7m')])[1]"
        self.traveldate = "//div[@aria-label='Choose Tuesday, December 9th, 2025']"
        self.Searchbutton = "//button[normalize-space()='Search']"

    # --------------------------
    # ELEMENT GETTERS
    # --------------------------

    def getDepartmentLocation(self):
        return self.driver.find_element(By.XPATH, self.department_from_field)

    def getdepartfromfield(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, self.depart_fromfield))
        )

    def getDepartedtoLocation(self):
        return self.driver.find_element(By.XPATH, self.department_to_field)

    def getdeparttofield(self):
        return self.driver.find_element(By.ID, self.depart_tofield)

    def getdepart_tolocation(self):
        return self.driver.find_element(By.XPATH, self.depart_tolocation)

    def getcalander(self):
        return self.driver.find_element(By.XPATH, self.calander)

    def gettraveldate(self):
        return self.driver.find_element(By.XPATH, self.traveldate)

    def getsearchbutton(self):
        return self.driver.find_element(By.XPATH, self.Searchbutton)

    # --------------------------
    # MAIN SEARCH FUNCTION
    # --------------------------

    def searchflight(self, departlocation, gotolocation):

        # FROM Location
        self.getDepartmentLocation().click()
        self.getdepartfromfield().send_keys(departlocation)
        time.sleep(3)

        search_results = self.driver.find_elements(By.XPATH, "//div[@class='MuiBox-root css-134xwrj']")
        self.log.info(f"Number of autosuggestions found: {len(search_results)}")

        for results in search_results:
            if "New York" in results.text:
                results.click()
                break

        # TO location
        self.getDepartedtoLocation().click()
        time.sleep(3)

        self.getdeparttofield().send_keys(gotolocation)
        time.sleep(2)

        self.getdepart_tolocation().click()
        time.sleep(3)

        # Calendar selection
        self.getcalander().click()
        time.sleep(2)

        self.gettraveldate().click()
        time.sleep(2)

        # Search flights
        self.getsearchbutton().click()
        time.sleep(40)

        search_flight_result = searchfile_resultpage(self.driver)
        return search_flight_result
