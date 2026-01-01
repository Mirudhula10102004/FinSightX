from flask import Blueprint
from services.forecast_service import arima_forecast, sarima_forecast
from services.budget_service import get_used_budget_series

budget_bp = Blueprint("budget_bp", __name__)


# -----------------------------
# ARIMA API
# -----------------------------
@budget_bp.route("/budgets/forecast/arima/<department>/<int:year>")
def arima_api(department, year):
    data = get_used_budget_series(department, year)

    # 🔴 SAFETY: ensure data exists
    if not data:
        data = [500000]

    forecast = arima_forecast(data)

    return {
        "model": "ARIMA",
        "department": department,
        "year": year,
        "forecast": forecast
    }


# -----------------------------
# SARIMA API
# -----------------------------
@budget_bp.route("/budgets/forecast/sarima/<department>/<int:year>")
def sarima_api(department, year):
    data = get_used_budget_series(department, year)

    # 🔴 SAFETY: ensure data exists
    if not data:
        data = [500000]

    forecast = sarima_forecast(data)

    return {
        "model": "SARIMA",
        "department": department,
        "year": year,
        "forecast": forecast
    }
