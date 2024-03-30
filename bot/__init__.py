import asyncio
import glob
import os
import time
from pathlib import Path
from sys import argv
from distutils.util import strtobool as sb
from logging import DEBUG, WARNING, basicConfig, getLogger, INFO
from logging.handlers import RotatingFileHandler

import telethon.utils
from telethon import TelegramClient, events, functions, types


ENV = os.environ.get("ENV", True)

if ENV:
    from bot.BotConfig import Config

botx = TelegramClient("thebotx", api_id=Config.API_ID, api_hash=Config.API_HASH)

if bool(ENV):
    CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))
    if CONSOLE_LOGGER_VERBOSE:
        basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            level=DEBUG,
        )
    else:
        basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=INFO
        )
    logger = getLogger(__name__)
    
if Config.BOT_TOKEN is None:
    logger.info("BOT_TOKEN is None. Bot Is Quiting")
    sys.exit(1)
if Config.API_ID is None:
    logger.info("API_ID Is None.")
    sys.exit(1)
if Config.API_HASH is None:
    logger.info("API_HASH Is None. Exiting...")
    sys.exit(1)
if Config.OWNER_ID is None:
    logger.info("OWNER_ID is None. Please Add Your ID to Continue.")
    sys.exit(1)
if Config.LOG_CHAT is None:
    logger.info("Add LOG_CHAT For This Bot to Work")
    sys.exit(1)
