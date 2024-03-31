import os
import logging

from telethon import custom, events, Button
from telethon.tl import types
from telethon.tl.types import InputMessagesFilterDocument, InputMessagesFilterVideo
from telethon.utils import get_display_name

from bot.BotConfig import Config
from bot import botx, botcli


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
    probot = await botx.get_me()
    bot_id = probot.first_name
    bot_username = probot.username
    mention = inline_mention(event.sender)
    msg = f"**سلام {mention} عزیز، به ربات {bot_username} خوش آمدید** \n**برای دریافت کانفیگ بر روی گزینه های زیر کلیک نمایید**"
    await botx.send_message(event.chat_id, msg, buttons=buttons)


@botx.on(events.NewMessage(pattern="Naspernet-Android", func=lambda e: e.is_private))
async def catcher(event):
    async for message in botcli.iter_messages(Config.LOG_CHAT, filter=InputMessagesFilterDocument):
        try:
            if ".npv4" in message.document.attributes[0].file_name:
                file = await botcli.download_media(message.document)
                await botx.send_file(event.chat_id, file, caption=message.message)
                os.remove(file)
        except AttributeError:
            return


@botx.on(events.NewMessage(pattern="Naspernet-iOS", func=lambda e: e.is_private))
async def catcher(event):
    async for message in botcli.iter_messages(Config.LOG_CHAT, filter=InputMessagesFilterDocument):
        try:
            if ".inpv" in message.document.attributes[0].file_name:
                file = await botcli.download_media(message.document)
                await botx.send_file(event.chat_id, file, caption=message.message)
                os.remove(file)
        except AttributeError:
            return


@botx.on(events.NewMessage(pattern="Dark Tunnel", func=lambda e: e.is_private))
async def catcher(event):
    async for message in botcli.iter_messages(Config.LOG_CHAT, filter=InputMessagesFilterDocument):
        try:
            if ".dark" in message.document.attributes[0].file_name:
                file = await botcli.download_media(message.document)
                await botx.send_file(event.chat_id, file, caption=message.message)
                os.remove(file)
        except AttributeError:
            return


@botx.on(events.NewMessage(pattern="V2rayNG", func=lambda e: e.is_private))
async def catcher(event):
    async for message in botcli.iter_messages(Config.LOG_CHAT):
        try:
            if "subscription" in message.message:
                await botx.send_message(event.chat_id, message.message)
        except Exception as e:
            logging.info(f"Error: {str(e)}")


@botx.on(events.NewMessage(pattern="آموزش", func=lambda e: e.is_private))
async def catcher(event):
    async for message in botcli.iter_messages(Config.LOG_CHAT, filter=InputMessagesFilterVideo):
        try:
            if message.message.startswith("آموزش"):
                file = await botcli.download_media(message.media)
                await botx.send_file(event.chat_id, file, caption=message.message)
                os.remove(file)
        except AttributeError:
            return
