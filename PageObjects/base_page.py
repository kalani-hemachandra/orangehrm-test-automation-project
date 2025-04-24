# PageObjects/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import datetime

class BasePage:
    """Base class for all page objects"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click(self, locator):
        """Click on an element"""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, text):
        """Send keys to an element"""
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_element_text(self, locator):
        """Get text from an element"""
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_visible(self, locator):
        """Check if element is visible"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return bool(element)

    def get_title(self):
        """Get page title"""
        return self.driver.title

    def take_screenshot(self, name):
        """Take screenshot and save it to Screenshots folder"""
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"{name}_{timestamp}.png"
        screenshots_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Screenshots")

        # Create Screenshots directory if it doesn't exist
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)

        screenshot_path = os.path.join(screenshots_dir, file_name)
        self.driver.save_screenshot(screenshot_path)
        return screenshot_path
