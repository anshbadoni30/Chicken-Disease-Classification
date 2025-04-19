import os
import urllib.request as request #for requesting of unzipping the dataset file
import zipfile #for unzipping the dataset file
from src.cnnClassifier.logger import logging
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import dataingestionconfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config:dataingestionconfig): #Initializes the class with a config object of type dataingestionconfig
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file): #Uses urllib.request.urlretrieve() to download the file from the URL specified in config.source_URL and saves it to config.local_data_file
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logging.info(f"{filename} download! with following info: \n{headers}")
        else:
             logging.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    
    def extract_zip_file(self):
        """
        zip_file_path: str
        extracts the zip into data directory
        Functions return none
        """
        unzip_path= self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)



