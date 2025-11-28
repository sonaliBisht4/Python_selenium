import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import HtmlTestRunner
import time

class LoginTest(unittest.TestCase):
    base_url = "https://admin-demo.nopcommerce.com/login?returnUrl=%2Fadmin%2F"

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(cls.base_url)
        cls.driver.maximize_window()
        time.sleep(2)

    def test_login(self):
        # Click login (fields already prefilled)
        login_btn = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_btn.click()

        # Wait until title becomes dashboard
        WebDriverWait(self.driver, 15).until(
            EC.title_is("Dashboard / nopCommerce administration")
        )

        # Assert
        self.assertEqual(
            "Dashboard / nopCommerce administration",
            self.driver.title,
            "Webpage title is not matching"
        )

        # Logout
        self.driver.find_element(By.LINK_TEXT, "Logout").click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="report"))
