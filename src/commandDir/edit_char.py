"""func to edit chars"""
import voltage

async def edit_char(message, args, database):
    """edit chars"""
    try:
        args[0] # checks if the character_name argument exists
    except IndexError:
        await message.reply("This command requires the argument \
            \n- character_name\n and the name of the field to change\n available fields:\n \
            - display-name\n- avatar\n - bio")
    else:
        names = []
        characters = database.get_char_from_user(message.author.id)
        if len(characters) != 0:
            for char in characters:
                names.append(char["name"])

            if args[0] in names:
                try:
                    args[1]
                except IndexError:
                    await message.reply("This command requires the argument \
                        \n- character_name\n and the name of the field to change\n available fields:\n \
                        - display-name\n- avatar\n - bio")
                else:
                    if args[1] in ["display-name", "avatar", "bio"]:
                        if args[1] == "display-name":
                            return
                        elif args[1] == "avatar":
                            return
                        elif args[1] == "bio":
                            return
                    else:
                        await message.reply(f"The field {args[1]} is not an option to edit")
            else:
                await message.reply(f"{args[0]} is not one of your characters")
        else:
            message.reply("you do not own any character")