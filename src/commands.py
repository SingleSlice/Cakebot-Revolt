import commandDir.insertChar as insertChar
import commandDir.help as help
import commandDir.hugs as hugs
import commandDir.database as database
import configCakebot

cakebotDB = database.databaseClient(configCakebot.connectionString, configCakebot.serverDatabase, configCakebot.userDatabase)

async def commandExecuter(message, prefix):

    args = message.content.split(sep= " ") #separate the arguments by spaces
    command = args[0][len(prefix):]
    args.pop(0) # removes the command from the arg list

    if command == "help":
        await message.reply(content = "here is the help you needed, meow~", embed = help.embed)
    elif command == "wenomachinesama":
        await message.reply("wenomachinesama")
    elif command == "hugs":
        await message.reply("there, there\n" + hugs.get_rand_hug())
    elif command == "insertChar":
        await insertChar.insertChar(message, args, cakebotDB)
    elif command == "myChars":
        cakebotDB.getCharactersFromUser(message.author.id)