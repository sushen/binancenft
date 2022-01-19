""" This the prototype of the project"""
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pathlib

# Setting the chrome_options
chrome_options = Options()
scriptDirectory = pathlib.Path().absolute()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--user-data-dir=chrome-data")
chrome_options.add_argument('--profile-directory=Profile 8')
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument('disable-infobars')
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument("user-data-dir=chrome-data")
chrome_options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")

driver = webdriver.Chrome("Driver/chromedriver.exe", chrome_options=chrome_options)


first_price_range = 1
second_price_range = 60
search_items = "ape"

# TODO : Put Your Collection Link
collection_link = "https://www.binance.com/en/nft/shopWindow/NFT%E2%96%B5PRIDE?reSale=0&tradeType=0&orderBy=list_time&orderType=-1&isBack=1&uid=aa80c3015e02724438bd7cb9e662c5b8&order=list_time%40-1"



driver.implicitly_wait(10)

# binance_web = "https://accounts.binance.com/en/register?ref=35023868"
binance_web = "https://binance.com/"

driver.get(binance_web)

print(input("Start Project ..... :"))


def binance_login(driver):
    driver.get(binance_web)
    login = "//a[@id='header_login']"
    driver.find_element_by_xpath(login).click()
    print(input("Login Page ..... :"))

    binance_email = os.environ.get('binance_email')
    binance_password = os.environ.get('binance_pass')

    email = "//input[@name='email']"
    driver.find_element_by_xpath(email).send_keys(binance_email)
    # print(input("Email ..... :"))

    password = "//input[@name='password']"
    driver.find_element_by_xpath(password).send_keys(binance_password)
    # print(input("Password ..... :"))

    login_submit = "//button[@id='click_login_submit']"
    driver.find_element_by_xpath(login_submit).click()
    # print(input("Submit ..... :"))

    print(input("Solve Puzzle Submit ..... :"))


binance_login(driver)


def buy_nft():
    nft_buy = "//button[normalize-space()='Buy Now']"
    driver.find_element_by_xpath(nft_buy).click()
    print(input("Made that funcationlaty :"))
    # switch_tab_to_wallet_payment(driver)
    # TODO : Make click conform button
    confirm = "//button[normalize-space()='Confirm']"
    confirm_elements = driver.find_elements_by_xpath(confirm)
    if driver.find_elements_by_xpath(confirm):
        confirm_elements[0].click()
        print("Wooo .. Finish buying")
    else:
        print("budget shortage")



def switch_tab_to_single_nft(driver):
    print(len(driver.window_handles))
    window_before = driver.window_handles[0]
    window_after = driver.window_handles[1]
    if driver.window_handles[1] == window_after:
        driver.switch_to.window(window_after)
        time.sleep(10)
        # We will buy when we need to
        buy_nft()

        time.sleep(2)
        name_of_the_nft = driver.title
        print(name_of_the_nft)

        driver.close()
        driver.switch_to.window(window_before)
    else:
        driver.switch_to.window(window_before)
        print(" Didn't find Second Tab")

# print(input("Complete Puzzle Start Project ..... :"))

# TODO: Tests Buy
# buy_test = driver.get("https://www.binance.com/en/nft/goods/detail?productId=21564969&isProduct=1")


driver.get(collection_link)


# driver.implicitly_wait(10)
# search_name = "//input[@placeholder='Search items']"
# driver.find_element_by_xpath(search_name).send_keys(search_items)
# print(input("Write Search ..... :"))
#
# search_btn = "//div[@class='bn-input-suffix css-vurnku']//*[name()='svg']"
# driver.find_element_by_xpath(search_btn).click()
# print(input("Finish Search ..... :"))
#
#
# first_edition = "//div[contains(text(),'First Edition')]"
# driver.find_element_by_xpath(first_edition).click()
# print(input("First Edition ..... :"))
#
# fixed_price = "//div[contains(text(),'Fixed Price')]"
# driver.find_element_by_xpath(fixed_price).click()
# print(input("Fixed Price ..... :"))
#
# busd_radio = "(//*[name()='svg'][@class='css-a4o4go'])[3]"
# driver.find_element_by_xpath(busd_radio).click()
#
# bnb_radio = "(//*[name()='svg'][@class='css-a4o4go'])[1]"
# driver.find_element_by_xpath(bnb_radio).click()
#
# busd_radio = "(//*[name()='svg'][@class='css-a4o4go'])[3]"
# driver.find_element_by_xpath(busd_radio).click()
#
# print(input("BUSD RADIO ..... :"))
#
# driver.implicitly_wait(10)
# time.sleep(.5)
# price_range_first = "(//input[@placeholder='BUSD Price'])[1]"
# driver.find_element_by_xpath(price_range_first).send_keys(first_price_range)
# print(input("First input ..... :"))
#
# price_range_second = "(//input[@placeholder='BUSD Price'])[2]"
# driver.find_element_by_xpath(price_range_second).send_keys(second_price_range)
# print(input("Second Input ..... :"))
#
ok_button = "//button[normalize-space()='OK']"
driver.find_element_by_xpath(ok_button).click()


nft_list = "//div[@class='css-8a1dsu']"
# nft_list_elements = driver.find_elements_by_xpath(nft_list)
# print(len(nft_list_elements))
# nft_numbers = len(nft_list_elements)

print(input("Logic Correction..... :"))

# TODO : We need to loop when the nft found is 0

condition = True
# count = 0
nft_list_elements = []

for idx in range(1000):
    nft_list_elements = driver.find_elements_by_xpath(nft_list)
    # print(len(nft_list_elements))
    nft_numbers = len(nft_list_elements)
    if nft_numbers >= 1:
        print(f"{idx} no search working and {nft_numbers} nft found")
        for nft in range(0, nft_numbers):
            print(nft)
            nft_list_elements[nft].click()

            switch_tab_to_single_nft(driver)

            # print(input("Fixed logic ..... :"))
        condition = False
    else:
        print(f"{idx} no search working, No nft found ")
        driver.find_element_by_xpath(ok_button).click()
        # if count == 10:
        #     first_edition = "//div[contains(text(),'First Edition')]"
        #     driver.find_element_by_xpath(first_edition).click()
        #     print(input("First Edition ..... :"))
        #
        #     fixed_price = "//div[contains(text(),'Fixed Price')]"
        #     driver.find_element_by_xpath(fixed_price).click()
        #     print(input("Fixed Price ..... :"))
        condition = True
    # count += 1

print(input("End Current performance ..... :"))

driver.quit()
