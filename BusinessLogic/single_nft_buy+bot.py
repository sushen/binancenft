import time

from Bots.AllPageBot import AllPageBot
from Pages.SingleNftBuy import SingleNftBuy

# Time Counting

StartTime = time.time()
print("This Script Start " + time.ctime())

all_page = AllPageBot()


#  login
try:
    login = all_page.login()
    print(input("Press any Key: "))
except:
    print("You already lodged in")

# single nft page
all_page.driver.get(SingleNftBuy.single_nft_page)
print(input("Start Buying : "))
