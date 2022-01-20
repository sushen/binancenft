import pickle
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

from Config.config import TestData

collection_link = "https://www.binance.com/en/nft/shopWindow/NFT%E2%96%B5PRIDE?reSale=0&tradeType=0&orderBy=list_time&orderType=-1&isBack=1&uid=aa80c3015e02724438bd7cb9e662c5b8&order=list_time%40-1"

driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)


def save_cookies(driver, location):
    pickle.dump(driver.get_cookies(), open(location, "wb"))


def load_cookies(driver, location, url=None):
    cookies = pickle.load(open(location, "rb"))
    # driver.delete_all_cookies()
    driver.get("https://www.binance.com/en" if url is None else url)
    for cookie in cookies:
        if isinstance(cookie.get('expiry'), float):
            cookie['expiry'] = int(cookie['expiry'])
        driver.add_cookie(cookie)


def delete_cookies(driver, domains=None):

    if domains is not None:
        cookies = driver.get_cookies()
        original_len = len(cookies)
        for cookie in cookies:
            if str(cookie["domain"]) in domains:
                cookies.remove(cookie)
        if len(cookies) < original_len:  # if cookies changed, we will update them
            # deleting everything and adding the modified cookie object
            driver.delete_all_cookies()
            for cookie in cookies:
                driver.add_cookie(cookie)
    else:
        driver.delete_all_cookies()


cookies_location = "cookies.txt"

driver.get(TestData.BASE_URL)

# login = "//a[@id='header_login']"
# driver.find_element(By.XPATH, "header_login").click()
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
print(input("Submit ..... :"))

save_cookies(driver, cookies_location)
# driver.quit()

load_cookies(driver, TestData.Cookie_location)
driver.get(collection_link)
