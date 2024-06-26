import os

from . import TheBWFSPAM

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command(["setpic", "updatepic"], prefixes=TheBWFSPAM.handler))
async def set_profile(BWFSPAM: Client, message: Message):
    if BWFSPAM.me.is_bot:
        return
    if await TheBWFSPAM.sudo.sudoFilter(message, 1):
        return
    replied = message.reply_to_message
    media_path = "BWFSPAM/resources/Profile.jpg"
    if (replied and replied.media and (replied.photo or (replied.document and "image" in replied.document.mime_type))):
            await BWFSPAM.download_media(message=replied, file_name=media_path)
            await BWFSPAM.set_profile_photo(photo=media_path)
            await message.reply(f"**Changed profile picture successfully** ✅")
            if os.path.exists(media_path):
                os.remove(media_path)
    else:
        await message.reply("__Reply To any Photo To Change Profile pic__")

@Client.on_message(filters.command(["setname", "updatename"], prefixes=TheBWFSPAM.handler))
async def set_name(BWFSPAM: Client, message: Message):
    if BWFSPAM.me.is_bot:
        return
    if await TheBWFSPAM.sudo.sudoFilter(message, 1):
        return
    args = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 0)
    if message.reply_to_message:
        name = str(message.reply_to_message.text)
    elif len(args) != 0:
        name = str(args[0])
    else:
        await message.reply(f"**Wrong usage!** \n __- syntax:__ `{TheBWFSPAM.handler}setname` (name)")
        return
    try:
        await BWFSPAM.update_profile(first_name=name)
        await message.reply(f"**✅ Profile Name Changed Successfully !!** \n\n **New Name:** {name}")
    except Exception as ex:
        await message.reply(f"**Error !!** \n\n {ex}")

@Client.on_message(filters.command(["setall", "updateall"], prefixes=TheBWFSPAM.handler))
async def set_all(BWFSPAM: Client, message: Message):
    if BWFSPAM.me.is_bot:
        return
    if await TheBWFSPAM.sudo.sudoFilter(message, 1):
        return
    args = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 0)
    if message.reply_to_message:
        x_name = str(message.reply_to_message.text)
    elif len(args) != 0:
        x_name = str(args[0])
    else:
        await message.reply(f"**Wrong usage!** \n __- syntax:__ `{TheBWFSPAM.handler}setall` (name)")
        return
    wait = await message.reply("__updating....__")
    client_position = 1
    for c in TheBWFSPAM.clients:
        if c.me.id == BWFSPAM.me.id:
            break
        else:
            client_position += 1

    if client_position:
        name = f"#{client_position} - {x_name}"
    else:
        name = x_name
    try:
        await BWFSPAM.update_profile(first_name=name)
        await message.reply(f"**✅ Profile Name Changed Successfully !!** \n\n **New Name:** {name}")
    except Exception as ex:
        await message.reply(f"**Error !!** \n\n {ex}")
    await wait.delete()


@Client.on_message(filters.command(["setbio", "updatebio"], prefixes=TheBWFSPAM.handler))
async def set_bio(BWFSPAM: Client, message: Message):
    if BWFSPAM.me.is_bot:
        return
    if await TheBWFSPAM.sudo.sudoFilter(message, 1):
        return
    args = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 0)
    if message.reply_to_message:
        bio = str(message.reply_to_message.text)
    elif len(args) != 0:
        bio = str(args[0])
    else:
        await message.reply(f"**Wrong usage!** \n __- syntax:__ `{TheBWFSPAM.handler}setbio` (bio)")
        return
    try:
        await BWFSPAM.update_profile(bio=bio)
        await message.reply(f"**✅ Profile Name Changed Successfully !!** \n\n **New bio:** {bio}")
    except Exception as ex:
        await message.reply(f"**Error !!** \n\n {ex}")