import logging

import pytest
from appium import webdriver

from selenpy.driver import capabilities
from selenpy.support import factory


class TestBase:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, config):
        logging.info(f"Starting the test on {str(pytest.driver)}")
        if pytest.driver.lower() == "ios":
            desired_caps = capabilities.get_ios_capabilities()

        elif pytest.driver.lower() == "android":
            desired_caps = capabilities.get_android_capabilities()
        else:
            print(f'The {pytest.driver} driver is not supported!')
            raise NotImplemented
        logging.info(f'desired_caps: {desired_caps}')
        factory.start_driver(pytest.driver.lower(), pytest.hub)

        yield
        print("Quit driver ...")
        factory.quit()
