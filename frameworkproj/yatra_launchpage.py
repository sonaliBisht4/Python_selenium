import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from frameworkproj.Util import Util
from frameworkproj.basedriver import BaseDriver
from frameworkproj.search_flight import searchfile_resultpage


class LaunchPage(BaseDriver):

    log = Util.custom_logger(logLevel=logging.WARNING)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # ------------------ HOME PAGE XPATHS ------------------
        self.from_city_btn = "//p[@title='New Delhi']"
        self.to_city_btn = "//p[normalize-space()='BOM, Chhatrapati Shivaji International']"
        self.from_input = "input-with-icon-adornment"
        self.to_input = "input-with-icon-adornment"
        self.to_autopick = "//span[normalize-space()='New Delhi']"

        self.calendar_btn = "(//div[contains(@class,'css-13lub7m')])[1]"
        self.date_pick = "//div[@aria-label='Choose Tuesday, December 9th, 2025']"
        self.search_btn = "//button[normalize-space()='Search']"

        # ------------------ INNER PAGE XPATHS ------------------
        self.inner_from = "(//input[@id='origin_0'])[1]"
        self.inner_to = "(//input[@id='destination_0'])[1]"
        self.inner_calendar = "(//input[@id='flight_depart_date_0'])[2]"
        self.inner_date_pick = "//div[@title='Wednesday, December 24, 2025']//span[@class='full date-val'][normalize-space()='24']"
        self.inner_search_btn = "(//button[contains(@class,'fs-14 btn-submit cursor-pointer bold')])[2]"

        # popup locators
        self.popup_paths = [
            "(//*[name()='svg'][@class='h-6 w-6'])[2]",
            "//iframe[@id='webpush-onsite']",
            "//img[contains(@src,'close') or contains(@class,'close')]",
            "//*[@id='popup-close-button']"
        ]

    # ------------------------------------------------------
    # POPUP HANDLER
    # ------------------------------------------------------
    def close_popups(self):
        for path in self.popup_paths:
            try:
                self.driver.find_element(By.XPATH, path).click()
                self.log.info("Popup closed")
                time.sleep(1)
            except:
                pass

    # ------------------------------------------------------
    # MAIN SEARCH FUNCTION
    # ------------------------------------------------------
    def searchflight(self, departlocation, gotolocation):

        # close popups
        self.close_popups()

        # scroll
        self.driver.execute_script("window.scrollBy(0,300);")
        time.sleep(1)

        # ------------------ HOME PAGE SEARCH ------------------

        # FROM
        self.driver.find_element(By.XPATH, self.from_city_btn).click()
        from_box = self.driver.find_element(By.ID, self.from_input)
        from_box.click()
        from_box.send_keys("new ")
        time.sleep(2)

        # autosuggest
        suggestions = self.driver.find_elements(By.XPATH, "//div[@class='MuiBox-root css-134xwrj']")
        for item in suggestions:
            if "New York" in item.text:
                item.click()
                break

        # TO
        self.driver.find_element(By.XPATH, self.to_city_btn).click()
        to_box = self.driver.find_element(By.ID, self.to_input)
        to_box.click()
        to_box.send_keys("new delhi")

        time.sleep(2)
        self.driver.find_element(By.XPATH, self.to_autopick).click()

        # DATE
        self.driver.find_element(By.XPATH, self.calendar_btn).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.date_pick).click()

        # CLICK SEARCH
        self.driver.find_element(By.XPATH, self.search_btn).click()
        time.sleep(5)

        # ------------------ INNER PAGE ------------------

        inner_from_box = self.driver.find_element(By.XPATH, self.inner_from)
        inner_from_box.click()
        inner_from_box.clear()
        inner_from_box.send_keys(departlocation)
        time.sleep(3)
        inner_from_box.send_keys(Keys.ENTER)

        time.sleep(2)

        inner_to_box = self.driver.find_element(By.XPATH, self.inner_to)
        inner_to_box.click()
        inner_to_box.clear()
        inner_to_box.send_keys(gotolocation)
        time.sleep(3)
        inner_to_box.send_keys(Keys.ENTER)

        # inner date
        self.driver.find_element(By.XPATH, self.inner_calendar).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.inner_date_pick).click()

        # inner search
        self.driver.find_element(By.XPATH, self.inner_search_btn).click()

        time.sleep(8)

        return searchfile_resultpage(self.driver)
