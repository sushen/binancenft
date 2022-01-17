import os
from BasePage import BasePage


class login_page(BasePage):
    binance_email = os.environ.get('binance_email')
    binance_password = os.environ.get('binance_pass')

    def __init__(self, driver):
        super().__init__(driver)

    def login_btn(self, login_btn):
        self.do_click(login_btn)

    def do_login(self, email, password):
        self.do_send_keys(self.binance_email, email)
        self.do_send_keys(self.binance_password, password)

    def do_input_click(self, element):
        self.do_click(element)
