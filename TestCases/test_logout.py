# TestCases/test_logout.py
import pytest
from PageObjects.login_page import LoginPage
from Config.config import TestData

@pytest.mark.usefixtures("init_driver")
class TestLogout:
    
    def test_logout(self):
        """Test case to verify logout functionality"""
        self.login_page = LoginPage(self.driver)
        self.dashboard_page = self.login_page.login(TestData.USERNAME, TestData.PASSWORD)
        
        # Verify login successful
        assert self.dashboard_page.is_dashboard_displayed(), "Dashboard page is not displayed after login"
        
        # Perform logout
        self.login_page = self.dashboard_page.perform_logout()
        
        # Verify logout successful
        assert self.login_page.is_login_page_displayed(), "Login page is not displayed after logout"
        self.login_page.take_screenshot("successful_logout")

