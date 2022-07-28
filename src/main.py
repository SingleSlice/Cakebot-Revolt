import voltage

import commands
import database
import configCakebot

cakebot = voltage.Client()
cakebotDB = database.databaseClient(configCakebot.connectionString, configCakebot.serverCollection, configCakebot.userCollection)

prefix = configCakebot.prefix

@cakebot.listen("ready")
async def on_ready():
    print("CakeBot online")


@cakebot.listen("message")
async def on_message(message):
    if message.content.startswith(prefix):
        await commands.commandExecuter(message, prefix)

cakebot.run(configCakebot.token)