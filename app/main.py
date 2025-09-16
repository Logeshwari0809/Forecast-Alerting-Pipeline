# app/main.py

import typer
from pathlib import Path
import pandas as pd
import sys
import os

# Add src folder to path
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from loader import load_data
from features import engineer_features
from models import forecast_prophet
from anomaly import detect_anomalies

app = typer.Typer()

@app.command()
def forecast(
    site_id: str = typer.Option(..., help="Site ID (e.g., SITE_001)"),
    target: str = typer.Option("units_produced", help="Target variable to forecast"),
    days: int = typer.Option(14, help="Number of days to forecast")
):
    """
    Generate forecast for a site and target variable.
    """
    df = load_data()
    df = engineer_features(df)

    forecast_df, _ = forecast_prophet(df, site_id, target, periods=days)

    output_file = f"outputs/forecast_{target}_{site_id}.csv"
    forecast_df.to_csv(output_file, index=False)
    print(f"✅ Forecast saved to {output_file}")


@app.command()
def anomalies():
    """
    Detect anomalies in all sites and save to alerts.csv
    """
    df = load_data()
    df = engineer_features(df)

    alerts_df = detect_anomalies(df)
    output_file = "outputs/alerts.csv"
    alerts_df.to_csv(output_file, index=False)
    print(f"⚠️ Alerts saved to {output_file}")


if __name__ == "__main__":
    app()
