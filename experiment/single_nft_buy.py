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

driver = webdriver.Chrome("../Driver/chromedriver.exe", chrome_options=chrome_options)

driver.implicitly_wait(10)

# binance_web = "https://www.binance.com/en/nft/goods/detail?productId=22229475&isProduct=1"
binance_web = "https://www.binance.com/en/nft/goods/detail?productId=22233878&isProduct=1"


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
    # print(input("Made that funcationlaty :"))
    # switch_tab_to_wallet_payment(driver)
    # TODO : Make click conform button
    confirm = "//button[normalize-space()='Confirm']"
    confirm_elements = driver.find_elements_by_xpath(confirm)
    if driver.find_elements_by_xpath(confirm):
        confirm_elements[0].click()
        print("Wooo .. Finish buying")
    else:
        print("budget shortage")


buy_nft()
