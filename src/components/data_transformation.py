import sys
import os
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path: str = os.path.join("artifacts", "preprocessor.pkl")


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_preprocessor(self):
        """Returns a preprocessor pipeline that transforms the input features"""

        # Define the numerical and categorical columns
        numerical_cols = ["time_since_launch", "orbital_altitude", "battery_voltage", 
                          "solar_panel_temperature", "attitude_control_error", 
                          "data_transmission_rate"]
        categorical_cols = ["thermal_control_status"]

        # Define the preprocessor pipeline for numerical columns
        num_transformer = Pipeline(steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler())
        ])

        # Define the preprocessor pipeline for categorical columns
        cat_transformer = Pipeline(steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder())
        ])

        # Combine the preprocessor pipelines for numerical and categorical columns
        preprocessor = ColumnTransformer(
            transformers=[
                ("num", num_transformer, numerical_cols),
                ("cat", cat_transformer, categorical_cols)
            ]
        )

        return preprocessor

    def initiate_data_transformation(self, train_path, test_path):
        """Performs data transformation on train and test data"""

        try:
            logging.info("Reading train and test data")
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Performing data transformation")
            preprocessor = self.get_preprocessor()

            # Transform train data
            X_train = preprocessor.fit_transform(train_df.drop(columns=["satellite_health"]))
            y_train = train_df["satellite_health"].values

            # Transform test data
            X_test = preprocessor.transform(test_df.drop(columns=["satellite_health"]))
            y_test = test_df["satellite_health"].values

            # Save the preprocessor object
            logging.info("Saving preprocessor object")
            save_object(self.data_transformation_config.preprocessor_obj_file_path, preprocessor)

            return X_train, y_train, X_test, y_test

        except Exception as e:
            raise CustomException(e, sys)
