#All Credits Belong to @CipherXBot

import os
import asyncio
import logging

from telethon import custom, events, Button
from telethon.tl import types
from telethon.utils import get_display_name
from telethon.tl.types import InputMessagesFilterDocument, InputMessagesFilterUrl
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import (
    ChannelParticipant, 
    ChannelParticipantCreator, 
    ChannelParticipantAdmin, 
    ChannelParticipantBanned,
)
from telethon.errors import UserNotParticipantError

from bot.BotConfig import Config
from bot import botx, botcli


buttons= [
             [
                 Button.text("Napsternetv-Android", resize=True), 
                 Button.text("Napsternetv-iOS", resize=True),
             ],
             [
                 Button.text("Dark Tunnel", resize=True), 
                 Button.text("V2rayNG", resize=True),
             ],
             [
                 Button.text("آموزش", resize=True),
                 Button.text("حمایت", resize=True),
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


async def is_member(user_id):
    try:
        values = await botx(GetParticipantRequest("@Hack_Team", user_id))
        if isinstance(values.participant, ChannelParticipant):
            return True
        if isinstance(values.participant, ChannelParticipantCreator):
            return True
        if isinstance(values.participant, ChannelParticipantAdmin):
            return True
        if isinstance(values.participant, ChannelParticipantBanned):
            return "FalseBanned"
    except UserNotParticipantError:
        return False


@botx_cmd("start", is_args=False)
async def start(event):
    user_id = int(event.sender.id)
    if await is_member(user_id) == False:
        await botx.send_message(event.chat_id, "لطفا برای استفاده از ربات، به چنل @Hack_Team جوین شوید.")
    if await is_member(user_id) == "FalseBanned":
        await botx.send_message(event.chat_id, "شما بن شده اید و نمی توانید از ربات استفاده نمایید.")
    if await is_member(user_id)== True:
        probot = await botx.get_me()
        bot_id = probot.first_name
        bot_username = probot.username
        mention = inline_mention(event.sender)
        msg = f"**سلام {mention} عزیز، به ربات 𝐿𝑂𝑅𝐷 𝐶𝑂𝑁𝐹𝐼𝐺 خوش آمدید** \n**برای دریافت کانفیگ بر روی گزینه های زیر کلیک نمایید**"
        await botx.send_message(event.chat_id, msg, buttons=buttons)


@botx.on(events.NewMessage(pattern="Napsternetv-Android", func=lambda e: e.is_private))
async def catcher(event):
    user_id = int(event.sender.id)
    if await is_member(user_id) == False:
        await botx.send_message(event.chat_id, "لطفا برای استفاده از ربات، به چنل @Hack_Team جوین شوید.")
    if await is_member(user_id) == "FalseBanned":
        await botx.send_message(event.chat_id, "شما بن شده اید و نمی توانید از ربات استفاده نمایید.")
    if await is_member(user_id) == True:
        async for message in botcli.iter_messages(Config.LOG_CHAT, filter=InputMessagesFilterDocument):
            try:
                if ".npv4" in message.document.attributes[0].file_name:
                    file = await botcli.download_media(message.document)
                    await botx.send_file(event.chat_id, file, caption=message.message)
                    os.remove(file)
            except AttributeError:
                return


@botx.on(events.NewMessage(pattern="Napsternetv-iOS", func=lambda e: e.is_private))
async def catcher(event):
    user_id = int(event.sender.id)
    if await is_member(user_id) == False:
        await botx.send_message(event.chat_id, "لطفا برای استفاده از ربات، به چنل @Hack_Team جوین شوید.")
    if await is_member(user_id) == "FalseBanned":
        await botx.send_message(event.chat_id, "شما بن شده اید و نمی توانید از ربات استفاده نمایید.")
    if await is_member(user_id) == True:
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
    user_id = int(event.sender.id)
    if await is_member(user_id) == False:
        await botx.send_message(event.chat_id, "لطفا برای استفاده از ربات، به چنل @Hack_Team جوین شوید.")
    if await is_member(user_id) == "FalseBanned":
        await botx.send_message(event.chat_id, "شما بن شده اید و نمی توانید از ربات استفاده نمایید.")
    if await is_member(user_id) == True:
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
    user_id = int(event.sender.id)
    if await is_member(user_id) == False:
        await botx.send_message(event.chat_id, "لطفا برای استفاده از ربات، به چنل @Hack_Team جوین شوید.")
    if await is_member(user_id) == "FalseBanned":
        await botx.send_message(event.chat_id, "شما بن شده اید و نمی توانید از ربات استفاده نمایید.")
    if await is_member(user_id) == True:
        async for message in botcli.iter_messages(Config.LOG_CHAT, filter=InputMessagesFilterUrl):
            try:
                if "subscription" in message.message:
                    await botx.send_message(event.chat_id, message.message, link_preview=False)
            except Exception as e:
                logging.info(f"Error: {str(e)}")


@botx.on(events.NewMessage(pattern="آموزش", func=lambda e: e.is_private))
async def catcher(event):
    user_id = int(event.sender.id)
    if await is_member(user_id) == False:
        await botx.send_message(event.chat_id, "لطفا برای استفاده از ربات، به چنل @Hack_Team جوین شوید.")
    if await is_member(user_id) == "FalseBanned":
        await botx.send_message(event.chat_id, "شما بن شده اید و نمی توانید از ربات استفاده نمایید.")
    if await is_member(user_id) == True:
        await botx.send_file(event.chat_id, "https://graph.org/file/8170922e5d374c592008e.mp4", caption="آموزش اتصال NapsternetV")
        await botx.send_file(event.chat_id, "https://graph.org/file/d6e4d3d5f4389caa759ae.mp4", caption="آموزش اتصال به کانفیگ DarkTunnel")
        await botx.send_file(event.chat_id, "https://graph.org/file/aa7c4aa1f578fdaba1dda.mp4", caption="آموزش وارد کردن سابکریپشن برنامه foxray برای ios")
        await botx.send_file(event.chat_id, "https://graph.org/file/c700388ebcc77c2a80538.mp4", caption="آموزش استفاده از سابکریپشن در برنامه v2rayng")


@botx.on(events.NewMessage(pattern="حمایت", func=lambda e: e.is_private))
async def catcher(event):
    user_id = int(event.sender.id)
    if await is_member(user_id) == False:
        await botx.send_message(event.chat_id, "لطفا برای استفاده از ربات، به چنل @Hack_Team جوین شوید.")
    if await is_member(user_id) == "FalseBanned":
        await botx.send_message(event.chat_id, "شما بن شده اید و نمی توانید از ربات استفاده نمایید.")
    if await is_member(user_id) == True:
        await botx.send_message(event.chat_id, "**✨حمایت مالی**\nUSDT(Trc20):\n`TKRdf1cXbrEDByP4nFMdMiyzTfG7AgBKWs`\n\n**TRX(tron):**\n`TKRdf1cXbrEDByP4nFMdMiyzTfG7AgBKWs`")
