"""inserts character in the database"""
async def insert_char(message, args, database, config):
    """inserts character in the database"""
    try:
        args[0]
    except IndexError:
        await message.channel.send("this command needs the 'name' argument, example\n=>nsertChar \
            Cake")
    else:
        if len(database.getCharactersFromUser(message.author.id)) < config.max_oc_user:
            names = []
            for char in database.getCharactersFromUser(message.author.id):
                names.append(char["name"])
            if args[0] not in names:
                database.insertCharacter(message.author.id, args[0])
                print(f"new char {message.author.id}, {args[0]}")
                await message.reply(f"your character, _{args[0]}_, has been created.")
            else:
                await message.reply(f"you already own a character named, _{args[0]}_")

        else:
            await message.channel.send("you already have reached the maximum number of OCs")