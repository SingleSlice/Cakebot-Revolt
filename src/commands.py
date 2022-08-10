import configCakebot
import commandDir.database as database
import commandDir.insertChar as insertchar
import commandDir.mychar as mychar
import commandDir.deleteChar as deletechar
import commandDir.sendAsChar as sendaschar
import commandDir.help as help
import commandDir.hugs as hugs

cakebotDB = database.databaseClient(configCakebot.connectionString, configCakebot.serverDatabase, configCakebot.userDatabase)

async def commandExecuter(message, prefix):

    args = message.content.split(sep= " ") #separate the arguments by spaces
    command = args[0][len(prefix):]
    args.pop(0) # removes the command from the arg list

    if command == "help":
        await message.reply(content = "here is the help you needed, meow~", embed = help.embed)
    elif command == "hugs":
        await message.reply("there, there\n" + hugs.get_rand_hug())
    elif command == "createChar":
        await insertchar.insertChar(message, args, cakebotDB)
    elif command == "deleteChar":
        await deletechar.deleteChar(message, args, cakebotDB)
    elif command == "myChars":
        await mychar.mychar(message, cakebotDB)
    elif command == "send":
        await sendaschar.sendAsChar(message,args,cakebotDB)