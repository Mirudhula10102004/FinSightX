from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["finsight"]
collection = db["budgets"]


def get_used_budget_series(department, year):
    cursor = collection.find(
        {
            "department": department,
            "month": {
                "$gte": datetime(year, 1, 1),
                "$lte": datetime(year, 12, 31)
            }
        }
    ).sort("month", 1)

    values = []
    for doc in cursor:
        if "used_budget" in doc:
            values.append(doc["used_budget"])

    return values
