from . import TheBWFSPAM

from pyrogram import Client, filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from BWFSPAM.functions.messages import helpMessages
from BWFSPAM.functions.keyboard import help_buttons

@Client.on_callback_query(filters.regex("help:.*$"))
async def helpCallbacks(_, callback: CallbackQuery):
    query = str(callback.data.lower().split(":")[1])

    if query == "reboot":
        await callback.answer("Rebooting BWFSPAM.....", show_alert=True)
        await callback.message.edit("__🔸 Rebooting BWFSPAM.....__")
        await TheBWFSPAM.reboot()

    elif query == "spam":
        await callback.message.edit(
            helpMessages.spam.format(TheBWFSPAM.handler, TheBWFSPAM.supportGroup),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔙", "help:back")
                    ]
                ]
            )
        )

    elif query == "raid":
        await callback.message.edit(
            helpMessages.raid.format(TheBWFSPAM.handler, TheBWFSPAM.supportGroup),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔙", "help:back")
                    ]
                ]
            )
        )

    elif query == "direct":
        await callback.message.edit(
            helpMessages.direct_message.format(TheBWFSPAM.handler, TheBWFSPAM.supportGroup),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔙", "help:back")
                    ]
                ]
            )
        )

    elif query == "basic":
        await callback.message.edit(
            helpMessages.basic.format(TheBWFSPAM.handler, TheBWFSPAM.supportGroup),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔙", "help:back")
                    ]
                ]
            )
        )

    elif query == "profile":
        await callback.message.edit(
            helpMessages.profile.format(TheBWFSPAM.handler, TheBWFSPAM.supportGroup),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔙", "help:back")
                    ]
                ]
            )
        )

    elif query == "extra":
        await callback.message.edit(
            helpMessages.extra.format(TheBWFSPAM.handler, TheBWFSPAM.supportGroup),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔙", "help:back")
                    ]
                ]
            )
        )

    elif query == "back":
        await callback.message.edit(
            helpMessages.start.format(TheBWFSPAM.handler, TheBWFSPAM.updateChannel, TheBWFSPAM.supportGroup),
            reply_markup=help_buttons,
        )