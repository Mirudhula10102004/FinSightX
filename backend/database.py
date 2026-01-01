from pymongo import MongoClient

MONGO_URI = "mongodb+srv://finsight_user:finsight123@cluster0.b9uzhuy.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)

db = client["finsightx"]
budget_collection = db["budgets"]
