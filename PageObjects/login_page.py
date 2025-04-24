# PageObjects/login_page.py
from selenium.webdriver.common.by import By
from PageObjects.base_page import BasePage
from PageObjects.dashboard_page import DashboardPage
from Config.config import TestData

class LoginPage(BasePage):
    """Login page object model"""

    # Locators
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    LOGIN_HEADER = (By.XPATH, "//h5[contains(@class, 'orangehrm-login-title')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_login_page_title(self):
        """Get login page title"""
        return self.get_title()

    def is_login_page_displayed(self):
        """Check if login page is displayed"""
        return self.is_visible(self.LOGIN_HEADER)

    def login(self, username, password):
        """Login with username and password"""
        self.send_keys(self.USERNAME_FIELD, username)
        self.send_keys(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)
        return DashboardPage(self.driver)
