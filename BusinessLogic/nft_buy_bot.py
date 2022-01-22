import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

from Bots.AllPageBot import AllPageBot
from Bots.Base_bot import BaseBot
from Config.config import TestData
from Pages.LoginPage import LoginPage
from Pages.BasePage import BasePage
from Pages.NftCollectionPage import NftCollectionPage

# Time Counting
StartTime = time.time()
print("This Script Start " + time.ctime())

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

def switch_tab_to_single_nft(driver):
    # print(len(driver.window_handles))
    start_tab_time = time.time()
    window_before = driver.window_handles[0]
    window_after = driver.window_handles[1]
    if driver.window_handles[1] == window_after:
        driver.switch_to.window(window_after)
        # We will buy when we need to
        # buy_nft()
        name_of_the_nft = driver.title
        print(name_of_the_nft)
        all_page.test_click_buy_now()
        driver.close()
        driver.switch_to.window(window_before)
        CurrentTime = time.time()
        totalRunningTime = CurrentTime - start_tab_time
        print("This Tab is running for " + str(float(totalRunningTime)))
    else:
        driver.switch_to.window(window_before)
        print(" Didn't find Second Tab")

# nft_list = all_page.driver.find_elements_by_xpath("//div[@class='css-8a1dsu']")
# print(len(nft_list))


for idx in range(1000):
    try:
        nft_list = all_page.test_find_nft()
    except:
        nft_list = ''
    print(nft_list)
    nft_numbers = len(nft_list)
    if nft_numbers >= 1:
        print(f"{idx+1} no search working and {nft_numbers} nft found")
        for nft in range(0, len(nft_list)):
            loop_start_time = time.time()
            nft_list[nft].click()
            switch_tab_to_single_nft(all_page.driver)
            CurrentTime = time.time()
            totalRunningTime = CurrentTime - loop_start_time
            print("This Loop is running for " + str(float(totalRunningTime)))
    else:
        print(f"{idx+1} no search working, No nft found ")
        all_page.test_click_ok_button()

# TODO: go to single nft
# TODO: buy nft
# TODO: Repeat the process
# TODO: go to collection

EndTime = time.time()
print("\nThis Script End " + time.ctime())
totalRunningTime = EndTime - StartTime
print("This Script is running for " + str(int(totalRunningTime)) + " Second. or\n")
print("This Script is running for " + str(int(totalRunningTime / 60)) + " Minutes.")