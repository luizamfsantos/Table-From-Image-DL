from src.tableDecoder import logger
from src.tableDecoder.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = 'Data Ingestion stage'
try:
    logger.info(f'>>>>>>>>>>>> Starting {STAGE_NAME} <<<<<<<<<<<<')
    obj = DataIngestionTrainingPipeline()
    obj.run()
    logger.info(f'>>>>>>>>>>>> Completed {STAGE_NAME} <<<<<<<<<<<<')
except Exception as e:
    logger.error(f'Error in {STAGE_NAME}')
    raise e