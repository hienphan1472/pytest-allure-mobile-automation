import allure
from appium.webdriver.common.mobileby import MobileBy

from selenpy.element.base_element import BaseElement
from tests.pages.base_page import BasePage
from tests.utilities import constants


class HomePage(BasePage):

    def __init__(self):
        super().__init__()
        self.__PROFILE = BaseElement({
            "iOS": (MobileBy.IOS_PREDICATE, ""),
            "Android": (MobileBy.XPATH, "//android.widget.TextView[@content-desc='PROFILE']")
        })
        self.__SKIP = BaseElement({
            "iOS": (MobileBy.IOS_PREDICATE, ""),
            "Android": (MobileBy.XPATH, "//android.widget.TextView[@text='Skip']")
        })

    @allure.step("Tap Profile")
    def tap_profile(self):
        if self.__SKIP.is_displayed(constants.SHORT_TIMEOUT):
            self.__SKIP.click()
        self.__PROFILE.wait_for_visible(constants.MEDIUM_TIMEOUT)
        self.__PROFILE.click()
