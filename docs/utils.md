# Utilities

The `brent.utils` package provides common utilities and configurations used across different modules of the framework. This package includes functions for file and directory operations, logging setup, configuration management, and other helper functions.

## Modules

The `brent.utils` package includes the following modules:

- `common.py`: Provides common utility functions for file operations, logging, and timestamps.
- `config.py`: Provides functionality for managing configuration settings.
- `logger.py`: Provides functionality for setting up logging.

## common.py

### Overview

The `common.py` module contains various utility functions that are commonly used throughout the framework.

### Functions

- `create_directory(path: str) -> str`
  - Creates a directory if it does not already exist.
  - `path`: The path of the directory to create.
  - Returns the path of the created directory.

- `get_timestamp() -> str`
  - Gets the current timestamp in a standard format.
  - Returns the current timestamp as a string.

- `setup_logging(log_file: str = None, level: int = logging.INFO)`
  - Sets up logging for the application.
  - `log_file`: The file to write logs to. If `None`, logs will be written to the console.
  - `level`: The logging level.

- `read_file(file_path: str) -> str`
  - Reads the contents of a file.
  - `file_path`: The path of the file to read.
  - Returns the contents of the file as a string.

- `write_file(file_path: str, content: str)`
  - Writes content to a file.
  - `file_path`: The path of the file to write to.
  - `content`: The content to write to the file.

- `file_exists(file_path: str) -> bool`
  - Checks if a file exists.
  - `file_path`: The path of the file to check.
  - Returns `True` if the file exists, otherwise `False`.

- `directory_exists(directory_path: str) -> bool`
  - Checks if a directory exists.
  - `directory_path`: The path of the directory to check.
  - Returns `True` if the directory exists, otherwise `False`.

- `list_files(directory_path: str, extension: str = None) -> list`
  - Lists all files in a directory optionally filtered by extension.
  - `directory_path`: The path of the directory to list files in.
  - `extension`: The file extension to filter by (e.g., `.txt`). If `None`, all files are listed.
  - Returns a list of file paths.

#### Example Usage

```python
from brent.utils.common import create_directory, get_timestamp, setup_logging, read_file, write_file, file_exists, directory_exists, list_files

# Create a directory
dir_path = create_directory('example_dir')
print(f"Directory created: {dir_path}")

# Get the current timestamp
timestamp = get_timestamp()
print(f"Current timestamp: {timestamp}")

# Set up logging
setup_logging(log_file='example.log')
logging.info("This is an info message.")

# Write to a file
write_file('example_dir/example.txt', 'Hello, world!')

# Read from a file
content = read_file('example_dir/example.txt')
print(f"File content: {content}")

# Check if a file exists
exists = file_exists('example_dir/example.txt')
print(f"File exists: {exists}")

# List files in a directory
files = list_files('example_dir', extension='.txt')
print(f"Files in directory: {files}")
```

## config.py

### Overview

The `config.py` module contains the `Config` class, which is used to manage configuration settings.

### Config Class

#### Initialization

```python
Config(config_file: str)
```

- `config_file`: The path to the configuration file.

#### Methods

- `load_config() -> dict`
  - Loads the configuration from the file.
  - Returns the configuration dictionary.

- `get(key: str, default: Any = None) -> Any`
  - Gets a configuration value by key.
  - `key`: The key of the configuration value.
  - `default`: The default value to return if the key is not found.
  - Returns the configuration value or the default value.

- `set(key: str, value: Any)`
  - Sets a configuration value by key.
  - `key`: The key of the configuration value.
  - `value`: The value to set.

- `save_config()`
  - Saves the current configuration to the file.

- `update(new_config: dict)`
  - Updates the configuration with a new dictionary.
  - `new_config`: The new configuration dictionary.

#### Example Usage

```python
from brent.utils.config import Config
import json

# Define a sample configuration file path
config_path = 'example_config.json'

# Example configuration content
sample_config = {
    "setting1": "value1",
    "setting2": "value2",
    "setting3": 12345
}

# Write the sample configuration to the file
if not os.path.exists(config_path):
    with open(config_path, 'w') as file:
        json.dump(sample_config, file, indent=4)

# Initialize the Config class with the config file path
config = Config(config_path)

# Get a configuration value
setting1 = config.get('setting1')
print(f"Setting1: {setting1}")

# Set a new configuration value
config.set('setting4', 'new_value')

# Get the new configuration value
setting4 = config.get('setting4')
print(f"Setting4: {setting4}")

# Update the configuration with a new dictionary
new_config = {
    "setting2": "new_value2",
    "setting5": "another_value"
}
config.update(new_config)

# Get updated configuration values
setting2 = config.get('setting2')
setting5 = config.get('setting5')
print(f"Updated Setting2: {setting2}")
print(f"Setting5: {setting5}")
```

## logger.py

### Overview

The `logger.py` module provides functionality for setting up logging in the application.

### Functions

- `setup_logger(name: str, log_file: str, level: int = logging.INFO, max_bytes: int = 10*1024*1024, backup_count: int = 5) -> logging.Logger`
  - Sets up a logger with a specified name, log file, and logging level.
  - `name`: The name of the logger.
  - `log_file`: The file to write logs to.
  - `level`: The logging level.
  - `max_bytes`: The maximum size of the log file before it gets rotated.
  - `backup_count`: The number of backup log files to keep.
  - Returns the configured logger.

#### Example Usage

```python
from brent.utils.logger import setup_logger

# Setup a logger for the application
app_logger = setup_logger('brent', 'logs/app.log')

# Log some messages
app_logger.info("This is an info message.")
app_logger.warning("This is a warning message.")
app_logger.error("This is an error message.")
```

## Detailed Descriptions

### Common Utilities

The `common.py` module provides a variety of utility functions that are commonly used throughout the framework. These functions include file and directory operations, logging setup, and timestamp generation. They are designed to simplify common tasks and ensure consistency across different parts of the application.

### Config

The `config.py` module provides the `Config` class, which manages configuration settings for the application. It allows for loading, saving, and updating configuration values from a file, making it easy to manage application settings in a structured way.

### Logger

The `logger.py` module provides the `setup_logger` function, which sets up logging for the application. It supports rotating log files to manage log file sizes and ensures that log messages are consistently formatted and written to the appropriate log files or the console.

## Notes

- Ensure that the configuration file used with the `Config` class is properly formatted and accessible.
- The `setup_logger` function in the `logger.py` module uses a rotating file handler to manage log file sizes. Adjust the `max_bytes` and `backup_count` parameters as needed to suit your application's logging requirements.
- The utility functions provided in the `common.py` module are designed to be general-purpose and can be used in various parts of the application to simplify common tasks.

### Explanation

- **Modules**: Lists the modules included in the `brent.utils` package.
- **common.py**: Provides an overview and detailed description of the utility functions, including their definitions and example usage.
- **config.py**: Provides an overview and detailed description of the `Config` class, including its initialization, methods, and example usage.
- **logger.py**: Provides an overview and detailed description of the `setup_logger` function, including its definition and example usage.
- **Detailed Descriptions**: Elaborates on the functionality and use cases of the utility functions, `Config` class, and `setup_logger` function.
- **Notes**: Provides additional information and considerations for using the classes and functions in the `brent.utils` package.