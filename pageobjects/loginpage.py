from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    loginbutton_xpath = "//button[@type='submit']"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def clicklogin(self):
        self.driver.find_element(By.XPATH, self.loginbutton_xpath).click()

    def clicklogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()
