import pytest

from tests.pages.settings_page import SettingsPage
from tests.base import BaseTest


class TestSettings(BaseTest):
    __PRODUCT_VERSION = 0

    @classmethod
    def setup_class(cls):
        print("\nSetup class ...")

    @pytest.mark.skipif(__PRODUCT_VERSION == 1, reason="This test does not support on production version 1")
    def test_toggle_airplane_mode(self, driver):
        settings_page = SettingsPage(driver)
        settings_page.toggle_airplane_mode()
        assert True
