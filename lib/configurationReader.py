import os
import json

CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'configuration')


def check_if_config_exists(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError("Configuration file not found!\n%s" % file_path)


def load_configuration_from_file(file_name):
    """Function opens json file from configuration directory
        :param file_name: config file name
        :return: data from json file in object.attribute format
    """
    file_path = os.path.join(CONFIG_PATH, file_name)
    check_if_config_exists(file_path)
    with open(file_path, 'r') as config_file:
        config = json.load(config_file)
    return config
