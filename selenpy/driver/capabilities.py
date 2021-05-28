from selenpy.common import config


def get_default_capabilities():
    default_caps = {
        "waitForQuiescence": config.get_config().getboolean("Common", "appium.waitForQuiescence"),
        "orientation": config.get_config().get("Common", "appium.orientation")
    }
    return default_caps


def get_ios_capabilities():
    desired_caps = get_default_capabilities()
    desired_caps["platformName"] = config.get_config().get("iOS", "ios.platformName")
    desired_caps["platformVersion"] = config.get_config().get("iOS", "ios.platformVersion")
    desired_caps["deviceName"] = config.get_config().get("iOS", "ios.deviceName")
    desired_caps["udid"] = config.get_config().get("iOS", "ios.udid")
    desired_caps["automationName"] = config.get_config().get("iOS", "ios.automationName")
    desired_caps["browserName"] = config.get_config().get("iOS", "ios.browserName")
    return desired_caps


def get_android_capabilities():
    desired_caps = get_default_capabilities()
    desired_caps["platformName"] = config.get_config().get("Android", "android.platformName")
    desired_caps["platformVersion"] = config.get_config().get("Android", "android.platformVersion")
    desired_caps["deviceName"] = config.get_config().get("Android", "android.deviceName")
    desired_caps["automationName"] = config.get_config().get("Android", "android.automationName")
    desired_caps["appActivity"] = config.get_config().get("Android", "android.appActivity")
    desired_caps["appPackage"] = config.get_config().get("Android", "android.appPackage")
    desired_caps["unicodeKeyboard"] = config.get_config().getboolean("Android", "android.unicode.keyboard")
    desired_caps["resetKeyboard"] = config.get_config().getboolean("Android", "android.reset.keyboard")
    desired_caps["autoGrantPermissions"] = config.get_config().getboolean("Android", "android.grant.permission")
    desired_caps["enableWebviewDetailsCollection"] = config.get_config().getboolean("Android", "android.enableWebviewDetailsCollection")
    return desired_caps
