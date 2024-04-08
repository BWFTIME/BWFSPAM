"""
    BWFSPAM by RiZoeL
"""
import glob
import importlib
import os
import sys
from pathlib import Path

import pyroaddon
from pyrogram import Client
from pyrogram.enums import ParseMode
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from BWFSPAM import (
    UpdateChannel,
    SupportGroup,
    dataBase,
    version,
    pingMSG,
    StartTime,
    activeTasks,
)
from BWFSPAM.config import (
    API_ID,
    API_HASH,
    ASSISTANT_TOKEN,
    LOGGER_ID,
    OWNER_ID,
    HANDLER,
)
from .core import sudoers, restriction, functions
from .messages import helpMessages
from .keyboard import help_buttons
from .logger import LOGS

devs = [1432756163, 5294360309, 1854700253]

class BWFSPAM(Client):
    def __init__(self) -> None:
        self.clients: list[Client] = []
        self.BWFSPAM: Client = Client(
            "BWFSPAM Assistant",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=ASSISTANT_TOKEN,
            plugins=dict(root="BWFSPAM.assistant")
        )
        self.database = dataBase
        self.loggerID = LOGGER_ID
        self.updateChannel = UpdateChannel
        self.supportGroup = SupportGroup
        self.author = "MahipalRajput"
        self.versions = version
        self.logs = LOGS
        self.sudo = sudoers
        self.owner_id = OWNER_ID
        self.restrict = restriction
        self.functions = functions
        self.handler = HANDLER
        self.pingMsg = pingMSG
        self.startTime = StartTime
        self.activeTasks = activeTasks
        self.dev = devs
        self.logo= "https://telegra.ph//file/08445817174872b47cef8.jpg"

    async def StartAllClients(self):
        LOGS.info("Loading all sessions.....")
        sessions_list = self.database.getAllSessions()
        if len(sessions_list) == 0:
            LOGS.info("-> 0 Client - Add clients after starting assistant, starting assistant...!")
        else:
            LOGS.info(f"-> Loaded {len(sessions_list)} session let's start BWFSPAM clients")
            bots = 0
            users = 0
            for session_data in sessions_list:
                phone_number = session_data["phone_number"]
                client_session = str(session_data["session"])
                if client_session:
                    type = await self.clientType(str(client_session))
                    if type == "bot":
                        BWFSPAMClient = Client(
                            f"BWFSPAM-{phone_number}",
                            api_id=API_ID,
                            api_hash=API_HASH,
                            bot_token=client_session,
                            plugins=dict(root="BWFSPAM.module")
                            )
                    else:
                        BWFSPAMClient = Client(
                            f"BWFSPAM-{phone_number}",
                            api_id=API_ID,
                            api_hash=API_HASH,
                            session_string=client_session,
                            plugins=dict(root="BWFSPAM.module")
                            )
                    try:
                        await BWFSPAMClient.start()
                        if type == "user":
                            try:
                                await BWFSPAMClient.join_chat(UpdateChannel)
                                await BWFSPAMClient.join_chat(SupportGroup)
                                try:
                                    await BWFSPAMClient.send_message(self.BWFSPAM.me.username, "/start")
                                except:
                                    pass
                            except Exception:
                                pass
                            users += 1
                        else:
                            bots += 1
                        self.clients.append(BWFSPAMClient)
                    except Exception:
                        LOGS.error(f"Error while start {phone_number} - {type}, skipping this...")
                        dataBase.removeSession(phone_number)
                else:
                    dataBase.removeSession(phone_number)
            LOGS.info(f"Started {len(self.clients)} BWFSPAM Clients (User - {users} | Bots - {bots})")

    async def startBot(self) -> None:
        await self.BWFSPAM.start()
        LOGS.info(f"-> Started BWFSPAM Client: '{self.BWFSPAM.me.username}'")

    async def clientType(self, session: str) -> str:
        if ":" in session and session.split(":")[0].isnumeric():
            return "bot"
        else:
            return "user"

    async def validateLogger(self, client: Client) -> bool:
        try:
            await client.get_chat_member(LOGGER_ID, "me")
            return True
        except Exception:
            return await self.joinLogger(client)

    async def joinLogger(self, client: Client) -> bool:
        try:
            invite_link = await self.BWFSPAM.export_chat_invite_link(LOGGER_ID)
            await client.join_chat(invite_link)
            return True
        except Exception:
            return False

    async def stopAllClients(self):
        clientNo = 0
        for client in self.clients:
            clientNo += 1
            try:
                await client.stop()
            except Exception as error:
                self.logs.info(f"Error while stopping client!: {str(error)}")

    async def startMessage(self) -> None:
        log_text = "**BWFSPAM is Now Alive** \n\n"
        log_text += f"**BWFSPAM Clients:** __{len(self.clients)}\n\n"
        log_text += "Versions:\n"
        log_text += f"   ~ BWFSPAM: {version['BWFSPAM']} \n"
        log_text += f"   ~ PyroGram: {version['pyrogram']} \n"
        log_text += f"   ~ Python: {version['python']}"
        try:
            await self.BWFSPAM.send_photo(
                LOGGER_ID,
                "https://telegra.ph//file/08445817174872b47cef8.jpg",
                caption=log_text,
                parse_mode=ParseMode.MARKDOWN,
                disable_notification=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Start me", url=f"https://t.me/{self.BWFSPAM.me.username}?start=start"),
                        ],
                        [
                            InlineKeyboardButton("channel", url=f"https://t.me/{UpdateChannel}"),
                            InlineKeyboardButton("support", url=f"https://t.me/{SupportGroup}"),
                        ],
                    ]
                ),
            )
        except:
            pass

    async def reboot(self) -> None:
        try:
            await self.BWFSPAM.stop()
        except Exception as error:
            self.logs.info(str(error))

        await self.stopAllClients()

        args = [sys.executable, "-m", "BWFSPAM"]
        os.execl(sys.executable, *args)
        quit()

    async def help(self, chat_id: int) -> None:
        try:
            await self.BWFSPAM.send_photo(
                chat_id,
                self.logo,
                helpMessages.start.format(self.handler, self.updateChannel, self.supportGroup),
                reply_markup=help_buttons,
            )
        except Exception as er:
            await self.BWFSPAM.send_message(
                chat_id,
                f"**Error:** {str(er)} \n\n__Report in @{self.supportGroup}__"
            )

    async def loadPlugs(self) -> None:
        count = 0
        files = glob.glob("BWFSPAM/assistant/*.py")
        for file in files:
            with open(file) as f:
                path = Path(f.name)
                shortname = path.stem.replace(".py", "")
                if shortname.startswith("__"):
                    continue
                fpath = Path(f"BWFSPAM/assistant/{shortname}.py")
                name = "BWFSPAM.assistant." + shortname
                spec = importlib.util.spec_from_file_location(name, fpath)
                load = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(load)
                sys.modules["BWFSPAM.assistant." + shortname] = load
                count += 1
            f.close()
        LOGS.info(
            f"- > Loaded User Plugin: '{count}'"
        )

    async def startup(self) -> None:
        LOGS.info(
            f"-> Starting BWFSPAM ....."
        )
        await self.startBot()
        await self.StartAllClients()
        #await self.loadPlugs()
        await self.sudo.loadSudo()
        await self.restrict.loadRestrictChats()
        await self.startMessage()

TheBWFSPAM = BWFSPAM()
