
from pymongo.mongo_client import MongoClient

client = MongoClient("mongodb://localhost:28080")

db = client["new"]
collection = db['main']
collection.insert_one({"data": "xd"})
result = collection.find_one({'data': 'xd'})
print("aha o to wynik: ",result)