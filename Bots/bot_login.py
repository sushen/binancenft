from Bots.Base_bot import BaseBot
from Config.config import TestData
from Pages.LoginPage import LoginPage


class Bot_Login(BaseBot):
    def login_page_title(self):
        print("test_login_page_title")
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_login_page_title(TestData.Login_page_title)
        assert title == TestData.Login_page_title

    def login(self):
        self.loginPage = LoginPage(self.driver)
        # print(TestData.email+" "+TestData.password)
        self.loginPage.do_login(TestData.email, TestData.password)


# Test_Login()
