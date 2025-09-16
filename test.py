# test.py

import os
import pandas as pd

from src.loader import load_data
from src.features import engineer_features
from src.models import forecast_prophet
from src.anomaly import detect_anomalies

def test_pipeline(site_id='S1', forecast_days=14):
    print("\n✅ Loading and engineering data...")
    df = load_data(
        ops_path='data/operations_daily_365d.csv',
        meta_path='data/site_meta.csv'
    )
    df = engineer_features(df)
    
    print("📊 Running forecasts...")
    for target in ['units_produced', 'power_kwh']:
        forecast_df, model = forecast_prophet(df, site_id, target, periods=forecast_days)
        forecast_path = f"outputs/forecast_{target}_{site_id}.csv"
        forecast_df.to_csv(forecast_path, index=False)
        print(f"✅ Saved forecast → {forecast_path}")
    
    print("🚨 Running anomaly detection...")
    alerts_df = detect_anomalies(df)
    alerts_path = "outputs/alerts.csv"
    alerts_df.to_csv(alerts_path, index=False)
    print(f"✅ Saved alerts → {alerts_path}")

    print("\n📁 Verifying output files...")
    for file in [
        f"outputs/forecast_units_produced_{site_id}.csv",
        f"outputs/forecast_power_kwh_{site_id}.csv",
        "outputs/alerts.csv"
    ]:
        print(f"✅ Exists: {file} →", os.path.exists(file))

    print("\n🎉 Pipeline test complete.")

if __name__ == "__main__":
    test_pipeline()
