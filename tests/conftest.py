import configparser
import os

import moment
import pytest
import sys

from appium import webdriver
from lib import helpers


now = moment.now().strftime("%d-%m-%Y")

# Ignore py cache
sys.dont_write_bytecode = True

AUTO_HOME = os.path.realpath(os.path.join(os.path.dirname(__file__), "."))


def pytest_exception_interact(node, report):
    path = node.location[0]
    print(f'\nPath: {path}')
    if node and report.failed:
        class_name = node._nodeid.split(".py::")[-1].replace("::", "_class_")
        helpers.save_screenshot(node.funcargs.get('driver'), class_name)


# Create driver and env command line addoption
def pytest_addoption(parser):
    parser.addoption("--driver", action="store", default="iOS", help="Mobile type")
    parser.addoption("--env", action="store", default="QA", help="Environment under test")


@pytest.fixture(scope="session")
def config():
    """
    Read local.ini file to get appropriate capabilities
    :return: config object
    """
    config = configparser.ConfigParser()
    config.read('../../local.ini')
    return config


def get_default_desired_caps(config):
    desired_caps = {
        "waitForQuiescence": config.get("AppiumCommon", "appium.waitForQuiescence"),
        "orientation": config.get("AppiumCommon", "appium.orientation")
    }
    return desired_caps


@pytest.fixture(scope="class", autouse=False)
def driver(request, config):
    """
    Init and yield driver
    """
    driver = request.config.getoption("--driver")
    desired_caps = get_default_desired_caps(config)
    hub = config["AppiumServer"]["appium.appiumServer"]

    if driver.lower() == "ios":
        desired_caps["platformName"] = config.get("AppiumiOS", "ios.platformName")
        desired_caps["platformVersion"] = config.get("AppiumiOS", "ios.platformVersion")
        desired_caps["deviceName"] = config.get("AppiumiOS", "ios.deviceName")
        desired_caps["udid"] = config.get("AppiumiOS", "ios.udid")
        desired_caps["app"] = config.get("AppiumiOS", "ios.app")
        desired_caps["automationName"] = config.get("AppiumiOS", "ios.automationName")
        # desired_caps["usePrebuiltWDA"] = config.get("AppiumiOS", "ios.usePrebuiltWDA")
        # desired_caps["noReset"] = config.get("AppiumiOS", "ios.noReset")

    elif driver.lower() == "android":
        desired_caps["platformName"] = config.get("AppiumAndroid", "android.platformName")
        desired_caps["deviceName"] = config.get("AppiumAndroid", "android.deviceName")
        desired_caps["automationName"] = config.get("AppiumAndroid", "android.automationName")
        desired_caps["app"] = config.get("AppiumAndroid", "android.app")
        desired_caps["appActivity"] = config.get("AppiumAndroid", "android.appActivity")
        desired_caps["appPackage"] = config.get("AppiumAndroid", "android.appPackage")

    else:
        print(f'The {driver} driver is not supported!')

    driver = webdriver.Remote(hub, desired_caps)
    request.cls.driver = driver

    yield driver
    print("Quit driver ...")
    driver.quit()
