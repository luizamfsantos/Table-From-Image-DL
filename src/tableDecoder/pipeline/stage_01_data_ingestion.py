from tableDecoder.config.configurations import ConfigurationManager
from tableDecoder.components.data_ingestion import DataIngestion
from tableDecoder import logger

STAGE_NAME = 'Data Ingestion stage'


class DataIngestionTrainingPipeline:
    def __init__(self):
        self.config_manager = ConfigurationManager()
        data_ingestion_config = self.config_manager.get_data_ingestion_config()
        self.data_ingestion = DataIngestion(config=data_ingestion_config)

    def run(self):
        self.data_ingestion.download_data()
        self.data_ingestion.unzip_data()


if __name__ == '__main__':
    try:
        logger.info(f'>>>>>>>>>>>> Starting {STAGE_NAME} <<<<<<<<<<<<')
        obj = DataIngestionTrainingPipeline()
        obj.run()
        logger.info(f'>>>>>>>>>>>> Completed {STAGE_NAME} <<<<<<<<<<<<')
    except Exception as e:
        logger.error(f'Error in {STAGE_NAME}')
        raise e