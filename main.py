from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.logger import logging

STAGE_NAME = "Data Ingestion stage"

try:
    logging.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logging.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    raise e