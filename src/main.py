import voltage

import commands
import configCakebot

cakebot = voltage.Client()
prefix = configCakebot.prefix

@cakebot.listen("ready")
async def on_ready():
    print("CakeBot online")

@cakebot.listen("message")
async def on_message(message):
    if message.content.startswith(prefix):
        await commands.commandExecuter(message, prefix)

cakebot.run(configCakebot.token)