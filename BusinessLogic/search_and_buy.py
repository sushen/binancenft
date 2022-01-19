# from Config.bot_config import BotData
# from Bots.bot_LoginPage import Bot_Login
# from Pages.LoginPage import LoginPage
#
# botlogin = Bot_Login()
#
# login = botlogin.test_login()

# try:
#     login = botlogin.test_login()
#     print(input("Press any Key: "))
# except:
#     print("You already lodged in")

from Config.bot_config import BotData
from Pages.LoginPage import LoginPage

username = "jkdkja"
password = "jnjdas"

all_page = LoginPage(BotData.CHROME_EXECUTABLE_PATH)


all_page.do_login(username, password)

