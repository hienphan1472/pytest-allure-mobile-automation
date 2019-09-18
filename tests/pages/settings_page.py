from appium.webdriver.common.mobileby import MobileBy

from lib.utils import Utils


class SettingsPage:
    __AIRPLANE_MODE_TOGGLE = {
        "iOS": (MobileBy.IOS_PREDICATE, "type == 'XCUIElementTypeSwitch'"),
        "Android": (MobileBy.ACCESSIBILITY_ID, "AndroidIdentifier")
    }

    def __init__(self, driver):
        self.driver = driver
        # Utils.wait_element_to_be_visible(self, self.driver, *self.__EMAIL_FIELD)

    def toggle_airplane_mode(self):
        print("Function: toggle_airplane_mode")
        Utils.click_to_element(self, self.driver, **self.__AIRPLANE_MODE_TOGGLE)
