from appium import webdriver

from selenpy.driver import capabilities
from selenpy.driver.driver import Driver


class AndroidDriver(Driver):

    def create_driver(self, remote_host):
        desired_caps = capabilities.get_android_capabilities()
        self._driver = webdriver.Remote(remote_host, desired_caps)
        return self
