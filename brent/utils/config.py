import json
import os
from pathlib import Path

class Config:
    def __init__(self, config_file):
        """
        Initialize the Config class with a path to the configuration file.

        :param config_file: The path to the configuration file.
        """
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        """
        Load the configuration from the file.

        :return: The configuration dictionary.
        """
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"Config file '{self.config_file}' not found.")
        
        with open(self.config_file, 'r') as file:
            config = json.load(file)
        
        return config

    def get(self, key, default=None):
        """
        Get a configuration value by key.

        :param key: The key of the configuration value.
        :param default: The default value to return if the key is not found.
        :return: The configuration value or the default value.
        """
        return self.config.get(key, default)

    def set(self, key, value):
        """
        Set a configuration value by key.

        :param key: The key of the configuration value.
        :param value: The value to set.
        """
        self.config[key] = value
        self.save_config()

    def save_config(self):
        """
        Save the current configuration to the file.
        """
        with open(self.config_file, 'w') as file:
            json.dump(self.config, file, indent=4)

    def update(self, new_config):
        """
        Update the configuration with a new dictionary.

        :param new_config: The new configuration dictionary.
        """
        self.config.update(new_config)
        self.save_config()
