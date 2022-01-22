import pytest

from Config.config import TestData
from Pages.NftCollectionPage import NftCollectionPage
from Tests.test_base import Basetest


class Test_Collection(Basetest):

    def test_search_page_title(self):
        print("search_page_title")
        self.search = NftCollectionPage(self.driver)
        search = self.search.get_search_page_title(TestData.Search_page_title)
        assert search == TestData.Search_page_title

    def test_is_visible_allow_page(self):
        self.search = NftCollectionPage(self.driver)
        flag = self.search.is_visible_allow_button()
        assert flag

    def test_click_allow(self):
        self.search = NftCollectionPage(self.driver)
        self.search.click_allow_button()

    # def test_is_visible_search_box(self):
    #     self.search = NftCollectionPage(self.driver)
    #     flag = self.search.is_visible_search_box()
    #     assert flag
    #
    # def test_input_search(self):
    #     self.search = NftCollectionPage(self.driver)
    #     self.search.input_search()
    #
    # def test_input_currency(self):
    #     self.search = NftCollectionPage(self.driver)
    #     self.search.click_currency()
    #
    # def test_input_min_value(self):
    #     self.search = NftCollectionPage(self.driver)
    #     self.search.input_min()
    #
    # def test_find_nft(self):
    #     self.search = NftCollectionPage(self.driver)
    #     self.search.find_nft()
    def test_click_ok_button(self):
        self.search = NftCollectionPage(self.driver)
        self.search.click_ok_button()

    # def test_single_nft_tab(self):
    #     self.nft_collection_page = NftCollectionPage(self.driver)
    #     self.nft_collection_page.single_nft_tab()



