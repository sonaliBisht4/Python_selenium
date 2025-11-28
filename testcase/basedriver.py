import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseDriver:

    def __init__(self, driver):
        self.driver = driver

    def pagescroll(self):
        pageLength = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight); return document.body.scrollHeight;"
        )

        match = False

        while not match:
            lastCount = pageLength
            time.sleep(2)

            pageLength = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight); return document.body.scrollHeight;"
            )

            if pageLength == lastCount:
                match = True

        time.sleep(15)
