# src/features.py

import pandas as pd

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # --- Time Features ---
    df['day_of_week'] = df['date'].dt.dayofweek     # 0 = Monday
    df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)
    df['month'] = df['date'].dt.month

    # --- Lag Features (per site) ---
    for col in ['units_produced', 'power_kwh']:
        df[f'{col}_lag1'] = df.groupby('site_id')[col].shift(1)
        df[f'{col}_rolling7'] = df.groupby('site_id')[col].shift(1).rolling(7).mean().reset_index(level=0, drop=True)
        df[f'{col}_rolling14'] = df.groupby('site_id')[col].shift(1).rolling(14).mean().reset_index(level=0, drop=True)

    # --- Drop rows with NA (from rolling) ---
    df.dropna(inplace=True)

    return df
