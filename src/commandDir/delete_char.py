"""deletes character from database"""
async def delete_char(message, args, database):
    """deletes character from database"""
    try:
        args[0]
    except IndexError:
        await message.reply("this command needs the 'name' argument, example\n deleteChar Cake")
    else:
        names = []
        for char in database.get_char_from_user(message.author.id):
            names.append(char["name"])
        if args[0] in names:
            database.delete_character_from_user(message.author.id, args[0])
            await message.reply("master! your character _" + args[0] + "_ has been deleted!")
        else: await message.channel.send("master, you do not own any character named _" + \
            args[0] + "_")
