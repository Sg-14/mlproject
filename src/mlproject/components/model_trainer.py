import os
import sys
from dataclasses import dataclass

from sklearn.metrics import mean_squared_error, r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor,GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression, Ridge,Lasso
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import RandomizedSearchCV
from catboost import CatBoostRegressor
from xgboost import XGBRegressor
from sklearn.ensemble import BaggingRegressor

from src.mlproject.exception import CustomException
from src.mlproject.logger import logging

from src.mlproject.utils import save_object

@dataclass
class ModelTrainerConfig:
    trained_model_obj_path = os.path.join('artifacts', 'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_trainer(self, train_arr, test_arr):
        """
        This function is responsible for model training
        """
        try:
            logging.info('Reading train and test data')
            X_train,y_train,X_test,y_test = (
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )
            bg = BaggingRegressor(estimator=RandomForestRegressor(max_depth = 5,max_leaf_nodes=35, warm_start=True),n_estimators=50,random_state=42)
            bg.fit(X_train, y_train) # Train model
            logging.info("Model Trained")
            # Make predictions
            y_train_pred = bg.predict(X_train)
            y_test_pred = bg.predict(X_test)
            
            save_object(
                file_path=self.model_trainer_config.trained_model_obj_path,
                obj=bg
            )

            r2_val = r2_score(y_test, y_test_pred)
            print(r2_val)
            return r2_val

        except Exception as e:
            raise CustomException(e, sys)