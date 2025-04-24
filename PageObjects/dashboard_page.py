# PageObjects/dashboard_page.py
from selenium.webdriver.common.by import By
from PageObjects.base_page import BasePage
from Config.config import TestData

class DashboardPage(BasePage):
    """Dashboard page object model"""

    # Locators
    DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")
    MY_LEAVE_ICON = (By.XPATH, '//button[@title="My Leave"]')
    USER_DROPDOWN = (By.CLASS_NAME, "oxd-userdropdown-tab")
    LOGOUT_OPTION = (By.XPATH, "//a[text()='Logout']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_dashboard_title(self):
        """Get dashboard page title"""
        return self.get_title()

    def is_dashboard_displayed(self):
        """Check if dashboard is displayed"""
        return self.is_visible(self.DASHBOARD_HEADER)

    def click_my_leave(self):
        """Click on My Leave icon"""
        self.click(self.MY_LEAVE_ICON)
        from PageObjects.leave_page import LeavePage
        return LeavePage(self.driver)

    def perform_logout(self):
        """Perform logout"""
        self.click(self.USER_DROPDOWN)
        self.click(self.LOGOUT_OPTION)
        from PageObjects.login_page import LoginPage
        return LoginPage(self.driver)

