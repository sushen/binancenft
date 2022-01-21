from selenium.webdriver.chrome import webdriver

from Bots.AllPageBot import AllPageBot
from Bots.Base_bot import BaseBot
from Config.config import TestData
from Pages.LoginPage import LoginPage
from Pages.BasePage import BasePage
from Pages.NftCollectionPage import SearchPage

all_page = AllPageBot()


# TODO: go to binance

# TODO: login
try:
    login = all_page.login()
    print(input("Press any Key: "))
except:
    print("You already lodged in")
if all_page.test_is_visible_allow_page():
    all_page.test_click_allow()
else:
    print("Allow page not found")
# TODO: find nft
print(input("Filter done:"))
# TODO: go to single nft
# TODO: buy nft
# TODO: Repeat the process


all_page.test_search_page_title()
all_page.driver.get(SearchPage.collection_link)
# TODO: go to collection

