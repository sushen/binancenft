""" Its a mixin class that mixed all Bot """

from Bots.bot_login import Bot_Login
from Bots.bot_nft_collection_page import Bot_Collection
from Bots.bot_single_nft_buy import bot_single_nft_buy


class AllPageBot(
    Bot_Login,
    Bot_Collection,
    bot_single_nft_buy
):
    pass
