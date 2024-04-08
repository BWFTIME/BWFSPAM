import time

from platform import python_version

from BWFSPAM.functions.database import dataBase
from BWFSPAM.config import PING_MSG

from pyrogram import __version__


# --- start time --- #
StartTime = time.time()

# --- versions --- #
version = {
    "BWFSPAM": "v2.0",
    "pyrogram": __version__,
    "python": python_version(),
}

UpdateChannel = "RiZoeL_X"
SupportGroup = "RiZoeLXSupport"

activeTasks: dict = {}
dataBase = dataBase

#  --- etx
if PING_MSG:
    pingMSG = str(PING_MSG)
else:
    pingMSG = "BWFSPAM"