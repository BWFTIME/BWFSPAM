from . import TheBWFSPAM

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command(["echo", "repeat"], prefixes=TheBWFSPAM.handler))
async def echo(BWFSPAM: Client, message: Message):
    if await TheBWFSPAM.sudo.sudoFilter(message, 3):
        return
    txt = ' '.join(message.command[1:])
    if message.reply_to_message:
        msg = message.reply_to_message.text.markdown
    elif txt:
        msg = str(txt)
    else:
        await message.reply_text(f"**Wrong Usage!** \n\n __- Syntax:__ `{TheBWFSPAM.handler}echo` (message or reply to message)")
        return

    try:
        await message.delete()
        await BWFSPAM.send_message(message.chat.id, msg)
    except Exception as a:
        await BWFSPAM.send_message(message.chat.id, msg)