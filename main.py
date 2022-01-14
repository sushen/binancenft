import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pathlib
import random

# Setting the chrome_options
global chrome_options
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


first_price_range = 69
second_price_range = 90

# print(input("Connect your waller address :"))
driver.implicitly_wait(10)
driver.get("https://www.binance.com")

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

print(input("Complete Puzzle Start Project ..... :"))

driver.get("https://www.binance.com/en/nft/market")

driver.get("https://www.binance.com/en/nft/shopWindow/Mulder?orderBy=list_time&orderType=-1&isBack=1&uid=0cc9e541fc1df9fb78598d71c06ebc1f&order=list_time%40-1")

first_edition = "//div[contains(text(),'First Edition')]"
driver.find_element_by_xpath(first_edition).click()
print(input("First Edition ..... :"))

fixed_price = "//div[contains(text(),'Fixed Price')]"
driver.find_element_by_xpath(fixed_price).click()
print(input("Fixed Price ..... :"))

busd_radio = "(//*[name()='svg'][@class='css-a4o4go'])[3]"
driver.find_element_by_xpath(busd_radio).click()
print(input("BUSD RADIO ..... :"))

price_range_first = "(//input[@placeholder='BUSD Price'])[1]"
driver.find_element_by_xpath(price_range_first).send_keys(first_price_range)
print(input("First input ..... :"))

price_range_second = "(//input[@placeholder='BUSD Price'])[2]"
driver.find_element_by_xpath(price_range_second).send_keys(second_price_range)
print(input("Second Input ..... :"))

ok_button = "//button[normalize-space()='OK']"
driver.find_element_by_xpath(ok_button).click()

nft_list = "//div[@class='css-8a1dsu']"
nft_list_elements = driver.find_elements_by_xpath(nft_list)
print(len(nft_list_elements))

print(input("End Current performance ..... :"))

ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()

driver.implicitly_wait(2)
time.sleep(9)
# lowest_prize_xpath = '//div[@class="component-objkt-gallery-element"]'
# lowest_prize_selector = driver.find_elements_by_xpath(lowest_prize_xpath)

# print(lowest_prize_selector)
# print(len(lowest_prize_selector))

all_nft_xpath = "//div[@type='img']"
all_nft_xpath_selector = driver.find_elements_by_xpath(all_nft_xpath)


def switch_tab_to_wallet_payment(driver):
    window_before = driver.window_handles[1]
    driver.implicitly_wait(10)
    time.sleep(10)
    print(len(driver.window_handles))
    window_after = driver.window_handles[2]
    if driver.window_handles[2] == window_after:
        driver.switch_to.window(window_after)
        time.sleep(2)
        # We will buy when we need to
        wallet_title = driver.title
        print(wallet_title)
        if wallet_title == "Confirm | Temple Wallet":
            time.sleep(2)
            ActionChains(driver).send_keys('Universe!1235813').pause(4).send_keys(Keys.ENTER).perform()
            time.sleep(4)
            ActionChains(driver).send_keys(Keys.TAB * 4).pause(2).send_keys(Keys.TAB * 5).pause(2).send_keys(Keys.ENTER).perform()
            time.sleep(4)
        driver.switch_to.window(window_before)
    else:
        driver.switch_to.window(window_before)
        print(" Didn't find third Tab")


def buy_nft():
    print(input("Made that funcationlaty :"))
    buy_button_xpath = "//button[@class='action-button buy mb-20']"
    buy_button_selector = driver.find_element_by_xpath(buy_button_xpath)
    buy_button_selector.click()
    switch_tab_to_wallet_payment(driver)


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


def click_and_open_new_tab(driver, element):
    element_action = ActionChains(driver)
    element_action.key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()


for i in range(len(all_nft_xpath_selector)):
    driver.implicitly_wait(5)
    time.sleep(5)
    print(all_nft_xpath_selector[i])
    click_and_open_new_tab(driver, all_nft_xpath_selector[i+2])
    switch_tab_to_single_nft(driver)
    print(input("nft element :"))
    print("We are in " + str(i+1) + " no NFT")