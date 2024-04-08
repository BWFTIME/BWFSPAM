from . import TheBWFSPAM

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(
    filters.command(["gcast", "broadcast"], prefixes=TheBWFSPAM.handler)
)
async def broadcast(BWFSPAM: Client, message: Message):
    if await TheBWFSPAM.sudo.sudoFilter(message, 1):
        return

    await TheBWFSPAM.functions.broadcast(BWFSPAM, message)

@Client.on_message(
    filters.command('join', prefixes=TheBWFSPAM.handler)
)
async def join(BWFSPAM: Client, message: Message):
    try:
        group = str(message.command[1])
    except:
        await message.reply("__Please give valid join link or username of group to join.__")
        return

    wait = await message.reply("__joining.....__")
    try:
        await BWFSPAM.join_chat(group)
        await message.reply("**✅ Joined successfully**")
    except Exception as er:
        await message.reply(f"**Error while join:** {str(er)} \n\n__Report in @{TheBWFSPAM.supportGroup}__")
    await wait.delete()

@Client.on_message(
    filters.command(["leave", "left"], prefixes=TheBWFSPAM.handler)
)
async def leave(BWFSPAM: Client, message: Message):
    if len(message.command) == 1:
        group = message.chat.id
    else:
        try:
            group = message.command[1]
        except:
            await message.reply("__Please give valid join link or username of group to join.__")
            return

    if group in [TheBWFSPAM.restrict.res, f"@{TheBWFSPAM.supportGroup}", f"@{TheBWFSPAM.updateChannel}", TheBWFSPAM.supportGroup, TheBWFSPAM.updateChannel]:
        return

    wait = await message.reply("__leaving.....__")
    try:
        await BWFSPAM.join_chat(group)
        await message.reply("**✅ Left successfully**")
    except Exception as er:
        await message.reply(f"**Error while Leave:** {str(er)} \n\n__Report in @{TheBWFSPAM.supportGroup}__")
    await wait.delete() 