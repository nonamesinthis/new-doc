
from pymongo.mongo_client import MongoClient

client = MongoClient("mongodb://localhost:28080")

db = client["new"]
collection = db['main']
collection.insert_one({"username": "hege","password":"123"})
collection.insert_one({"username": "k","password":"m"})
result = collection.find_one({})
print("aha o to wynik: ",result)

