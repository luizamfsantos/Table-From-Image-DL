import os
from tableDecoder.utils.common import get_size
import zipfile
import gdown
from tableDecoder import logger
from tableDecoder.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        '''
        Fetch data from the url
        '''
        try:
            dataset_url = self.config.source_url
            zip_download_dir = self.config.local_data_file
            os.makedirs('artifacts/data_ingestion', exist_ok=True)
            logger.info(f'Downloading data from {dataset_url} to {zip_download_dir}')

            file_id = dataset_url.split('/')[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix + file_id, zip_download_dir, quiet=False)

            logger.info(f'Downloaded data from {dataset_url} to {zip_download_dir}')
        
        except Exception as e:
            logger.error(f'Error in downloading data from {dataset_url} to {zip_download_dir}')
            raise e

    def unzip_data(self):
        '''
        Unzip the data
        '''
        try:
            zip_file_path = self.config.local_data_file
            unzip_dir = self.config.unzip_dir
            os.makedirs(unzip_dir, exist_ok=True)
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(unzip_dir)

            logger.info(f'Unzipped data from {zip_file_path} to {unzip_dir}')
        
        except Exception as e:
            logger.error(f'Error in unzipping data from {zip_file_path} to {unzip_dir}')
            raise e
            