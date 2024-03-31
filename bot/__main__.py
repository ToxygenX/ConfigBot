import asyncio 
import glob
import sys
from sys import argv
from pathlib import Path
from logging import getLogger

import telethon.utils
from telethon import TelegramClient

from bot.utils import botx_cmd, start_botx
from bot import Config, botx  

    
LOGS = getLogger("CythonX")

if len(argv) not in (1, 3, 4):
    botx.disconnect()
else:
    botx.start(bot_token=Config.BOT_TOKEN)
    
path = "bot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        start_botx(shortname.replace(".py", ""))

LOGS.info("Your Bot is Ready.")
LOGS.info("Try Sending /start")

if len(argv) not in (1, 3, 4):
    botx.disconnect()
else:
    botx.run_until_disconnected()
