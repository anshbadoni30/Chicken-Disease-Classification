from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import dataingestionconfig

class ConfigurationManager:
    def __init__(self, 
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAM_FILE_PATH):

        self.config= read_yaml(config_filepath)
        self.params= read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])
        #Creation of Artifacts folder


    def get_data_ingestion_config(self) -> dataingestionconfig: #This function is expected to return an object of type dataingestionconfig
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = dataingestionconfig(
            root_dir=config.root_dir,
            source_URL= config.source_URL,
            local_data_file= config.local_data_file,
            unzip_dir= config.unzip_dir
        )

        return data_ingestion_config