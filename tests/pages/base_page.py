from appium.webdriver.common.mobileby import MobileBy


class BasePage:
    __COMMON = {
        "iOS": (MobileBy.IOS_PREDICATE, ""),
        "Android": (MobileBy.XPATH, "")
    }

    def common_function(self):
        print("Function: common_function")
        print(self.__COMMON.get("iOS"))
