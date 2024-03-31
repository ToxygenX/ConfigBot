import asyncio
import glob
import os
import time
from pathlib import Path
from sys import argv
from distutils.util import strtobool as sb

import telethon.utils
from telethon import TelegramClient, events, functions, types


ENV = os.environ.get("ENV", True)

if ENV:
    from bot.BotConfig import Config

botx = TelegramClient("thebotx", api_id=Config.API_ID, api_hash=Config.API_HASH)
    
if Config.BOT_TOKEN is None:
    print("BOT_TOKEN is None. Bot Is Quiting")
    sys.exit(1)
if Config.API_ID is None:
    print("API_ID Is None.")
    sys.exit(1)
if Config.API_HASH is None:
    print("API_HASH Is None. Exiting...")
    sys.exit(1)
if Config.OWNER_ID is None:
    print("OWNER_ID is None. Please Add Your ID to Continue.")
    sys.exit(1)
if Config.LOG_CHAT is None:
    print("Add LOG_CHAT For This Bot to Work")
    sys.exit(1)
