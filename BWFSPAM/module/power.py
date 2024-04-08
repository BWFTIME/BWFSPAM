import random

from . import TheBWFSPAM

from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery

@Client.on_message(
    filters.command(
        [
            "spam",
            "bigspam",
            "timespam",
            "tspam",
            "delayspam",
            "dspam",
            "futurespam",
            "fspam",
            "pornspam",
            "pspam",
            "uspam",
            "unlimitedspam",
            "inlinespam",
            "ispam",
            "cspam",
            "commonspam",
        ],
        prefixes=TheBWFSPAM.handler,
    )
)
async def spam_messages(client: Client, message: Message):
    if await TheBWFSPAM.sudo.sudoFilter(message, 3):
        return
    x = message.text[1:]
    if " " in x:
        command = str(x.split(" ")[0])
    else:
        command = str(x)
    if command.lower() in ["spam", "bigspam"]:
        await TheBWFSPAM.functions.start_spam(client, message, spam="spam")

    elif command.lower() in ["delayspam", "dspam"]:
        await TheBWFSPAM.functions.start_spam(client, message, spam="delay")

    elif command.lower() in ["futurespam", "fspam", "timespam", "tspam"]:
        await TheBWFSPAM.functions.start_spam(client, message, spam="future")

    elif command.lower() in ["pornspam", "pspam"]:
        await TheBWFSPAM.functions.start_spam(client, message, spam="porn")

    elif command.lower() in ["unlimitedspam", "uspam"]:
        if await TheBWFSPAM.sudo.sudoFilter(message):
            return
        await TheBWFSPAM.functions.start_spam(client, message, spam="loop")

    elif command.lower() in ["inlinespam", "ispam"]:
        await TheBWFSPAM.functions.inline_spam(client, message)

    elif command.lower() in ["commonspam", "cspam"]:
        await TheBWFSPAM.functions.start_common_spam(client, message)

@Client.on_message(
    filters.command(
        [
            "dmspam",
            "dm",
            "message",
            "dmraid",
        ],
        prefixes=TheBWFSPAM.handler
    )
)
async def direct_messages(client: Client, message: Message):
    if await TheBWFSPAM.sudo.sudoFilter(message, 3):
        return
    x = message.text[1:]
    if " " in x:
        command = str(x.split(" ")[0])
    else:
        command = str(x)
    if command.lower() == "dmspam":
        await TheBWFSPAM.functions.direct_messages(client, message, "spam")

    elif command.lower() == "dmraid":
        await TheBWFSPAM.functions.direct_messages(client, message, "raid")

    elif command.lower() in ["dm", "message"]:
        await TheBWFSPAM.functions.direct_messages(client, message, "message")

@Client.on_message(
    filters.command(
        [
            "raid",
            "multiraid",
            "mraid",
            "replyraid",
            "rraid",
            "areplyraid",
            "arraid",
            "dreplyraid",
            "drraid",
        ],
        prefixes=TheBWFSPAM.handler
    )
)
async def raids(client: Client, message: Message):
    if await TheBWFSPAM.sudo.sudoFilter(message, 3):
        return
    x = message.text[1:]
    if " " in x:
        command = str(x.split(" ")[0])
    else:
        command = str(x)
    if command.lower() == "raid":
        await TheBWFSPAM.functions.raid(client, message)

    elif command.lower() in ["multiraid", "mraid"]:
        await TheBWFSPAM.functions.raid(client, message, multi=True)

    elif command.lower() in ["replyraid", "rraid"]:
        await TheBWFSPAM.functions.replyraid(client, message)

    elif command.lower() in ["areplyraid", "arraid"]:
        await TheBWFSPAM.functions.replyraid(client, message, "enable")

    elif command.lower() in ["dreplyraid", "drraid"]:
        await TheBWFSPAM.functions.replyraid(client, message, "disable")

@Client.on_message(
    filters.all
)
async def replayraid_watcher(_, message: Message):
    if message.from_user.id in TheBWFSPAM.functions.raid_users:
        await message.reply(random.choice(TheBWFSPAM.functions.raid_args))

@Client.on_message(
    filters.command("stop")
)
async def stop_uspam(_, message: Message):
    if await TheBWFSPAM.sudo.sudoFilter(message):
        return
    if message.chat.id in TheBWFSPAM.functions.unlimited:
        TheBWFSPAM.functions.unlimited.remove(message.chat.id)
        await message.reply(f"__✅ Stopped Unlimited spam in {message.chat.title}!__")
        TheBWFSPAM.activeTasks.pop(message.chat.id)
    else:
        await message.reply(f"__❎ No any active task in {message.chat.title}.__")

@Client.on_callback_query(filters.regex("inline"))
async def inlineSpamCB(_, callback: CallbackQuery):
    await callback.answer(
        str(random.choice(TheBWFSPAM.functions.raid_args)),
        show_alert=True,
    )
