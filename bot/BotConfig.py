import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    API_HASH = os.environ.get("API_HASH", None)
    API_ID = int(os.environ.get("APP_ID", 6))
    SESSION = os.environ.get("SESSION", None)
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "").split())
    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", "^/")
    LOG_CHAT = int(os.environ.get("LOG_CHAT", False))
