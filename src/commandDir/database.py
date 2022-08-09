import pymongo

class databaseClient:
    def __init__(self,connectionString, serverDatabase, userDatabase):
        self.mgClient = pymongo.MongoClient(connectionString)
        self.serverDB = self.mgClient[serverDatabase]
        self.userDB = self.mgClient[userDatabase]
        print("currently existing databases -> " + str(self.mgClient.list_database_names()))
        print("currently existing collections -> " + str(self.serverDB.list_collection_names()))
        print("currently existing collections -> " + str(self.userDB.list_collection_names()))


    def insertCharacter(self, ownerID, characterName):
        characterID = self.userDB.get_collection("characters").count_documents({}) + 1

        self.userDB.get_collection("characters").insert_one({
            "ownerID"   :   ownerID,
            "name"      :   characterName
        })


    def deleteCharacterFromUser(self, ownerID, characterName):
        query = {"ownerID" : ownerID, "name" : characterName} # gets characters that the user owns
        characterQuery = self.userDB.get_collection("characters").find(query)
        character = list(characterQuery)[0]
        
        self.userDB.get_collection("characters").delete_one({"_id" : character["_id"]}) # yeets oc


    def getCharactersFromUser(self, ownerID):
        query = {"ownerID" : ownerID}
        characterQuery = self.userDB.get_collection("characters").find(query)
        listOfChar = list(characterQuery)
 
        return listOfChar
