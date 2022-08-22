"""char"""
async def my_char(message, database):
    """sends characters"""
    characters = database.get_char_from_user(message.author.id)

    if len(characters) != 0 :
        line_to_send = "master~ here are your characters : \n   "

        for char in characters:
            line_to_send = line_to_send + "- " + char["name"] + "\n"

        await message.reply(f"{line_to_send}")
    else:
        await message.reply("You do not own any OC :<")
