from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):

    Email = (By.XPATH, "//input[@name='email']")
    Password = (By.XPATH, "//input[@name='password']")
    LoginBtn = (By.XPATH, "//button[@id='click_login_submit']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def do_login(self, username, password):
        self.do_send_keys(self.Email, username)
        self.do_send_keys(self.Password, password)
        self.do_click(self.LoginBtn)
