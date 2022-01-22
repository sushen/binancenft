from Bots.Base_bot import BaseBot
from Pages.SingleNftBuy import SingleNftBuy


class bot_single_nft_buy(BaseBot):

    def test_click_buy_now(self):
        self.single_nft = SingleNftBuy(self.driver)
        self.single_nft.click_buy_now_button()
        print("pressed buy now button")
