"""
Код Ревью:
- структура каталогов src/data/data.py
- отсутствует стат типизация
"""

import pandas as pd
# добавить еще одину пустую строку
def load_data(path):
    """ """
    return pd.read_csv(path)

def split_data(data):
    """ """
    from sklearn.model_selection import train_test_split
    features = data.drop('fare_amount', axis=1)
    target = data['fare_amount']
    return train_test_split(features, target, test_size=0.2)
