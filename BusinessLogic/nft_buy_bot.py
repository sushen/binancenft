import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

from Bots.AllPageBot import AllPageBot
from Bots.Base_bot import BaseBot
from Config.config import TestData
from Pages.LoginPage import LoginPage
from Pages.BasePage import BasePage
from Pages.NftCollectionPage import NftCollectionPage

all_page = AllPageBot()


# TODO: go to binance

# TODO: login
try:
    login = all_page.login()
    print(input("Press any Key: "))
except:
    print("You already lodged in")
# if all_page.test_is_visible_allow_page():
#     all_page.test_click_allow()
# else:
#     print("Allow page not found")
# TODO: find nft
all_page.driver.get(NftCollectionPage.collection_link)
print(input("Filter done:"))
nft_list = all_page.test_find_nft()

def switch_tab_to_single_nft(driver):
    print(len(driver.window_handles))
    window_before = driver.window_handles[0]
    window_after = driver.window_handles[1]
    if driver.window_handles[1] == window_after:
        driver.switch_to.window(window_after)
        time.sleep(10)
        # We will buy when we need to
        # buy_nft()

        time.sleep(2)
        name_of_the_nft = driver.title
        print(name_of_the_nft)

        driver.close()
        driver.switch_to.window(window_before)
    else:
        driver.switch_to.window(window_before)
        print(" Didn't find Second Tab")

# nft_list = all_page.driver.find_elements_by_xpath("//div[@class='css-8a1dsu']")
for nft in range(0, len(nft_list)):
    nft_list[nft].click()
print(len(nft_list))
print(nft_list)
# TODO: go to single nft
# TODO: buy nft
# TODO: Repeat the process
# TODO: go to collection

