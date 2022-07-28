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
            "_id"       :   characterID,
            "ownerID"   :   ownerID,
            "name"      :   characterName
            })