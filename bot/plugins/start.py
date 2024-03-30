from telethon import custom, events, Button
from telethon.tl import types
from telethon.tl.types import InputMessagesFilterDocument
from telethon.utils import get_display_name

from bot.BotConfig import Config

buttons= [
             [
                 Button.text("Naspernet-Android"), 
                 Button.text("Naspernet-iOS"),
             ],
             [
                 Button.text("Dark Tunnel"), 
                 Button.text("V2rayNG"),
             ],
             [
                 Button.text("آموزش"),
             ],
             resize=True,
        ]

def inline_mention(user, custom=None, html=False):
    mention_text = get_display_name(user) or "Deleted Account" if not custom else custom
    if isinstance(user, types.User):
        if html:
            return f"<a href=tg://user?id={user.id}>{mention_text}</a>"
        return f"[{mention_text}](tg://user?id={user.id})"
    if isinstance(user, types.Channel) and user.username:
        if html:
            return f"<a href=https://t.me/{user.username}>{mention_text}</a>"
        return f"[{mention_text}](https://t.me/{user.username})"
    return mention_text


@botx_cmd("start", is_args=False)
async def start(event):
    usr_cmd = event.text.split("_")[-1]
    probot = await botx.get_me()
    bot_id = probot.first_name
    bot_username = probot.username
    mention = inline_mention(event.sender)
    msg = f"**سلام {mention} عزیز، به ربات {bot_username} خوش آمدید** \n**برای دریافت کانفیگ بر روی گزینه های زیر کلیک نمایید**"
    await botx.send_message(event.chat_id, msg, buttons=buttons)
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
    
