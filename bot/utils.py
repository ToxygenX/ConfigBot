#All Credits Belong to @CipherXBot

import re 
import inspect
import logging
import glob
from pathlib import Path
import functools

from telethon import events

from bot import botx, Config 

bothandler = Config.COMMAND_HAND_LER

def botx_cmd(add_cmd, is_args=False):
    def cmd(func):
        if is_args:
            pattern = bothandler + add_cmd + "(?: |$)(.*)"
        else:
            pattern = bothandler + add_cmd + "$"
        botx.add_event_handler(
            func, events.NewMessage(incoming=True, pattern=pattern)
        )
    return cmd

def god_only():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            moms = Config.OWNER_ID
            if event.sender_id in moms:
                await func(event)
            else:
                pass
        return wrapper
    return decorator

def start_botx(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import importlib
        import sys
        from pathlib import Path
        import bot.utils
        path = Path(f"bot/plugins/{shortname}.py")
        name = "bot.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print("Starting Your Bot.")
        print("Sucessfully imported " + shortname)
    else:
        import importlib
        import sys
        from pathlib import Path
        import bot.utils
        path = Path(f"bot/plugins/{shortname}.py")
        name = "bot.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.botx_cmd = botx_cmd
        mod.botx = botx
        mod.Config = Config
        mod.god_only = god_only()
        spec.loader.exec_module(mod)
        sys.modules["bot.plugins" + shortname] = mod
        print("Bot Has imported " + shortname)
