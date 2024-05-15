import os
import logging
from datetime import datetime
from pathlib import Path

def create_directory(path):
    """
    Create a directory if it doesn't already exist.

    :param path: The path of the directory to create.
    :return: The path of the created directory.
    """
    Path(path).mkdir(parents=True, exist_ok=True)
    return path

def get_timestamp():
    """
    Get the current timestamp in a standard format.

    :return: The current timestamp as a string.
    """
    return datetime.now().strftime("%Y%m%d%H%M%S")

def setup_logging(log_file=None, level=logging.INFO):
    """
    Set up logging for the application.

    :param log_file: The file to write logs to. If None, logs will be written to the console.
    :param level: The logging level.
    """
    logger = logging.getLogger()
    logger.setLevel(level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    if log_file:
        handler = logging.FileHandler(log_file)
    else:
        handler = logging.StreamHandler()

    handler.setFormatter(formatter)
    logger.addHandler(handler)

def read_file(file_path):
    """
    Read the contents of a file.

    :param file_path: The path of the file to read.
    :return: The contents of the file as a string.
    """
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    """
    Write content to a file.

    :param file_path: The path of the file to write to.
    :param content: The content to write to the file.
    """
    with open(file_path, 'w') as file:
        file.write(content)

def file_exists(file_path):
    """
    Check if a file exists.

    :param file_path: The path of the file to check.
    :return: True if the file exists, False otherwise.
    """
    return os.path.isfile(file_path)

def directory_exists(directory_path):
    """
    Check if a directory exists.

    :param directory_path: The path of the directory to check.
    :return: True if the directory exists, False otherwise.
    """
    return os.path.isdir(directory_path)

def list_files(directory_path, extension=None):
    """
    List all files in a directory optionally filtered by extension.

    :param directory_path: The path of the directory to list files in.
    :param extension: The file extension to filter by (e.g., '.txt'). If None, all files are listed.
    :return: A list of file paths.
    """
    files = []
    for entry in os.listdir(directory_path):
        if extension:
            if entry.endswith(extension):
                files.append(os.path.join(directory_path, entry))
        else:
            files.append(os.path.join(directory_path, entry))
    return files

