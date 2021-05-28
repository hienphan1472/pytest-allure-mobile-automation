import configparser

import moment
import pytest
import sys

import rootpath

now = moment.now().strftime("%d-%m-%Y")

# Ignore py cache
sys.dont_write_bytecode = True

AUTO_HOME = rootpath.detect()


# def pytest_exception_interact(node, report):
#     path = node.location[0]
#     print(f'\nPath: {path}')
#     if node and report.failed:
#         if node.funcargs.get('driver') is not None:
#             class_name = node._nodeid.split(".py::")[-1].replace("::", "_class_")
#             helpers.save_screenshot(node.funcargs.get('driver'), class_name)


def pytest_addoption(parser):
    parser.addoption("--driver", action="store", help="Mobile type")
    parser.addoption("--hub", action="store", help="Mobile type")


def pytest_configure(config):
    pytest.driver = config.getoption("--driver", "Android", True)
    pytest.hub = config.getoption("--hub", "http://localhost:4723/wd/hub", True)


@pytest.fixture(scope="session")
def config():
    """
    Read config.ini file to get appropriate capabilities
    :return: config object
    """
    config = configparser.ConfigParser()
    config.read(f'{AUTO_HOME}/config.ini')
    return config
