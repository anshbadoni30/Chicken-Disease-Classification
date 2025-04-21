from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainigPipeline
from cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from cnnClassifier.logger import logging

STAGE_NAME = "Data Ingestion stage"

try:
    logging.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logging.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    raise e




STAGE_NAME = "Prepare Base Model"

try:
    logging.info(f"*****************")
    logging.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    obj = PrepareBaseModelTrainigPipeline()
    obj.main()
    logging.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nx=====================x")
except Exception as e:
    raise e



STAGE_NAME = "Training"

try:
    logging.info(f"******************************")
    logging.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<")
    model_trainer=ModelTrainingPipeline()
    model_trainer.main()
    logging.info(f">>>>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<\n\nx==============x")
except Exception as e:
    raise e