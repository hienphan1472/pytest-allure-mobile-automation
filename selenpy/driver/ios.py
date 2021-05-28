from appium import webdriver

from selenpy.driver import capabilities
from selenpy.driver.driver import Driver


class iOSDriver(Driver):

    def create_driver(self, remote_host):
        desired_caps = capabilities.get_ios_capabilities()
        self._driver = webdriver.Remote(remote_host, desired_caps)
        return self
