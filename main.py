import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pathlib
import random

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

driver = webdriver.Chrome("chromedriver.exe", chrome_options=chrome_options)


first_price_range = 10
second_price_range = 100


driver.implicitly_wait(10)

binance_web = "https://accounts.binance.com/en/register?ref=35023868"

driver.get(binance_web)


def binance_login(driver):
    driver.get(binance_web)

    login = "//a[@id='header_login']"
    driver.find_element_by_xpath(login).click()
    # print(input("Login Page ..... :"))

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

# TODO: Test Buy
# buy_test = driver.get("https://www.binance.com/en/nft/goods/detail?productId=21564969&isProduct=1")


# driver.get("https://www.binance.com/en/nft/market")

# driver.get("https://www.binance.com/en/nft/shopWindow/Mulder?orderBy=list_time&orderType=-1&isBack=1&uid=0cc9e541fc1df9fb78598d71c06ebc1f&order=list_time%40-1")

driver.get("https://www.binance.com/en/nft/shopWindow/Mytheria?currency=BUSD&amountTo=10&orderBy=list_time&orderType=-1&isBack=0&uid=c19522ee08f014f8b98d7f3ce4309f64&order=list_time%40-1")

first_edition = "//div[contains(text(),'First Edition')]"
driver.find_element_by_xpath(first_edition).click()
# print(input("First Edition ..... :"))

fixed_price = "//div[contains(text(),'Fixed Price')]"
driver.find_element_by_xpath(fixed_price).click()
# print(input("Fixed Price ..... :"))

busd_radio = "(//*[name()='svg'][@class='css-a4o4go'])[3]"
driver.find_element_by_xpath(busd_radio).click()

bnb_radio = "(//*[name()='svg'][@class='css-a4o4go'])[1]"
driver.find_element_by_xpath(bnb_radio).click()

busd_radio = "(//*[name()='svg'][@class='css-a4o4go'])[3]"
driver.find_element_by_xpath(busd_radio).click()

# print(input("BUSD RADIO ..... :"))

driver.implicitly_wait(10)
time.sleep(.5)
price_range_first = "(//input[@placeholder='BUSD Price'])[1]"
driver.find_element_by_xpath(price_range_first).send_keys(first_price_range)
# print(input("First input ..... :"))

price_range_second = "(//input[@placeholder='BUSD Price'])[2]"
driver.find_element_by_xpath(price_range_second).send_keys(second_price_range)
# print(input("Second Input ..... :"))

ok_button = "//button[normalize-space()='OK']"
driver.find_element_by_xpath(ok_button).click()


nft_list = "//div[@class='css-8a1dsu']"
nft_list_elements = driver.find_elements_by_xpath(nft_list)
print(len(nft_list_elements))
nft_numbers = len(nft_list_elements)

# print(input("Fixed logic ..... :"))

if nft_numbers >= 1:
    print("nft found")
    for nft in range(0, nft_numbers):
        print(nft)
        nft_list_elements[nft].click()

        switch_tab_to_single_nft(driver)

        print(input("Fixed logic ..... :"))
else:
    print("No nft found")

print(input("End Current performance ..... :"))

driver.quit()
