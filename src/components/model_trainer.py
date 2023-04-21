import os
import sys
from dataclasses import dataclass

from catboost import CatBoostClassifier
from sklearn.ensemble import (
    AdaBoostClassifier,
    GradientBoostingClassifier,
    RandomForestClassifier,
)
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier

from src.exceptions import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_models


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Split training and test input data")
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1],
            )

            models = {
                "Logistic Regression": LogisticRegression(),
                "Decision Tree": DecisionTreeClassifier(),
                "Random Forest": RandomForestClassifier(),
                "Gradient Boosting": GradientBoostingClassifier(),
                "K Nearest Neighbors": KNeighborsClassifier(),
                "XGBClassifier": XGBClassifier(),
                "CatBoosting Classifier": CatBoostClassifier(verbose=False),
                "AdaBoost Classifier": AdaBoostClassifier(),
            }

            params = {
                "Logistic Regression": {
                    "penalty": ["l1", "l2", "elasticnet", "none"],
                    "C": [0.1, 0.5, 1.0, 5.0, 10.0],
                    "solver": ["newton-cg", "lbfgs", "liblinear", "sag", "saga"],
                },
                "Decision Tree": {
                    "criterion": ["gini", "entropy"],
                    "splitter": ["best", "random"],
                    "max_depth": [None, 10, 20, 30],
                },
                "Random Forest": {
                    "criterion": ["gini", "entropy"],
                    "n_estimators": [8, 16, 32, 64, 128, 256],
                    "max_depth": [None, 10, 20, 30],
                },
                "Gradient Boosting": {
                    "loss": ["deviance", "exponential"],
                    "learning_rate": [0.01, 0.05, 0.1],
                    "subsample": [0.6, 0.7, 0.75, 0.8, 0.85, 0.9],
                    "max_depth": [3, 4, 5, 6],
                    "n_estimators": [8, 16, 32, 64, 128, 256],
                },
                                "K Nearest Neighbors": {"n_neighbors": [3, 5, 7, 9]},
                "XGBClassifier": {
                    "learning_rate": [0.01, 0.05, 0.1],
                    "max_depth": [3, 4, 5, 6],
                    "n_estimators": [8, 16, 32, 64, 128, 256],
                },
                "CatBoosting Classifier": {
                    "depth": [4, 6, 8, 10],
                    "learning_rate": [0.01, 0.05, 0.1],
                    "iterations": [30, 50, 100],
                    "l2_leaf_reg": [3, 5, 7, 9]
                },
                "AdaBoost Classifier": {
                    "n_estimators": [8, 16, 32, 64, 128, 256],
                    "learning_rate": [0.01, 0.05, 0.1],
                },
            }

            model_report = evaluate_models(X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test,
                                           models=models, param=params)
            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise CustomException("No best model found")

            logging.info(f"Best model found on both training and testing dataset")

            save_object(file_path=self.model_trainer_config.trained_model_file_path, obj=best_model)

            predicted = best_model.predict(X_test)

            accuracy = accuracy_score(y_test, predicted)
            return accuracy

        except Exception as e:
            raise CustomException(e, sys)
