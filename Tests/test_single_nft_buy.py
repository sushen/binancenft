from Pages.SingleNftBuy import SingleNftBuy
from Tests.test_base import Basetest


class Test_single_nft(Basetest):

    # def test_is_visible_allow_page(self):
    #     self.search = SingleNftBuy(self.driver)
    #     flag = self.search.is_visible_allow_button()
    #     assert flag
    #
    def test_click_allow(self):
        self.search = SingleNftBuy(self.driver)
        self.search.click_allow_button()
    #
    def test_click_buy_now(self):
        self.single_nft = SingleNftBuy(self.driver)
        self.single_nft.click_buy_now_button()
    #
    # def test_is_visible_confirm_button(self):
    #     self.search = SingleNftBuy(self.driver)
    #     flag = self.search.is_visible_confirm_button()
    #     assert flag

    def test_click_confirm_button(self):
        self.single_nft = SingleNftBuy(self.driver)
        self.single_nft.click_buy_now_button()
        # print(input("click confirm button"))
        self.single_nft.click_confirm_button()
        # print(input("click confirm button"))
