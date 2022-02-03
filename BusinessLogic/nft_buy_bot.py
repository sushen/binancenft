import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Bots.AllPageBot import AllPageBot
from Pages.NftCollectionPage import NftCollectionPage


# Time Counting
from Pages.SingleNftBuy import SingleNftBuy

StartTime = time.time()
print("This Script Start " + time.ctime())

all_page = AllPageBot()

all_page.login()

try:
    print(input("Press any Key: "))
except:
    print("You already lodged in")

# single nft page
all_page.driver.get("https://www.binance.com/en/nft/home")
# print(input("Set Password : "))

# TODO: find nft
all_page.driver.get(NftCollectionPage.collection_link)
print(input("Filter done:"))


# sold_out_xpath = "//button[normalize-space()='Sold Out']"

buy_now_xpath = "//button[contains(text(),'Buy Now')]"

not_enough_xpath = "//div[contains(text(),'have enough crypto')]"

success_paid_xpath = "//div[@class='css-57wjep']"

payment_failed_xpath = "//h6[contains(text(), 'Payment failed')]"

def availability(sold_out, buy_now):
    # print(input("Check availability:"))
    print(buy_now)
    if all_page.driver.find_elements(By.XPATH, buy_now):
        all_page.test_click_buy_now()
        # TODO : It didn't buy with continues loop
        print("clicked buy now")
        print("checking availability")
        print("going to eligibility")
        eligibility()
    except:
        print("sold out")


def eligibility():
    try:
        print("eligibility passed")
        all_page.test_click_confirm_button()
        after_payment()
    except:
        print("eligibility failed")


def after_payment():
    try:
        print("checking status")
        if WebDriverWait(all_page.driver, 5).until(EC.visibility_of_element_located((By.XPATH, success_paid_xpath))):
            print("payment successful")
    except:
        print("payment failed")
        all_page.test_click_return_button()
        try:
            all_page.test_click_buy_now()
            print("clicked buy now")
            print("checking availability")
            print("going to eligibility")
        except:
            print("sold out")
        all_page.test_click_confirm_button()


def ok_button():
    for i in range(2):
        time.sleep(1)
        print(i)
        all_page.test_click_ok_button()


def switch_tab_to_single_nft(driver):
    start_tab_time = time.time()
    window_before = driver.window_handles[0]
    # TODO : Got Error
    """ here window_after = driver.window_handles[1] IndexError: list index out of range """
    window_after = driver.window_handles[1]

    if driver.window_handles[1] == window_after:
        driver.switch_to.window(window_after)
    #
    #     # print(input("Change NFT for tasting :"))
    #     # all_page.driver.get("https://www.binance.com/en/nft/goods/detail?productId=23911067&isProduct=1")
    #     # print(input("Close Tab :"))
    #
    #     if all_page.driver.find_elements_by_xpath(sold_out_xpath):
    #         print("NFT sold out go bach to search")
    #         # print(input("Find the Sold out button :"))
    #         driver.close()
    #         driver.switch_to.window(window_before)
    #
    #     else:
    #         print(" I am buying")
    #         all_page.test_click_confirm_button()
    #
    #
    #         after_payment(success, payment_failed)

        print("going to availability")

        availability()

        driver.close()
        driver.switch_to.window(window_before)


        CurrentTime = time.time()
        totalRunningTime = CurrentTime - start_tab_time
        print("This Tab is running for " + str(float(totalRunningTime)))
    else:
        driver.switch_to.window(window_before)
        print(" Didn't find Second Tab")


# Repeat the process
buying_start_time = time.time()

for idx in range(6000):
    search_loop_start_time = time.time()
    nft_xpath = "//body/div[@id='__APP']/div[@class='css-1vvpahx']/div[@class='css-tq0shg']/main[@class='css-1wr4jig']/div[@class='css-37nf1f']/div[@class='css-7mtbla']/div[@class='css-1c5bfos']/div[@class='css-vurnku']/div[@class='css-dp93ju']/a"
    nft_list = all_page.driver.find_elements(By.XPATH, nft_xpath)

    # try:
    #     nft_list = all_page.test_find_nft()
    # except:
    #     nft_list = ''
    print(nft_list)
    nft_numbers = len(nft_list)
    if nft_numbers >= 1:
        print(f"{idx + 1} no search working and {nft_numbers} nft found")
        nft_urls = []
        for nft in nft_list:
            nft_urls.append(nft.get_attribute('href'))
            print(nft.get_attribute('href'))
        for nft_url in nft_urls:
            loop_start_time = time.time()
            # nft_url = nft_list[nft].get_attribute('href')
            print(nft_url)
            all_page.driver.execute_script("window.open()")
            all_page.driver.switch_to.window(all_page.driver.window_handles[1])
            all_page.driver.get(nft_url)
            switch_tab_to_single_nft(all_page.driver)

            ok_button()

            # TODO: Base on nft no. we wll open tabs and buy all the nft together
            CurrentTime = time.time()
            totalRunningTime = CurrentTime - loop_start_time
            print("This Loop is running for " + str(float(totalRunningTime)))
            print("................")
    else:

        print(f"{idx + 1} no search working, No nft found ")
        all_page.test_click_ok_button()
        CurrentTime = time.time()
        totalRunningTime = CurrentTime - search_loop_start_time
        print("This Search is running for " + str(float(totalRunningTime)))

        totalBuyingTime = CurrentTime - buying_start_time
        print("This Total Process is running less than " + str(float(totalBuyingTime / 60)) + " Minutes.\n")

# TODO: go to collection

EndTime = time.time()
print("\nThis Script End " + time.ctime())
totalRunningTime = EndTime - StartTime
print("This Script is running for " + str(int(totalRunningTime)) + " Second. or\n")
print("This Script is running for " + str(int(totalRunningTime / 60)) + " Minutes.")
