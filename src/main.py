"main func"
import voltage

import commands
import configCakebot

cakebot = voltage.Client()
PREFIX = configCakebot.prefix


@cakebot.listen("ready")
async def on_ready():
    """on ready"""
    await cakebot.set_status(PREFIX + "help")


@cakebot.listen("message")
async def on_message(message):
    """function that gets executed with each message"""
    if message.content.startswith(PREFIX):
        await commands.command_executer(message, PREFIX)

cakebot.run(configCakebot.token)