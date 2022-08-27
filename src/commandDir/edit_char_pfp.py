import voltage


async def edit_char_pfp(message, args, database):
    """edit chars"""
    try:
        args[0] # checks if the character_name argument exists
    except IndexError:
        await message.reply("This command requires the argument\n- character_name\n and a picture attachment")
    else:
        try:
            message.attachments[0].url # checks if the there is an attachment
        except IndexError:
            await message.reply("This command requires the argument\n- character_name\n and a picture attachment")
        else:
            picture = message.attachments[0]
            names = []

            for char in database.get_char_from_user(message.author.id):
                names.append(char["name"])

            if args[0] in names:
                if picture.type is voltage.AssetType.image:
                    database.edit_character_field(message.author.id, args[0], "picture", picture.url)
                    await message.reply(f"{args[0]}'s profile picture has been changed successfully")
                else:
                    await message.reply("The attachment is not a valid picture")
            else:
                await message.reply(f"{args[0]} is not one of your characters")
