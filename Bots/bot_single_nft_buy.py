from Bots.Base_bot import BaseBot
from Pages.SingleNftBuy import SingleNftBuy
import time


class bot_single_nft_buy(BaseBot):

    def test_click_buy_now(self):
        start_tab_time = time.time()
        self.single_nft = SingleNftBuy(self.driver)
        self.single_nft.click_buy_now_button()
        print("pressed buy now button")
        CurrentTime = time.time()
        totalRunningTime = CurrentTime - start_tab_time
        print("This single nft buy is running for " + str(float(totalRunningTime)))

    def test_click_confirm_button(self):
        self.search = SingleNftBuy(self.driver)
        self.search.click_confirm_button()
