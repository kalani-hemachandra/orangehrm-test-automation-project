# TestCases/conftest.py
import pytest
from selenium import webdriver
from datetime import datetime
import os

# Define the directories
REPORTS_DIR = "Reports"
SCREENSHOTS_DIR = "Screenshots"  # Corrected: Define at the top, relative to project root


def pytest_configure(config):
    """
    Configure pytest to generate an HTML report in the Reports directory.
    """
    # Create the Reports directory if it doesn't exist
    if not os.path.exists(REPORTS_DIR):
        os.makedirs(REPORTS_DIR, exist_ok=True)
    report_name = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    config.option.htmlpath = os.path.join(REPORTS_DIR, report_name)
    config.option.self_contained_html = False

    # Create the Screenshots directory if it doesn't exist.  Do this *once* in pytest_configure
    if not os.path.exists(SCREENSHOTS_DIR):
        os.makedirs(SCREENSHOTS_DIR, exist_ok=True)


@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    # Updated initialization for Selenium 4+
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        # Take screenshot on failure
        if report.failed:
            if hasattr(item, "cls") and hasattr(item.cls, "driver"):
                try:
                    driver = item.cls.driver
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    screenshot_name = f"failure_{item.name}_{timestamp}.png"
                    screenshot_path = os.path.join(SCREENSHOTS_DIR, screenshot_name)  # Use the consistent SCREENSHOTS_DIR
                    driver.save_screenshot(screenshot_path)
                    if pytest_html is not None:
                        # Add screenshot to HTML report
                        extra = getattr(report, "extra", [])
                        extra.append(pytest_html.extras.image(screenshot_path))
                        report.extra = extra
                except Exception as e:
                    print(f"Failed to take screenshot: {e}")

