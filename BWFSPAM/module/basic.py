import datetime
import time
import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatType, ChatMemberStatus

from . import TheBWFSPAM

@Client.on_message(
    filters.command("ping", prefixes=TheBWFSPAM.handler) #& filters.user(TheBWFSPAM.sudo.sudoUsers)
)
async def ping(_, message: Message):
    if await TheBWFSPAM.sudo.sudoFilter(message, 3):
        return
    start = datetime.datetime.now()
    #u_time = int(int(time.time()) - int(TheBWFSPAM.startTime))
    #uptime = await TheBWFSPAM.functions.get_time(time=u_time)
    pong_msg = await message.reply("**Pong !!**")
    end = datetime.datetime.now()
    ms = (end-start).microseconds / 1000
    try:
        await pong_msg.edit_text(f"⌾ {TheBWFSPAM.pingMsg} ⌾ \n\n ༝ ᴘɪɴɢ: `{ms}` ᴍs \n ༝ ᴠᴇʀsɪᴏɴ: `{TheBWFSPAM.versions['BWFSPAM']}`")
    except:
        await pong_msg.edit_text(f"⌾ {TheBWFSPAM.pingMsg} ⌾ \n\n ༝ ᴘɪɴɢ: `{ms}` ᴍs \n ༝ ᴠᴇʀsɪᴏɴ: `{TheBWFSPAM.versions['BWFSPAM']}`")
        await pong_msg.delete()

@Client.on_message(
    filters.command("alive", prefixes=TheBWFSPAM.handler) #& filters.user(TheBWFSPAM.sudo.sudoUsers)
)
async def alive(BWFSPAM: Client, message: Message):
    if await TheBWFSPAM.sudo.sudoFilter(message, 3):
        return
    await TheBWFSPAM.functions.send_alive(BWFSPAM, message)

@Client.on_message(
    filters.command("limit", prefixes=TheBWFSPAM.handler) #& filters.user(TheBWFSPAM.sudo.sudoUsers)
)
async def check_limit(BWFSPAM: Client, message: Message):
    if await TheBWFSPAM.sudo.sudoFilter(message, 3):
        return
    if BWFSPAM.me.is_bot:
        return
    event = await message.reply_text("__Checking your account for Spambot...__")
    try:
        await BWFSPAM.unblock_user("spambot")
        await BWFSPAM.send_message("spambot", "/start")
        await asyncio.sleep(2)
        async for history in BWFSPAM.get_chat_history("spambot", limit=1):
            await TheBWFSPAM.functions.delete_reply(message, event, str(history.text))
    except Exception as error:
        await TheBWFSPAM.functions.delete_reply(message, event, str(error))

@Client.on_message(
    filters.command(["help", "restart", "reboot"], prefixes=TheBWFSPAM.handler) #& filters.user(TheBWFSPAM.sudo.sudoUsers)
)
async def help_reboot(_, message: Message):
    if await TheBWFSPAM.sudo.sudoFilter(message, 3):
        return
    if "reboot" or "restart" in message.text.lower():
        await message.reply(
            f"**[Click Here.](https://t.me/{TheBWFSPAM.BWFSPAM.me.username}?start=reboot) to reboot your BWFSPAM!**",
            disable_web_page_preview=True,
        )
    elif "help" in message.text.lower():
        await message.reply(
            f"**[Click Here.](https://t.me/{TheBWFSPAM.BWFSPAM.me.username}?start=help) for help menu of BWFSPAM!**",
            disable_web_page_preview=True,
        )

@Client.on_message(filters.command(["stats", "stat"], prefixes=TheBWFSPAM.handler))
async def stats(BWFSPAM: Client, message: Message):
    if BWFSPAM.me.is_bot:
        await message.reply("__This command is only for id not for bot__")
        return
    if await TheBWFSPAM.sudo.sudoFilter(message):
        return
    wait = await message.reply_text("collecting....")
    start = datetime.datetime.now()
    private = 0
    gc = 0
    super_gc = 0
    channel = 0
    bot = 0
    admin_gc = 0
    async for dialog in BWFSPAM.get_dialogs():
        if dialog.chat.type == ChatType.PRIVATE:
            private += 1
        elif dialog.chat.type == ChatType.BOT:
            bot += 1
        elif dialog.chat.type == ChatType.GROUP:
            gc += 1
        elif dialog.chat.type == ChatType.SUPERGROUP:
            super_gc += 1
            admin = await dialog.chat.get_member(int(BWFSPAM.me.id))
            if admin.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
                admin_gc += 1
        elif dialog.chat.type == ChatType.CHANNEL:
            channel += 1

    end = datetime.datetime.now()
    ms = (end - start).seconds
    stats = f"{BWFSPAM.me.first_name}'s stats \n\n"
    stats += "------------- » «» « ------------- \n"
    stats += f"Private Messages: `{private}` \n"
    stats += f"Bots in Inbox: `{bot}` \n"
    stats += f"Total Groups: `{gc}` \n"
    stats += f"Total Super Groups: `{super_gc}` \n"
    stats += f"Total Channels: `{channel}` \n"
    stats += f"Admin in: `{admin_gc}` chats \n\n"
    stats += "------------- » «» « ------------- \n\n"
    stats += f"Time Taken `{ms}secs` \n"
    stats += f"© @{TheBWFSPAM.updateChannel}"
    await TheBWFSPAM.functions.delete_reply(message, wait, stats)