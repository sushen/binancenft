import pytest

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import Basetest


class Test_Login(Basetest):
    def test_login_page_title(self):
        print("test_login_page_title")
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_login_page_title(TestData.Login_page_title)
        assert title == TestData.Login_page_title

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.email, TestData.password)


# Test_Login()
