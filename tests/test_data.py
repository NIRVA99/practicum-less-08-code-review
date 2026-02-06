"""
Код Ревью:
- отсутствует стат типизация
"""

import pandas as pd # излишний импорт
from src.data import load_data
# добавить еще одину пустую строку
def test_load_data():
    """ """
    df = load_data("data/uber.csv")
    assert not df.empty

# нужен тест на логику предобработки
# нужен тест на обработку пограничных условий в данных
