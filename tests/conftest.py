import configparser
import os

import moment
import pytest
import sys

import rootpath
from appium import webdriver
from lib import helpers


now = moment.now().strftime("%d-%m-%Y")

# Ignore py cache
sys.dont_write_bytecode = True

AUTO_HOME = rootpath.detect()


def pytest_exception_interact(node, report):
    path = node.location[0]
    print(f'\nPath: {path}')
    if node and report.failed:
        if node.funcargs.get('driver') is not None:
            class_name = node._nodeid.split(".py::")[-1].replace("::", "_class_")
            helpers.save_screenshot(node.funcargs.get('driver'), class_name)


# Create driver and env command line addoption
def pytest_addoption(parser):
    parser.addoption("--driver", action="store", default="Android", help="Mobile type")
    parser.addoption("--env", action="store", default="QA", help="Environment under test")
    parser.addoption("--url", action="store", default="https://staging.distiller.com/", help="URL under test")


@pytest.fixture(scope="session")
def config():
    """
    Read config.ini file to get appropriate capabilities
    :return: config object
    """
    config = configparser.ConfigParser()
    config.read(f'{AUTO_HOME}/config.ini')
    return config


@pytest.fixture(scope="class", autouse=False)
def driver(request, config):
    """
    Init and yield driver
    """
    driver = request.config.getoption("--driver")
    desired_caps = {
        "waitForQuiescence": config.getboolean("Common", "appium.waitForQuiescence"),
        "orientation": config.get("Common", "appium.orientation")
    }
    hub = config.get("AppiumServer", "appium.appiumServer")

    if driver.lower() == "ios":
        desired_caps["platformName"] = config.get("iOS", "ios.platformName")
        desired_caps["platformVersion"] = config.get("iOS", "ios.platformVersion")
        desired_caps["deviceName"] = config.get("iOS", "ios.deviceName")
        desired_caps["udid"] = config.get("iOS", "ios.udid")
        # desired_caps["app"] = config.get("iOS", "ios.app")
        desired_caps["automationName"] = config.get("iOS", "ios.automationName")
        desired_caps["browserName"] = config.get("iOS", "ios.browserName")

    elif driver.lower() == "android":
        desired_caps["platformName"] = config.get("Android", "android.platformName")
        desired_caps["platformVersion"] = config.get("Android", "android.platformVersion")
        # desired_caps["deviceName"] = config.get("Android", "android.deviceName")
        desired_caps["automationName"] = config.get("Android", "android.automationName")
        desired_caps["appActivity"] = config.get("Android", "android.appActivity")
        desired_caps["appPackage"] = config.get("Android", "android.appPackage")
        desired_caps["unicodeKeyboard"] = config.getboolean("Android", "android.unicode.keyboard")
        desired_caps["resetKeyboard"] = config.getboolean("Android", "android.reset.keyboard")
        desired_caps["autoGrantPermissions"] = config.getboolean("Android", "android.grant.permission")

    else:
        print(f'The {driver} driver is not supported!')
    print(desired_caps)
    driver = webdriver.Remote(hub, desired_caps)
    request.cls.driver = driver

    yield driver
    print("Quit driver ...")
    driver.quit()
