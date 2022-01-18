import os


class BotData:
    CHROME_EXECUTABLE_PATH = "../Driver/chromedriver.exe"
    FIREFOX_EXECUTABLE_PATH = "../geckodriver.exe"
    BASE_URL = "https://www.binance.com/"

    # My Account
    EMAIL = os.environ.get('binance_email')
    PASSWORD = os.environ.get('binance_pass')
