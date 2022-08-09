async def deleteChar(message, args, cakebotDB):
    try: args[0]
    except IndexError: await message.reply("this command needs the 'name' argument, example\n deleteChar Cake")
    else:
        names = []
        for char in cakebotDB.getCharactersFromUser(message.author.id):
            names.append(char["name"])
        
        if args[0] in names:
            cakebotDB.deleteCharacterFromUser(message.author.id, args[0])
            await message.reply("master! your character _" + args[0] + "_ has been deleted!")
        else: await message.channel.send("master, you do not own any character named _" + args[0] + "_")