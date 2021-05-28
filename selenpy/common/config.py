import configparser

import rootpath

AUTO_HOME = rootpath.detect()
timeout = 5
poll_during_waits = 0.5


def get_config():
    config = configparser.ConfigParser()
    config.read(f'{AUTO_HOME}/config.ini')
    return config
