# src/models.py

import pandas as pd
from prophet import Prophet

def forecast_prophet(df: pd.DataFrame, site_id: str, target_col: str, periods: int = 14) -> pd.DataFrame:
    # Filter for one site
    df_site = df[df['site_id'] == site_id].copy()

    # Prepare data for Prophet
    df_prophet = df_site[['date', target_col]].rename(columns={'date': 'ds', target_col: 'y'})

    # Initialize and fit model
    model = Prophet(daily_seasonality=True)
    model.fit(df_prophet)

    # Make future dataframe
    future = model.make_future_dataframe(periods=periods)

    # Predict
    forecast = model.predict(future)

    # Return only forecasted rows
    forecast = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
    forecast['site_id'] = site_id
    forecast['target'] = target_col

    return forecast.tail(periods), model
