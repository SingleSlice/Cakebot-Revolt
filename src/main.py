import voltage

import commands
import configCakebot

cakebot = voltage.Client()
prefix = configCakebot.prefix

@cakebot.listen("ready")
async def on_ready():
    await cakebot.set_status(prefix + "help")

@cakebot.listen("message")
async def on_message(message):
    if message.content.startswith(prefix):
        await commands.commandExecuter(message, prefix)

cakebot.run(configCakebot.token)