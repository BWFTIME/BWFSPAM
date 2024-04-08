from pyrogram import idle
from BWFSPAM.functions.clients import TheBWFSPAM

async def main():
    await TheBWFSPAM.startup()
    TheBWFSPAM.logs.info("-- BWFSPAM started --")
    await idle()
    await TheBWFSPAM.BWFSPAM.stop()
    await TheBWFSPAM.stopAllClients()

if __name__ == "__main__":
    TheBWFSPAM.run(main())