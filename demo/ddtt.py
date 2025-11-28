import time
from ddt import ddt, data, unpack, file_data
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from testcase.util import Util


@ddt
class DdttTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://www.myntra.com/")
        time.sleep(2)

   # @data(
        #("men",), ("women",), ("kids",), ("fashion",)
    #)
    #@unpack
   # @file_data("../testcase/demodata.json")
    @data(*Util.readdata_from_excel(r"C:\Users\Fleek\PycharmProjects\PythonProjectwithpomandunittest\testdata.xlsx",
                                    "Sheet3"))
    @unpack
    def test_search_flight(self, product):
        search_bar = self.driver.find_element(By.XPATH, "//input[@placeholder='Search for products, brands and more']")
        search_bar.click()
        search_bar.send_keys(product)

        search_icon = self.driver.find_element(By.XPATH, "//a[@class='desktop-submit']")
        search_icon.click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
