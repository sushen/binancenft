from Bots.Base_bot import BaseBot
from Pages.SingleNftBuy import SingleNftBuy
import time


class bot_single_nft_buy(BaseBot):

    def test_click_buy_now(self):
        start_tab_time = time.time()
        self.single_nft = SingleNftBuy(self.driver)
        self.single_nft.click_buy_now_button()
        print("pressed buy now button")

    def test_click_confirm_button(self):
        self.single_nft = SingleNftBuy(self.driver)
        self.single_nft.click_confirm_button()
        print("click confirm button")


    def test_is_visible_collection_button(self):
        self.single_nft = SingleNftBuy(self.driver)
        collection_button = self.single_nft.is_visible_collection_button()
        print(str(collection_button))
        return collection_button

    def test_is_visible_payment_failed(self):
        self.single_nft = SingleNftBuy(self.driver)
        Payment = self.single_nft.is_visible_payment_failed()
        return Payment

    def test_click_return_button(self):
        self.single_nft = SingleNftBuy(self.driver)
        self.single_nft.click_return_button()

    def test_is_visible_buy_now_button(self):
        self.search = SingleNftBuy(self.driver)
        flag = self.search.is_visible_buy_now_button()
        return flag

    def test_is_visible_not_enough_button(self):
        self.search = SingleNftBuy(self.driver)
        flag = self.search.is_visible_not_enough_button()
        return flag

    def test_is_visible_sold_out_button(self):
        self.search = SingleNftBuy(self.driver)
        flag = self.search.is_visible_sold_out()
        return flag
