from pymongo import MongoClient

Mongo_URI = 'mongodb//localhost'

client = MongoClient(Mongo_URI)

db = client['teststore']
collection = db['products']
print(collection)
