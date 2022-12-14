"""cakebot database class"""
import pymongo

class DatabaseClient:
    """cakebot database client"""
    def __init__(self,con_string, serv_string, usr_string):
        self.dbclient = pymongo.MongoClient(con_string)
        self.server_db = self.dbclient[serv_string]
        self.user_db = self.dbclient[usr_string]
        print("currently existing databases -> " + str(self.dbclient.list_database_names()))
        print("currently existing collections -> " + str(self.server_db.list_collection_names()))
        print("currently existing collections -> " + str(self.user_db.list_collection_names()))


    def insert_character(self, ownerid, character_name):
        """insert character in the database"""
        self.user_db.get_collection("characters").insert_one({
            "ownerID"       :   ownerid,
            "name"          :   character_name,
            "display-name"  :   character_name,
            "picture"       :   "https://i.imgur.com/Gew7Bmk.jpeg",
            "bio"           :   "placeholder",
        })

    def update_character_fields(self):
        characters = list(self.user_db.get_collection("characters").find({}))
        for char in characters:
            print(char)
            self.user_db.get_collection("characters").update_many({"_id": char["_id"] }, {"$set": {"display-name": char["name"] }})

    def edit_character_field(self, ownerid, character_name, field, value):
        """edits a field"""
        query = {"ownerID": ownerid, "name": character_name}
        changed_field = {"$set": {field: value}}

        self.user_db.get_collection("characters").update_one(query, changed_field)

    def delete_character_from_user(self, ownerid, character_name):
        """deletes character from the database"""
        query = {"ownerID": ownerid, "name": character_name}  # gets characters that the user owns
        character_query = self.user_db.get_collection("characters").find(query)
        character = list(character_query)[0]

        self.user_db.get_collection("characters").delete_one({"_id": character["_id"]})  # yeets oc


    def get_char_from_user(self, ownerid):
        """gets character array from user"""
        query = {"ownerID": ownerid}
        character_query = self.user_db.get_collection("characters").find(query)
        list_of_chars = list(character_query)

        return list_of_chars

    def insert_device(self, ownerid, device_name):
        """insert device in the database"""
        self.user_db.get_collection("specfetch").insert_one({
            "ownerID"   :   ownerid,
            "name"      :   device_name,
            "os_pic"    :   "placeholder"
        })
