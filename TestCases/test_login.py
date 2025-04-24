# TestCases/test_login.py
import pytest
from PageObjects.login_page import LoginPage
from Config.config import TestData

@pytest.mark.usefixtures("init_driver")
class TestLogin:
    
    def test_login(self):
        """Test case to verify login functionality"""
        self.login_page = LoginPage(self.driver)
        self.dashboard_page = self.login_page.login(TestData.USERNAME, TestData.PASSWORD)
        assert self.dashboard_page.is_dashboard_displayed(), "Dashboard page is not displayed after login"
        self.dashboard_page.take_screenshot("successful_login")
