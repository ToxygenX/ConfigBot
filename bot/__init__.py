import asyncio
import glob
import os
import time
import sys
from pathlib import Path
from sys import argv
import logging

import telethon.utils
from telethon import TelegramClient, events, functions, types
from telethon.sessions import StringSession

ENV = os.environ.get("ENV", True)

if ENV:
    from bot.BotConfig import Config
    
logging.basicConfig(
    level=logging.INFO,
    datefmt="%d/%m/%Y %H:%M:%S",
    format="[%(asctime)s][%(name)s][%(levelname)s] ==> %(message)s",
    handlers=[logging.StreamHandler(stream=sys.stdout),
              logging.FileHandler("botx.log", mode="a", encoding="utf-8")],)

logging.getLogger("telethon").setLevel(logging.INFO)

botx = TelegramClient("thebotx", api_id=Config.API_ID, api_hash=Config.API_HASH)

botcli = TelegramClient(StringSession(Config.SESSION), api_id=Config.API_ID, api_hash=Config.API_HASH)


if Config.BOT_TOKEN is None:
    logging.info("BOT_TOKEN is None. Bot Is Quiting")
    sys.exit(1)
if Config.API_ID is None:
    logging.info("API_ID Is None.")
    sys.exit(1)
if Config.API_HASH is None:
    logging.info("API_HASH Is None. Exiting...")
    sys.exit(1)
if Config.OWNER_ID is None:
    logging.info("OWNER_ID is None. Please Add Your ID to Continue.")
    sys.exit(1)
if Config.LOG_CHAT is None:
    logging.info("Add LOG_CHAT For This Bot to Work")
    sys.exit(1)
