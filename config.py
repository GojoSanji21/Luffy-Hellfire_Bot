# +++ Made By Sanjiii [telegram username: @Urr_Sanjiii] +++

import asyncio
import os
import logging
from logging.handlers import RotatingFileHandler


#Bot token @Botfather, --⚠️ REQUIRED--
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7777755843:AAHEpM9PI-ooL4qgy_VST-cRcAeuTQeDNcw")

#Your API ID from my.telegram.org, --⚠️ REQUIRED--
APP_ID = int(os.environ.get("APP_ID", "24371796"))

#Your API Hash from my.telegram.org, --⚠️ REQUIRED--
API_HASH = os.environ.get("API_HASH", "8121c78f4b8b31e88cc2623d1277338d")

#Your db channel Id --⚠️ REQUIRED--
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002301848493"))

#OWNER ID --⚠️ REQUIRED--
OWNER_ID = int(os.environ.get("OWNER_ID", "1683225887"))

#SUPPORT_GROUP: This is used for normal users for getting help if they don't understand how to use the bot --⚠ OPTIONAL--
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP", "-1002361458256")

#Port
PORT = os.environ.get("PORT", "5000")

#Database --⚠️ REQUIRED--
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://sagatobots00001:sagatobots100@cluster00001.vgdshkw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster00001")
DB_NAME = os.environ.get("DATABASE_NAME", "monkey_d_luffy_file_bot")

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#Collection of pics for Bot // #Optional but atleast one pic link should be replaced if you don't want predefined links
PICS = (os.environ.get("PICS", "https://ibb.co/mCBwVrTJ")).split() #Required

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
