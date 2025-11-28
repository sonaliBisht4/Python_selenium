import logging
import time
from selenium.webdriver.common.by import By
from testcase.basedriver import BaseDriver
from testcase.util import Util


class searchfile_resultpage(BaseDriver):

    log = Util.custom_logger(logging.WARNING)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # GENERIC FLIGHT FILTER METHOD
    def filter_flights(self, stop_type):
        cards = self.driver.find_elements(By.CSS_SELECTOR, "div.flightItem.border-shadow.pr")
        stop_list = []

        for card in cards:
            try:
                stop_el = card.find_element(By.CSS_SELECTOR, f"span[aria-label='{stop_type}']")
                stop_list.append(stop_el)
            except:
                pass

        self.log.debug(f"{stop_type} flights:", len(stop_list))

        # Assertion inside method
        for item in stop_list:
            actual = item.get_attribute("aria-label")
            assert actual == stop_type, f"FAILED: expected {stop_type} but got {actual}"

        self.log.warning(f"{stop_type} flights assertion passed")

        time.sleep(1)
        return stop_list
