#All Credits Belong to @CipherXBot

import asyncio 
import glob
import sys
from sys import argv
from pathlib import Path
import logging

import telethon.utils
from telethon import TelegramClient

from bot.utils import botx_cmd, start_botx
from bot import Config, botx, botcli

if len(argv) not in (1, 3, 4):
    botx.disconnect()
    botcli.disconnect()
else:
    botx.start(bot_token=Config.BOT_TOKEN)
    logging.info("API Client Started")
    botcli.start()
    logging.info("CLI Client Started")
    
path = "bot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        start_botx(shortname.replace(".py", ""))

logging.info("Your Bot is Ready.")
logging.info("Try Sending /start")

if len(argv) not in (1, 3, 4):
    botx.disconnect()
    botcli.disconnect()
else:
    botx.run_until_disconnected()
    botcli.run_until_disconnected()
