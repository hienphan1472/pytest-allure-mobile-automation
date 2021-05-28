from selenpy.support.driver_manager import DriverManager

__driver = {}


def start_driver(name, remote_host, driver_key="default"):
    driver = DriverManager().start_driver(name, remote_host)
    __driver[driver_key] = driver
    Key.current = driver_key


def get_driver():
    return __driver[Key.current].get_driver()


def get_contexts():
    return get_driver().contexts


def quit():
    get_driver().quit()


class Key:
    current = "default"
