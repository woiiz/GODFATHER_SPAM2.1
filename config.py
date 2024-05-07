import os
from telethon import TelegramClient
from decouple import config
from os import getenv
import logging


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


#values
API_ID = 863616
API_HASH = "d4fb9f1a28a828fb42b05f2362ee8760"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = config("irfan zafwan", None)
HEROKU_API_KEY = config("HRKU-142caffa-6b45-4019-8f01-8e6281b15c60", None)
BOT_TOKEN = config("6846588038:AAGoB924wB-B92e_Tsd-TZgHJkV0WTVuH7M", default=None)
BOT_TOKEN2 = config("6895455557:AAE2jpasj4tI4HS5fu4WLSklyeP8MqEnsqA", default=None)
BOT_TOKEN3 = config("6555960539:AAEAGReL4Euo92FIgsGha32Xnuint6FqE34", default=None)
BOT_TOKEN4 = config("6575377322:AAHE8qKv59aj3mQDXgg5bw2PHCCPrE-NiGE", default=None)
BOT_TOKEN5 = config("7005284304:AAFWNH6pspK_I0-uF2sqeId8tN6kubNu2WU", default=None)
BOT_TOKEN6 = config("6401252259:AAHMknDNm2HtIY2Wm3iprIpyTRfnnI0HgTY", default=None)
BOT_TOKEN7 = config("7180683439:AAF_XxCr3dYvcb6gVKXRPNnD1rbdZZ7OQQ4", default=None)
BOT_TOKEN8 = config("6790295599:AAGGZPHNRjOrq6188N5AoFbYQljUpAXZD1E", default=None)
BOT_TOKEN9 = config("6738358490:AAEQwSwPVgtQW41d3-00taIPaT5jv-gp1PM", default=None)
BOT_TOKEN10 = config("6434888097:AAEh_EfdjDHJAxd1JvAXaDyafyCGWoow5rU", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
SUDO_USERS.append(5551014551)
SUDO_USERS.append(6218518584)
SUDO_USERS.append(6218518584)

OWNER_ID = int(os.environ.get(6778796199", None))


# Don't Mess with Codes !! 
DB_URI = config("DATABASE_URL", None)
SUDO_USERS.append(OWNER_ID)

# Tokens
MK1 = TelegramClient('MK', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
MK2 = TelegramClient('MK2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)
MK3 = TelegramClient('MK3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)
MK4 = TelegramClient('MK4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)
MK5 = TelegramClient('MK5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)
MK6 = TelegramClient('MK6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)
MK7 = TelegramClient('MK7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)
MK8 = TelegramClient('MK8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)
MK9 = TelegramClient('MK9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)
MK10 = TelegramClient('MK10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)
