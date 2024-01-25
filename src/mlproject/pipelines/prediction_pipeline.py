import sys
import os
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
import numpy as np
from src.mlproject.utils import load_object


class CustomData:
    def __init__(self, age:int, gender: str, bmi:float, children:int, smoker:str, region: str):
        self.age = age
        self.gender = gender
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = region
    
    def get_data_as_df(self):
        try:
            data_dict = {
                'age': [self.age],
                'sex': [self.gender],
                'bmi': [self.bmi],
                'children': [self.children],
                'smoker': [self.smoker],
                'region': [self.region]
            }
            return pd.DataFrame(data_dict)
        except Exception as e:
            raise CustomException(e, sys)

class PredictionPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path='D:/mlproject/artifacts/model.pkl'
            preprocessor_path='D:/mlproject/artifacts/preprocessor.pkl'
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)