from pymongo import MongoClient    

client = MongoClient('mongodb://localhost:27017/')
class mongodata():
    def __init__(self):
        self.db = client['protected_routes']
        self.users = self.db['users']