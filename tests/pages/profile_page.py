import allure
from appium.webdriver.common.mobileby import MobileBy

from selenpy.element.base_element import BaseElement
from tests.pages.base_page import BasePage
from tests.utilities import constants


class ProfilePage(BasePage):

    def __init__(self):
        super().__init__()
        self.__REGISTER = BaseElement({
            "iOS": (MobileBy.IOS_PREDICATE, ""),
            "Android": (MobileBy.XPATH, "//android.widget.TextView[@content-desc='REGISTER']")
        })
        self.__SIGN_IN = BaseElement({
            "iOS": (MobileBy.IOS_PREDICATE, ""),
            "Android": (MobileBy.XPATH, "//android.widget.TextView[@text='SIGN IN']")
        })

    @allure.step("Tap Sign In")
    def tap_sign_in(self):
        self.__SIGN_IN.wait_for_visible(constants.MEDIUM_TIMEOUT)
        self.__SIGN_IN.click()
