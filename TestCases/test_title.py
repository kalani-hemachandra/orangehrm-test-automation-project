# TestCases/test_title.py
import pytest
from PageObjects.login_page import LoginPage
from Config.config import TestData

@pytest.mark.usefixtures("init_driver")
class TestTitle:
    
    def test_login_page_title(self):
        """Test case to verify login page title"""
        self.login_page = LoginPage(self.driver)
        title = self.login_page.get_login_page_title()
        assert title == TestData.LOGIN_PAGE_TITLE, f"Login page title is not matching. Expected: {TestData.LOGIN_PAGE_TITLE}, Got: {title}"

    def test_login_page_displayed(self):
        """Test case to verify login page is displayed"""
        self.login_page = LoginPage(self.driver)
        assert self.login_page.is_login_page_displayed(), "Login page is not displayed"
        self.login_page.take_screenshot("login_page_displayed")

    def test_dashboard_title(self):
        """Test case to verify dashboard page title"""
        self.login_page = LoginPage(self.driver)
        self.dashboard_page = self.login_page.login(TestData.USERNAME, TestData.PASSWORD)
        title = self.dashboard_page.get_dashboard_title()
        assert title == TestData.DASHBOARD_PAGE_TITLE, f"Dashboard page title is not matching. Expected: {TestData.DASHBOARD_PAGE_TITLE}, Got: {title}"

