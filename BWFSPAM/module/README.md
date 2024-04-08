<h1> Add your Own Plugin <h1>

```python
from . import TheBWFSPAM
from pyrogram import Client, filters

@Client.on_message(
    filters.command("hi", , prefixes=TheBWFSPAM.handler)
)
async def hi(_, message):
    if await TheBWFSPAM.sudo.sudoFilter(message, 3): #sudo filter
        return
    await message.reply("Hello")
```
