import asyncio
import glob
import os
import time
from pathlib import Path
from sys import argv
from logging import INFO, WARNING, FileHandler, StreamHandler, basicConfig, getLogger

import telethon.utils
from telethon import TelegramClient, events, functions, types


ENV = os.environ.get("ENV", True)

if ENV:
    from bot.BotConfig import Config
    
LOGS = getLogger("bot")
TelethonLogger = getLogger("Telethon")
TelethonLogger.setLevel(WARNING)

botx = TelegramClient("thebotx", api_id=Config.API_ID, api_hash=Config.API_HASH)
    
if Config.BOT_TOKEN is None:
    LOGS.info("BOT_TOKEN is None. Bot Is Quiting")
    sys.exit(1)
if Config.API_ID is None:
    LOGS.info("API_ID Is None.")
    sys.exit(1)
if Config.API_HASH is None:
    LOGS.info("API_HASH Is None. Exiting...")
    sys.exit(1)
if Config.OWNER_ID is None:
    LOGS.info("OWNER_ID is None. Please Add Your ID to Continue.")
    sys.exit(1)
if Config.LOG_CHAT is None:
    LOGS.info("Add LOG_CHAT For This Bot to Work")
    sys.exit(1)
