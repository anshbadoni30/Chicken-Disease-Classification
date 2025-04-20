from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier.logger import logging

STAGE_NAME = "Prepare Base Model"

class PrepareBaseModelTrainigPipeline:
    def __init__(self):
        pass

    def main(self):
        config= ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model= PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()



if __name__=="__main__":
    try:
        logging.info(f"*****************")
        logging.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
        obj = PrepareBaseModelTrainigPipeline()
        obj.main()
        logging.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nx=====================x")
    except Exception as e:
        raise e