import logging
from selenium.webdriver.common.by import By
from frameworkproj.basedriver import BaseDriver
from frameworkproj.Util import Util


class searchfile_resultpage(BaseDriver):

    log = Util.custom_logger(logging.WARNING)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # --------------------------------------------------------------------
    # CLEAN FLIGHT FILTER METHOD
    # --------------------------------------------------------------------
    def filter_flights(self, stop_type):

        # All flight card containers
        cards = self.driver.find_elements(By.CSS_SELECTOR, "div.flightItem.border-shadow.pr")

        stop_flights = []

        for c in cards:
            # Check only exact stop-type
            stop_span = c.find_elements(By.CSS_SELECTOR, f"span[aria-label='{stop_type}']")
            if stop_span:
                stop_flights.append(stop_span[0])

        # Logging
        self.log.warning(f"Found {len(stop_flights)} flights for: {stop_type}")

        return stop_flights
