from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["property_management"]
properties_collection = db["properties"]
