import os
from Pages.BasePage import BasePage

from selenium.webdriver.common.by import By

from Config.bot_config import BotData

class LoginPage(BasePage):

    login_btn = (By.XPATH, "//a[@id='header_login']")

    EMAIL = (By.XPATH, "//input[@name='email']")
    PASSWORD = (By.XPATH, "//input[@name='password']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(BotData.BASE_URL)

    """ this is used to login """
    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)




