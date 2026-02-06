"""
Код Ревью:
- структура каталогов src/feature/feature.py
- отсутствует стат типизация
- отсутствует обработка пропусков и анамалий
- отсутствует обработка пограничных данных
"""

import pandas as pd
from datetime import datetime # излишний импорт


def add_time_features(df):
    """ """
    df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
    df['hour'] = df['pickup_datetime'].dt.hour
    df['day_of_week'] = df['pickup_datetime'].dt.dayofweek
    return df.drop('pickup_datetime', axis=1)
