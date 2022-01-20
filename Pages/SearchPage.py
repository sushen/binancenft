from Config.config import TestData
from Config.config_cookies import cookies
from Pages.BasePage import BasePage


# from experiment.cookies import load_cookies


class SearchPage(BasePage):
    collection_link = "https://www.binance.com/en/nft/shopWindow/NFT%E2%96%B5PRIDE?reSale=0&tradeType=0&orderBy=list_time&orderType=-1&isBack=1&uid=aa80c3015e02724438bd7cb9e662c5b8&order=list_time%40-1"

    def __init__(self, driver):
        super().__init__(driver)
        cookies.load_cookies(self.driver, TestData.Cookie_location)
        self.driver.get(self.collection_link)

    def get_search_page_title(self, title):
        return self.get_title(title)

    def click_allow_button(self, button):
        self.do_click(button)
