from pymongo import MongoClient
from datetime import datetime

# 🔁 CHANGE USERNAME & PASSWORD ONLY
MONGO_URI = "mongodb+srv://finsight_user:finsight123@cluster0.b9uzhuy.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
db = client["finsightx"]
collection = db["budgets"]

# Clear old data (optional but recommended)
collection.delete_many({})

departments = ["IT", "HR", "Finance", "Operations"]

monthly_data = [
    ("2025-01-31", 500000, 480000),
    ("2025-02-28", 510000, 495000),
    ("2025-03-31", 520000, 505000),
    ("2025-04-30", 530000, 515000),
    ("2025-05-31", 540000, 525000),
    ("2025-06-30", 550000, 535000),
    ("2025-07-31", 560000, 545000),
    ("2025-08-31", 570000, 555000),
    ("2025-09-30", 580000, 565000),
    ("2025-10-31", 590000, 575000),
    ("2025-11-30", 600000, 585000),
    ("2025-12-31", 610000, 595000),
]

records = []

for dept in departments:
    for month, planned, used in monthly_data:
        records.append({
            "department": dept,
            "month": datetime.strptime(month, "%Y-%m-%d"),
            "planned_budget": planned,
            "used_budget": used
        })

collection.insert_many(records)

print("✅ Inserted 4 departments × 12 months successfully")
