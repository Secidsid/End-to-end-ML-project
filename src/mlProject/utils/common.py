import os
import sys
import yaml
from functools import wraps
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


from src.mlProject.logger import logging
from src.mlProject.exception import CustomException


def exception_handler(func: callable) -> callable:
    """
    This function is used to handle exceptions. It wraps the function and catches any exception raised by the function.
    To be used as a decorator.

    Args:
        func: Function to be wrapped.

    Returns:
        callable: Wrapped function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            raise CustomException(e, sys)
    return wrapper


def log_handler(func: callable) -> callable:
    """
    This function is used to log the function name, arguments and keyword arguments before and after the function is
    executed.
    To be used as a decorator.

    Args:
        func: Function to be wrapped.

    Returns:
        callable: Wrapped function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling function '{func.__name__}' with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Function '{func.__name__}' executed successfully!")
        return result
    return wrapper



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"created directory at: {path}")



@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

