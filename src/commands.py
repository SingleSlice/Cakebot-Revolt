"""commands"""
import configCakebot
from commandDir import database
import commandDir.insert_char as insertchar
from commandDir import my_char
from commandDir import edit_char_pfp
import commandDir.delete_char as deletechar
import commandDir.send_message_char as sendaschar
import commandDir.help as help_com
from commandDir import hugs

cakeDatabase = database.DatabaseClient(configCakebot.connectionString,\
    configCakebot.serverDatabase, configCakebot.userDatabase)

async def command_executer(message, prefix):
    """manages commnands"""
    if not message.author.bot:
        args = message.content.split(sep= " ") #separate the arguments by spaces
        command = args[0][len(prefix):].lower()
        args.pop(0) # removes the command from the arg list

        if command == "help":
            await message.reply(content = "here is the help you needed, meow~\n\n" + help_com.help)
        elif command == "hugs":
            await message.reply("there, there\n" + hugs.get_rand_hug())
        elif command == "createchar":
            await insertchar.insert_char(message, args, cakeDatabase, configCakebot)
        elif command == "deletechar":
            await deletechar.delete_char(message, args, cakeDatabase)
        elif command == "mychars":
            await my_char.my_char(message, cakeDatabase)
        elif command == "send":
            await sendaschar.send_as_char(message,args,cakeDatabase, configCakebot)
        elif command == "editcharpfp":
            await edit_char_pfp.edit_char_pfp(message, args, cakeDatabase)
