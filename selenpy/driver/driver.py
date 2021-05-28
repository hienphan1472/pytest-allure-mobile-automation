from abc import abstractmethod


class Driver:
    def __init__(self):
        self._driver = None

    @abstractmethod
    def create_driver(self, remote_host):
        pass

    def get_driver(self):
        return self._driver

    def quit(self):
        self._driver.quit()
