from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Utils(object):
    @staticmethod
    def get_current_os(driver):
        return str(driver.desired_capabilities['platformName'])

    @staticmethod
    def return_element(self, driver, *element_identifier):
        return driver.find_element(*element_identifier)

    @staticmethod
    def wait_element_to_be_visible(self, driver, *element_identifier, time_out=None):
        if time_out is None:
            time_out = 10

        # wait for element to be visible
        self.wait = WebDriverWait(driver, time_out)
        self.wait.until(ec.visibility_of_element_located(element_identifier))

    @staticmethod
    def return_element_text(self, driver, *element_identify) -> str:
        text_for_element = Utils.return_element(self, driver, *element_identify)
        return text_for_element.text

    @staticmethod
    def click_to_element(self, driver, **element_identifier):
        element = driver.find_element(*element_identifier[Utils.get_current_os(driver)])
        element.click()

    @staticmethod
    def type_text_to_element(self, driver, text, **element_identifier):
        element = driver.find_element(*element_identifier[Utils.get_current_os(driver)])
        element.send_keys(text)
