import pytest

from tests.pages.settings_page import SettingsPage
from tests.test_base import BaseTest


class TestDemo(BaseTest):

    @classmethod
    def setup_class(cls):
        print("\nSetup class ...")

    def test_demo(self, driver):
        print(driver.page_source)
