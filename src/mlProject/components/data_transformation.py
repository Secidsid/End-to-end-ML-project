import os
import pandas as pd
from sklearn.model_selection import train_test_split

from src.mlProject.logger import logging
from src.mlProject.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

        

    # Only adding train_test_spliting as this data is already cleaned up


    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logging.info("Splited data into training and test sets")
        logging.info(train.shape)
        logging.info(test.shape)

        print(train.shape)
        print(test.shape)
        
