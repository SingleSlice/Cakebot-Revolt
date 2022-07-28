async def insertChar(message, args, cakebotDB):
    try: args[0]
    except IndexError:await message.channel.send("this command needs the 'name' argument")
    else:cakebotDB.insertCharacter(message.author.id, args[0])