# src/anomaly.py

import pandas as pd

def detect_anomalies(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    alerts = []

    for _, row in df.iterrows():
        if row['downtime_minutes'] > 60:
            alerts.append({
                'date': row['date'],
                'site_id': row['site_id'],
                'type': 'High Downtime',
                'value': row['downtime_minutes']
            })
        elif row['units_produced'] == 0 and row['downtime_minutes'] == 0:
            alerts.append({
                'date': row['date'],
                'site_id': row['site_id'],
                'type': 'Zero Production Without Downtime',
                'value': 0
            })

    return pd.DataFrame(alerts)
