import time
from selenium.webdriver.common.by import By
from selenium import webdriver

class Demojs():
    def demo_javascript(self):
        driver = webdriver.Chrome()
       # driver.get("https://training.rcvacademy.com/")
       # driver.maximize_window()
        driver.execute_script("window.open('https://training.rcvacademy.com/', '_self');")
        time.sleep(4)
        driver.maximize_window()
        demo_element = driver.execute_script(" return document.getElementsByTagName('p')[6];")
        driver.execute_script("arguments[0].click();", demo_element)
        time.sleep(4)

        driver.quit()
demojs = Demojs()
demojs.demo_javascript()

