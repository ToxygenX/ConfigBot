import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    API_HASH = os.environ.get("API_HASH", "0c30e3026276a17c3cc4471d7d0883de")
    API_ID = int(os.environ.get("APP_ID", 26109053))
    SESSION = os.environ.get("SESSION", None)
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "").split())
    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", "^/")
    LOG_CHAT = int(os.environ.get("LOG_CHAT", False))
