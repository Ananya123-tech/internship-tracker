from pymongo import MongoClient

# connect to local mongodb
client = MongoClient("mongodb://localhost:27017/")

# create database
db = client["internship_tracker"]

# create collection
collection = db["users"]