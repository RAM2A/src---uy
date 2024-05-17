#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = "24665357" #config("API_ID", default=None, cast=int)
API_HASH = "beb7e4b83ada668fa85f9a9b56338f1d" #config("API_HASH", default=None)
BOT_TOKEN = "6561626656:AAEofDQ_-uaIk3vJmiY1xuzjPEeczUXVNt4" #config("BOT_TOKEN", default=None)
SESSION = "BQF4XQ0AK4XzYLE5k1IGJKNxnmUx2Z8Obg4p1dIp2ZMDtqh5APO5S4Al_XIFqEGNDhSex6-SPiV-XVKY-PZtu0jrluwLhwTZlbrLAzEmrO8OErlOeGOYsiCgkYsk9xDrtN9NVXva3Z9YdXqmW3fMpe0GGKPd_DfQsTC9w5A7ksraWIYiDS808eP8sVJTIIFUb4XdSbTfkfXsYjxKUbm8hVwuaxm66Z-B6KykVAmR0kPkGjlLxH3FzKjV6B0v3gkkQhcReNf49ZRvUa8uw4AlS8cE4H574supRAnG3quK9Sjolj3oZykZ18_CQgyzjKxLgh0IyQGfKtiSpKXW1NW6cB4x1eBa6wAAAABmXyPCAA" #config("SESSION", default=None)
FORCESUB = "1002137417670" #config("FORCESUB", default=None)
AUTH = "1717511106" #config("AUTH", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
