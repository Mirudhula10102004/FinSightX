from flask import Flask, jsonify
from flask_cors import CORS

# ---------------- APP INIT ----------------
app = Flask(__name__)
CORS(app)

# ---------------- ROOT ----------------
@app.route("/")
def home():
    return "FinSightX Backend Running"

# ---------------- ACTUAL BUDGET DATA ----------------
@app.route("/budgets/actual")
def actual_budget():
    return jsonify({
        "status": "success",
        "months": [
            "2024-10", "2024-11", "2024-12",
            "2025-01", "2025-02", "2025-03",
            "2025-04", "2025-05", "2025-06",
            "2025-07", "2025-08", "2025-09",
            "2025-10", "2025-11", "2025-12"
        ],
        "values": [
            480000, 490000, 500000,
            510000, 520000, 530000,
            540000, 550000, 560000,
            570000, 580000, 590000,
            600000, 610000, 620000
        ]
    })

# ---------------- ARIMA FORECAST ----------------
@app.route("/budgets/forecast/arima/<dept>/<year>")
def arima_forecast(dept, year):
    forecast = [
        {"month": "2025-01", "value": 505000},
        {"month": "2025-02", "value": 515000},
        {"month": "2025-03", "value": 525000},
        {"month": "2025-04", "value": 535000},
        {"month": "2025-05", "value": 545000},
        {"month": "2025-06", "value": 555000},
        {"month": "2025-07", "value": 565000},
        {"month": "2025-08", "value": 585000},
        {"month": "2025-09", "value": 595000},
        {"month": "2025-10", "value": 605000},
        {"month": "2025-11", "value": 615000},
        {"month": "2025-12", "value": 625000}
    ]

    return jsonify({
        "status": "success",
        "model": "ARIMA",
        "department": dept,
        "year": year,
        "forecast": forecast
    })

# ---------------- SARIMA FORECAST ----------------
@app.route("/budgets/forecast/sarima/<dept>/<year>")
def sarima_forecast(dept, year):
    forecast = [
        {"month": "2025-01", "value": 510000},
        {"month": "2025-02", "value": 520000},
        {"month": "2025-03", "value": 535000},
        {"month": "2025-04", "value": 545000},
        {"month": "2025-05", "value": 555000},
        {"month": "2025-06", "value": 565000},
        {"month": "2025-07", "value": 575000},
        {"month": "2025-08", "value": 600000},
        {"month": "2025-09", "value": 610000},
        {"month": "2025-10", "value": 620000},
        {"month": "2025-11", "value": 630000},
        {"month": "2025-12", "value": 640000}
    ]

    return jsonify({
        "status": "success",
        "model": "SARIMA",
        "department": dept,
        "year": year,
        "forecast": forecast
    })

# ---------------- SUMMARY TABLE ----------------
@app.route("/budgets/summary")
def budget_summary():
    return jsonify([
        {"department": "IT", "planned": 26640000, "used": 10009000},
        {"department": "HR", "planned": 26640000, "used": 15465000},
        {"department": "Finance", "planned": 26640000, "used": 17055000},
        {"department": "Operations", "planned": 26640000, "used": 6475000},
        {"department": "Sales", "planned": 0, "used": 18360000}
    ])

# ---------------- RUN (LOCAL ONLY) ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
