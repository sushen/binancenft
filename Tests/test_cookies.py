import pytest

from Config.config import TestData
from Pages.SearchPage import SearchPage
from Tests.test_base import Basetest


class Test_Cookies(Basetest):
    allow_button = "//button[contains(text(),'Accept')]"

    def test_search_page_title(self):
        print("search_page_title")
        self.search = SearchPage(self.driver)
        search = self.search.get_search_page_title(TestData.Search_page_title)
        assert search == TestData.Search_page_title

    # def test_login(self):
    #     self.search = SearchPage(self.driver)
    #     self.search.click_allow_button(self.allow_button)
