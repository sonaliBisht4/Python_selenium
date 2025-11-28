import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="edge")


@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class")
def setup(request, browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Invalid browser option")

    driver.maximize_window()
    driver.get("https://www.yatra.com/")
    time.sleep(4)

    request.cls.driver = driver



    # Close popups
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

    time.sleep(3)
    driver.execute_script("window.scrollBy(0, 300);")

    yield driver

    driver.quit()


# 📌 Attach screenshots on failure

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    # If HTML plugin is not enabled, no need to continue
    html = item.config.pluginmanager.getplugin("html")
    if html is None:
        return

    extra = getattr(report, "extra", [])

    # Capture screenshot on failure
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("setup")

        # Create screenshot folder
        report_dir = os.path.join(os.getcwd(), "REPORTS", "screenshots")
        if not os.path.exists(report_dir):
            os.makedirs(report_dir)

        # Screenshot file name
        file_name = (
            report.nodeid.replace("::", "_").replace("/", "_").replace("\\", "_") +
            "_" + str(int(time.time())) + ".png"
        )
        file_path = os.path.join(report_dir, file_name)

        # Save screenshot
        driver.save_screenshot(file_path)

        # Add screenshot to HTML report
        img_html = html.extras.html(
            f'<div><img src="screenshots/{file_name}" '
            f'style="width:300px;height:200px" '
            f'onclick="window.open(this.src)" /></div>'
        )

        extra.append(img_html)

        # Add URL also
        extra.append(html.extras.url(driver.current_url))

    report.extra = extra


def pytest_html_report_title(report):
    report.title = "Yatra Automation Report"
