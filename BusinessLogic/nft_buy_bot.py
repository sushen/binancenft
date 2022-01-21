from selenium.webdriver.chrome import webdriver

from Bots.AllPageBot import AllPageBot
from Bots.Base_bot import BaseBot
from Config.config import TestData
from Pages.LoginPage import LoginPage
from Pages.BasePage import BasePage

all_page = AllPageBot()


# TODO: go to binance

# TODO: login
try:
    login = all_page.login()
    print(input("Press any Key: "))
except:
    print("You already lodged in")

# TODO: go to collection
# TODO: find nft
# TODO: go to single nft
# TODO: buy nft
# TODO: Repeat the process


