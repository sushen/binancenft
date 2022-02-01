from selenium.webdriver.common.by import By

from Config.config import TestData
from Config.config_cookies import cookies
from Pages import NftCollectionPage
from Pages.BasePage import BasePage


# from experiment.cookies import load_cookies


class SingleNftBuy(BasePage):

    single_nft_page = "https://www.binance.com/en/nft/goods/detail?productId=23684237&isProduct=1"
    buy_now_button = (By.XPATH, "//button[normalize-space()='Buy Now']")
    allow_button = (By.XPATH, "//button[contains(text(),'Accept')]")
    confirm = (By.XPATH, "//button[@class=' css-rtsl4l']")
    collections = (By.XPATH, "//button[normalize - space() = 'Collections']")
    buy_now = (By.XPATH, "//button[contains(text(),'Buy Now')]")
    not_enough = (By.XPATH, "//div[contains(text(),'have enough crypto')]")
    sold_out_xpath = (By.XPATH, "//button[normalize-space()='Sold Out']")
    return_button = (By.XPATH, "//button[normalize-space()='Return']")
    success_paid = (By.XPATH, "// h6[normalize - space() = 'Success paid']")

    def __init__(self, driver):
        super().__init__(driver)
        # cookies.load_cookies(self.driver, TestData.Cookie_location)
        # self.driver.get(self.single_nft_page)

    def is_visible_allow_button(self):
        return self.is_visible(self.allow_button)

    def click_allow_button(self):
        self.do_click(self.allow_button)

    def click_buy_now_button(self):
        self.do_click(self.buy_now_button)

    def is_visible_confirm_button(self):
        return self.is_visible(self.confirm)

    def is_visible_buy_now_button(self):
        return self.is_visible(self.buy_now)

    def is_visible_not_enough_button(self):
        return self.is_visible(self.not_enough)

    def click_confirm_button(self):
        self.do_click(self.confirm)

    def is_visible_collection_button(self):
        return self.is_visible(self.collections)

    def is_visible_payment_failed(self):
        return self.is_visible(self.failed_text)

    def is_visible_sold_out(self):
        return self.is_visible(self.sold_out_xpath)

    def click_return_button(self):
        self.do_click(self.return_button)


