import asyncio 
import glob
import logging
import sys
from sys import argv
from pathlib import Path

import telethon.utils
from telethon import TelegramClient

from bot.utils import botx_cmd, start_botx
from bot import Config, botx  

logging.basicConfig(
    level=logging.INFO,
    datefmt="%d/%m/%Y %H:%M:%S",
    format="[%(asctime)s][%(levelname)s] => %(message)s",
    handlers=[logging.StreamHandler(stream=sys.stdout),
              logging.FileHandler("bot.log", mode="a", encoding="utf-8")],)

logging.getLogger("telethon").setLevel(logging.ERROR)
logging.getLogger("bot").setLevel(logging.INFO)

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

print("Your Bot is Ready.")
print("Try Sending /start")

if len(argv) not in (1, 3, 4):
    botx.disconnect()
else:
    botx.run_until_disconnected()
