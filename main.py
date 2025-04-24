from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainigPipeline
from src.cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline
from src.cnnClassifier.logger import logging

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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



STAGE_NAME= "Evaluation stage"

try:
    logging.info(f"*******************")
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = EvaluationPipeline()
    obj.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)
    raise e