import os
from box.exceptions import BoxValueError
import yaml
from ...cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    '''
    reads yaml file and returns a ConfigBox object

    Args:
        path_to_yaml (str): 
            path like input

    Raises:
        ValueError: 
            if yaml file is empty
        FileNotFoundError:
            if file is not found

    Returns:
        ConfigBox: 
            ConfigBox object   
    '''
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'YAML file loaded from {path_to_yaml}')
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f'YAML file is empty: {path_to_yaml}')
    except FileNotFoundError:
        raise FileNotFoundError(f'File not found: {path_to_yaml}')


@ensure_annotations
def create_directories(path_to_directories: list[Path], verbose=True) -> None:
    '''
    creates directories if they do not exist

    Args:
        path_to_directories (list[Path]): 
            list of paths to directories
        verbose (bool, optional):
            whether to print messages or not. Defaults to True.
    '''
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f'Directory created: {path}')


@ensure_annotations
def save_json(path: Path, data: dict) -> None:
    '''
    saves data to a json file

    Args:
        path (Path): 
            path to save the json file
        data (dict): 
            data to be saved
    '''
    with open(path, 'w') as json_file:
        json.dump(data, json_file)
    
    logger.info(f'JSON file saved to {path}')


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    '''
    loads data from a json file

    Args:
        path (Path): 
            path to the json file

    Returns:
        ConfigBox: 
            ConfigBox object
    '''
    with open(path, 'r') as json_file:
        data = json.load(json_file)

    logger.info(f'JSON file loaded from {path}')
    return ConfigBox(data)


@ensure_annotations
def save_bin(data: Any, path: Path) -> None:
    '''
    save binary file

    Args:
        data (Any): 
            data to be saved as binary
        path (Path): 
            path to save the binary file
    '''
    joblib.dump(value=data, filename=path)
    logger.info(f'Binary file saved to {path}')


@ensure_annotations
def load_bin(path: Path) -> Any:
    '''
    load binary file

    Args:
        path (Path): 
            path to the binary file

    Returns:
        Any: 
            data
    '''
    data = joblib.load(path)
    logger.info(f'Binary file loaded from {path}')
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    '''
    get size in KB of a file

    Args:
        path (Path): 
            path to the file

    Returns:
        str: 
            size in KB
    '''
    size_in_kb = round(os.path.getsize(path)/1024)
    return f'~ {size_in_kb} KB'


def decode_image(imgstring: str, file_name: str) -> None:
    '''
    Decodes image from base64 string and saves it to a file

    Args:
        imgstring (str): 
            base64 string
        file_name (str): 
            file name to save the image
    '''
    imgdata = base64.b64decode(imgstring)
    with open(file_name, 'wb') as f:
        f.write(imgdata)

    logger.info(f'Image saved to {file_name}')


def encode_image(file_name: str) -> str:
    '''
    Encodes image to base64 string

    Args:
        file_name (str): 
            path to the image file

    Returns:
        str: 
            base64 string
    '''
    with open(file_name, 'rb') as f:
        imgstring = base64.b64encode(f.read()).decode('utf-8')

    return imgstring