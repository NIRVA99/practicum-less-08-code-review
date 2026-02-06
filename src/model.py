"""
Код Ревью:
- структура каталогов src/model/model.py
- отсутствует стат типизация
- отсутствует сохранение параметров модели и ее обученой версии
- отсутствие сохранения Метрики и артефактов обучения (json, yaml и т. п.)
- def GridSearch(self)
- def score(self) # проверка типов входных данных
"""

from sklearn.ensemble import GradientBoostingRegressor


class TaxiFareModel:
    """ """
    def __init__(self):
        """ """
        # random_state=None
        self.model = GradientBoostingRegressor()

    def fit(self, X, y):
        """ """
        self.model.fit(X, y)

    def predict(self, X):
        """ """
        return self.model.predict(X)
