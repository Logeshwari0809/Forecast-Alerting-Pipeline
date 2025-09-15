# src/loader.py

import pandas as pd
from datetime import datetime

def load_data(ops_path='data/operations_daily_365d.csv',
              meta_path='data/site_meta.csv') -> pd.DataFrame:
    
    # Load and parse
    df_ops = pd.read_csv(ops_path)
    df_ops['date'] = pd.to_datetime(df_ops['date'])

    df_meta = pd.read_csv(meta_path)

    # Optional: derive site age
    current_year = datetime.now().year
    df_meta['site_age'] = current_year - df_meta['commissioned_year']

    # Merge and sort
    df = df_ops.merge(df_meta, on='site_id', how='left')
    df = df.sort_values(['site_id', 'date']).reset_index(drop=True)

    return df
