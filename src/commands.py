async def commandExecuter(message, prefix):
    command = message.content[len(prefix):]

    if command == "wenomacinesama":
        await message.channel.send("tumartbitsaund")
    