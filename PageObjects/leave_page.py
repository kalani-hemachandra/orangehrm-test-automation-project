# PageObjects/leave_page.py
from selenium.webdriver.common.by import By
from PageObjects.base_page import BasePage

class LeavePage(BasePage):
    """Leave page object model"""

    # Locators
    LEAVE_HEADER = (By.XPATH, "//h6[text()='Leave']")
    FROM_DATE = (By.XPATH, "//label[text()='From Date']/following::input[1]")
    TO_DATE = (By.XPATH, "//label[text()='To Date']/following::input[1]")

    def __init__(self, driver):
        super().__init__(driver)

    def get_leave_page_title(self):
        """Get leave page title"""
        return self.get_title()

    def is_leave_page_displayed(self):
        """Check if leave page is displayed"""
        return self.is_visible(self.LEAVE_HEADER)

    def get_leave_header_text(self):
        """Get leave header text"""
        return self.get_element_text(self.LEAVE_HEADER)

