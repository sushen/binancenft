from Config.bot_config import BotData
from Pages.LoginPage import LoginPage

username = "jkdkja"
password = "jnjdas"

all_page = LoginPage(BotData.CHROME_EXECUTABLE_PATH)


all_page.do_login(username, password)

