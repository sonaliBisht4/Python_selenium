import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseDriver:

    def __init__(self, driver):
        self.driver = driver

    # --------------------------------------------------------------------
    # INFINITE PAGE SCROLL (CLEAN, OPTIMIZED)
    # --------------------------------------------------------------------
    def pagescroll(self, pause_time=2):

        last_height = self.driver.execute_script(
            "return document.body.scrollHeight"
        )

        while True:
            # Scroll to bottom
            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )
            time.sleep(pause_time)

            # Get new height
            new_height = self.driver.execute_script(
                "return document.body.scrollHeight"
            )

            # If height did not change → reached end of page
            if new_height == last_height:
                break

            last_height = new_height

        # final small wait for last elements
        time.sleep(1)
