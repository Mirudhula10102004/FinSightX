import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX


# -----------------------------
# FALLBACK FORECAST (NO NULL)
# -----------------------------
def fallback_forecast(last_value, months=6, growth=0.02):
    forecast = []
    start_date = datetime(2026, 1, 1)

    value = float(last_value)

    for i in range(months):
        value = value * (1 + growth)
        forecast.append({
            "month": (start_date + relativedelta(months=i)).strftime("%Y-%m-%d"),
            "value": round(value, 2)
        })

    return forecast


# -----------------------------
# ARIMA FORECAST
# -----------------------------
def arima_forecast(data, periods=6):
    series = pd.Series(data)

    # 🔴 CRITICAL FIX: NO ERROR, USE FALLBACK
    if len(series) < 6:
        return fallback_forecast(series.iloc[-1], periods)

    model = ARIMA(series, order=(1, 1, 1))
    fitted = model.fit()
    preds = fitted.forecast(steps=periods)

    start_date = datetime(2026, 1, 1)

    return [
        {
            "month": (start_date + relativedelta(months=i)).strftime("%Y-%m-%d"),
            "value": round(float(preds.iloc[i]), 2)
        }
        for i in range(periods)
    ]


# -----------------------------
# SARIMA FORECAST
# -----------------------------
def sarima_forecast(data, periods=6):
    series = pd.Series(data)

    # 🔴 CRITICAL FIX: NO ERROR, USE FALLBACK
    if len(series) < 12:
        return fallback_forecast(series.iloc[-1], periods, growth=0.015)

    model = SARIMAX(
        series,
        order=(1, 1, 1),
        seasonal_order=(1, 1, 1, 12),
        enforce_stationarity=False,
        enforce_invertibility=False
    )

    fitted = model.fit(disp=False)
    preds = fitted.forecast(steps=periods)

    start_date = datetime(2026, 1, 1)

    return [
        {
            "month": (start_date + relativedelta(months=i)).strftime("%Y-%m-%d"),
            "value": round(float(preds.iloc[i]), 2)
        }
        for i in range(periods)
    ]
