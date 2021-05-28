import logging
import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from selenpy.common import config
from selenpy.support import factory


class BaseElement:
    def __init__(self, element_identifier):
        self.__locators = element_identifier

    @property
    def _driver(self):
        return factory.get_driver()

    @property
    def _locator(self):
        return self.__locators[self._driver.desired_capabilities['platformName']]

    @property
    def _element(self):
        return self.find_element()

    @property
    def text(self):
        text = self.find_element().text
        return text

    def find_element(self):
        return WebDriverWait(self._driver, config.timeout).until(ec.presence_of_element_located(self._locator))

    def find_elements(self):
        return WebDriverWait(self._driver, config.timeout).until(ec.presence_of_all_elements_located(self._locator))

    def delay(self, seconds):
        time.sleep(seconds)

    def get_attribute(self, name):
        return self._element.get_attribute(name)

    def is_enabled(self):
        return self._element.is_enabled()

    def is_selected(self):
        return self._element.is_selected()

    def is_displayed(self, timeout=None):
        try:
            logging.info(f"is_displayed: {self._locator}")
            return self.wait_for_visible(timeout).is_displayed()
        except (NoSuchElementException, TimeoutException, StaleElementReferenceException):
            return False
        except Exception as e:
            raise e

    def wait_for_visible(self, timeout=None):
        if timeout is None:
            timeout = config.timeout
        return WebDriverWait(self._driver, timeout).until(ec.visibility_of_element_located(self._locator))

    def wait_for_invisible(self, timeout=None):
        if timeout is None:
            timeout = config.timeout
        return WebDriverWait(self._driver, timeout).until(ec.invisibility_of_element_located(self._locator))

    def wait_for_presence(self, timeout=None):
        if timeout is None:
            timeout = config.timeout
        return WebDriverWait(self._driver, timeout).until(ec.presence_of_element_located(self._locator))

    def wait_for_clickable(self, timeout=None):
        if timeout is None:
            timeout = config.timeout
        return WebDriverWait(self._driver, timeout).until(ec.element_to_be_clickable(self._locator))

    def click(self):
        self._element.click()

    def enter(self, text):
        self._element.send_keys(text)
