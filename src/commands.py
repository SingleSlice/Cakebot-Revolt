"""commands"""
import configCakebot
import commandDir.database as database
import commandDir.insert_char as insertchar
import commandDir.my_char as my_char
import commandDir.delete_char as deletechar
import commandDir.send_message_char as sendaschar
import commandDir.help as help_com
import commandDir.hugs as hugs

cakeDatabase = database.databaseClient(configCakebot.connectionString,\
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
