from selenpy.driver.android import AndroidDriver
from selenpy.driver.ios import iOSDriver
from selenpy.support.platforms import PlatformName


class DriverManager:
    platform_manager = None

    def __init__(self):
        self.platform_manager = {
            PlatformName.iOS: self._start_ios,
            PlatformName.ANDROID: self._start_android
        }

    def start_driver(self, name, remote_host):
        return self.platform_manager[name](remote_host)

    def _start_ios(self, remote_host):
        return iOSDriver().create_driver(remote_host=remote_host)

    def _start_android(self, remote_host):
        return AndroidDriver().create_driver(remote_host=remote_host)
