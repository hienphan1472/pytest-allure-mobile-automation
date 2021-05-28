import os
import allure
import moment

now = moment.now().strftime("%d-%m-%Y")
path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
screen_dir = os.path.join(path, "../reports/screenshot", str(now))


def screen_path():
    global screen_dir
    if not os.path.exists(screen_dir):
        os.makedirs(screen_dir)
        os.chmod(screen_dir, 0o755)
    return screen_dir


def remove_special_characters(text):
    return text.translate({ord(i): None for i in '\ / : * ? " < > |'})


def save_screenshot(driver, name):
    _name = remove_special_characters(name)
    allure.attach(driver.get_screenshot_as_png(), _name + "_" + now, attachment_type=allure.attachment_type.PNG)
