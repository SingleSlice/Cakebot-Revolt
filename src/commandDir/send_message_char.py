import voltage

async def send_as_char(message, args, database, config):
    """sends messages as choosen character"""
    try:
        args[0] # checks if the character's name argument exists
    except IndexError:
        await message.reply("this command requires a character name to work. ex.\n =>send imposter amongus is a very nice game")
    else: # if it exists, it executes this section of code
        try:
            args[1]
        except IndexError:
            await message.reply(content = "This command requires a message to output, ex. \n=>send imposter amongus is a very nice game")

        else:
            characters = database.get_char_from_user(message.author.id)
            names = []
            for char in characters:
                names.append(char["name"])

            if args[0] in names: # checks if the argument is in the list of characters
                for char in characters:
                    if char["name"] == args[0]:
                        char_name = char["name"]
                        char_pic = char["picture"]

                masq = voltage.MessageMasquerade(name=char_name, avatar=char_pic)
                message_to_send = message.content[len(config.prefix)+4+1+len(args[0])+1:] # removes the prefix, command name and leaves only the intended message.
                try:
                    message.replies[0]
                except IndexError:
                    await message.channel.send(content = message_to_send , masquerade = masq) # check if the server has masquerade enabled
                    await message.delete()
                else:
                    await message.replies[0].reply(content = message_to_send , masquerade = masq) # check if the server has masquerade enabled
                    await message.delete()

            else:
                await message.channel.send(f"no character named _{args[0]}_ found")
