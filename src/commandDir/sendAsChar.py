import voltage
import configCakebot

async def sendAsChar(message, args, cakebotDB):
    try: args[0] # checks if the character's name argument exists
    except IndexError: await message.reply("this command requires a character name to work. ex.\n =>send imposter amongus is a very nice game")
    else: # if it exists, it executes this section of code
        try: args[1]
        except IndexError:
            await message.reply("cakebot does not support sending pictures at this time and empty messages.")

        else:
            characters = cakebotDB.getCharactersFromUser(message.author.id)
            names = []
            for char in characters:
                names.append(char["name"])

            if args[0] in names:
                for char in characters:
                    if char["name"] == args[0]:
                        char_name = char["name"]
                        char_pic = char["picture"]
                        
                masq = voltage.MessageMasquerade(name=char_name, avatar=char_pic)

                message_to_send = message.content[len(configCakebot.prefix)+4+1+len(args[0])+1:] # removes the prefix, command name and leaves only the intended message.
                await message.channel.send(content = message_to_send , masquerade = masq)

            else:
                await message.channel.send(f"no character named _{args[0]}_ found")