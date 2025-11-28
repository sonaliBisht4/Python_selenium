import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# ----------------------------------------------
# ADD COMMAND LINE OPTION
# ----------------------------------------------
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="edge")


# ----------------------------------------------
# FIXTURE: PROVIDE BROWSER NAME
# ----------------------------------------------
@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")


# ----------------------------------------------
# MAIN SETUP FIXTURE
# ----------------------------------------------
@pytest.fixture(scope="class")
def setup(request, browser):

    # ---- SELECT BROWSER ----
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Invalid browser option")

    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.yatra.com/")
    time.sleep(4)

    # ---- ATTACH DRIVER TO CLASS ----
    request.cls.driver = driver

    # ---- CLOSE POPUPS ----
    popup_xpaths = [
        "(//*[name()='svg'][@class='h-6 w-6'])[2]",
        "//iframe[@id='webpush-onsite']",
        "//img[contains(@src,'close') or contains(@class,'close')]",
        "//*[@id='popup-close-button']"
    ]

    for path in popup_xpaths:
        try:
            driver.find_element(By.XPATH, path).click()
        except:
            pass

    # ---- SCROLL ----
    driver.execute_script("window.scrollBy(0, 300);")
    time.sleep(2)

    yield driver

    # ---- QUIT AFTER TEST CLASS ----
    driver.quit()


# ----------------------------------------------
# HTML REPORT HOOK + SCREENSHOT ON FAILURE
# ----------------------------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    html = item.config.pluginmanager.getplugin("html")
    if not html:
        return

    extra = getattr(report, "extra", [])

    # capture only when test fails (call phase)
    if report.when == "call" and report.failed:

        # GET DRIVER FROM TEST CLASS
        driver = getattr(item.instance, "driver", None)

        if driver:
            # folder
            screenshot_dir = os.path.join(os.getcwd(), "REPORTS", "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)

            # file name
            file_name = (
                report.nodeid.replace("::", "_")
                .replace("/", "_")
                .replace("\\", "_")
                + f"_{int(time.time())}.png"
            )

            file_path = os.path.join(screenshot_dir, file_name)

            # save screenshot
            driver.save_screenshot(file_path)

            # Add to report
            img_html = html.extras.html(
                f'<div><img src="screenshots/{file_name}" '
                f'style="width:300px;height:200px;cursor:pointer" '
                f'onclick="window.open(this.src)" /></div>'
            )

            extra.append(img_html)
            extra.append(html.extras.url(driver.current_url))

    report.extra = extra


# ----------------------------------------------
# SET HTML REPORT TITLE
# ----------------------------------------------
def pytest_html_report_title(report):
    report.title = "Yatra Automation Report"
