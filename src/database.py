import pymongo

class databaseClient:

    def __init__(self,connectionString, collectionServer, collectionUser):
        self.mgClient = pymongo.MongoClient(connectionString)
        self.serverDB = self.mgClient[collectionServer]
        self.userDB = self.mgClient[collectionUser]
        print("currently existing databases -> " + str(self.mgClient.list_database_names()))
        print("currently existing collections -> " + str(self.serverDB.list_collection_names()))
        print("currently existing collections -> " + str(self.userDB.list_collection_names()))

    def insertCharacter(self, name):
        pass