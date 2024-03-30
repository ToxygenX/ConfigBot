import re

from telethon import custom, events, Button
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import InputMessagesFilterDocument

from bot.BotConfig import Config

@botx_cmd("start", is_args=False)
async def start(event):
    usr_cmd = event.text.split("_")[-1]
    probot = await chatbot.get_me()
    bot_id = probot.first_name
    bot_username = probot.username
    replied_user = await event.client(GetFullUserRequest(event.sender_id))
    firstname = replied_user.user.first_name
    uname = replied_user.user.username
    msg = f"**سلام {firstname} عزیز، به ربات {bot_username} خوش آمدید** \n**برای دریافت کانفیگ بر روی گزینه های زیر کلیک نمایید**"
    await botx.send_message(
        event.chat_id, 
        msg, 
        buttons = [
             [Button.text("Naspernet (Android)"), Button.text("Naspernet (iOS)")],
             [Button.text("Dark Tunnel"), Button.text("V2rayNG")],
             [Button.text("آموزش")],
              ],
        resize=True,
    )
    if usr_cmd == "Naspernet (Android)":
        async for message in client.iter_messages(Config.LOG_CHAT, filter=InputMessagesFilterDocument):
            if message.text == "#nasperand":
                await botx.send_file(event.chat_id, message.document, caption="Naspernet (Android)")
    if usr_cmd == "Naspernet (iOS)":
        async for message in client.iter_messages(Config.LOG_CHAT, filter=InputMessagesFilterDocument):
            if message.text == "#nasperios":
                await botx.send_file(event.chat_id, message.document, caption="Naspernet (iOS)")
    if usr_cmd == "Dark Tunnel":
        async for message in client.iter_messages(Config.LOG_CHAT, filter=InputMessagesFilterDocument):
            if message.text == "#dark":
                await botx.send_file(event.chat_id, message.document, caption="Dark Tunnel")
    if usr_cmd == "V2rayNG":
        async for message in client.iter_messages(Config.LOG_CHAT, filter=InputMessagesFilterDocument):
            if message.text == "#v2ray":
                await botx.send_file(event.chat_id, message.document, caption="V2rayNG")
    if usr_cmd == "آموزش":
        async for message in client.iter_messages(Config.LOG_CHAT, filter=InputMessagesFilterDocument):
            if message.text == "#tutorial":
                await botx.send_file(event.chat_id, message.document, caption="آموزش")
    
