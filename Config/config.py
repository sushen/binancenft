import os

class TestData:
    CHROME_EXECUTABLE_PATH = "../Driver/chromedriver.exe"

    BASE_URL = "https://accounts.binance.com/en/login"
    email = os.environ.get('binance_email')
    password = os.environ.get('binance_pass')
    Login_page_title = "Log In | Binance"
