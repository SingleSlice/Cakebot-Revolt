import configCakebot

async def insertChar(message, args, cakebotDB):
    try: args[0]
    except IndexError:await message.channel.send("this command needs the 'name' argument, example\n --insertChar Cake")
    else:
        if len(cakebotDB.getCharactersFromUser(message.author.id)) < configCakebot.max_oc_user:
            names = []
            for char in cakebotDB.getCharactersFromUser(message.author.id):
                names.append(char["name"])
            
            if args[0] not in names:
                cakebotDB.insertCharacter(message.author.id, args[0])
                print(f"new char {message.author.id}, {args[0]}")
                await message.reply(f"your character, _{args[0]}_, has been created.")
            else:
                await message.reply(f"you already own a character named, _{args[0]}_")

        else:
            await message.channel.send("you already have reached the maximum number of OCs")