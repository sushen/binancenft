""" Its a mixin class that mixed all Bot """

from Bots.bot_login import Bot_Login
from Bots.bot_nft_collection_page import Bot_Collection


class AllPageBot(
    Bot_Login,
    Bot_Collection
):
    pass
