from pymongo import MongoClient
from dotenv import load_dotenv
import os 


load_dotenv()
class Database:
    def __init__(self):
        self.client = MongoClient(os.getenv("MONGO_URI"))
        self.db = self.client["news_db"]
        self.collection = None
    
    def set_collection(self, category):
        collection_name = category + "_news"
        if collection_name not in self.db.list_collection_names():
            self.db.create_collection(collection_name)
        self.collection = self.db[collection_name]

    def store_data(self, data):
        self.collection.update_one(
            filter={"_id": data["_id"]},
            update={"$set": data},
            upsert=True
        )
    
    def get_data(self, _id):
        return self.collection.find_one({"_id": _id})
