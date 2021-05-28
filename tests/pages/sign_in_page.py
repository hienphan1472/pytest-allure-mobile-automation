import allure
from appium.webdriver.common.mobileby import MobileBy

from selenpy.element.base_element import BaseElement
from tests.pages.base_page import BasePage
from tests.utilities import constants, messages


class SignInPage(BasePage):

    def __init__(self):
        super().__init__()
        self.__EMAIL = BaseElement({
            "iOS": (MobileBy.IOS_PREDICATE, ""),
            "Android": (MobileBy.XPATH, "//android.widget.EditText[@text='EMAIL']")
        })
        self.__PASSWORD = BaseElement({
            "iOS": (MobileBy.IOS_PREDICATE, ""),
            "Android": (MobileBy.XPATH, "//android.widget.EditText[@text='PASSWORD']")
        })
        self.__SIGN_IN = BaseElement({
            "iOS": (MobileBy.IOS_PREDICATE, ""),
            "Android": (MobileBy.XPATH, "//android.widget.Button[@text='SIGN IN']")
        })
        self.__WELCOME_MESSAGE = BaseElement({
            "iOS": (MobileBy.IOS_PREDICATE, ""),
            "Android": (MobileBy.ID, "android:id/message")
        })

    @allure.step("Sign In")
    def sign_in(self, email, password):
        self.__EMAIL.wait_for_visible(constants.MEDIUM_TIMEOUT)
        self.__EMAIL.enter(email)
        self.__PASSWORD.enter(password)
        self.__SIGN_IN.click()

    @allure.step("Verify User Is Sign In Successfully")
    def verify_sign_in(self):
        assert self.__WELCOME_MESSAGE.text == messages.SIGN_IN_SUCCESS
