# TestCases/test_leave.py
import pytest
from PageObjects.login_page import LoginPage
from Config.config import TestData

@pytest.mark.usefixtures("init_driver")
class TestLeave:
    
    def test_leave_page(self):
        """Test case to verify leave page functionality"""
        self.login_page = LoginPage(self.driver)
        self.dashboard_page = self.login_page.login(TestData.USERNAME, TestData.PASSWORD)
        
        # Click on My Leave icon
        self.leave_page = self.dashboard_page.click_my_leave()
        
        # Verify leave page is displayed
        assert self.leave_page.is_leave_page_displayed(), "Leave page is not displayed"
        
        # Verify leave page header
        header_text = self.leave_page.get_leave_header_text()
        assert header_text == TestData.LEAVE_PAGE_HEADER, f"Leave page header is not matching. Expected: {TestData.LEAVE_PAGE_HEADER}, Got: {header_text}"

        self.leave_page.take_screenshot("leave_page_displayed")

